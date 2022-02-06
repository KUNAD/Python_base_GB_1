def convert_name_extract(list_in: list) -> list:
    """Извлекает имена из элементов и формирует список приветствий."""
    i = 0
    list_out = []
    while i < (len(list_in)):
        element = list_in.pop(i)
        element_list = element.split(' ')
        name = element_list.pop()
        list_test = ["Привет, ", name.title(), "!"]
        element_str = "".join(list_test)
        list_out.append(element_str)

    return list_out


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)


