# Створіть контекстний менеджер DividerContext, який буде прінтити символ, який
# ми до нього передамо як розділитель для основного блоку коду до та після його
# виконання. Реалізувати контекстний менеджер потрібно 2 способами, за допомогою
# декоратора contextmanager та за допомогою класу.

from contextlib import contextmanager

sym = input("enter: ")


class DividerContext:

    def __init__(self, symbol):
        self.symbol = symbol

    def __enter__(self):
        print(self.symbol * 20)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"\n{self.symbol * 20}")


with DividerContext(sym):
    for i in range(1, 11):
        print(i, end=' ')


@contextmanager
def divide_context(symbol):
    print(symbol * 20)
    yield

    print(f"\n{symbol * 20}")


with divide_context(sym):
    for i in range(10, 0, -1):
        print(i, end=' ')

