import os
from datetime import timedelta, datetime

import matplotlib.pyplot as plt
import pandas as pd


path_folder = "C:\\Users\\VGGusevsky\\Documents\\BitAnalytics\\call_recording\\"


def check_file(path_folder):
    """
    Проверка существованиея файла Excel в папке
    Если он есть, возвращаем ссылку на него
    """
    path_file_exls = ""
    for file in os.listdir(path_folder):
        if file.endswith('.xlsx'):
            path_file_exls = path_folder + os.path.join(file)
    return path_file_exls

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
    first_time = 32400  # начало рабочего дня 9:00 в секундах
    end_time = 61200  # конец рабочего дня 17:00 в секундах
    time_interval = []
    for i, y in frame.iterrows():
        if y['Операция'] == "Звонок" and (
            y['Кто звонил'] == manager or y['Кому звонил'] == manager
        ):
            # Массив строк дат с временем из DataFrame
            ar = [y['Дата'], y['Время разговора'], y['Время ожидания']]
            second_time = sum_time(ar)  # получаем сумму секунд
            # добавляем секунды в масиив
            time_interval.append([first_time, second_time])
            first_time = second_time  # делаем второе время первым.
        # для посчета времени от последнего звонка до конца рабочего дня.
        if i == len(frame)-1:
            time_interval.append([first_time, end_time])
    return time_interval


def save_schedule(manager, time_list, path_folder):
    plt.figure()
    plt.title(f"{manager.split(' ')[0]} {datetime.today().strftime('%d-%m-%Y')}")
    plt.xlabel('колличество')
    plt.ylabel('интенсивность')
    time_for_graph = []
    for i in time_list:
        time_for_graph.append((i[0]-i[1])//60)
    plt.plot(time_for_graph)
    for i, v in enumerate(time_list):
        # Если отклонение > 20 мин. вывести текст на крафик.
        if (v[0]-v[1])//60 < -20:
            # Две переменные для отображения на графике без секунд.
            v0 = ':'.join(str(timedelta(seconds=v[0])).split(':')[:2])
            v1 = ':'.join(str(timedelta(seconds=v[1])).split(':')[:2])
            # i+1 один для смещения текста в право относительно минимальной точки на графике, чтоб лучше видно было.
            # set_rotation - наклон(вращение)
            # fontsize - размер текста на графике
            plt.text(i, (v[0]-v[1])//60-10, f"{v0}-{v1}", fontsize=7).set_rotation(75)
    plt.grid()
    plt.savefig(
        f"{path_folder}\\{manager.split(' ')[0]}.png"
    )


def main():
    # Ищем Excel
    path_to_file = check_file(path_folder)
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
        save_schedule(manager, time_list, path_folder)
        # print(time_list)

if __name__ == '__main__':
    main()
