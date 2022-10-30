
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