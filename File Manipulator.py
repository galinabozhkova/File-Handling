import os

command = input()

while command != "End":

    if command.startswith("Create"):
        command = command.split("-")
        file = open(f"{command[1]}", "w")
        file.close()

    elif command.startswith("Add"):
        command = command.split("-")
        try:
            file = open(f"{command[1]}", "a")
            file.write(command[2]+"\n")
            file.close()
        except FileNotFoundError:
            file = open(f"{command[1]}", "w")
            file.close()


    elif command.startswith("Replace"):
        command = command.split("-")
        try:
            file = open(f"{command[1]}", "r+")

            lines = file.readlines()

            for i in range(len(lines)):
                lines[i] = lines[i].replace(command[2], command[3])
            file.seek(0)
            file.write("".join(lines))
            file.truncate()
            file.close()

        except FileNotFoundError:
            print("An error occurred")

    elif command.startswith("Delete"):
        command = command.split("-")
        try:
            os.remove(f"{command[1]}")
        except FileNotFoundError:
            print("An error occurred")


    command = input()
