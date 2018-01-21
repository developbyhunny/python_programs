import calendar

weekday = {0: 'MONDAY', 1: 'TUESDAY', 2: 'WEDNESDAY', 3: 'THURSDAY', 4: 'FRIDAY', 5: 'SATURDAY', 6: 'SUNDAY'}

mm, dd, year = map(int, input().split())

print(weekday[calendar.weekday(year, mm, dd)])

