# mylist=["Ostap", 36, 45, 56, True, "A"]
# print(mylist)
# mylist.append("Hi")
# print(mylist)
#Append function adds a new element at the end of the list
# mylist.remove(45)
# print(mylist)
#remove function is used to remove a particular value from the list
# mylist.pop(2)
# print(mylist)
#pop function is used to remove a particular value by using its index
# mylist.insert(2,100)
# print(mylist)
#insert function adds a particular value at a particular index in the list
# mylist.reverse()
# print(mylist)
# mylist.clear()
# print(mylist)
#clear function removes all the elements of the list
# newlist=mylist.copy()
# print(newlist)
#.copy function makes a shallow copy. shallow copy means both of the lists are stored at different address in the memory but having same elements
#sorting is done based on alphabetical order in the case of letters, sorting is done based on ascending and descending orders in the case of numbers
# mylist= [4,6,9,8,7,2,3,54,67,87,42,69,44]
# mylist.sort()
# mylist.sort(reverse=True)
# print(mylist)
#sort function by default sorts in the order. But by putting it reversed = True, it sorts in the descending order
mylist=["Hello", "Ostap", "age"]
mylist.sort()
print(mylist)