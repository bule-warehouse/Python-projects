# TODO console app
while True:
    user_action=input("Type add, show, edit, complete, delete or exit: ").lower().strip()
    match user_action:
        case "add":
            with open("files/todos.txt", "r") as file:
                todos=file.readlines()

            todo=input("Enter a TODO: ")+"\n"
            todos.append(todo.capitalize())

            with open("files/todos.txt", "w") as file:
                file.writelines(todos)
        case "show" | "display":
            with open("files/todos.txt", "r") as file:
                todos = file.readlines()
            print(f"You have {len(todos)} TODOs:")
            for index,item in enumerate(todos):
                print(f"{index+1}-{item.strip("\n")}")
        case "edit":
            number=int(input("Type a number of TODO to edit: "))
            number=number-1
            if number<len(todos):
                existing_todo=todos[number]
                print(f"You want to edit the TODO -> {existing_todo}")
                new_todo=input("Type a TODO: ").capitalize()
                todos[number]=new_todo
            else:
                print(f"You have only {len(todos)} TODOs.  Invalid input")
        case "complete":
            index = int(input("Number of the TODO to complete: "))
            if index<len(todos):
                todos.pop(index-1)
            else:
                print("Invalid input. Try again!!")
        case "delete":
            user_selection= input("Do you want to delete all TODOs? Type yes or no: ").lower().strip()
            if user_selection=="yes":
                todos.clear()
            elif user_selection=="no":
                program_close=input("Do you want to close the program? Type yes or no: ").lower().strip()
                if program_close=="yes":
                    break
            else:
                print("Invalid input. Try again!!")
        case "exit":
            break
        case _:
            print("Invalid input")
