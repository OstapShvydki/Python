# my_set = set([1,2,3,4,4,3,3,2,2,1,1])
# print(my_set)
# my_set = {1,2,3,4}
# print(my_set)

# my_set = {1,2,3}
# my_set.add(4)
# print(my_set)

# my_set = {1,2,3,4}
# my_set.remove(3)
# print(my_set)
# my_set = {1,2,3,4}
# my_set.discard(2)
# print(my_set)

# set1 = {1,2,3}
# set2 = {3,4,5}
# union_set = set1.union(set2)
# print(union_set)

# set1 = {1,2,3}
# set2 = {3,4,5}
# union_set = set1|set2
# print(union_set)

# set1 = {1,2,3}
# set2 = {3,4,5}
# intersection_set = set1.intersection(set2)
# print(intersection_set)

# set1 = {1,2,3}
# set2 = {3,4,5}
# intersection_set = set1 & set2
# print(intersection_set)

# set1 = {1,2,3}
# set2 = {3,4,5}
# difference_set = set1.difference(set2)
# print(difference_set)

# set1 = {1,2,3}
# set2 = {3,4,5}
# difference_set = set1 - set2
# print(difference_set)

# set1 = {1,2,3}
# set2 = {3,4,5}
# sym_diff_set = set1.symmetric_difference(set2)
# print(sym_diff_set)

# set1 = {1,2,3}
# set2 = {3,4,5}
# sym_diff_set = set1 ^ set2
# print(sym_diff_set)

# my_set = {1,2,3}
# print(2 in my_set)
# print(4 in my_set)

# my_set = {1,2,3}
# for item in my_set:
#     print(item)

# Given a list of integers, convert it to a set to remove duplicates.
# List: L = [1, 2, 2, 3, 4, 4, 5]

# L = [1,2,2,3,4,4,5]
# my_set = set(L)
# print(my_set)

# Given a set of strings and a specific string, check if the string exists in the set.
# Set: S = {"apple", "banana", "cherry"}, String: "banana"

# S = {"apple","banana","cherry"}
# String =  "banana"
# if String in S:
#     print("yes")
# else:
#     print("no")

# Add an Element to a Set
# Given a set of numbers, add a new number to the set.
# Set: S = {1, 2, 3}, Number: 4

# S = {1,2,3}
# Number = 4
# print(S)
# S.add(Number)
# print(S)

# Given a set of strings, remove a specified string.
# Set: S = {"apple", "banana", "cherry"}, String: "banana"

# S = ["apple","banana","cherry"]
# String = "banana"
# if String in S:
#     S.remove(String)
#     print(S)

# Given a set of numbers, find the number of elements in the set.
# Set: S = {1, 2, 3, 4, 5}

# S = {1,2,3,4,5}
# Length = len(S)
# print(Length)

# Given two sets, find the difference (elements in the first set but not in the second set).
# Sets: A = {1, 2, 3} and B = {3, 4, 5}

# A = {1,2,3} 
# B = {3,4,5}
# print(A.difference(B))

# Given two sets, find their intersection.
# Sets: A = {1, 2, 3} and B = {3, 4, 5}

# A = {1,2,3}
# B = {3,4,5}
# print(A.intersection(B))

# Find the Union of Two Sets
# Given two sets, find their union.
# Sets: A = {1, 2, 3} and B = {3, 4, 5}

# A = {1,2,3}
# B = {3,4,5}
# print(A.union(B))

# Given a set of strings, remove a specified string.
# Set: S = {"apple", "banana", "cherry"}, String: "peach"

# S = ["apple","banana","cherry"]
# String = "peach"
# if String in S:
#      S.remove(String)
#      print(S)
# else:
#      print("error")

# Given two sets, check if they are disjoint (no common elements).
# Sets: A = {1, 2, 3} and B = {4, 5, 6}

# A = {1,2,3}
# B = {4,5,6}
# if A.intersection(B) == ("set()"):
#     print("No join")
# else:
#     print("disjoined")

# Given three lists, find the common elements.
# Lists: L1 = [1, 2, 3, 4], L2 = [3, 4, 5, 6], L3 = [4, 5, 6, 7]

# L1 = [1,2,3,4]
# L2 = [3,4,5,6]
# L3 = [4,5,6,7]
# ans = set(L1) & set(L2) & set(L3)
# print(ans)