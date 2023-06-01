class Todo():
    """Base Python Class."""
    __class_attr = 'Hello'
    num_instances = 0
    
    def __init__(self) -> None:
        # Todo.num_instances += 1
        type(self).num_instances += 1
    
    def _my_str(self):
        return f"This is class attribute: {self.__class_attr}"
    
    def my_method(self):
        """My Class Method."""
        # print(f"This is class attribute: {self.__class_attr}")
        print(self._my_str())
    # pass
    
# print(Todo)
# print(type(Todo))
# print(dir(Todo))

# print(Todo.__doc__)

todo_1 = Todo()
# print(todo_1)
# print(type(todo_1))
# print(dir(todo_1))
todo_1.class_attr = 'Hello Object'
Todo.class_attr = 'Hello Class'

# print(Todo.__class_attr)
# print(todo_1.__class_attr)
print(todo_1.num_instances)

todo_2 = Todo()
# print(todo_2.__class_attr)
print(todo_1.num_instances)

class MyClass:
    pass

todo_3 = Todo()
print(todo_1.num_instances)
print(todo_2.num_instances)

todo_1.my_method()
todo_2.my_method()


print(Todo.__dict__)

