import math, os, time

def polygon():
    num_n = int(input("Введите количество сторон: "))
    num_s = float(input("Введите длину стороны: "))
    time_begin = time.time()
    def the_bomb(n_sides, length):
        area = (n_sides * (length ** 2)) / (4 * math.tan((math.pi) / n_sides))
        print('Результат: ',area,'\n')
    the_bomb(num_n, num_s)
    print ('Время выполнения функции: ', float(time.time()-time_begin))

def summ():
    count_n = int(input('Введите число первых N положительных чисел: '))
    time_begin = time.time()
    result_n = int(0)
    for number in range(count_n):
        result_n = result_n + number + 1
    print('Сумма первых ',count_n,'положительных чисел = ', result_n,'\n')
    print ('Время выполнения функции: ', float(time.time()-time_begin))

print(
    'Здравствуйте! Нажмите ..\n' 
    'P - для расчета многоугольника\n' 
    'S - для расчета суммы первых N положительных чисел\n'
    'Любую другую литеру - для завершения программы\n'
    )
key = input ()
if key == 'p': 
    print ('Была вызвана функция расчета площади правильного многоугольника\n')
    polygon ()
elif key == 's': 
    print ('Была вызвана функция расчета суммы первых N положительных чисел\n')
    summ()
else: 
    print ('Осуществлен выход из программы')

