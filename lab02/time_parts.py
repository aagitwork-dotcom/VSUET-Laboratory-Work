total_seconds_all = int(input("Введите количество секунд:"))

total_hour = total_seconds_all // 3600
total_minute = (total_seconds_all - (total_hour * 3600)) // 60
total_seconds = total_seconds_all - (total_hour * 3600 + total_minute * 60)

if total_seconds_all < 0:
    print("Неправильный ввод секунд")
else:
    print(f"{total_seconds_all} cек = {total_hour} ч {total_minute} мин {total_seconds} сек")