#Python Lists: Coding Questions
#Question 1: Write a Python program to add an item to the end of a list.
#Example input: [1, 2, 3] and 4
#Example output: [1, 2, 3, 4]

list=[1,2,3,]
list.append(4)
print(list)

#Question 2: Write a Python function that merges two lists and returns a single list.
#Example input: [1, 2, 3] and [4, 5, 6]
#Example output: [1, 2, 3, 4, 5, 6]

list=[1,2,3,]
list2=[4,5,6]
list.append(list2)
print(list)

# Question 3: Write a Python function that reverses a list without using the built-in reverse() method.
# Example input: [1, 2, 3, 4]
# Example output: [4, 3, 2, 1]

list=[1,2,3,4]
list.sort(reverse=True)
print(list)

# Question 4: Write a Python program to find the list element with the highest value.
# Example input: [10, 8, 12, 5]
# Example output: 12

list=[10,8,12,5]
list.sort(reverse=False)
list.pop(0)
list.pop(0)
list.pop(0)
print(list)

# Question 5: Write a Python program to remove duplicates from a list.
# Example input: [1, 2, 2, 3, 3, 3, 4]
# Example output: [1, 2, 3, 4]



# Question 6: Write a Python function that checks if a list is empty or not.
# Example input: []
# Example output: True

list=[]
if len(list)==0:
    print(True)
else:
    print(False)

# Question 7: Write a Python function to get the difference between the two lists (elements present in the first list, but not in the second).
# Example input: [1, 2, 3, 4] and [2, 3, 5]
# Example output: [1, 4]

list=[1,2,3,4]
list2[2,3,5]
