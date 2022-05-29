#challendge

phone = input("phone ")
digits_mapping = {
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five"
}

output = ""
for phones in phone:
    output += digits_mapping.get(phones, "!") + " "
print(output)