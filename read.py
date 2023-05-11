def read_stock():
    stock = {}
    with open('stock.txt', 'r') as file:
        for line in file:
            data = line.strip().split(',')
            stock[data[0]] = [int(data[1]), float(data[2])]
    return stock
