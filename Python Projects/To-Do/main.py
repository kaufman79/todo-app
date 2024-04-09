def get_todos(filepath="todos.txt"):
    """ Read text file and return list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """ Write the to-do items into the text file."""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


while True:
    user_action = input("type add, edit, show, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + "\n")

        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number_edendum = int(user_action[5:])
            print(number_edendum)

            number_edendum = number_edendum - 1

            todos = get_todos()

            new_todo = input("what is the altered todo? ")
            todos[number_edendum] = new_todo + '\n'

            write_todos(todos)

        except ValueError:
            print("your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number_delendum = int(user_action[9:])

            todos = get_todos()

            index = number_delendum - 1
            todo_delendum = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Todo {todo_delendum} was removed from the list."
            print(message)
        except IndexError:
            print("your command is not valid")
            continue
        except ValueError:
            print("your command is not valid")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("command is not valid.")

print("bye!")
