def is_valid_input(value):
    if value == "":
        return False
    try:
        float(value)
        return True
    except ValueError:
        return False

def decimal_to_nine_base(n):
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        result = str(n % 9) + result
        n //= 9
    return result

def main():
    user_input = input("Введите число: ")

    if is_valid_input(user_input):
        decimal_number = int(float(user_input))  # Берем целую часть
        positive_number = abs(decimal_number)
        nine_number = decimal_to_nine_base(positive_number)

        if decimal_number < 0:
            print(f"Число {decimal_number} в девятеричной системе: -{nine_number}")
        else:
            print(f"Число {decimal_number} в девятеричной системе: {nine_number}")
    else:
        print("Ошибка: ввод должен быть числом.")
        main()

main()
