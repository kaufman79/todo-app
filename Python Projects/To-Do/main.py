# from functions import get_todos, write_todos
import functions

while True:
    user_action = input("type add, edit, show, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number_edendum = int(user_action[5:])
            print(number_edendum)

            number_edendum = number_edendum - 1

            todos = functions.get_todos()

            new_todo = input("what is the altered todo? ")
            todos[number_edendum] = new_todo + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number_delendum = int(user_action[9:])

            todos = functions.get_todos()

            index = number_delendum - 1
            todo_delendum = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

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
