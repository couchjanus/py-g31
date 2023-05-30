# test_todo.py

from typer.testing import CliRunner

from todo import view, __app_name__, __version__

runner = CliRunner()

def test_version():
   result = runner.invoke(view.app, ["--version"])
   assert result.exit_code == 0
   assert f"Awesome CLI {__app_name__} Version: {__version__}\n" in result.stdout