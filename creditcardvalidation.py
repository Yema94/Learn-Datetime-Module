from datetime import datetime, date

def validateCard(expDate):
    if expDate > datetime.now().date():
        print("Valid")
    else:
        print("Expired")

validateCard(date(2021, 6, 25))
print(datetime.now())
print(datetime.today())