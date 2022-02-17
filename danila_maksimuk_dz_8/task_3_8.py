from functools import wraps


def type_logger(func):
    """Декоратор наей функции"""
    @wraps(func)
    def wrapper(*args):
        """Здесь логируем и выводим имя функции и словарь с нащим значением в виде ключа и тип нашего значения(для того , чтобы выводить сразу несколько аргументов)"""
        our_dict_of_logs = {}
        our_list = [*args]
        for key in our_list:
            our_dict_of_logs[key] = type(key)
            print(func.__name__, our_dict_of_logs)
        return func(*args)
    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(5)




