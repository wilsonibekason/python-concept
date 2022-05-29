for item in ['wilson', 'john']:
    print(item)
    #the range function creates a new object and in each iteration each object spins out a new number
for item in range(10):
    print(item)
prices = [20, 30, 40, 50, 60, 70, 80, 90]
total = 0
for cost in prices:
    total += cost
print(total)

#nested loop --- neting loops in loops
for x in range(4):
    for y in range(3):
        print(f'{x}, {y} ')

for t in range(6):
    for o in range(5):
        print(f'{t}, {o}')

#nested loop challenge
number = [5, 2, 5, 2, 2]
for x_count in number:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

#nested loop challendge
