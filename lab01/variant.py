order = input("Введите название заказа:")
customer = input("Введите имя заказчика:")
seedlings = input("Введите название саженца:")
seedlings_quantity = int(input("Введите количество саженцев:"))
seedlings_price = float(input("Введите цену саженца в рублях:"))
pots = input("Введите название горшка:")
pots_quantity = int(input("Введите количество горшков:"))
pots_price = float(input("Введите цену горшка в рублях:"))
delivery_cost = float(input("Введите стоимость доставки:"))
sum = float(input("Введите внесённую сумму"))
value_seedlings = (seedlings_quantity * seedlings_price) 
value_pots = (pots_quantity * pots_price) 
total_cost = value_pots + value_seedlings + delivery_cost
total_quantity = seedlings_quantity + pots_quantity
change = sum - total_cost
print("Ваш заказ:")
print(f"Имя заказчика: {customer}")
if seedlings_quantity >= 0 and seedlings_price > 0:
    print(f"{order} | {seedlings_quantity:.2f} | {seedlings_price:.2f} | {value_seedlings:.2f}")
else:
    print("Вы допустили ошибку при вводе количества саженцов или их стоимости")
if pots_quantity >= 0 and pots_price > 0:
    print(f"{order} | {pots_quantity:.2f} | {pots_price:.2f} | {value_pots:.2f}")
else:
    print("Вы допустили ошбку при вводе количества коршков или их стоимости")
if delivery_cost > 0:
    print(f"Общая стоимость заказа: {total_cost:.2f}")
    print(f"Внесённая сумма: {sum:.2f}")
    print(f"Сдача: {change:.2f}")
