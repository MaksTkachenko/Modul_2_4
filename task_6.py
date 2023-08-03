# Реалізувати декоратор кешування memoize, який кешує результати декорованої
# функції для покращення продуктивності при повторних викликах з тими самими
# аргументами. Тобто він повинен запамʼятовувати аргументи з якими функція
# визивалась і результат роботи функції з цими аргументами. І у випадку, якщо ми
# вже маємо результат для цих аргументів, просто повернути закешований результат,
# замість виклику функції.


import time


def memoize(func):
    memoize_cache = {}

    def wrapper():
        if 'result' not in memoize_cache:
            memoize_cache['result'] = func()
            print("Result saved")
        else:
            print("Already in memory")
        return memoize_cache['result']
    return wrapper


@memoize
def test_fun():
    res = 0
    for _ in range(100000):
        res = 12434533 * 76 / 777892 ** 345
    return res


def work_time():
    stat_time = time.time()
    print(test_fun())
    end_time = time.time()
    print(f"Execution time: {end_time - stat_time} sec\n")


for _ in range(5):
    work_time()
