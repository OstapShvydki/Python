#A dictianary contains multiple key value pairs
# mydict = {"name":"Ostap", "age":10, "grade":5}
# print(mydict)
# print(mydict["grade"])
# mydict["grade"]=10
# print(mydict)
# mydict["fruit"]="Apple"
# print(mydict)
# mydict.pop("name")
# print(mydict)
# mydict.popitem()
# print(mydict)
# print(mydict.keys())
# print(mydict.values())
# print(mydict.items())
#pop method is used to remove a particular key value pair by putting key in it.
#popitem is used to remove the last entered key/value pair.
#key method is used to get all the keys.
#values method is used to get all the values.
#items method is used to get all the key value pairs.
mylist = [1,2,2,2,3,4,14,10,1,1,3,13,1]
#Question: Find how many times each digit is present in the list?
mydict = {}
for item in mylist:
    if item in mydict.keys():
        print(mydict[item])
        mydict[item]+=1
    else:
        mydict[item]=1
print(mydict)