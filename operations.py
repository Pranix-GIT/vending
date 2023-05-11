import csv

def display_laptops():
    with open('laptops.csv', 'r') as f:
        laptops = csv.reader(f)
        laptops = list(laptops)
        print(laptops)

def purchase_laptop():
    item = input('Enter the laptop name: ')
    quantity = int(input('Enter the quantity: '))
    shipping = input('Is shipping required? (y/n): ')

    with open('laptops.csv', 'r') as f:
        laptops = csv.reader(f)
        laptops = list(laptops)
        for i in range(len(laptops)):
            if laptops[i][0] == item:
                laptops[i][4] = str(int(laptops[i][4]) + quantity)
                break

    with open('laptops.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(laptops)

    print(f'{quantity} {item}(s) added to the stock.')

def sell_laptop():
    item = input('Enter the laptop name: ')
    quantity = int(input('Enter the quantity: '))
    shipping = input('Is shipping required? (y/n): ')

    with open('laptops.csv', 'r') as f:
        laptops = csv.reader(f)
        laptops = list(laptops)
        for i in range(len(laptops)):
            if laptops[i][0] == item:
                if int(laptops[i][4]) < quantity:
                    print(f"Sorry, only {laptops[i][4]} {item}(s) are available in the stock.")
                    return
                laptops[i][4] = str(int(laptops[i][4]) - quantity)
                break

    with open('laptops.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(laptops)

    price = 0.0
    for laptop in laptops:
        if laptop[0] == item:
            price = float(laptop[3])
            break

    total_price = price * quantity
    if shipping == 'y':
        total_price += 10.0

    print(f'You have purchased {quantity} {item}(s) for {total_price}.')

def add_laptop():
    item = input('Enter the laptop name: ')
    brand = input('Enter the brand name: ')
    model = input('Enter the model name: ')
    price = input('Enter the price: ')
    stock = input('Enter the stock: ')

    with open('laptops.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([item, brand, model, price, stock])

    print(f'{item} added to the stock.')

def remove_laptop():
    item = input('Enter the laptop name: ')

    with open('laptops.csv', 'r') as f:
        laptops = csv.reader(f)
        laptops = list(laptops)
        for i in range(len(laptops)):
            if laptops[i][0] == item:
                laptops.pop(i)
                break

    with open('laptops.csv', 'w', newline='') as f:
        writer
