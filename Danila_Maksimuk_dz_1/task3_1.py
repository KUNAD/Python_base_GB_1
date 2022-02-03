def transform_string(number: int) -> str:
    """Возвращает строку вида 'N процентов' с учётом склонения по указанному number"""
    if number % 10 == 1 and number // 10 != 1:
        end = ''
        print(number, "Процент{}".format(end))
    if number % 10 == 2 and number // 10 != 1:
            end = 'а'
            print(number, "Процент{}".format(end))
    if number % 10 == 3 and number // 10 != 1:
        end = 'а'
        print(number, "Процент{}".format(end))
    if number % 10 == 4 and number // 10 != 1:
        end = 'а'
        print(number, "Процент{}".format(end))
    if number % 10 == 5:
        end = 'ов'
        print(number, "Процент{}".format(end))
    if number % 10 == 6:
        end = 'ов'
        print(number, "Процент{}".format(end))
    if number % 10 == 7:
        end = 'ов'
        print(number, "Процент{}".format(end))
    if number % 10 == 8:
        end = 'ов'
        print(number, "Процент{}".format(end))
    if number % 10 == 9:
        end = 'ов'
        print(number, "Процент{}".format(end))
    if number % 10 == 0:
        end = 'ов'
        print(number, "Процент{}".format(end))

    return number

for n in range(1, 101):
    transform_string(n)
