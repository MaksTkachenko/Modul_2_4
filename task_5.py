# Створіть декоратор retry який приймає першим аргументом число - кількість
# разів, яку потрібно буде повторити виконання функції у разі викидання нею помилки.


def retry(num):
    def decorator(func):
        def wrapper(*args):
            attempts = 0
            while attempts < num:
                try:
                    result = func(*args)
                    return result
                except Exception as e_1:
                    attempts += 1
                    print(f"Error: {e_1}")
            return f"Function failed after {num} attempts."
        return wrapper
    return decorator


@retry(num=3)
def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is impossible!")
    else:
        return f"{a}/{b}={a / b}"


try:
    a_2 = int(input("Enter a: "))
    b_2 = int(input("Enter b: "))
    print(divide(a_2, b_2))
except Exception as e_2:
    print(f"Error: {e_2}")
