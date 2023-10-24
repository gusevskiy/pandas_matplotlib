import pandas
from datetime import datetime



ex = pandas.read_excel('count_time.xlsx')

# start_day = datetime.strptime(f"{ex['Дата'].tolist()[0]}", "%d-%m-%Y %H:%M:%S")
first_time = datetime.strptime("12-10-2023 09:00:00", "%d-%m-%Y %H:%M:%S")
second_time = datetime.strptime("12-10-2023 09:15:51", "%d-%m-%Y %H:%M:%S")

print(second_time - first_time)

time_interval = []

for i, y in ex.iterrows():
    # print(datetime.strptime(f"{y['Дата']}", "%d-%m-%Y %H:%M:%S"))
    # bell = ex['Операция'].tolist()[i]
    # who_called = ex['Кто звонил'].tolist()[i]
    if y['Операция'] == "Звонок" and y['Кто звонил'] == 'Бойцун Марина Викторовна (3082)':
        # print(y['Кто звонил'])
        res = datetime.strptime(f"{y['Дата']}", "%d-%m-%Y %H:%M:%S")
        result = first_time - res
        # print(res, '-', first_time, '=', result)
        time_interval.append(int(result.total_seconds()//60))
        first_time = res

# re = datetime.strptime(f"{ex['Дата'].tolist()[0]}", "%d-%m-%Y %H:%M:%S")

print(time_interval)
