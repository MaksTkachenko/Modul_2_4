# Реалізувати декоратор кешування memoize, який кешує результати декорованої
# функції для покращення продуктивності при повторних викликах з тими самими
# аргументами. Тобто він повинен запамʼятовувати аргументи з якими функція
# визивалась і результат роботи функції з цими аргументами. І у випадку, якщо ми
# вже маємо результат для цих аргументів, просто повернути закешований результат,
# замість виклику функції.


import time


def memoize(func):
    memoize_cache = {}

    def wrapper(*args):
        if args in memoize_cache:
            print("Already in memory")
            return memoize_cache[args]
        else:
            result = func(*args)
            memoize_cache[args] = result
            print("Result saved")
            return result
    return wrapper


@memoize
def test_fun(x, y):
    res = 0
    for _ in range(100000):
        res = x * 76 / y ** 345
    return res


def work_time(x_2, y_2):
    stat_time = time.time()
    print(f"{x_2} * 76 / {y_2} ** 345={test_fun(x_2, y_2)}")
    end_time = time.time()
    print(f"Execution time: {end_time - stat_time} sec\n")


work_time(125231, 64434)
work_time(5532342, 765456)
work_time(125231, 64434)
work_time(3123, 872)
