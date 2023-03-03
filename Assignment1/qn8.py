import calendar
date = input("Enter your birthday in DD/MM/YYYY format")
month = int(date[3]+date[4])
year = int(date[6]+date[7]+date[8]+date[9])
print(calendar.month(year,month))
