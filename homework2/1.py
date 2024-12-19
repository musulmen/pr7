def convert_number():
    x = input('Введите целое число: ')

    if x.lstrip('-').isdigit():
        number = int(x)

        abs_number = abs(number)

        binary_number = bin(abs_number)[2:]
        octal_number = oct(abs_number)[2:]

        if number < 0:
            print(f'Число {number} в двоичной системе счисления: -{binary_number}')
            print(f'Число {number} в восьмеричной системе счисления: -{octal_number}')
        else:
            print(f'Число {number} в двоичной системе счисления: {binary_number}')
            print(f'Число {number} в восьмеричной системе счисления: {octal_number}')
    else:
        print('Ошибка: введите целое число.')
        convert_number()

convert_number()
