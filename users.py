import functions

class login:
    def login():
        system = 3
        users = []
        file = "csv/users.csv"
        functions._csv.read(file,users)
        print("You have 3 attemps to login\n")
        while system != 0:
            user = input("User: ").lower()
            password = input("Password: ").lower()
            rol = input("Role: ").lower()
            for i in range(len(users)):
                if users[i]["user"] == user and users[i]["password"] == password and users[i]["role"] == rol:
                    print("Sucessfully Loged in")
                    return True
            system -= 1
            print(f"Incorrent, you have {system} attemps more\n")
        return False