# TODO console app
while True:
    user_action=input("Type add, show, edit, complete, delete or exit: ").lower().strip()
    if "add" in user_action:
        with open("files/todos.txt", "r") as file:
            todos=file.readlines()
        todo=input("Enter a TODO: ")+"\n"
        todos.append(todo.capitalize())
        with open("files/todos.txt", "w") as file:
                file.writelines(todos)
    elif "show" in user_action:
        with open("files/todos.txt", "r") as file:
            todos = file.readlines()
        print(f"You have {len(todos)} TODOs:")
        for index,item in enumerate(todos):
            print(f"{index+1}-{item.strip("\n")}")
    elif "edit" in user_action:
        with open("files/todos.txt", "r") as file:
            todos=file.readlines()
        number=int(input("Type a number of TODO to edit: "))
        number=number-1
        if number<len(todos):
            existing_todo=todos[number]
            print(f"You want to edit the TODO -> {existing_todo.strip("\n")}")
            new_todo=input("Type a TODO: ").capitalize()+"\n"
            todos[number]=new_todo
            with open("files/todos.txt", "w") as file:
                file.writelines(todos)
        else:
            print(f"You have only {len(todos)} TODOs.  Invalid input")
    elif "complete" in user_action:
        with open("files/todos.txt", "r") as file:
            todos=file.readlines()
        index = int(input("Number of the TODO to complete: "))
        todo_to_remove=todos[index-1].strip("\n")
        if index<=len(todos):
            todos.pop(index-1)
            with open("files/todos.txt", "w") as file:
                file.writelines(todos)
            print(f"You have removed - {todo_to_remove} - TODO from the list.")
        else:
            print("Invalid input. Try again!!")
    elif "delete" in user_action:
        with open("files/todos.txt", "r") as file:
            todos=file.readlines()
        user_selection= input("Do you want to delete all TODOs? Type yes or no: ").lower().strip()
        if user_selection=="yes":
            todos.clear()
            with open("files/todos.txt", "w") as file:
                file.writelines(todos)
        elif user_selection=="no":
            program_close=input("Do you want to close the program? Type yes or no: ").lower().strip()
            if program_close=="yes":
                break
        else:
            print("Invalid input. Try again!")
    elif "exit" in user_action:
        break
    else:
        print("Invalid input. Try again!")
