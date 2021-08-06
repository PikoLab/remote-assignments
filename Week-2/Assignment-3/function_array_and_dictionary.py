data={"products": [{"name": "Product 1","price": 100},{"name": "Product 2","price": 700},{"name": "Product 3","price": 300}]}


def avg(data):
    count=0
    total_price=0
    for i in data["products"]:
        total_price += i["price"]
        count += 1
    return round(total_price/count,3)


print('The average price is: {}'.format(avg(data)))

