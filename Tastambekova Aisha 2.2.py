try:
        # Запрос на ввод четырехзначного числа
        number = int(input("Введите четырехзначное число: "))
        thousands = number // 1000
        hundreds = (number // 100) % 10
        tens = (number // 10) % 10
        ones = number % 10

        print("Цифры числа:")
        print("Тысячи:", thousands)
        print("Сотни:", hundreds)
        print("Десятки:", tens)
        print("Единицы:", ones)

except ValueError as e:
        print("Ошибка:", e)
