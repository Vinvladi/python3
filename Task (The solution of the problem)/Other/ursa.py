price = 127
good_price = 150.00
percent = float(round(1 - price/good_price,2))
print(percent)
two_mount_card = 2000 # rub
two_mount_game = 7633 # gold
good_1 = two_mount_card*1000/price
good_2 = two_mount_game*2
print(f"Через деньги: {good_1} Через голду: {good_2}")
print(f"Через деньги: {good_1/1000} Через голду: {good_2/1000}")
print(f"В рублях за 1 голд Через деньги: {float(price/(good_1/1000))} Через голду: {float(price/(good_2/1000))}")