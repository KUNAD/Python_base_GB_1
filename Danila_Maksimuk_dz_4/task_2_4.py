import requests


def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    currency_dict = {}
    currency_list = response.text.split('ID=')
    del currency_list[0]
    for element in currency_list:
        exchange_cource = element[(element.find('<Value>') + 7):element.find('</Value>')]
        exchange_cource = float(exchange_cource.replace(',', '.'))
        nominal = int(element[(element.find('<Nominal>') + 9):element.find('</Nominal>')])
        currency_dict[(element[(element.find('<CharCode>') + 10):element.find('</CharCode>')])] = exchange_cource/nominal
        result_value = currency_dict.get(code.upper())
    return result_value

if __name__ == '__main__':
    print(currency_rates("USD"))
    print(currency_rates("eur"))
