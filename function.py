#function ---- it is reusuable in other programs, descriptive naming

def greet_user(name):
    print('Hi wilson, and how are you')
    print(f'hi {name}')
print("start")

greet_user('john')
greet_user('mary')
print("finish")

# keyword Arguement
# if you have a numerical arguement in your function use the keyword arguement greet_user(firstname='wilson', lastname='ibekason')
# if you are passing both positional and keyword arguement in a function use positional arguement before using keyword arguement
# EXAMPLE GREET_USER('WILSON', LAST_NAME='IBEKASON')


# RETURN STATEMENT

def square(num):
    return  num ** num
result = square(3)
print(result)
#- -------------  ||||||||||| -------------------#
# all function return none --- an object with no value

#creating a resusable function

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

# exceptions --- for error that cratches our program
try:
    age = int(input('Age '))
    income = 20000
    age = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be divided by zero')
except ValueError:
    print('Invalid value')

# use comments to add whys and hows
