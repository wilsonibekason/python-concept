# topos are immutable
# if you want to create a list that you don't want to change in the application, then topo is good
numbers = (1,2,3)

#unpacking
codinates = (1,3,4)
x = codinates[0]
y = codinates[1]
z = codinates[2]
# unpacking in python
x,y,z = codinates
# dictionaries -- to store values that have key values pairs

customer = {
    "name": "wilson",
    "age": 30,
    "is_verified": True
}
# the get method returns a value that is none
print(customer.get("name"))

#challendge

phone = input("phone ")
digits_mapping = {
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five"
},
output = ""
for phones in phone:
    output += digits_mapping.get(phones, "!")
print(output)