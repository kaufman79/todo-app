def get_todos():
    with open('todos.txt', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


while True:
    user_action = input("type add, edit, show, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + "\n")

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

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

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
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

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
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
