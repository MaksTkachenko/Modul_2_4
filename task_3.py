# Створіть простий декоратор логування log_func, який буде прінтити будь яке
# повідомлення перед визовом декорованої функції, та після.


def log_func(factorial):
    def print_fun():
        print(30 * '^')
        factorial()
        print(35 * '^')
    return print_fun


@log_func
def print_factorial():
    number = input("Entre any number: ")

    if number.isdigit():

        number = int(number)

        if number <= -1:
            print("The specified number cannot be negative!!!")
        if number == 0:
            print("0! = 1")
        else:
            fact = 1

            for i in range(1, number + 1):
                fact *= i
            print(f"{number}! = {fact}")
    else:
        print("You entered the wrong number!!!")


print_factorial()
