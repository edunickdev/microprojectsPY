import time

reminder = time.localtime()

print(reminder)

monthLst = {1: "January", 2: 'February', 3: 'March', 4: 'April', 5: 'Mayo', 6: 'June', 7: 'Jule', 8: 'Agost',
            9: 'September', 10: 'October', 11: 'November', 12: 'December'}
dayLst = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}

day = reminder.tm_mday

month = reminder.tm_mon
monthWord = monthLst[month]

year = reminder.tm_year
hour = reminder.tm_hour
minute = reminder.tm_min

if hour < 19:
    hour = 19 - hour
    print('Hi, today is ' + str(monthWord) + ' ' + str(day) + ' of ' +
          str(year) + ' how are you feeling?, tired?, energize?, you are ' +
          str(hour) + ' with ' + str(minute) + ' hours away from finishing your work')
elif hour >= 19 and 1 <= minute <= 59:
    minute = 60 - minute
    print('Hey! hurry up!, you are ' + str(minute) + ' minutes away from finishing your work')
elif hour >= 20:
    print('oh no!, it´s time off, time to share with your friends, family and loved ones')
