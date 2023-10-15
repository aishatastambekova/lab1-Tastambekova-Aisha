#код в котором может возникнуть исключение помещено в try
try:
    #ввод длины ребра
    edge_length=int(input('Введите длину ребра куба: '))
    #рассчет объема куба
    volume = edge_length**3
    #рассчет площади поверхности куба
    area = 6*edge_length**2
    #вывод на экран значения объема и площади с использованием f-строки
    print(f"Volume= {volume} \n Total surface area = {area}")
except ValueError:
    print("Ввод данных неверный")
