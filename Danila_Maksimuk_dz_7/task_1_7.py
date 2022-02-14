import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

project_name = 'my_project'
folders = [['settings', []], ['mainapp', []], ['adminapp', []], ['authapp', []]]


full_path = os.path.join(BASE_DIR, project_name)


def create_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)


def build_structure(root, data):
    if data:
        for d in data:
            name = d[0]
            path = os.path.join(root, name)
            create_folder(path)
            build_structure(path, d[1])


create_folder(full_path)
build_structure(full_path, folders)





