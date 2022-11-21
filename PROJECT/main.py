import os
import CRUD as CRUD

if __name__ == "__main__":
    operationSytem = os.name

    match operationSytem:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    print(20*'='+"WELCOME TO MY MUSIC"+'='*20)
    print(59*'-')

    CRUD.init_console()

    while(True):
        match operationSytem:
            case "posix": os.system("clear")
            case "nt": os.system("cls")

        print(41*'='+"WELCOME TO MY MUSIC"+'='*41)
        print(100*'-')

        print(f"\n1. Read Data")
        print(f"2. Create Data")
        print(f"3. Update Data")
        print(f"4. Delete Data\n")

        option = input("What Do you want? ")

        match option:
            case "1": CRUD.read_console()
            case "2": CRUD.create_console()
            case "3": CRUD.update_console()
            case "4": CRUD.delete_console()

        done = input("Anything Else? (y/n)")
        if done == "n" or done == "N":
            break

    print(f"\nTHANK YOU!\n")