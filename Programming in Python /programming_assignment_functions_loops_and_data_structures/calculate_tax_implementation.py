
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


# Args:
#         order: list of dicts that contain an item name and price

# creating a list that will contain an item name and prices as a dictionaries or key-value pairs
order = []

for key_1, value_1 in menu.items():
    order.append(value_1)


def calculate_subtotal(list_of_dictionary):
    sum_of_the_prices = 0
    list_of_product_names_and_prices = []
    list_of_prices = []
    for items_dictionaries in order:
        for key, value in items_dictionaries.items():
            if type(value) != 'str':
                list_of_product_names_and_prices.append(value)
    for i in range(len(list_of_product_names_and_prices)):
        if i % 2 != 0:
            list_of_prices.append(list_of_product_names_and_prices[i])
    sum_of_the_prices = round(sum(list_of_prices), 2)
    return sum_of_the_prices


subtotal = calculate_subtotal(order)


def calculate_tax(subtotal):
    """ Calculates the tax of an order

    [IMPLEMENT ME]
        1. Multiply the subtotal by 15% and return the product rounded to two decimals.

    Args:
        subtotal: the price to get the tax of

    Returns:
        float - The tax required of a given subtotal, which is 15% rounded to two decimals.
    """
    print('Calculating tax from subtotal...')
    return round(((15/100) * subtotal), 2)
    # WRITE SOLUTION HERE


# This function is provided for you, and will print out the items in an order


def print_order(order):
    print('You have ordered ' + str(len(order)) + ' items')
    items = []
    items = [item["name"] for item in order]
    print(items)
    return order

# This function is provided for you, and will display the menu


def display_menu():
    print("------- Menu -------")
    for selection in menu:
        print(
            f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")
    print()

# This function is provided for you, and will create an order by prompting the user to select menu items


def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input('Select menu item number ' +
                     str(count) + ' (from 1 to 5): ')
        count += 1
        order.append(menu[int(item)])
    return order


'''
Here are some sample function calls to help you test your implementations.
Feel free to change, uncomment, and add these as you wish.
'''


def main():
    order = take_order()
    print_order(order)

    # subtotal = calculate_subtotal(order)
    # print("Subtotal for the order is: " + str(subtotal))

    # tax = calculate_tax(subtotal)
    # print("Tax for the order is: " + str(tax))

    # items, subtotal = summarize_order(order)


if __name__ == "__main__":
    main()
