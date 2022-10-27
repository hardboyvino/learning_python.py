"""
Practice project. Automate Boring Stuff. Dictionaries
"""
import pprint

inventory = {"rope": 1, "torch": 6, "gold coin": 42, "dagger": 1, "arrow": 12}
dragon_stuff = ["gold coin", "dagger", "gold coin", "gold coin", "ruby", "ruby"]

def display_inventory(inventory_dict):
   """Function to display all the items in the invetory neatly."""
   count = 0

   print("\nInventory:")

   for k, v in sorted(inventory_dict.items()):
      print(f"{v} {k}")
      count += v

   print(f"\nTotal number of items: {count}")


def add_to_invetory(inventory_dict, added_list):
   """Update the value of dictionary based on items in the list."""
   for item in added_list:
      if item not in inventory_dict:
         inventory_dict[item] = 1

      else:
         inventory_dict[item] += 1

   # pprint.pprint(inventory_dict)


add_to_invetory(inventory, dragon_stuff)
display_inventory(inventory)
