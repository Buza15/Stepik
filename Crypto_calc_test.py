import requests

from binance.client import Client

# Enter your Binance API keys here
api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'

# Initialize the Binance client with your API keys
client = Client(api_key, api_secret)

# Replace 'CRYPTO_SYMBOL' with the symbol of the crypto token you want to get the price for, e.g. 'BTCUSDT', 'ETHUSDT', etc.

print(" "*6,"-"*20,"Привет!","-"*20,"\nЭта программа поможет посчитать прибыль или убыток вложенных средств в крипте!\n"," "*23)

crypto_symbol =input("                        Выбери крипту:") + "USDT"

# Get the current price from Binance API
ticker = client.get_symbol_ticker(symbol=crypto_symbol)

# Get the price in USDT
current_price = ticker['price']

print(f"Текущая стоимость {crypto_symbol} {current_price}$")

to_calculate = current_price

value = float(input("На сколько $ покупаем? :"))

curr_price = float(to_calculate)

curr_result = value / curr_price

print("Куплено", curr_result, "монет")

print("Будем рассчитывать будущий прайс или нет?")
print("+ или -")

next = input()

if next == "-":
 print("Хорошо, пока!")
else:
 new_price = float(input("Новая цена монеты:"))
 new_vlaue = curr_result * new_price
 profit = new_vlaue - value
 if profit > 0:
  print("Можно продать за", new_vlaue, "$")
  print("Вы вложили", value, "$ и получили", new_vlaue, "$")
  print("Чистая прибыль составила", profit, "$")
 else:
  print("Можно продать за", new_vlaue, "$")
  print("Вы вложили", value, "$ и остаток составил", new_vlaue, "$")
  print("Убыток составил", profit, "$")

#test
