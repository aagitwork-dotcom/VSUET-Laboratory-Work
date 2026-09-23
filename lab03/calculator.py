x = float(input("Введите первое число: "))
y = float(input("Введите второе число: "))
znak = input("Введите одну из операций(+, -, *, /): ")

if znak in "+":
    print(f"{x + y:.2f}")
elif znak in "-":
    print(f"{x - y:.2f}")
elif znak in "*":
    print(f"{x * y:.2f}")
elif znak in "/":
    if y == 0:
        print("Деление на ноль запрещено")
    else:
        print(f"{x / y:.2f}")