import uuid
import datetime

class members:
    def register(_list,name,doc,tel,mail,plan):
        id = str(uuid.uuid4())[:5]
        initial_date = datetime.date.today()
        end_date = initial_date + datetime.timedelta(days=30)
        _list.append({"id":id,"name":name,"personal_id":doc,"telephone_number":tel,"email":mail,"plan":plan,"initial_date":initial_date,"end_date":end_date,"status":"active"})
        print("Sucessfully added\n")

    def show(_list):
        print("----------------------------------------Members----------------------------------------")
        for i in range(len(_list)):
            print(f"Member Id: {_list[i]["id"]} | Name: {_list[i]["name"]} | Personal Id: {_list[i]["personal_id"]} | Phone number: {_list[i]["telephone_number"]} | Email: {_list[i]["email"]} | Plan: {_list[i]["plan"]} | Plan start date: {_list[i]["initial_date"]} | Plan end date: {_list[i]["end_date"]} | Status: {_list[i]["status"]}")
        print("")

    def renew(_list,i):
        if _list[i]["status"] == "active":
            print("The member is already active\n")
        else:
            _list[i]["status"] = "active"
            _list[i]["end_date"] = datetime.date.today() + datetime.timedelta(days=30)
            print("Sucessfully updated\n")

    def inactive(_list):
        for i in range(len(_list)):
            if (datetime.datetime.strptime(f'{_list[i]["end_date"]}', '%Y-%m-%d').date()) == datetime.date.today():
                _list[i]["status"] = "inactive"