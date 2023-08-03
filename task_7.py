# Створіть декоратор **`rate_limit`**, який обмежує кількість викликів декорованої функції
# протягом певного періоду часу. Декоратор повинен приймати два параметри `max_calls` та `period`.
# Перший парметр - максимальна кількість допустимих викликів функції.
# Другий параметр - кількість секунд у рамках яких ми можемо зробити `max_calls`викликів.
# Вам допоможе модуль `datetime` для вирішення цієї задачі.

import time


def rate_limit(max_calls, period):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            for _ in range(max_calls):
                result = func(*args, **kwargs)
                end_time = time.time() - start_time

                if end_time > period:
                    print(f"Exceeded period ({period}) for {max_calls} attempt")
                    return result
        return wrapper
    return decorator


@rate_limit(max_calls=5, period=10)
def my_function():
    res = 0
    for _ in range(100000):
        res = 12434533 * 76 / 777892 ** 345
    print(res)


my_function()
