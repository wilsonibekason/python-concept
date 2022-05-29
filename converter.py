#challendge

#emoji converter
message = input('> ')
# split creates a boundary to seperate a string into multiple words
words = message.split(" ")
emoji = {
    ":)": ".o.",
    ":(": "-0-",
}
output = ""
for word in words:
    output += emoji.get(word, word) + " "
print(output)
#  rebuilt with function
def emoji_converter(message):
    words = message.split(" ")
    emoji = {
        ":)": ".o.",
        ":(": "-0-",
    }
    output = ""
    for word in words:
        output += emoji.get(word, word) + " "
    return output

message = input('> ')
print(emoji_converter(message))

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