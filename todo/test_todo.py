from typer.testing import CliRunner
import json
import pytest

from todo import (
    DB_READ_ERROR,
    ID_ERROR,
    SUCCESS,
    __app_name__,
    __version__,
    view,
    controller,
)


runner = CliRunner()

def test_version():
    result = runner.invoke(view.app, ["--version"])
    assert result.exit_code == 0
    assert f"Awesome CLI {__app_name__} Version: {__version__}\n" in result.stdout


def test_help():
    result = runner.invoke(view.app, ["--help"])
    assert result.exit_code == 0
    assert f"""Usage: main [OPTIONS] COMMAND [ARGS]""" in result.stdout.split('\n')[1].strip().split('.')[0]

# @pytest.fixture
# def mock_json_file(tmp_path):
#     todo = [{"Description": "Get some milk.", "Priority": 2, "Done": False}]
#     db_file = tmp_path / "todo.json"
#     with db_file.open("w") as db:
#         json.dump(todo, db, indent=4)
#     return db_file


test_data1 = {
    "description": ["Clean", "the", "house"],
    "priority": 1,
    "todo": {
        "Description": "Clean the house.",
        "Priority": 1,
        "Done": False,
    },
}
test_data2 = {
    "description": ["Wash the car"],
    "priority": 2,
    "todo": {
        "Description": "Wash the car.",
        "Priority": 2,
        "Done": False,
    },
}


@pytest.mark.parametrize(
    "description, priority, expected",
    [
        pytest.param(
            test_data1["description"],
            test_data1["priority"],
            (test_data1["todo"], SUCCESS),
        ),
        pytest.param(
            test_data2["description"],
            test_data2["priority"],
            (test_data2["todo"], SUCCESS),
        ),
    ],
)
def test_add(mock_json_file, description, priority, expected):
    todos = controller.Todo(mock_json_file)
    assert todos.add(description, priority) == expected
    read = todos._db_handler.read_todos()
    assert len(read.todo_list) == 2


# @pytest.fixture
# def mock_wrong_json_file(tmp_path):
#     db_file = tmp_path / "todo.json"
#     return db_file


def test_add_wrong_json_file(mock_wrong_json_file):
    todos = controller.Todo(mock_wrong_json_file)
    response = todos.add(["test task"], 1)
    assert response.error == DB_READ_ERROR
    read = todos._db_handler.read_todos()
    assert len(read.todo_list) == 0


# @pytest.fixture
# def mock_wrong_json_format(tmp_path):
#     db_file = tmp_path / "todo.json"
#     with db_file.open("w") as db:
#         db.write("")
#     return db_file


def test_add_wrong_json_format(mock_wrong_json_format):
    todos = controller.Todo(mock_wrong_json_format)
    assert todos.add(test_data1["description"], test_data1["priority"]) == (
        test_data1["todo"],
        SUCCESS,
    )
    read = todos._db_handler.read_todos()
    assert len(read.todo_list) == 1


test_todo1 = {
    "Description": "Get some milk.",
    "Priority": 2,
    "Done": True,
}
test_todo2 = {}


@pytest.mark.parametrize(
    "todo_id, expected",
    [
        pytest.param(1, (test_todo1, SUCCESS)),
        pytest.param(3, (test_todo2, ID_ERROR)),
    ],
)
def test_set_done(mock_json_file, todo_id, expected):
    todos = controller.Todo(mock_json_file)
    assert todos.set_done(todo_id) == expected


test_todo3 = {
    "Description": "Get some milk.",
    "Priority": 2,
    "Done": False,
}
test_todo4 = {}


@pytest.mark.parametrize(
    "todo_id, expected",
    [
        pytest.param(1, (test_todo3, SUCCESS)),
        pytest.param(3, (test_todo4, ID_ERROR)),
    ],
)
def test_remove(mock_json_file, todo_id, expected):
    todos = controller.Todo(mock_json_file)
    assert todos.remove(todo_id) == expected


def test_remove_all(mock_json_file):
    todos = controller.Todo(mock_json_file)
    assert todos.remove_all() == ({}, SUCCESS)
