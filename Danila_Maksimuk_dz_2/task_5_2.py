from random import uniform




#Пункты A) B)
def transfer_list_in_str(list_in: list) -> str:
    """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
        формирует из них единую строковую переменную разделяя значения запятой."""
    i = 0
    list_out = []
    list_in.sort()
    print("Список по возрастанию - ", list_in)
    while i < (len(list_in)):
        element = list_in.pop(i)
        if element < 1:
            element = str(element)
            element_list = element.split('.')
            cents = element_list.pop(1)
            list_test = [cents, " кк"]
            element_str = "".join(list_test)
            list_out.append(element_str)

        if element > 1:
            element = str(element)
            element_list = element.split('.')
            rubles = element_list.pop(0)
            cents = element_list.pop(0)
            list_test = [rubles, " руб ", cents, " кк "]
            element_str = "".join(list_test)
            list_out.append(element_str)

    return list_out

my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]








#Список по убыванию C)
def sort_price_adv(list_in: list) -> list:
    """Создаёт новый список и возвращает список с элементами по убыванию"""
    new_list = []
    new_list.extend(list_in)

    new_list.sort(reverse=True)

    return new_list


result_3 = sort_price_adv(my_list)
print("Список по убыванию - ", result_3)


def check_five_max_elements(list_in: list) -> list:
    """Проверяет элементы входного списка вещественных чисел и возвращает
        список из ПЯТИ максимальных значений"""
    new_list = []
    new_list.extend(list_in)
    new_list.sort(reverse=True)
    list_out = []
    i = 0
    while i < 5:
        element = new_list.pop(0)
        list_out.append(element)
        i += 1

    return list_out


result_4 = check_five_max_elements(my_list)
print("Пять самых больших", result_4)



print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print("Результат - ", result_1)
















