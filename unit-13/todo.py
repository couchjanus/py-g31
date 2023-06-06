from typing import Any, Dict, List, NamedTuple

class DBResponse(NamedTuple):
    todo_list: List[Dict[str, Any]]

class DBHandler:
    
    def __init__(self) -> None:
        self.todo_list = []
        
    def read_todos(self) -> DBResponse:
        return DBResponse(self.todo_list)
    
    def write_todos(self, todo_list: List[Dict[str, Any]]) ->DBResponse:
        self.todo_list = todo_list
        return DBResponse(self.todo_list)

class CurrentTodo(NamedTuple):
    todo: Dict[str, Any]

class Todo:
    
    def __init__(self) -> None:
        # self.todo_list = []
        self._db_handler = DBHandler()
    
    def get_todo_list(self)->List[Dict[str, Any]]:
        # return self.todo_list
        read = self._db_handler.read_todos()
        return read.todo_list
    
    def add(self, description: List[str], priority:int = 2)->CurrentTodo:
        description_text = " ".join(description)
        if not description_text.endswith('.'):
            description_text += '.'
        todo = {'Description': description_text, 'Priority': priority, 'Done': False,}
        read = self._db_handler.read_todos()
        read.todo_list.append(todo)
        write = self._db_handler.write_todos(read.todo_list)
        # self.todo_list.append(todo)
        return CurrentTodo(todo)
    
    def remove(self):
        pass
    
if __name__ == '__main__':
    
    todo_1 = Todo()
    current_todo = todo_1.add('To do something')
    print(current_todo)
    current_todo = todo_1.add('To do something other')
    print(current_todo)
    print(todo_1.get_todo_list())