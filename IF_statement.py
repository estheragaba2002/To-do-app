#import functions (here you have to call it everytime you use it i.e. functions.getodos())
from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H: %M: %S")
print("It is ", now)

while True:
    user_input = input("Type 'show', 'add','edit' or 'exit'")
    user_input = user_input.strip()

    if user_input.startswith("add") :
        # todo = input("Enter the to do : "+ "/n")
        todo = user_input[4:]

        todos = get_todos("todos.txt")

        todos.append(todo + "\n")

        write_todos("todos.txt", todo)

    elif user_input.startswith("show"):
        todos = get_todos("todos.txt")

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            # print(index,"-",item.title())
            item = item.strip("\n")
            row = f"{index}-{item.capitalize()}"
            print(row)
    elif user_input.startswith("edit") :
        try:
            edited_todo = int(user_input[5:])
            number = edited_todo - 1

            todos = get_todos("todos.txt")

            replacement = input("What would you like to replace it with?")
            todos[number] = replacement + "\n"

            write_todos("todos.txt", todos)

        except ValueError:
            print("Your input is invalid")
            continue

    elif user_input.startswith("complete"):
        try:
            edited_todo = int(user_input[9:])

            todos = get_todos("todos.txt")
            index = edited_todo - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            with open("todos.txt", "w") as file:
                write_todos("todos.txt", todos)

            message = f"Todos {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that index")
            continue

    elif user_input.startswith("exit") :
        break
      # case  "whatever":
      #     print("You have entered an unknown entry")
print("bye")
