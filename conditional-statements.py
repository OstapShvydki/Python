'''
mood=input("do you want to eat an ice cream? ")
mood=mood.lower()
if mood=="yes":
    print("eat an ice cream🍦")
else:
    print("I am not in the mood🥶")  
 ''' 

# print("What do you want to eat. Here are the options \n1: Burger\n2: Pizza\n3: Donut\n4: French Fries\n5: cookies\n6: Taco\n7: Salad\n8: cake\n9: sushi\n10: popcorn\n11: pancakes ")
# if 3 == 4:
#     print("Equal")
# elif (3 > 4):
#     print("greater")
# else:
#     print("less")

# x = 4
# if x == 4:
#     print("equal")
# elif x >= 4:
#     print("greater or equal")
# elif x > 4:
#     print("greater")
# else:
#     print("default")

# if 3 > 4 or 5 > 4:
#     print("one")
# elif 8 > 4 and 6 > 4:
#     print("two")
# else:
#     print("none")
#T and T = T
#T and F = F
#F and T = F
#F and F = F
#F or F = F
#F or T = T
#T or T = T
#T or F = T

# if 3 > 4 or 5 < 4:
#     print("one")
# elif 8 > 4 and 6 > 4:
#     print("two")
# else:
#     print("none")

# if not(3 < 4):
#     print("one")
# elif 4 > 3:
#     print("two")
# else:
#     print("none")

# if not(4 > 6) and not(8 > 5):
#     print("one")
# elif 4 > 5 or not(5 == 5):
#     print("two")
# else:
#     print("none")

# if 4 > 6 and not(8 > 5):
#     print("one")
# elif not(4 > 5) or not(5 == 5):
#     print("two")
# else:
#     print("none")

# if 4 > 3:
#     print("three")
# if 4 > 2:
#     print("four")
# if 5 > 4:
#     print("five")
# elif 4 == 4:
#     print("six")
# elif 4 > 3:
#     print("seven")
# else:
#     print("default")
#when there are multiple if statements check all of them and consider the last if statement till the end of as a seperate blocks only one statement will execute from them

# if 4 < 3:
#      print("three")
# if 4 > 2:
#      print("four")
# if 5 < 4:
#      print("five")
# elif 4 != 4:
#      print("six")
# elif 4 > 3:
#      print("seven")
# else:
#      print("default")

# x = 3 
# y = 12
# if x <= y and x > 0:
#     print("three")
# if x > y or y < 11:
#     print("four")
# if not(x < 4) and y < 24:
#     print("five")
# elif y != 4:
#     print("six")
# elif y >= x:
#     print("seven")
# else:
#     print("default")

# x = 12
# y = 3
# z = 11
# if (x == 2 and x < 3):
#      print(x)
# if x != 5:
#     print("whatever")
# if x != 5 and y >= 5 and z <= 13:
#      print("its gonna happen")
# if z != 0 or x == 2:
#      print("you say")
# if (not(y < 10)):
#     print("you say")
# elif (x < 10 or x < 5):
#      print("okkkkkkk")
# elif (y < 10 or y <= 0):
#     print("pikachu")
# elif(z == 0 or y ==5):
#     print("pikaboo")
# else:
#     print("Default value")

# nested if/else
# if 3 > 4 and 5 < 3:
#     if 4 > 0 or 5 == 8:
#         print("Nested")

# if 3 < 4 and 5 > 3:
#     if 4 > 0 or 5 == 8:
#         print("Nested")

# if 3 < 4 and 5 > 3:
#       if 4 > 0 or 5 == 8:
#           print("Nested")
#       if 7 >= 6 or 3 != 0:
#         print("nested again")
#       elif (5 - 4) <= 0:
#         print("23")
#       else:
#         print("nested default")
# else:
#     ("outside")

# x = 10
# y = 12
# if x > y:
#     print("x > y")
# elif x < y:
#     print("x < y")
# else:
#     print("x == y")

# a = 5
# b = 5
# if a > b:
#     print("a is greater")
# elif a == b:
#     if a + b == 10:
#         print("Sum is 10")
#     else:
#         print("a is equal to b but sum is not 10")
# else:
#     print("b is greater")

# x = 15
# if x < 10:
#     print("Less than 10")
# elif 10 <= x <= 20:
#     print("In range 10-20")
# else:
#     print("Greater than 20")

# age = 25
# if age < 18:
#     if age < 12:
#         print("Child")
#     else:
#         print("Teen")
# elif age < 30:
#     if age < 21:
#         print("Young Adult")
#     else:
#         print("Adult")
# else:
#     print("Senior")

# a = 2
# b = 4
# if a > b:
#     print("A")
# elif a < b:
#     if b - a > 1:
#         print("B - A > 1")
#     else:
#         print("B - A <= 1")
# else:
#     print("A == B")

# if n % 2 == 0:
#         return "Even"
# elif n % 3 == 0:
#         return "Divisible by 3"
# else:
#         return "Other"

# a, b, c = 10, 20, 30
# if a > b:
#     if b > c:
#         result = "A"
#     else:
#         result = "B"
# elif a < b:
#     if a > c:
#         result = "C"
#     else:
#         result = "D"
# else:
#     result = "E"
# print(result)

# x = 5
# y = -5
# if x > 0:
#     if y > 0:
#         print("Both positive")
#     else:
#         print("x positive, y not positive")
# elif x <= 0:
#     if y <= 0:
#         print("Both not positive")
#     else:
#         print("y positive, x not positive")

# x, y, z = 15, 10, 5
# if x > y > z:
#     print("Descending")
# elif x < y < z:
#     print("Ascending")
# else:
#     print("Neither")

# age = 65
# status = "senior" if age > 60 else "adult"
# if status == "adult":
#     category = "Working class"
# elif status == "senior":
#     if age > 70:
#         category = "Retired"
#     else:
#         category = "Almost retired"
# else:
#     category = "Undefined"
# print(category)

# x = 8
# y = 3
# if x / y > 2:
#     print("x is more than twice y")
# elif x / y == 2:
#     print("x is twice y")
# else:
#     print("x is less than twice y")

# temperature = 30
# humidity = 85
# if temperature > 28 and humidity > 80:
#     comfort = "Hot and humid"
# elif temperature > 28 or humidity > 80:
#     comfort = "Hot or humid"
# else:
#     comfort = "Comfortable"
# print(comfort)

# age = 60
# if age >=0 and age <= 1:
#     print ("infant")
# elif age >=2 and age <= 12:
#     print ("child")
# elif age >=13 and age <= 19:
#     print ("Teenager")
# elif age >=20 and age <= 59:
#     print ("Adult")
# elif age >=60 and age <=70:
#     print ("Senior")

# score = 96
# if score >=90 and score <=100:
#     print ("A")
# if score >=80 and score <=89:
#     print ("B")
# if score >=70 and score <=79:
#     print ("C")
# if score >=60 and score <=69:
#     print ("D")
# if score >=0 and score <=59:
#     print ("F")

#choice = input ("choose your pet from Dog, Cat, Rabbit ")
#if choice == "Dog":
#    print ("You'll have a playful friend to take on walks and play fetch with.")
#if choice == "Cat":
#    print ("You'll have a cozy companion who loves to nap and purr by your side.")
#if choice == "Rabbit":
#    print ("You'll care for a quiet, gentle friend who loves to hop around safely indoors.")
num = 24
if num%2 == 0 and num>0:
    print("even positive")
elif num%2 == 1 and num>0:
    print("odd positive")
elif num%2 == 1 and num<0:
    print("odd negative")
elif num%2 == 2 and num<0:
    print("even negative")
else num == 0:
    print("Zero")
