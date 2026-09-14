first_subjest = input("Ввелите название первого предмета:")
second_subjest = input("Введите название второго предмета:")
quantity_first_subjest = int(input("Введите количество занятий в неделю по первому предмету:"))
quantity_second_subjest = int(input("Введите количесвто занятий в неделю по второму предмету:"))
time_one_subjest = int(input("Введите продолжительность одного занятия в минутах:"))
time_one_subjest_hour = time_one_subjest / 60
available_time = int(input("Введите доступное время на неделю в часах:"))
full_time = (quantity_first_subjest + quantity_second_subjest) * time_one_subjest
full_time_hour = ((quantity_first_subjest + quantity_second_subjest) * time_one_subjest) // 60
first_subjest_time = quantity_first_subjest * time_one_subjest
second_subjest_time = quantity_second_subjest * time_one_subjest
first_subjest_time_hour = quantity_first_subjest * time_one_subjest_hour
second_subjest_time_hour = quantity_second_subjest * time_one_subjest_hour
remaining_available_time = available_time - full_time_hour
full_time_hour_week = full_time_hour * 4
if quantity_first_subjest >= 0 and quantity_first_subjest % 1 == 0 and quantity_second_subjest >= 0 and quantity_second_subjest % 1 == 0 and available_time >= full_time_hour and time_one_subjest >= 0:
    print("Учебная нагрузка:")
    print(f"Время для первого предмета: {first_subjest_time}", "/", f"{first_subjest_time_hour:.2f}")
    print(f"Время для второго предмета: {second_subjest_time}", "/", f"{second_subjest_time_hour:.2f}")
    print(f"Время общей нагрузки: {full_time}", "/", f"{full_time_hour:.2f}")
    print(f"Остаток свободного времени: {remaining_available_time:.2f}")
    print(f"Нагрузка за 4 одинаковые недели: {full_time_hour_week:.2f}")