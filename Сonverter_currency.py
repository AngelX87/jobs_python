import freecurrencyapi

# блок подключения API
client = freecurrencyapi.Client("fca_live_vGpzLKXR8gU06GddyRGijL4ilxbQiYyF0PBIY6rO")
def actual_currencies(client):
    result = client.latest()
    return result
CURRENCIES = actual_currencies(client)

# Инструкция конвертации валют
def convert(amount, from_currency, to_currency, currencies):
    from_value = currencies.get(from_currency)  # CURRENCIES[current_currency]
    to_value = currencies.get(to_currency)

    coefficient = to_value / from_value
    return round(amount * coefficient, 2)



# Блок проверки правильности введенной валюты
def cheking_availability_currency(CURRENCIES):
    while True:
        current_currency = input("Введите исходную валюту: ")
        if current_currency in CURRENCIES['data']:
            break
    while True:
        result_currency = input("Введите результирующую валюту: ")
        if current_currency in CURRENCIES['data']:
            break
    return current_currency, result_currency

# 1 Приветствие
print("Добро пожаловать в конвертатор валют!")

# 2 Инструкциия последовательности ввода
print("""
Инструкция:
1. Ввести исходную валюту
2. Ввести результирующую валюту
3. Ввести количество валюты
""")

# 3 Запрос справочника Валют
print("Доступные валюты:")

for key in CURRENCIES['data']:
    print(f'* {key}')

# 4 Передаем данные проверки ввода и вводим кол-во
curses = cheking_availability_currency(CURRENCIES)
amount = input("Введите количество: ")

# 5 Получаем данные проделланных вычеслений и выводим на экран
result = convert(float(amount), curses[0], curses[1], CURRENCIES['data'])
print(f'{amount} {curses[0]} = {result} {curses[1]}')

# Памятка Валют (LIST EXCHANGER)

# EUR	Euro
# USD	US Dollar
# JPY	Japanese Yen
# BGN	Bulgarian Lev
# CZK	Czech Republic Koruna
# DKK	Danish Krone
# GBP	British Pound Sterling
# HUF	Hungarian Forint
# PLN	Polish Zloty
# RON	Romanian Leu
# SEK	Swedish Krona
# CHF	Swiss Franc
# ISK	Icelandic Króna
# NOK	Norwegian Krone
# HRK	Croatian Kuna
# RUB	Russian Ruble
# TRY	Turkish Lira
# AUD	Australian Dollar
# BRL	Brazilian Real
# CAD	Canadian Dollar
# CNY	Chinese Yuan
# HKD	Hong Kong Dollar
# IDR	Indonesian Rupiah
# ILS	Israeli New Sheqel
# INR	Indian Rupee
# KRW	South Korean Won
# MXN	Mexican Peso
# MYR	Malaysian Ringgit
# NZD	New Zealand Dollar
# PHP	Philippine Peso
# SGD	Singapore Dollar
# THB	Thai Baht
# ZAR	South African Rand