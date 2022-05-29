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


