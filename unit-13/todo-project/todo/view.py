"""This module provides UI for todo"""

from typing import Optional
from pathlib import Path
import typer
from todo import __app_name__, __version__, model, config, ERRORS, controller
from typing import List
from typing_extensions import Annotated

# створюємо екземпляр Typer.
app = typer.Typer()

@app.command()
def init(db_path: str = typer.Option(str(model.DEFAULT_DB_FILE_PATH), "--db-path", "-db", prompt="TODO database location?")) -> None:
   """Initialize the Todo database."""
   app_init_error = config.init_app(db_path)
   print("app_init_error ", app_init_error)
   if app_init_error:
      typer.secho(
         f'Creating config file failed with "{ERRORS[app_init_error]}"', fg=typer.RED
      )
      raise typer.Exit(1)
   db_init_error = model.init_database(Path(db_path))
   if db_init_error:
      typer.secho(
         f'Creating database failed with "{ERRORS[db_init_error]}"',
         fg=typer.colors.RED
      )
      raise typer.Exit(1)
   else:
      typer.secho(
         f'The TODO database is {db_path}',
         fg=typer.colors.GREEN
      )

def get_todos()->controller.Todo:
   db_path = model.get_database_path(config.CONFIG_FILE_PATH)
   return controller.Todo(db_path)

@app.command()
def add(
   description: List[str] = typer.Argument(...),
   priority: int = typer.Option(2, "--priority", "-p", min=1, max=3),
)->None:
   todos = get_todos()
   todo, error = todos.add(description, priority)
   if error:
      typer.secho(f'Adding to-do failed with "{ERRORS[error]}"', fg=typer.colors.RED)
      raise typer.Exit(1)
   else:
      typer.secho(f"""To-do: "{todo['Description']}" was added """
                  f"""with priority: {priority} """,
                  fg=typer.colors.GREEN)
   
@app.command()
def list_all():
   todos = get_todos()
   todo_list = todos.get_todo_list()

def _version_callback(value) :
   if value:
       typer.echo(f"Awesome CLI {__app_name__} Version: {__version__}")
       raise typer.Exit()

@app.callback()
def main(
   version: Annotated[
      Optional[bool], 
      typer.Option("--version",  "-v", help="Show the application's version and exit.",  callback=_version_callback, is_eager=True)
   ] = None
   # version: Optional[bool] = typer.Option(None,  "--version",  "-v", help="Show the application's version and exit.",  callback=_version_callback, is_eager=True)
   ) -> None:
   return
