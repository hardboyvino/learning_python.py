# Store the locations in a list. Make sure the list is not in alphabetical order
locations = ["bali", "zanzibar", "northern lights", "victoria falls", "jamiaca"]

# Print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list.
print(locations)

# Use sorted() to print your list in alphabetical order without modifying the actual list.
print()
print(sorted(locations))

#  Show that your list is still in its original order by printing it.
print()
print(locations)

# Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
print()
print(sorted(locations, reverse=True))

#  Show that your list is still in its original order by printing it again.
print()
print(locations)

# Use reverse() to change the order of your list. Print the list to show that its order has changed.
print()
locations.sort(reverse=True)
locations.reverse()
print(locations)
