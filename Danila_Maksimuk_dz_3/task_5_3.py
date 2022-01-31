nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

import random
from random import choice

def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""
    list_out = []
    joke = ()
    i = 0
    while i < count:
        joke = (choice(nouns), choice(adverbs), choice(adjectives))
        joke_str = ' '.join(joke)
        list_out.append(joke_str)
        joke = ()
        i += 1
    return list_out


print(get_jokes(2))
print(get_jokes(10))