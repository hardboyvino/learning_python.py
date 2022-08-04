# List of guest for the dinner
guest_list = ["einstein", "2pac", "branson", "eminem", "kanye"]

# Loop through the list and print a personalised message to each guest
for i in range(len(guest_list)):
    message = guest_list[i].title() + ", You are invited to my dinner."
    print(message)
print()

# Who was absent
absent = "2pac"

# Find the index of the absent guest
# Remove the absent guest
# Insert a new guest at the place of the absent guest
absent_index = guest_list.index(absent)
guest_list.remove(absent)
guest_list.insert(absent_index, "asake")

print(guest_list)
print()

# Print new set of invites for the guests
for i in range(len(guest_list)):
    message = guest_list[i].title() + ", You are invited to my dinner."
    print(message)
print()

# Message to everyone that more guests are coming
print("The more the merrier. More people joining the party.")
print()

# Add 3 new guests to the list
# 1 guest at the beginning of the list
# 1 guesst at the middle of the list
# 1 guest at the end of the list
guest_list.insert(0, "lana del rey")
guest_list.insert(len(guest_list) // 2, "david malan")
guest_list.append("bezos")

# Print new set of invites for the guests
for i in range(len(guest_list)):
    message = guest_list[i].title() + ", You are invited to my dinner."
    print(message)
print()

# Message saying only 2 people can come for the dinner
print("Oh! Only 2 folks can be invited")
print()

while len(guest_list) > 2:
    uninvited_guest = guest_list.pop()
    print("Sorry, " + uninvited_guest.title() + ", next party surely!")
print()

print(guest_list)

