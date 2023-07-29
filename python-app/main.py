import calendar

print('Welcome to calendar\n')

year = int(input('Enter year: '))
month = int(input('Enter month: '))

print(calendar.month(year, month))

print('Have a good day!')