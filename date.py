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