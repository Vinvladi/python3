shop = [['футболка', 800], ['кроссовки', 5000], ['штаны', 500], ['шорты', 960], ['штаны', 450], ['кепка', 600], ['куртка', 9000], ['кроссовки', 2000], ['штаны', 870]]
name = input('Название товара: ')
total_amount = 0
total_cost = 0
for item in shop:
    if name == item[0]:
        total_amount += 1
        total_cost += item[1]
print(f'Кол-во товаров - {total_amount}')
print(f'Общая стоимость - {total_cost} руб.')