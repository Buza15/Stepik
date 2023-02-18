value = float(input("На сколько $ покупаем? :"))
curr_price = float(input("Текущая цена монеты:"))

curr_result = value / curr_price

print("Куплено", curr_result, "монет")

print("Будем рассчитывать будущий прайс или нет?")
print("+ или -")

next = input()

if next == "-":
 print("OK")
else:
 new_price = int(input("Новая цена монеты:"))
 new_vlaue = curr_result * new_price
 print("Можно продать за", new_vlaue, "$")
 print("Вы вложили", value, "$ и получили", new_vlaue, "$")
 print("Чистая прибыль составила", new_vlaue - value, "$")