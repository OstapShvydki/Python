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

#x=(input("enter a string(x):     "))
#y=(input("enter a string(y):     "))
#if len(x) > len(y):
#    print("x is longer")
#elif len(x) < len(y):
#    print("y is longer")
#else:
#    print("they are the same length")

#you need to take two strings and check if their first character matches or not. Print yes or no accordingly

#x=("cow")
#y=("sheep")
#if x[0] == y[0]:
#    print("yes")
#else:
#    print("no")

#Write a Python program to determine the classification of a movie based on its release year and critical rating. 
#Use year_released for the year it came out and rating for its score out of 10. 
#Assume the current year is 2024. Classify the movie as follows:
#If released within the last 5 years:
#Over 8.0 rating: "Modern hit"
#5.0 to 8.0 rating: "Modern average"
#Below 5.0 rating: "Modern flop"
#If released 5 to 20 years ago:
#Over 8.0 rating: "Recent classic"
#5.0 to 8.0 rating: "Recent average"
#Below 5.0 rating: "Recent miss"
#If released more than 20 years ago:
#Over 8.0 rating: "Certified classic"
#5.0 to 8.0 rating: "Old but good"
#Below 5.0 rating: "Old flop"

#name = "Harry_Potter"
#year = 0-2003
#rating = 7

#if year == 2019-2024 and rating > 8:
#    print("Modern hit")
# elif year == 2019-2024 and rating < 8 and rating > 5:
#     print("Modern average")
# elif year == 2019-2024 and rating < 5:
#     print("Modern flop")
# elif year == 2004-2018 and rating > 8:
#     print("Recent classic")
# elif year == 2004-2018 and rating < 8 and rating > 5:
#     print("Recent average")
# elif year == 2004-2018 and rating < 5:
#     print("Recent Miss")
# elif year == 0-2003 and rating > 8:
#     print("Certified classic")
# elif year == 0-2003 and rating < 8 and rating > 5:
#     print("Old but good")
# elif year == 0-2003 and rating < 5:
#     print("Old flop")

# Print all the numbers from 1 to 50 which are divisible by 3 and 5

# for i in range (1, 50):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)

# print the square numbers from 1 - 10

# for i in range (1, 11):
#         print(i * i)

#Print all of the even numbers from 1 to 20

for i in range (1, 20):
    print(i % 2 == 0)