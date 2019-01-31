from classic_strategy import LineItem, FidelityPromo, LargeOrderPromo, BulkItemPromo, Customer, Order, Promotion

joe = Customer('John Doe', 0)  # <1>
ann = Customer('Ann Smith', 1100)
cart = [LineItem('banana', 4, .5),  # <2>
    LineItem('apple', 10, 1.5),
    LineItem('watermellon', 5, 5.0)]
print(Order(joe, cart, FidelityPromo()))
print(Order(ann, cart, FidelityPromo()))
banana_cart = [LineItem('banana', 30, .5), LineItem('apple', 10, 1.5)]
print(Order(joe, banana_cart, BulkItemPromo()))  # <6>

long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
print(Order(joe, long_order, LargeOrderPromo()))
print(Order(joe, cart, LargeOrderPromo()))
