# Реалізувати декоратор timeit, який вимірює час виконання декорованої функції
# і виводить його. Для отримання часу роботи скористуйтесь модулем time і
# функцією time.time()

import time


def timeit(random_task):
    def wrapper():
        print("Time has passed!")
        start_time = time.time()
        random_task()
        end_time = time.time()
        print("Time has stopped!")
        print(f"Program execution time: {end_time - start_time}")
    return wrapper


@timeit
def fun_for():
    time.sleep(1)
    for i in range(1000000):
        pass


fun_for()
