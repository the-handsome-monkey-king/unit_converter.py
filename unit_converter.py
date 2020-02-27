#!/usr/bin/env python
"""unit_converter.py

A program that converts measurements in one unit to another.

Temperature: celsius, fahrenheit, and kelvin
Currency: convert CAD and USD to other currencies"""

__author__ = "Ryan Morehouse"
__license__ = "MIT"


# TEMPERATURE

temperature = {
    1: 'celsius',
    2: 'fahrenheit',
    3: 'kelvin'}

def convert_kelvin(k, new_units):
    if new_units == 1:
        c = k - 273.0
        return c
    elif new_units == 2:
        f =  ((9.0/5.0) * (k-273.0)) +32.0
        return f

def convert_fahrenheit(f, new_units):
    if new_units == 1:
        c = (f - 32.0) * (5.0/9.0)
        return c
    elif new_units == 3:
        k = ((5.0/9.0) * (f - 32.0)) + 273.0
        return k

def convert_celsius(c, new_units):
    if new_units == 2:
        f = ((9.0/5.0)*c) + 32.0
        return f
    elif new_units == 3:
        k = c + 273.0
        return k

def convert_temperature():
    print("temperature conversion")
    options = {
        1: 'celsius',
        2: 'fahrenheit',
        3: 'kelvin'}
    temp_menu_from = {
        'msg': "Temperature units to convert from:",
        'options': options}
    temp_menu_to = {
        'msg': "Temperature units to convert to:",
        'options': options}

    from_units = menu(temp_menu_from)
    temp = get_float("Enter the temperature to convert: ")
    to_units = menu(temp_menu_to)

    if from_units == to_units:
        print("The units are the same: no conversion.")
    else:
        if from_units == 1:
            new_temp = convert_celsius(temp, to_units)
        elif from_units == 2:
            new_temp = convert_fahrenheit(temp, to_units)
        elif from_units == 3:
            new_temp = convert_kelvin(temp, to_units)

        print("{} {} = {} {}".format(
            temp, temperature[from_units],
            new_temp, temperature[to_units]))


# CURRENCY
cad_conversion = {
    'USD': 0.76,
    'EURO': 0.68,
    'JPY': 82.43,
    'GBP': 0.61,
    'AUD': 1.09,
    'CHF': 0.75,
    'CNH': 5.26,
    'SEK': 7.12,
    'NZD': 1.14}

usd_conversion = {
    'CAD': 1.31,
    'EURO': 0.89,
    'JPY': 107.74,
    'GBP': 0.79,
    'AUD': 1.42,
    'CHF': 0.98,
    'CNH': 6.88,
    'SEK': 9.31,
    'NZD': 1.49}

euro_conversion = {
    'CAD': 1.48,
    'USD': 1.13,
    'JPY': 121.60,
    'GBP': 0.90,
    'AUD': 1.60,
    'CHF': 1.11,
    'CNH': 7.76,
    'SEK': 10.51,
    'NZD': 1.68}

jpy_conversion = {
    'CAD': 0.012,
    'USD': 0.0093,
    'EURO': 0.0082,
    'GBP': 0.0074,
    'AUD': 0.013,
    'CHF': 0.0091,
    'CNH': 0.064,
    'SEK': 0.086,
    'NZD': 0.014}

gbp_conversion = {
    'CAD': 1.64,
    'USD': 1.26,
    'EURO': 1.11,
    'JPY': 135.46,
    'AUD': 1.79,
    'CHF': 1.24,
    'CNH': 8.65,
    'SEK': 11.70,
    'NZD': 1.87}

aud_conversion = {
    'CAD': 0.92,
    'USD': 0.70,
    'EURO': 0.62,
    'JPY': 75.81,
    'GBP': 0.56,
    'CHF': 0.69,
    'CNH': 4.84,
    'SEK': 6.55,
    'NZD': 1.05}

chf_conversion = {
    'CAD': 1.33,
    'USD': 1.01,
    'EURO': 0.90,
    'JPY': 109.30,
    'GBP': 0.81,
    'AUD': 1.44,
    'CNH': 6.98,
    'SEK': 9.44,
    'NZD': 1.51}

cnh_conversion = {
    'CAD': 0.19,
    'USD': 0.15,
    'EURO': 0.13,
    'JPY': 15.66,
    'GBP': 0.12,
    'AUD': 0.21,
    'CHF': 0.14,
    'SEK': 1.35,
    'NZD': 0.22}

sek_conversion = {
    'CAD': 0.14,
    'USD': 0.11,
    'EURO': 0.095,
    'JPY': 11.57,
    'GBP': 0.085,
    'AUD': 0.15,
    'CHF': 0.11,
    'CNH': 0.74,
    'NZD': 0.16}

nzd_conversion = {
    'CAD': 0.88,
    'USD': 0.67,
    'EURO': 0.59,
    'JPY': 72.33,
    'GBP': 0.53,
    'AUD': 0.95,
    'CHF': 0.66,
    'CNH': 4.62,
    'SEK': 6.25}

currency_conversion = {
    'CAD': cad_conversion,
    'USD': usd_conversion,
    'EURO': euro_conversion,
    'JPY': jpy_conversion,
    'GBP': gbp_conversion,
    'AUD': aud_conversion,
    'CHF': chf_conversion,
    'CNH': cnh_conversion,
    'SEK': sek_conversion,
    'NZD': nzd_conversion}

def get_new_currency(amt, old_units, new_units):
    try:
        factor = currency_conversion[old_units][new_units]
        new_amt = amt * factor
        return new_amt
    except(KeyError):
        return "ERROR"

def convert_currency():
    valid_currency = currency_conversion.keys()
    currency_options = {}
    for i in range(len(valid_currency)):
        currency_options[i] = valid_currency[i]

    currency_menu = {
        'msg': "Please select a currency from the list: ",
        'options': currency_options}

    old_units = menu(currency_menu)
    old_units = currency_options[old_units]
    amt = get_float("Amount to convert: ")
    new_units = menu(currency_menu)
    new_units = currency_options[new_units]

    if old_units == new_units:
        print("Currency units are the same, no conversion required.")
    else:
        new_amt = get_new_currency(amt, old_units, new_units)
        print("{} {} = {} {}".format(amt, old_units, new_amt, new_units))

# GENERAL USE METHODS
def get_float(msg):
    while(True):
        try:
            arg = (float)(raw_input(msg))
            return arg
        except(ValueError):
            print("That input was invalid. Please try again.")

def menu(menu_dict):
    while(True):
        try:
            print(menu_dict['msg'])
            options = menu_dict['options']
            for key, value in options.items():
                print("{}: {}".format(key, value))
            selection = (int)(raw_input("Menu number: "))
            if selection in options.keys():
                return selection
            else:
                raise ValueError
        except(ValueError):
            print("That was not one of the menu options.")
            print("Please try again.")
            print('\n')

def main():
    print("---Unit Converter---")
    main_menu = {
        'msg': "Select a unit type from the menu:",
        'options': {
            1: "temperature",
            2: "currency"}
        }

    selection = menu(main_menu)
    if selection == 1:
        convert_temperature()
    elif selection == 2:
        convert_currency()


if __name__ == "__main__":
    main()
