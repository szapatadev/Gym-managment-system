import users
import menus
import members
import functions

member = []
members_file = "csv/members.csv"

if users.login.login():
    try:
        functions._csv.read(members_file,member)
    except FileNotFoundError:
        functions._csv.write(members_file,member,["id","name","personal_id","telephone_number","email","plan","initial_date","end_date","status"])
    except:
        print("We are solving these problems\n")

    members.members.inactive(member)
    while True:
        system = menus.menu.principal()
        if system == 1:
            menus.menu.member_managment(member)
        elif system == 2:
            menus.menu.asistances()
        elif system == 3:
            menus.menu.workouts()
        elif system == 4:
            print("Reports")
        else:
            functions._csv.write(members_file,member,["id","name","personal_id","telephone_number","email","plan","initial_date","end_date","status"])
            break