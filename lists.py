names = ['john', 'alex', 'amaji', 'sarah', 'matha']
print(names[1:3])
names[0] = 'wilson'
print(names)

#print largest number in a list
#step1
nums = [1,4,6,7,4,8,9,34]
print(max(nums))
#step2
max = nums[0]
for num in nums:
    if num > max:
        max = num
print(max)

#2D list ---- each item in the list is another list
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for role in matrix:
    for item in role:
        print(item)
    print(item)
print(matrix[0][1])
#list methods
query = [2,4,6,8]
query.append(20)
query.insert(0,10)
#query.remove(1)
#query.clear()
#query.pop()
print(query.index(4))
print(query)
# check for sequence of characters
print(4 in query)
print(query.count(2))
# sort lists
query.sort()
query.reverse()
print(query)
number2 = query.copy()
query.append(9)
print(number2)

# REMOVE DUPLICATES IN A LIST

sam_list = [11, 13, 15, 16, 13, 15, 16, 11]
# define new list to store the duplicates
duplicates = []
# loop
for i in sam_list:
    if i not in duplicates:
        duplicates.append(i)

print(str(duplicates))

mylist = ["a", "b", "b", "c", "a"]
mylist = sorted(set(mylist))
print(mylist)

