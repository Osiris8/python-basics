items = ['cake', 'cookie', 'bread']
total_items = items + ['biscuit', 'tart']
print(total_items)
# Result: ['cake', 'cookie', 'bread', 'biscuit', 'tart']

numbers = [1, 2, 3, 4, 10]
print(numbers)
names = ['Jenny', 'Sam', 'Alexis']
print(names)
mixed = ['Jenny', 1, 2]
print(mixed)
list_of_lists = [['a', 1], ['b', 2]]
print(list_of_lists)


# 2D list of people's heights
heights = [["Noelle", 61], ["Ali", 70], ["Sam", 67]]
# Access the sublist at index 0, and then access the 1st index of that sublist. 
noelles_height = heights[0][0] 
print(noelles_height)

# Output
# 61


# Create a list
shopping_line = ["Cole", "Kip", "Chris", "Sylvana", "Chris"]
 
# Removes the first occurance of "Chris"
shopping_line.remove("Chris")
print(shopping_line)

# Output
# ["Cole", "Kip", "Sylvana", "Chris"]

backpack = ['pencil', 'pen', 'notebook', 'textbook', 'pen', 'highlighter', 'pen']
numPen = backpack.count('pen')

print(numPen)
# Output: 3

knapsack = [2, 4, 3, 7, 10]
size = len(knapsack)
print(size) 
# Output: 5