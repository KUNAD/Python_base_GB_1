

def thesaurus(*args) -> dict:
    dict_out = {}
    for arg in args:
        first_letter = arg[0]
        dict2 = {first_letter: arg}
        if first_letter not in dict_out:
            dict_out.update(dict2)
        else:
            dict_out[first_letter] = dict_out[first_letter] + ', ' +  arg


    return dict_out


print(thesaurus("Иван", "Мария", "Петр", "Илья"))