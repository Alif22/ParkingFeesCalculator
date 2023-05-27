import datetime
from datetime import date
def isWeekday(receivedDate):
    if receivedDate.weekday() < 5 :
        print("its weekday")
        return True
    else:
        print("its weekend")
        return False

if __name__ == "__main__":
    isWeekday(date(2023,5,27))