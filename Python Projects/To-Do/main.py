while True:
    user_action = input("type add, edit, show, complete, or exit: ")
    user_action = user_action.strip()

# need to apply this method to the other elif & else lines.
    if user_action.startswith("add"):
        todo = user_action[4:]

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo + "\n")

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith("show"):
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith("edit"):
        number_edendum = int(user_action[5:])
        print(number_edendum)

        number_edendum = number_edendum - 1

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("what is the altered todo? ")
        todos[number_edendum] = new_todo + '\n'

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith("complete"):
        number_delendum = int(user_action[9:])

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        index = number_delendum - 1
        todo_delendum = todos[index].strip('\n')
        todos.pop(index)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith("exit"):
        break
    else:
        print("command is not valid.")

print("bye!")
