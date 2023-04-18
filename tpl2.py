import tkinter as tk
import requests
from tkinter import ttk

window = tk.Tk()
window.title("Currency Converter")
window.geometry("400x250")

instruction_label = tk.Label(window, text="Select the currencies and enter the amount to convert:")
instruction_label.grid(row=1)

# Fetch the list of currencies from the API
url = "https://openexchangerates.org/api/latest.json?app_id=3a7a1d3d1f97409ab8c24a9d8239808c"
response = requests.get(url)
currencies = response.json()['rates']

# Create a list of currency codes
currency_codes = []
for currency_code in currencies:
    currency_codes.append(currency_code)

# Create a dropdown menu to display the list of currencies
from_currency_var = tk.StringVar()
from_currency_dropdown = tk.OptionMenu(window, from_currency_var, *currency_codes)
from_currency_var.set("USD")
from_currency_dropdown.grid(row=2)

to_currency_var = tk.StringVar()
to_currency_dropdown = tk.OptionMenu(window, to_currency_var, *currency_codes)
to_currency_var.set("EUR")
to_currency_dropdown.grid(row=3)

amount_label = tk.Label(window, text="Amount:")
amount_label.grid(row=4)

amount_entry = tk.Entry(window)
amount_entry.grid(row=5)


def convert_currency():
    # Fetch the exchange rate from the API
    url = "https://openexchangerates.org/api/latest.json?app_id=3a7a1d3d1f97409ab8c24a9d8239808c"
    response = requests.get(url).json()
    exchange_rates = response["rates"]

    # Convert the amount to the selected currency
    converted_amount = float(amount_entry.get()) * exchange_rates[to_currency_var.get()]

    # Display the converted amount
    result_label.config(text="Converted amount: " + str(round(converted_amount, 2)) + " " + to_currency_var.get())


convert_button = tk.Button(window, text="Convert", command=convert_currency)
convert_button.grid(row=6)

result_label = tk.Label(window)
result_label.grid(row=7)


def reset_fields():
    amount_entry.delete(0, tk.END)
    result_label.config(text="")
    from_currency_var.set("USD")
    to_currency_var.set("EUR")


reset_button = tk.Button(window, text="Reset", command=reset_fields)
reset_button.grid(row=8)

window.mainloop()