from datetime import datetime, time
import pandas

ex = pandas.read_excel('count_time.xlsx')

# Исходный массив временных интервалов
rw = datetime.strptime(f"{ex['Время разговора'].tolist()[19]}", "%H:%M:%S").time()
ty = datetime.strptime(f"{ex['Время ожидания'].tolist()[19]}", "%H:%M:%S").time()
hj = datetime.strptime(f"{ex['Дата'].tolist()[19]}", "%d-%m-%Y %H:%M:%S").time()
# print(hj)
intervals = [rw, ty, hj]

# Преобразование временных интервалов в объекты datetime.time и вычисление суммы
total_seconds = 0
for interval in intervals:
    # time_format = "%H:%M:%S"
    # time_obj = datetime.strptime(interval, time_format).time()
    total_seconds += interval.hour * 3600 + interval.minute * 60 + interval.second

# Преобразование общего количества секунд в datetime.time
result_time = time(total_seconds // 3600, (total_seconds % 3600) // 60, total_seconds % 60)

print(result_time)
