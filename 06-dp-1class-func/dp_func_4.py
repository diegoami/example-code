from strategy_best3 import Customer, LineItem, Order, best_promo

joe = Customer('John Doe', 0)  # <1>
ann = Customer('Ann Smith', 1100)
cart = [LineItem('banana', 4, .5),  # <2>
    LineItem('apple', 10, 1.5),
    LineItem('watermellon', 5, 5.0)]
print(Order(joe, cart, fidelity_promo))
print(Order(ann, cart, fidelity_promo))
banana_cart = [LineItem('banana', 30, .5), LineItem('apple', 10, 1.5)]
print(Order(joe, banana_cart, bulk_item_promo))  # <6>

long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
print(Order(joe, long_order, large_order_promo))
print(Order(joe, cart, large_order_promo))

print(Order(joe, long_order, best_promo))
print(Order(joe, banana_cart, best_promo))
print(Order(ann, cart, best_promo))