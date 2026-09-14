first_room = input("Введите название первой аудитории: ")
second_room = input("Введите название второй аудитории: ")

print(f"Исходные значения: {first_room}, {second_room}")

room = first_room
first_room = second_room
second_room = room
print(f"Результат: {first_room}, {second_room}")