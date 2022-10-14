def get_expression():
    return str(input("Введите выражение: "))

def result_output(user_expression, user_result):
    if not user_result == False:
        print(f"Результат решения выражения {user_expression} равен {user_result}")
    else:
        print(f"Вы ввели недопустимую операцию")
