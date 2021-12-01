import math, os

def polygon():
    num_n = int(input("Введите количество сторон: "))
    num_s = float(input("Введите длину стороны: "))
    def the_bomb(n_sides, length):
        area = (n_sides * (length ** 2)) / (4 * math.tan((math.pi) / n_sides))
        print('Результат: ',area)
    the_bomb(num_n, num_s)

def summ():
    N=int(input('Введите число N: '))
    rez=int(0)
    for number in range(N):
        rez=rez+number+1
    print('Сумма первых ',N,'положительных чисел = ', rez)

print(
    'Здравствуйте! Нажмите ..\n' 
    'P - для расчета многоугольника\n' 
    'S - для расчета суммы первых N положительных чисел\n'
    'Любую другую литеру - для завершения программы\n')
key = input ()
if key == 'p': 
    print ('Выполняется функция расчета площади правильного многоугольника\n')
    polygon ()
elif key == 's': 
    print ('Выполняется функция для расчета суммы первых N положительных чисел\n')
    summ()
else: 
    print ('Осуществлен выход из программы')

