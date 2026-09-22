pages = int(input("Введите количество страниц: "))
copybook = int(input("Введите количество страниц в тетради: "))

remains = pages % copybook
book = (pages - remains) // copybook
total_book_min = book + 1

if copybook >= 0:
    print(f"Количество полностью заполненных тетрадей: {book}")
    print(f"Остаток страниц: {remains}")
    print(f"Минимальное количество тетрадей для всех страниц: {total_book_min}")
else:
    print("Ввели отрицательное количество страниц в тетради")