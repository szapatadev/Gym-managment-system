import datetime
import uuid

class asistances:
    def check_in_out(_list,member_list,i,type):
        id = str(uuid.uuid4())[:5]
        date = datetime.date.today()
        time = ((datetime.datetime.now()).time()).strftime("%H:%M:%S")
        _list.append({"asistance_id":id,"member_id":member_list[i]["id"],"name":member_list[i]["name"],"date":date,"time":time,"type":type})
        print("Asistance sucessfully added\n")
    
    def show(_list,member_list,i):
        for e in range(len(_list)):
            if member_list[i]["id"] == _list[e]["member_id"]:
                print(f"Asistance id: {_list[e]["asistance_id"]} | Member id: {_list[e]["member_id"]} | Member name: {_list[e]["name"]} | Date: {_list[e]["date"]} | Time: {_list[e]["time"]} | Type: {_list[e]["type"]}")
        print("")