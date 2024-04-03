todos = []


while True:
    user_action = input("type add or show or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':        # this is a bitwise OR operator
            for item in todos:
                item = item.title()     # This makes all the items display as title case
                print("-", item)        # I like this display, like in Markdown
        case 'exit':
            break
        case _:
            print("you entered an unknown command, moron")

print("bye!")
