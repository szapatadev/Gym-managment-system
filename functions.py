import csv

class ver:
    def not_empthy(_list):
        if not _list:
            print("The list is empthy, there are not matches\n")
            return False
        else:
            return True
        
    def search(_list,key,value):
        for i in range(len(_list)):
            if _list[i][key] == value:
                return True, i
        return False, "There are not matches\n"

class _csv:
    def write(file,_list,headers):
        with open(file, "w") as writer:
            csv_writer = csv.DictWriter(writer,fieldnames=headers,delimiter=",")
            csv_writer.writeheader()
            csv_writer.writerows(_list)

    def read(file,_list):
        with open(file,"r") as reader:
            csv_reader = csv.DictReader(reader)
            for i in csv_reader:
                _list.append(i)
        