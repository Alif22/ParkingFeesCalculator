from datetime import datetime as dt
from datetime import timedelta

def isWeekday(receivedDate):
    #return true if it is weekday
    if receivedDate.weekday() < 5 :
        return True
    else:
        return False
  
def showOutput(regNo,inDateTime,outDateTime,ticPrice):
    duration = outDateTime - inDateTime
    hours, remainder = divmod(duration.total_seconds(), 3600) 
    minutes = remainder// 60
    print('Reg No.: ' + regNo)
    print('In: '+ inDateTime.strftime("%Y-%m-%d %H:%M"))
    print('Out: ' + outDateTime.strftime("%Y-%m-%d %H:%M"))
    if hours > 0:
        print('Duration: {0} hours {1} minutes'.format(int(hours),  int(minutes)))
    else:
        print('Duration: {0} minutes'.format(int(minutes)))
    print('Amount to paid: ${:.2f}'.format(ticPrice))

def calcTicPrice(outDateTime,inDateTime):    
    ticketPrice = 0
    durationParked = outDateTime - inDateTime
    totalMinParked = durationParked.total_seconds()/60

    #if the car packed less than 15 minutes
    if totalMinParked > 15:
        hours, remainder = divmod(durationParked.total_seconds(), 3600) 
        minutes = remainder// 60
        #check if within grace period
        if minutes > 5:
            hours +=1
        if isWeekday(inDateTime.date()):
            #$3 dollar for the first 3 hour on weekday
            ticketPrice += 3
            #calculating ticket price after the first 3 hour
            if hours > 3:
                hours -= 3
                ticketPrice += hours*1.50
            if ticketPrice > 20:
                ticketPrice = 20
        else:
            #$5 dollar for the first 3 hour on weekend
            ticketPrice += 5
            if hours > 3:
                hours -= 3
                ticketPrice += hours*2
            if ticketPrice > 40:
                ticketPrice = 40
                
    return ticketPrice

if __name__ == "__main__":
    #insert inputs here such as time in, time out and car registration number 
    # year,month,day, hour,minute,second,millisecond
    inDateTime = dt(2021,10,25,8,16,0,0) 
    outDateTime = dt(2021,10,25,12,19,0,0)
    regNumber = "SN 3453 G"

    ticketPrice = calcTicPrice(outDateTime,inDateTime)
    showOutput(regNumber,inDateTime,outDateTime,ticketPrice)
            