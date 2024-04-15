FILEPATH = "todos.txt"
def get_todos(filepath=FILEPATH):
    """
    Read a text file and return the list of to-d items.
    :param filepath:
    :return:
    """
    with open(filepath, 'r', encoding='utf-8') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to-do items list in the text file."""
    with open(filepath, 'w', encoding='utf-8') as file:
        file.writelines(todos_arg)

print(__name__)