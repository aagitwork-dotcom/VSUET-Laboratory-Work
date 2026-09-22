notebook_price = float(input("Введите цену одной тетради: "))
notebook_count = int(input("Введите количество тетрадей: "))
cost = notebook_price * notebook_count
paid = float(input("Введите внесённую сумму: "))
change = paid - cost

if notebook_price >= 0:
    if notebook_count >= 0:
        if paid >= cost:
            print(f"Стоимость: {cost} | Сдача: {change}")
    else:
        print("Введино неверное количество тетрадей")
else:
    print("Введина неверная стоимость одной тетради")