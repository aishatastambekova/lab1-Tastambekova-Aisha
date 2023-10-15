#код в котором может возникнуть исключение помещено в try
try:
    #вводим две цифры и операцию плюс минус деление умножение
    num_first=int(input("Please enter the first number: "))
    num_second=int(input("Please enter the second number: "))
    operation=int(input("Please choose the operation (+,-,*,/): "))
    if operation=="+" :
        sum=num_first+num_second
        print(sum)
    if operation== "-":
        subst=num_first-num_second
        print(subst)
    if operation== "*":
        mult= num_first * num_second
        print(mult)
    else:
        div=num_first / num_second
        print(div)
except ZeroDivisionError:
    print("Деление на ноль")
except ValueError:
    print("Вод данных неверный")

