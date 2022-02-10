import sys

with open('bakery.csv', 'a+', encoding='utf-8') as fa:
    fa.writelines(sys.argv[1])
    fa.write(' '*30)
    fa.write('\n')