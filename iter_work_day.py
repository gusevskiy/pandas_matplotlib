from datetime import datetime

# получаем только дату
date_today = datetime.now().date()

# получаем время начала рабочего дня в формате datetime
start_day = datetime.strptime(
    f"{str(date_today)} 09:00", "%Y-%m-%d %H:%M"
)

# получаем время окончания рабочего дня в формате datetime
end_day = datetime.strptime(
    f"{str(date_today)} 18:00", "%Y-%m-%d %H:%M"
)


work_day_minute = []
# итерируемся по интервалу рабочего дня в минутах.
# for i in range(int((end_day-start_day).total_seconds()/60)):
    # work_day_minute.append(i)
for i in range(int((end_day-start_day))):
    work_day_minute.append(i)

print(work_day_minute)