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


def calculate_subtotal(order_list):
    sum = 0
    prices_array = []
    for key, value in menu.items():
        for key_2, value_2 in value.items():
            if type(value_2) == float:
                prices_array.append(value_2)
    for price in prices_array:
        sum += price
    total_sum = round(sum, 2)
    return total_sum


test_order_list_data = [1, 2, 4]
sum_value = calculate_subtotal(test_order_list_data)
print(sum_value)
