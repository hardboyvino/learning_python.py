def make_sandwich(list):
    """Printing all the items to be on the sandwich"""
    print(f"Making a sandwich with: ")
    for item in list:
        print(f"- {item}")

def make_unlimited_sandwich(*items):
    """Print all the items to be in the sandwich without knowing how many items will be passed."""
    print(f"Making a sandwich with: ")
    for item in items:
        print(f"- {item}")    


on_sandwich = ["pepper", "onions", "carrots"]

make_sandwich(on_sandwich)
make_unlimited_sandwich("pepper", "onions", "carrots")

