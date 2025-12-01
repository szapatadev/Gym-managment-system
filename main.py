import users
import menus
import members
import functions
import reports

member = []
asistance = []
workout = []
payment = []
members_file = "csv/members.csv"
asistance_file = "csv/asistances.csv"
workout_file = "csv/workouts.csv"
payment_file = "csv/payments.csv"

if users.login.login():
    try:
        functions._csv.read(members_file,member)
        functions._csv.read(asistance_file,asistance)
        functions._csv.read(workout_file,workout)
        functions._csv.read(payment_file,payment)
    except FileNotFoundError:
        functions._csv.write(members_file,member,["id","name","personal_id","telephone_number","email","plan","initial_date","end_date","status"])
        functions._csv.write(asistance_file,asistance,["asistance_id","member_id","name","date","time","type"])
        functions._csv.write(workout_file,workout,["workout_id","member_id","date","duration","type","calories"])
        functions._csv.write(payment_file,payment,["payment_id","member_id","member_name","amount","payment_date","payment_month","payment_year","method"])
    except:
        print("We are solving these problems\n")

    members.members.inactive(member)
    while True:
        system = menus.menu.principal()
        if system == 1:
            menus.menu.member_managment(member,payment)
        elif system == 2:
            menus.menu.asistances(asistance,member)
        elif system == 3:
            menus.menu.workouts(workout,member)
        elif system == 4:
            if functions.ver.not_empthy(member):
                id = input("Enter the id member: ")
                search, i = functions.ver.search(member,"id",id)
                if search:
                    reports.reports.reports(member,asistance,workout,i)
                else:
                    print(i)
        else:
            functions._csv.write(members_file,member,["id","name","personal_id","telephone_number","email","plan","initial_date","end_date","status"])
            functions._csv.write(asistance_file,asistance,["asistance_id","member_id","name","date","time","type"])
            functions._csv.write(workout_file,workout,["workout_id","member_id","date","duration","type","calories"])
            functions._csv.write(payment_file,payment,["payment_id","member_id","member_name","amount","payment_date","payment_month","payment_year","method"])
            break