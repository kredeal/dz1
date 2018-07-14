# По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из этих отрезков.
#  Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.

segment1 = float(input('Введите длину первого отрезка (положительное число): '))
segment2 = float(input('Введите длину второго отрезка (положительное число): '))
segment3 = float(input('Введите длину третьего отрезка (положительное число): '))

if segment1 + segment2 > segment3 and segment1 + segment3 > segment2 and segment2 + segment3 > segment1:
    print('\nТреугольник существует',end='')
    if segment1 == segment2 == segment3:
        print(', и он равносторонний\n')
    elif segment1 == segment2 or segment1 == segment3 or segment2 == segment3:
        print(', и он равнобедренный\n')

else:
    print('Треугольника с такими сторонами не существует')