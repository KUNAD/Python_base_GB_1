tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Коля', 'Данила']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def check_gen(tutors: list, klasses: list):
    i = 0
    for code in tutors:
        if i + 1 > len(klasses):
            my_cortege = (tutors[i], None)
            yield(my_cortege)
        else:
            my_cortege = (tutors[i], klasses[i])
            yield(my_cortege)
        i += 1



generator = check_gen(tutors, klasses)
print(type(generator))
for _ in range(len(tutors)):
    print(next(generator))