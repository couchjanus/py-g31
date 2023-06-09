"""controller"""
from typing import Any, Dict, List, NamedTuple
from todo.model import DBHandler
from pathlib import Path
from todo import DB_READ_ERROR

class CurrentTodo(NamedTuple):
    todo: Dict[str, Any]
    error: int

class Todo:
    
    def __init__(self, db_path: Path) -> None:
        self._db_handler = DBHandler(db_path)
    
    def get_todo_list(self)->List[Dict[str, Any]]:
        read = self._db_handler.read_todos()
        return read.todo_list
    
    def add(self, description: List[str], priority:int = 2)->CurrentTodo:
        description_text = " ".join(description)
        if not description_text.endswith('.'):
            description_text += '.'
        todo = {
            'Description': description_text, 
            'Priority': priority, 
            'Done': False,
            }
        read = self._db_handler.read_todos()
        if read.error == DB_READ_ERROR:
            return CurrentTodo(todo, read.error)
        read.todo_list.append(todo)
        write = self._db_handler.write_todos(read.todo_list)
        return CurrentTodo(todo, write.error)
    
    def remove(self):
        pass