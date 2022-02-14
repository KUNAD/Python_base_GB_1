def odd_nums(number: int) -> int:
    """Генератор, возвращающий по очереди нечетные целые числа от 1 до number (включительно)"""
    nums_gen = (num for num in range(1, n + 1, 2))
    for num in range(1, n + 1, 2):
        print(next(nums_gen))


n = 15
odd_nums(n)


