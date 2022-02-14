import shutil
import os

for f in os.walk("my_project_2"):

    for files in f[1]:
        if f == 'templates':
            shutil.copytree(os.path.join(f[0], f[1]), 'my_project_2/templates', dirs_exist_ok=True)
