
number = [2,4,6,8,2,4]
def find_max(numbers):
    max = numbers[0]
    for item in numbers:
        if item > max:
            max = item
    return max

