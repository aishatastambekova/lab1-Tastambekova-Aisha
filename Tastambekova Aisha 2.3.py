#код в котором может возникнуть исключение помещено в try
try:
    #вводим число
    num=int(input())
    #определяем округленное число
    odd=(num+1)//2
    #вывод округленного числа
    print(odd)
except ValueError:
    print("Ввод данных неверный")
