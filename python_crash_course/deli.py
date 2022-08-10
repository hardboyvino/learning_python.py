sandwich_orders = ["meat", "beef", "tuna"]
finished_sandwiches = []

while sandwich_orders:
    order = sandwich_orders.pop()

    finished_sandwiches.append(order)
    print(f"Making {order} sandwich.")