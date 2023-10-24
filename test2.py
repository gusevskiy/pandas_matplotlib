from datetime import datetime, timedelta
 

first_time = datetime.strptime("12-10-2023 09:00:00", "%d-%m-%Y %H:%M:%S")

# получить из даты только минуты
print(first_time.minute)

numdays = 10
# dateList = [first_time + timedelta(minutes=x) for x in range(numdays)]

dateList = []

for i in range(1,540):
    res = first_time + timedelta(minutes=i)
    dateList.append(res.strftime("%H:%M"))



# print(first_time)
print(dateList)