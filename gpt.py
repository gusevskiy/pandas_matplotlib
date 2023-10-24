from datetime import datetime, time

# Исходные временные интервалы
interval1 = "09:26:50"
interval2 = "00:00:52"

# Преобразование временных интервалов в объекты datetime.time
time_format = "%H:%M:%S"
time1 = datetime.strptime(interval1, time_format).time()
time2 = datetime.strptime(interval2, time_format).time()

# Сложение интервалов
total_seconds = (time1.hour + time2.hour) * 3600 + (time1.minute + time2.minute) * 60 + (time1.second + time2.second)
result_time = time(total_seconds // 3600, (total_seconds % 3600) // 60, total_seconds % 60)

print(result_time)