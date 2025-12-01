import functions
import members

class menu:
    def principal():
        print("")
        try:
            system = int(input("1 - Members managment\n2 - Asistances\n3 - Workouts\n4 - Reports\n5 - Quit\nWhat do you want to do? "))
            if system < 1 or system > 5:
                print("Please enter a valid value\n")
            else:
                print("")                
                return system
        except:
            print("Please enter a valid value\n")

    def member_managment(_list):
        while True:
            try:
                system = int(input("1 - Register a member\n2 - Show all members\n3 - Search a member by id\n4 - Renew the plan with payment\n5 - Quit\nWhat do you want to do? "))
                if system < 1 or system > 5:
                    print("Please enter a valid value\n")
                else:   
                    if system == 1:
                        name = input("Enter the member name: ").lower()
                        while True:
                            id = int(input("Enter the member id: "))
                            tel = int(input("Enter the member phone number: "))
                            if id < 0 or tel < 0:
                                print("Enter a valid value\n")
                            else:
                                break
                        mail = input("Enter the member email: ").lower()
                        while True:
                            plan = input("Enter the member plan (Basic,Premium,Full): ").lower()
                            if plan == "basic" or plan == "premium" or plan == "full":
                                break
                            else:
                                print("Enter a valid value\n")
                        members.members.register(_list,name,id,tel,mail,plan)
                    elif system == 2:
                        if functions.ver.not_empthy(_list):
                            members.members.show(_list)
                    elif system == 3:
                        if functions.ver.not_empthy(_list):
                            id = input("Enter the member id: ").lower()
                            search, i = functions.ver.search(_list,"id",id)
                            if search:
                                print(f"Member Id: {_list[i]["id"]} | Name: {_list[i]["name"]} | Personal Id: {_list[i]["personal_id"]} | Phone number: {_list[i]["telephone_number"]} | Email: {_list[i]["email"]} | Plan: {_list[i]["plan"]} | Plan start date: {_list[i]["initial_date"]} | Plan end date: {_list[i]["end_date"]} | Status: {_list[i]["status"]}\n")
                            else:
                                print(i)
                    elif system == 4:
                        if functions.ver.not_empthy(_list):
                            id = input("Enter the member id: ").lower()
                            search, i = functions.ver.search(_list,"id",id)
                            if search:
                                members.members.renew(_list,i)
                            else:
                                print(i)
                    else:
                        break
            except:
                print("Please enter a valid value\n")

    def asistances():
        while True:
            try:
                system = int(input("1 - Check in/out/\n2 - History per member\n3 - Quit\nWhat do you want to do? "))
                if system < 1 or system > 3:
                    print("Please enter a valid value\n")
                else:
                    if system == 1:
                        print("Check in/out/")
                    elif system == 2:
                        print("History per member")
                    else:
                        break
            except:
                print("Please enter a valid value\n")

    def workouts():
        while True:
            try:
                system = int(input("1 - Record a workout\n2 - Calculate calories\n3 - Quit\nWhat do you want to do? "))
                if system < 1 or system > 3:
                    print("Please enter a valid value\n")
                else:
                    if system == 1:
                        print("Record a workout")
                    elif system == 2:
                        print("Calculate calories")
                    else:
                        break
            except:
                print("Please enter a valid value\n")
