while True:
    user_input = input("Type 'show', 'add','edit' or 'exit'")
    user_input = user_input.strip()

    match user_input:
        case "add":
            todo = input("Enter the to do : "+ "/n")

            #  file = open("todos.txt", "r")
           # todos = file.readlines()
            #file.close()

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            todos.append(todo)

            with open("todos.txt", "w") as file:
                todos = file.writelines(todos)

        case "show" | "display":
            with open("todos.txt", "r") as file:
                todos = file.readlines()

            new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                                # print(index,"-",item.title())
                row = f"{index}-{item.capitalize()}"
                print(row)
        case "edit":
            edited_todo = int(input("What to do action would you like to edit?"))
            number = edited_todo - 1

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            replacement = input("What would you like to replace it with?")
            todos[number] = replacement + "\n"

            with open("todos.txt", "w") as file:
                todos = file.writelines(todos)

        case "complete":
            edited_todo = int(input("What to do action would you like to edit?"))

            with open("todos.txt", "r") as file:
                todos = file.readlines()
            index = edited_todo - 1
            todo_to_remove = todos(index).strip("\n")
            todos.pop(index)

            with open("todos.txt", "w") as file:
                file.writelines(todos)

            message = f"Todos {todo_to_remove} was removed from the list"
            print(message)

        case "exit":
            break
#       case  "whatever":
#           print("You have entered an unknown entry")
print("bye")
