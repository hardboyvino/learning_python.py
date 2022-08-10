sandwich_orders = ["meat", 'pastrami',"beef", 'pastrami', "tuna", 'pastrami']
finished_sandwiches = []

print("We no longer have pastrami")

# Remove pastrami from sandwich_orders list
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

# Make all the orders by removing from the orders list and appending to finished list
while sandwich_orders:
    order = sandwich_orders.pop()

    finished_sandwiches.append(order)
    print(f"Making {order} sandwich.")