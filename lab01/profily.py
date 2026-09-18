username = input("Введите фамилию:")
name = input("Введите имя:")
group = input("Введите группу:")
town = input("Введите город:")
age = int(input("Введите возраст:"))
love_pred = input("Введите любимый предмет:")
time = int(input("Введите количество часов подгтовки в неделю:"))
full_name = name + " " + username
age4 = age + 4
time_ned = time * 7
time_cred = time_ned / 7
print("Учебная карточка:")
print(f"Имя и фамилия: {full_name}")
if 1 < age < 120:
    print(f"Возраст через 4 года: {age4}")
else:
    print("Неверный ввод возраста")
if time > 0:
    print(f"Время подготовки за 4 недели:{time_ned}")
else:
    print("Неверный ввод времени")
if time_cred > 0:    
    print(f"В среднем в день: {time_cred:.2f}ч")
