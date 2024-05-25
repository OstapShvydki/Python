#Given a list of grades (e.g., [67, 90, 78, 85, 92, 70, 83]), write a program that prints the highest grade, the lowest grade, and the average grade. 
#Also, classify each grade as 'Fail' (below 60), 'Pass' (60-79), or 'Excellent' (80 and above).

#Grades=[67, 90, 78, 85, 92, 70, 83]
#maximum=max(Grades)
#minimum=min(Grades)
#average=sum(Grades)/len(Grades)
#print(maximum)
#print(minimum)
#print(average)

#for i in Grades:
#    if i < 60:
#        print("Fail")
#    elif i > 60 and i < 79:
#        print("Pass")
#    elif i > 79:
#        print("Exellent")

#You need to take 2 numbers as input and print which number is greater

#x=int(input("enter a number(x):    "))
#y=int(input("enter a number(y):    "))
#if x > y:
#    print("x is larger")
#elif x < y:
#    print("y is larger")
#else:
#    print("they are the same")

#You need to take 3 numbers as input and print which number is the greatest

#x=int(input("enter a number(x):     "))
#y=int(input("enter a number(y):     "))
#z=int(input("enter a number(z):     "))
#if x > y and x > z:
#    print("x is the largest")
#elif y > x and y > z:
#    print("y is the largest")
#elif z > x and z > y:
#    print("z is the largest")
#else:
#    print("they are all the same")

#you need to take two strings as input and check which one has more length

x=(input("enter a string(x):     "))
y=(input("enter a string(y):     "))
if len(x) > len(y):
    print("x is longer")
elif len(x) < len(y):
    print("y is longer")
else:
    print("they are the same length")

#you need to take two strings and check if their first character matches or not. Print yes or no accordingly

x=("pig")
y=("piglet")
