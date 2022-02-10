import sys
import json


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """
    users_list = []
    with open(path_users_file, 'r', encoding='utf-8') as fr:
        for line in fr:
            users_list.append(line.replace(',', ' '))

    hobby_list = []
    with open(path_hobby_file, 'r', encoding='utf-8') as fr:
        for line in fr:
            hobby_list.append(line)

    all_we_need_is_dict = {}
    if len(users_list) >= len(hobby_list):
        while len(users_list) > len(hobby_list):
            hobby_list.append(None)
        index = 0
        for name in users_list:
            all_we_need_is_dict[name.strip()] = hobby_list[index].strip().split(',')
            index += 1
    else:
        all_we_need_is_dict = sys.exit(1)

    return all_we_need_is_dict


dict_out = prepare_dataset('users.csv', 'hobby.csv')
print(dict_out)
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)