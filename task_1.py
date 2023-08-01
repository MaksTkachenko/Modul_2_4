# Реалізувати менеджер контексту Timer, який вимірює час виконання блоку коду.
# Контекстний менеджер повинен виводити час, що минув, при виході з контексту.
# Використовуйте контекстний менеджер для вимірювання часу виконання певного
# фрагменту коду. Реалізувати контекстний менеджер потрібно 2 способами, за
# допомогою декоратора contextmanager та за допомогою класу.

import time
c

set_range = int(100000)


class Timer:
    """context manager using a class"""

    def __enter__(self):
        print("Creating a context manager using a class")
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()

        work_time = self.end_time - self.start_time
        print(f"Program execution time: {work_time}")


with Timer():
    for _ in range(set_range):
        pass

print("\n")


@contextmanager
def my_context():
    """context manager for using the contextmanager decorator"""

    print("Creating a context manager for using the contextmanager decorator")
    start_time = time.time()
    yield

    end_time = time.time()
    work_time = end_time - start_time
    print(f"Program execution time: {work_time}")


with my_context():
    for _ in range(set_range):
        pass
