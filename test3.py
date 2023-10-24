'''сдесь складывается время в строчном формате'''

from datetime import timedelta


timeList = ["12-10-2023 09:15:51", "00:23:34", "01:32:21"]

def sum_time(timeList):
    total_time = timedelta()
    for i in timeList:
        hour, minutes, seconds = i[-8::].split(':')
        hour, minutes, seconds = int(hour), int(minutes), int(seconds)
        total_time += timedelta(hours=hour, minutes=minutes, seconds=seconds)
        a = total_time.total_seconds()
    return a
    
print(sum_time(timeList))