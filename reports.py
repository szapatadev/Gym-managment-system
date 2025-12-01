import functions
import workouts

class reports:
    def total_asistances(member_list,asistance_list,i):
        counter = 0
        for e in range(len(asistance_list)):
            if member_list[i]["id"] == asistance_list[e]["member_id"]:
                counter += 1
        return counter

    def reports(member_list,asistance_list,workouts_list,i):
        id = member_list[i]["id"]
        name = member_list[i]["name"]
        total_asistances = reports.total_asistances(member_list,asistance_list,i)
        file = f"reports/{name}.csv"
        total_calories = workouts.workout.calories(workouts_list,member_list,i)
        plan = member_list[i]["plan"]
        print(f"Member Id: {id}\nMember name: {name}\nTotal asistances: {total_asistances}\nTotal calories: {total_calories}\nPlan: {plan}\n")
        functions._csv.write(file,[{"member_id":id,"member_name":name,"total_asistances":total_asistances,"total_calories":total_calories,"plan":plan}],["member_id","member_name","total_asistances","total_calories","plan"])
        print(f"Csv already saved with all this info in {file}")