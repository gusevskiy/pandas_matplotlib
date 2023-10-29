import os
from datetime import timedelta

import matplotlib.pyplot as plt
import pandas as pd


def check_file():
    """
    Проверка существованиея файла Excel
    C:\robots\bit_analytics_three\call_recording
    Если он есть, возвращаем ссылку на него
    """
    path_file = ".\\"
    for file in os.listdir(path_file):
        if file.endswith('.xlsx'):
            if not file:
                print("пусто")
            return path_file + os.path.join(file)


def sum_time(timeList):
    """
    Получает на вход массив
    ["12-10-2023 09:15:51", "00:23:34", "01:32:21"]
    return 40306 количество секунд
    """
    sum_time = timedelta()
    for i in timeList:
        hour, minutes, seconds = i[-8::].split(':')  # отрезается дата если она есть
        hour, minutes, seconds = int(hour), int(minutes), int(seconds)
        sum_time += timedelta(hours=hour, minutes=minutes, seconds=seconds)
    sum_time = int(sum_time.total_seconds())
    return sum_time

def list_managers(column: str) -> list:
    """
    Функция принимает столбец (ex['Кто звонил']) из DateFrame
    возвращает set содаржащие ФИО в столбце
    """
    list_managers = []
    for i in set(column):
        if any(char.isalpha() for char in i):
            list_managers.append(i)
    return list_managers


def create_time_list(manager: list, frame: pd.DataFrame) -> list:
    """
    Принимает список манагеров и весь DataFrame (ex) см main()
    """
    first_time = 32400  # начало рабочего дня 9:00
    end_time = 61200  # конец рабочего дня 17:00 
    time_interval = []
    for i, y in frame.iterrows():
        if y['Операция'] == "Звонок" and (
            y['Кто звонил'] == manager or y['Кому звонил'] == manager
        ):
            # Массив строк дат с временем из DataFrame
            ar = [y['Дата'], y['Время разговора'], y['Время ожидания']]
            second_time = sum_time(ar)  # получаем сумму секунд
            # result = (first_time - second_time)//60  # из первого времени вычитаем следующие, переводим в минуты
            time_interval.append([first_time, second_time])  # добавляем минуты в масиив
            first_time = second_time  # делаем второе время первым.
        # для посчета времени от последнего звонка до конца рабочего дня.
        if i == len(frame)-1:
            result_end = (first_time - end_time)//60
            time_interval.append([first_time, end_time, result_end])
    return time_interval


def save_schedule(manager, time_list):
    plt.figure()
    plt.title(manager.split(' ')[0])
    plt.xlabel('колличество')
    plt.ylabel('интенсивность')
    plt.plot(time_list)
    plt.grid()
    # plt.show()
    plt.savefig(
        f"C:\\robots\\bit_analytics_three\\call_recording\\{manager.split(' ')[0]}.png"
    )


def main():
    # Ищем Excel
    path_to_file = check_file()
    # Читаем Excel
    ex = pd.read_excel(path_to_file)
    # Заполнем пустые ячейки в DataFrame нулями 00:00:00
    ex[['Время разговора', 'Время ожидания']] = ex[
        ['Время разговора', 'Время ожидания']
    ].fillna('00:00:00')
    # Формируем список манагеров
    managers = list_managers(ex['Кто звонил'])
    for manager in managers:
        # Массив манагеров и DataRfame
        time_list = create_time_list(manager, ex)
        # Сохраняем график
        # save_schedule(manager, time_list)
        print(time_list)

if __name__ == '__main__':
    main()
    # print(check_file())
    # path_file = "C:\\robots\\bit_analytics_three\\call_recording\\"
    # print(os.listdir(path_file))
