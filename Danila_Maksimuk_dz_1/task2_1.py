def sum_list_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    dataset = list(range(1, 1001, 2))
    j = 0
    while j < (len(dataset)):
        dataset[j] = dataset[j] ** 3
        j += 1
    z = 0
    sum_digit = 0
    sum = 0
    n = 0
    while z <(len(dataset)):
        n = dataset[z]
        while n > 0:
            digit = n % 10
            sum_digit += digit
            n = n // 10
        if sum_digit % 7 == 0:
                sum += dataset[z]
        sum_digit = 0
        z += 1

    return sum  # Верните значение полученной суммы

def sum_list_2(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
        сумма цифр которых делится нацело на 7
        Задачу решил не создавая новый список!!!! (Т.Е. в этой функции реализованы подпункты b) и c)"""
    dataset = list(range(1, 1001, 2))
    j = 0
    while j < (len(dataset)):
        dataset[j] = dataset[j] ** 3 + 17
        j += 1
    z = 0
    sum_digit = 0
    sum = 0
    n = 0
    while z < (len(dataset)):
        n = dataset[z]
        while n > 0:
            digit = n % 10
            sum_digit += digit
            n = n // 10
        if sum_digit % 7 == 0:
            sum += dataset[z]
        sum_digit = 0
        z += 1
    return sum  # Верните значение полученной суммы



my_list = []  # Соберите нужный список по заданию
result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)