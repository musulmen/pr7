def valid_input(value):
    if value == "":
        return False
    try:
        float(value)
        return True
    except ValueError:
        return False


def main():
    a_input = input("Введите значение a: ")
    b_input = input("Введите значение b: ")
    c_input = input("Введите значение c: ")

    if valid_input(a_input) and valid_input(b_input) and valid_input(c_input):
        a = float(a_input)
        b = float(b_input)
        c = float(c_input)

        if b == 0:
            print("Ошибка: b не должно быть равно нулю.")
            main()

        x = (a / b) + (c * a)
        print(f"Решение уравнения: x = {x}")
    else:
        print("Ошибка: все значения должны быть числами.")
        main()

main()
