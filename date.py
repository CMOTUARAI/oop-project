day_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def day_of_year(day, month ,year):
    
    if day > 31 or month > 12 or day < 1 or month < 1:
        return exit() 
    
    day_of_year = 0
    if(is_leap(year)):
        day_in_month[2] = 29
    else:
        if(month == 2 and day == 29):
            return exit()
    for i in range(1,month):
        day_of_year += day_in_month[i]
    day_of_year += day
    return day_of_year
try:
    date = input("Enter a date : ").split("-")
    try:
        year = int(date[2])
    except:
        year = date[2]
    try:    
        month = int(date[1])
    except:
        month = date[1]
    try:    
        day = int(date[0]) 
    except:
        day = date[0]     

    doy = day_of_year(day, month ,year)
    leap_pa = is_leap(year)   
except :
    doy = "Invalid"
    leap_pa = is_leap(year)

print("day of year:",doy,end=" ,")
print("is_leap:",leap_pa)

def day_in_year(year):
    if(is_leap(year)):
        return 366
    else:
        return 365

def date_diff(date1,date2):
    date1 = list(map(int, date1.split("-")))
    date2 = list(map(int, date2.split("-")))
    doy1 = day_of_year(date1[0], date1[1] ,date1[2])
    doy2 = day_of_year(date2[0], date2[1] ,date2[2])
    totalnday = 0
    for x in range(date1[2]+1,date2[2]):
        totalnday += day_in_year(x)
    if date1[2]==date2[2]:
        dur = doy2 - doy1 + 1
    else:
        dur = (day_in_year(date1[2])-doy1) + totalnday + doy2+1

    if date1[1] < 1 or date1[1] > 12 or date2[1] < 1 or date2[1] > 12:
        print("Invalid")    
    elif date1[0] < 1 or date1[0] > day_in_month[date1[1]] or date2[0] < 1 or date2[0] > day_in_month[date2[1]]:
        print("Invalid")   
    elif (date1[1] == 2 and date1[0] == 29 and not is_leap(date1[2])) or (date2[1] == 2 and date2[0] == 29 and not is_leap(date2[2])):
        print("Invalid")
    else:
        print(dur)

date = input("Enter Input: ").split(",")
date1 = date[0]
date2 = date[1]
date_diff(date1,date2)

print("love you all jubu jubu")