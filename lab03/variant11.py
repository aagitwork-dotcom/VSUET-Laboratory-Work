parking = int(input("Введите число от 0 до 100: "))
if 0 <= parking <= 59:
    print("Много мест на парковке")
elif 50 <= parking <= 89:
    print("Мало мест на парковке")
elif 90 <= parking <= 100:
    print("Парковка почти занята")

if parking > 100 or parking < 0:
    print("Ошибка диапозона")