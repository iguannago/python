import time
from datetime import tzinfo, timedelta, datetime

frecuently = 2 # every two weeks I change the city. 
today = time.strftime 
current_city = "VVA"

print "Today is:", today("%d/%m/%Y")
print "Current City is:", current_city

def ObtainDateFromUser():
    isValid=False
    while not isValid:
        userIn = raw_input("Type Date: dd/mm/yy: ")
        try:
            d1 = datetime.strptime(userIn, "%d/%m/%y")
            isValid=True
        except:
            print "Invalid Format!\n"
    return d1

# t = (ObtainDate() - datetime.now()).total_seconds()
# print t


userDate = ObtainDateFromUser()
print "userDate:", userDate




