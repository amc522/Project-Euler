import sys

#                    31 28  31  30  31   30   31   31   30   31   30   31

daysInMonth       = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
daysInMonthLeap   = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
daysPast          = (1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335)
daysPastLeap      = (1, 32, 61, 92, 122, 153, 183, 214, 245, 275, 306, 336)

epoch = (1, 1, 1900)

def y(date):
    return date[2]

def m(date):
    return date[1]

def d(date):
    return date[0]

def isLeapYear(year):
    return year % 4 == 0 and (not year % 100 == 0 or year % 400 == 0);

def daysSinceEpoch(date):
    years = y(date) - y(epoch)

    days = 0
    # leap years in a century
    leapYears = years / 100 * 24 
    # leap years that are on a century
    leapYears += (((years - 1)/ 100) + 3) / 4
    # remaining leap years
    leapYears += max(years % 100 - 1, 0) / 4

    days += (years - leapYears) * 365 + leapYears * 366

    if not isLeapYear(y(date)):
        days += daysPast[m(date) - 1] - 1
    else:
        days += daysPastLeap[m(date) - 1] - 1

    days += d(date) - 1

    return days

def findSundaysOnFirst(startDate, endDate):
    sundays = 0

    month = m(startDate)
    year = y(startDate)

    days = daysSinceEpoch(startDate)

    while(year < y(endDate) or (year == y(endDate) and month <= m(endDate))):
        if days % 7 == 6:
            #print (1, month, year)
            sundays += 1

        if not isLeapYear(year):
            days += daysInMonth[month - 1]
        else:
            days += daysInMonthLeap[month - 1]

        month += 1

        if month == 13:
            month = 1
            year += 1

    return sundays

startDate = (1, 1, 1901)
endDate = (31, 12, 2000)
if len(sys.argv) == 4:
    endDate = (int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))

sundays = findSundaysOnFirst(startDate, endDate)
print "There are", sundays, " sundays that are on the 1st of the month between", startDate, "and", endDate
