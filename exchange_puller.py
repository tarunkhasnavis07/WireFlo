import requests, json

currency_list = ['USD', 'IDR', 'BGN', 'ILS', 'GBP', 'DKK', 'CAD', 'JPY', 'HUF', 'RON', 'MYR', 'SEK', 'SGD', 'HKD', 'AUD', 'CHF', 'KRW', 'CNY', 'TRY', 'HRK', 'NZD', 'THB', 'EUR', 'NOK', 'RUB', 'INR', 'MXN', 'CZK', 'BRL', 'PLN', 'PHP', 'ZAR']
base_url = "https://api.fixer.io/latest?base="

def exchange_rates():
    rates_dict = {}
    for currency in currency_list:
        r = requests.get(base_url + currency)
        rates_dict[currency] = dict(r.json())['rates']
        print(rates_dict[currency])
    return rates_dict

if __name__ == '__main__':
    rates = exchange_rates()
    with open('rates.json', 'w') as fp:
        json.dump(rates, fp)
