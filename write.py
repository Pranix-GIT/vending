def update_stock(stock):
    with open('stock.txt', 'w') as file:
        for item, data in stock.items():
            file.write(item + ',' + str(data[0]) + ',' + str(data[1]) + '\n')
