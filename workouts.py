import uuid
import datetime

class workout:
    def add(_list,member_list,i,duration,type):
        id = str(uuid.uuid4())[:5]
        date = datetime.date.today()
        if type == "cardio":
            calories = duration * 8
        elif type == "strong":
            calories = duration * 5
        elif type == "hit":
            calories = duration * 12
        elif type == "stretch":
            calories = duration * 3 
        _list.append({"workout_id":id,"member_id":member_list[i]["id"],"date":date,"duration":duration,"type":type,"calories":calories})
        print("Workout sucssfully added\n")

    def calories(_list,member_list,i):
        total_calories = 0
        for e in range(len(_list)):
            if _list[e]["member_id"] == member_list[i]["id"]:
                total_calories += int(_list[e]["calories"])
        return total_calories