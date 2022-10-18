menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee',
        "price": 2.50},
    3: {"name": 'cake',
        "price": 2.79},
    4: {"name": 'soup',
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4.99}
}


def calculate_subtotal(order):
    prices_array = []
    sum = 0
    for key, value in menu.items():
        for key_2, value_2 in value.items():
            if type(value_2) == float:
                prices_array.append(value_2)
    for price in prices_array:
        sum += price
    total_price = round(sum, 2)
    print(total_price)


calculate_subtotal(menu)
