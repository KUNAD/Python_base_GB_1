def convert_time(duration: int) -> str:
    if duration < 60:
        print(duration, ' сек')
    if (duration >= 60) and (duration < 3600):
        m = duration // 60
        s = duration % 60
        print(m, ' мин', s, ' сек')
    if (duration >= 3600) and (duration < 86400):
        h = duration // 3600
        duration = duration - (3600 * h)
        m = duration // 60
        duration = duration - (60 * m)
        s = duration
        print(h, 'час(ов)', m, ' мин', s, ' сек')
    if duration >= 86400:
        d = duration // 86400
        duration = duration - (86400 * d)
        h = duration // 3600
        duration = duration - (3600 * h)
        m = duration // 60
        duration = duration - (60 * m)
        s = duration
        print(d, ' дней', h, 'час(ов)', m, ' мин', s, ' сек')

    return 0

dur = input('Введите время в секундах: ')
dur = int(dur)
convert_time(dur)