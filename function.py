def write_a_book(character, setting, special_skill):
  print(character + " is in " + 
        setting + " practicing her " + 
        special_skill)
write_a_book("Luna", "enchanted forest", "magic spells")


def ready_for_school(backpack, pencil_case):
  if (backpack == 'full' and pencil_case == 'full'):
    print ("I'm ready for school!")

ready_for_school('full', 'full')


# Define a function my_function() with parameter x

def my_function(x):
  return x + 1

# Invoke the function

print(my_function(2))      # Output: 3
print(my_function(3 + 5))  # Output: 9


def findvolume(length=1, width=1, depth=1):
  print("Length = " + str(length))
  print("Width = " + str(width))
  print("Depth = " + str(depth))
  return length * width * depth;

findvolume(1, 2, 3)
findvolume(length=5, depth=2, width=4)
findvolume(2, depth=3, width=4)