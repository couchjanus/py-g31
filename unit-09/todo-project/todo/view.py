"""This module provides UI for todo"""

from typing import Optional
from pathlib import Path
import typer
from todo import __app_name__, __version__

# створюємо екземпляр Typer.
app = typer.Typer()


def _version_callback(value) :
   if value:
       typer.echo(f"{__app_name__} v{__version__}")
       raise typer.Exit()

@app.callback()
def main( version: Optional[bool] = typer.Option( None,  "--version",  "-v",  help="Show the application's version and exit.",  callback=_version_callback,  is_eager=True, )):
   return
