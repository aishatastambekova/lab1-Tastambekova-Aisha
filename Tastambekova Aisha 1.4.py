#код в котором может возникнуть исключение помещено в try
try:
    #ввод трех цифр
    num1=int(input())
    num2=int(input())
    num3=int(input())
    #рассчет суммы трех цифр
    sum=num1+num2+num3
    #вывод полученной суммы с использованием f-строки
    print(f"Полученная сумма sum= {sum}")
except ValueError:
    print("Ввод данных неверный")
