def num_translate(value: str) -> str:
    """переводит числительное с английского на русский """
    if value != ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"):
        str_out = None
    if value == "one":
        str_out = "один"
    if value == "two":
        str_out = "два"
    if value == "three":
        str_out = "три"
    if value == "four":
        str_out = "четыре" 
    if value == "five":
        str_out = "пять"
    if value == "six":
        str_out = "шесть"
    if value == "seven":
        str_out = "семь"
    if value == "eight":
        str_out = "восемь"
    if value == "nine":
        str_out = "девать"
    if value == "ten":
        str_out = "десять"
    if value == "zero":
        str_out = "нуль"
    return str_out

print(num_translate("one"))
print(num_translate("eight"))
print(num_translate("eleven"))







