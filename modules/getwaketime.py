#read frome outfile_debt_calc file
#get day """check"""
#check day against payment value 
#compute if day == True
#else check if day has passed, compute if True, pass if False---not sure how to write this---
#exit if day == False
#

# x = str(1000)

# print(x)

### Read in stored date of payment from .csv doc as get_day ###

#wake_time = x #some stuff from that file




#print('yee import data from datetime: ')
#print(now.year, now.month, now.day, now.hour, now.minute, now.second)




"""this needs to be called as a classs from getinfo.py"""

def getwakehour():
    try:
        wake_hour = int(input("""Plaese enter a number between 1 and 24 to set the 
hour at which you would like to wake up. \n"""))
        while (wake_hour <=0) or (wake_hour >24 ):
            wake_hour = int(input("That's not a supported time, please try again. \n"))
    except ValueError:
        wake_hour = int(input("Numbers only, please. \n"))
    return int(wake_hour)


def getwakeminute():
    try:
        wake_minute = int(input("""Plaese enter a number between 0 and 59 to set the 
minute at which you would like to wake up. \n"""))
        while (wake_minute <0) or (wake_minute >24 ):
            wake_minute = int(input("That's not a supported time, please try again. \n"))
    except ValueError:
        wake_minute = int(input("Numbers only, please. \n"))
    return int(wake_minute)





# import datetime

# now = datetime.datetime.now()

# # #the date is supplied in intigers as demonstrated here
# # n = now.month+now.year
# # print(n)

# wake_time = getwakeminute()

# # #outfile_debt.write(str( day_pay) + ',')

# # print(type(wake_time))


# if now.minute == wake_time:
#     print('i got the time!')
# else:
#     print('wht?')