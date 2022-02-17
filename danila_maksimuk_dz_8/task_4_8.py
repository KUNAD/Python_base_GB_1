from my_exeptions import FuncError



def val_checker(func):
    def wrapper(arg):
        if isinstance(arg, int) and arg <= 0:
            raise FuncError('Наше значение должно быть целочисленным и положительным')

        return func(arg)
    return wrapper


@val_checker
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x ** 3


print(calc_cube(5))
print(calc_cube('ss'))
print(calc_cube(-5))

