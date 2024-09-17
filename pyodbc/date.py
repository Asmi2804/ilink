from datetime import datetime, timedelta,date, time
# current date and time
current=datetime.now()
print("current date and time:",current)
print("print the current day:",current.day)
print("print the current year:",current.year)
print("print the current month:",current.month)
print("print the current hour:",current.hour)
print("print the current minute:",current.minute)
print("print the current second:",current.second)

# specific date and time
dt = datetime(2024, 7, 12, 15, 30)
print("specific date and time",dt) 

# Formatting dates and times
formated_date = current.strftime("%d-%m-%Y %H:%M:%S")
print("format the date and time",formated_date)

# date time calculation
future_date = current + timedelta(days=10)
print("Date 10 days from now:", future_date)
past_date = current - timedelta(days=10)
print("Date 10 days ago:", past_date)

# combine date and time
d = date(2024, 7, 12)
t=time(5,30)
combined = datetime.combine(d, t)
print("Combined datetime:", combined)

