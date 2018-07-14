# Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.



# Числа могут быть введены пользователем, просто раскоментируйте 4 нижележащих строки
# a = input('Введите первое число, a = ')
# b = input('Введите второе число,b = ')
# a = int(a)
# b = int(b)

a = 5
b = 6

print()
print('Логическое "И", {} & {} '.format(a,b))
print('Решение: {} & {} = {} = {}'.format(bin(a),bin(b),bin(a&b),a&b))
print()
print('Логическое "ИЛИ", {} | {}  '.format(a,b))
print('Решение: {} | {} = {} = {}'.format(bin(a),bin(b),bin(a|b),a|b))
print()
print('Логическое "Исключительное ИЛИ", {} ^ {}  '.format(a,b))
print('Решение: {} ^ {} = {} = {}'.format(bin(a),bin(b),bin(a^b),a^b))
print()
print('Бинарный комплиментарный оператор, ~a ')
print('~ {} = {} = {}'.format(bin(a),bin(~a),~a))
print('Бинарный комплиментарный оператор, ~b ')
print('~ {} = {} = {}'.format(bin(b),bin(~b),~b))
print()
print('Побитовый сдвиг {} влево на 2'.format(a))
print('Решение:\n'
      '1) {} = {}\n'
      '2) {} << 2 = {} = {}\n'.format(a,bin(a),bin(a),bin(a << 2), a << 2))
print('Побитовый сдвиг {} вправо на 2 '.format(a))
print('Решение:\n'
      '1) {} = {}\n'
      '2) {} >> 2 = {} = {}'.format(a,bin(a),bin(a),bin(a >> 2), a >> 2))

