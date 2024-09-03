# Create the adding_practice list with the following entry: 273.15
# adding_practice= [273.15]
# print(adding_practice)
# # Use the append method to add the number 42 and the string "hello" to the list. Add these new items one at a time.  Print the list after each step to confirm the changes.
# adding_practice[1:1]=[42]
# print(adding_practice)

# adding_practice[2:2]=["hello"]
# print(adding_practice)

# # Use list concatenation to add these three items to the list all at once: [False, -4.6, '87'].
# adding_practice[3:3]=[False, -4.6, '87']
# print(adding_practice)
# Use the cargo_hold list for the next set of exercises.
cargo_hold = ['oxygen tanks', 'space suits', 'parrot', 'instruction manual', 'meal packs', 'slinky', 'security blanket']
print(cargo_hold)

# # Use bracket notation to replace 'slinky' in the list with 'space tether'. Print the list to confirm the change.

cargo_hold[5]='space teter'
print(cargo_hold)


# Remove the last item from the list with pop. Print the element removed and the updated list.

print(cargo_hold)

cargo_hold[6]='pop'
print(cargo_hold)


# 
# Remove the first item from the list with pop. Print the element removed and the updated list.

print(cargo_hold)

cargo_hold[0]='pop'
print(cargo_hold)

# append and insert require arguments inside the (). Add the items 1138 and ‘20 meters’ to the the list - the number at the start and the string at the end. Print the updated list to confirm the changes.
print(cargo_hold)

cargo_hold.insert(0,1138)
cargo_hold.append('20meters')
print(cargo_hold)
# Use the remove method to take the parrot out of cargo_hold, then print the updated list.
del cargo_hold[3]
print(cargo_hold)

# Use .format() to print the final list and its length. "The list ___ contains ___ items."

length_of_list= len(cargo_hold)
print("The list {} contains {} items." .format(cargo_hold, length_of_list))