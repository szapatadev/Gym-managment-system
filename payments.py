import uuid
import datetime

class payments:
    def payment(_list,member_list,method,i):
        id = str(uuid.uuid4())[:5]
        member_id = member_list[i]["id"]
        member_name= member_list[i]["name"]
        date_payment = datetime.date.today()
        month = date_payment.month
        year = date_payment.year
        if member_list[i]["plan"] == "basic":
            amount = 29.99
        elif member_list[i]["plan"] == "premium":
            amount = 39.99
        else:
            amount = 49.99
        _list.append({"payment_id":id,"member_id":member_id,"member_name":member_name,"amount":amount,"payment_date":date_payment,"payment_month":month,"payment_year":year,"method":method})
        return True