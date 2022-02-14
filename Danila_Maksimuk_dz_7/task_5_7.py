import os
import random
from string import ascii_lowercase, digits

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

letters = ''.join([ascii_lowercase, digits])
folder = os.path.join(BASE_DIR, 'some_data')
os.makedirs(folder, exist_ok=True)
for _ in range(15):
   f_name = ''.join(random.sample(letters, random.randint(5, 10)))
   f_content = bytes(random.randint(0, 255)
                     for _ in range(random.randrange(10 ** 3)))
   with open(os.path.join(folder, f'{f_name}.bin'), 'wb') as f:
       f.write(f_content)

# our_dict = {}
# if os.path.exists(folder):
#     very_small_files = [f for f in os.scandir(folder) if f.stat().st_size <= 100]
#     our_dict[100] = len(very_small_files)
#     small_files = [f for f in os.scandir(folder) if f.stat().st_size >= 100 and f.stat().st_size <= 1000]
#     our_dict[1000] = len(small_files)
#     files = [f for f in os.scandir(folder) if f.stat().st_size >= 1000 and f.stat().st_size <= 10000]
#     our_dict[10000] = len(files)
#     big_files = [f for f in os.scandir(folder) if f.stat().st_size >= 10000 and f.stat().st_size < 100000]
#     our_dict[100000] = len(big_files)
#
# print(our_dict)
if os.path.exists(folder):
    our_dict = {10 ** x: 0 for x in range(2, 6)}
    for f in os.scandir(folder):
        for key in sorted(our_dict.keys()):
            if f.stat().st_size > key:
                continue
            else:
                our_dict[key] += 1
                break

print(our_dict)




