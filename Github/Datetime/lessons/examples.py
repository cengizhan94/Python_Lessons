from datetime import datetime

now = datetime.now()
print(now)

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
seond = now.second
timestamp = now.timestamp()

print(day,month,year,hour,minute)
print("timestamp: ",timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')