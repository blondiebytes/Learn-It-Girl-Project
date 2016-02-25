# Basics Part 2:

# More Math
print(5 + 6)
print(-6)
print((2+5) * 3 / 7)
print("\n")

# More Than Math
print("Hello")
print("Hello " + "Waterloo")
print("\n")

# Figuring out TypeError
# cannot do --> print("Hello" + 4)
print(type(4)) # <class 'int'>
print(type("hello")) # <class 'str'>

# Using int() and str() to convert between types
print(type(str(4))) # <class 'str'>
print("\n")

# 1. What would we change in print("Hello" + 4) to make it not throw an error anymore and output Hello4?
# a) print(int("Hello") + 4)
# b) print(str("Hello") + 4)
# c) print("Hello" + str(4))
# The answer is C!

# Variable --> a box
box = 3
print(box)
double_box = box * 2
print(double_box)
number_box = 8
number_box = number_box + 1
print(number_box)
box = "kittens"
print(box)
box = "kittens" + "love" + "yarn"
print(box)
print("\n")

# 2. If I run the following code, what will be the final value of b?
a = 1
b = a * 5
a = 2
# a) 5
# b) 1
# c) 10
# The answer would be 5 (A)

# Lists: a collection box
groceries = ["apples", "cabbage", "soylent"]
print(groceries[0]) # apples
print(groceries[2]) # soylent
print(groceries[-1]) # soylent --> DOESN'T GIVE ERROR (weird)
print("\n")

# 3. What is the result of running the code print(groceries[3])?
# a) Error
# b) Soylent
# c) Apples
# Guess: Error bc out of range
#print(groceries[3])
# Reality: IndexError: list index out of range

# Get length of a list
print(len(groceries))

# Append things to a list
groceries.append("tofu")
print(groceries[3])
print(groceries)

# Uppercase letters
kittens = "kittens"
print(kittens.upper())
print(kittens) # strings are immutable
print("\n")

# ?? Why can't I do whos? --> shows variables & table & stuff

# Boolean: Python finds out the truth
print(5 > 3) # True
print(5 <= 2) # False
print('a' in "face") # True
print('b' in "pants") # False
print("pants" == "face") # False
print(2 == 4/2.0) # True
print("\n")

# 4. What will be the results of...
hands = 2
handy_person = hands > 2
print(handy_person)
print("\n")
#a) True
#b) False
#c) Error
# B --> False b/c 2 is not greater than 2

# Flow Control: Programs have to be guided through 
# multiple steps. They do this by checking what's true 
# at every step.
today = "Sunday"
if today == "Saturday":
	print ("Pizza")
else:
	print("No Pizza")
print("\n")

# I/O: Talking to people:
name = input("What's your name?")
print("Hello " + name)

# 5. Why doesn't this code work?
# age = input("How old are you?")
# print(age + 7)
# We get a "TypeError: Can't convert 'int' object to str implicitly"
# to fix this we can do...
age = input("How old are you?")
newAge = int(age) + 7
print("{}".format(newAge))
print(str(newAge))
# We needed to turn age into an int to add it to 7 and then
# convert it back to a string to print it out
print("\n")

# 6. A person puts in the amount of cupcakes they want 
# and your program returns the total amount they have to pay. 
# The cupcakes are 1.25$ each and only 5 cupcakes can be 
# made at a time!
user_input = input("Enter the amount of cupcakes you desire: ")
# Convert to int so we can do some computations
amount = int(user_input)
if amount <= 5:
	cost = amount * 1.25
	print("Your order costs", cost)
else:
	print("We can only make 5 cupcakes at a time!")
print("\n")

# Repeating Actions with Loops
# for-each loop
names = ["ron", "harry", "hermione"]
for name in names :
	print("Hi "+ name.capitalize())
print("\n")
# for loop
pie_num = 5
for pie in range(0, pie_num):
	print(str(pie) + " pies")
# while 
given = 0
while given <= 5:
	ans = input("Enter a number that is greater than 5: ")
	given = int(ans)
print("You said "+ ans) # ?? Scope? Based on method.
print("\n")

# 7. Tweet Validator
# Tweets are these messages you post on the Internet that 
# have to be 140 characters or shorter. How can we make sure that 
# a given string is the appropriate length? Print out the 
# length of the string and whether it is valid or not.
# INPUT:
# "OMG Python!"
# OUTPUT:
# 11
# Valid
maxTweetLength = 140
tweet = "OMG Python!"
count = 0
for char in tweet:
    count = count + 1
# OR WE COULD DO: count = len(tweet) --> 
# to get the length (i.e. number of characters)
print(count)
if count <= maxTweetLength:
    print("Valid")
else:
    print("Invalid")
print("\n")

# 8. Processing Grades
# Given a list of grades, grades = [81, 70, 60, 91],
# print the average and the number of grades above 80.
grades = [81, 70, 60, 91]
goodGrade = 80
numberOfGrades = len(grades)
totalOfGrades = 0
numberOfGoodGrades = 0;
for grade in grades: 
	if (grade > goodGrade):
		print("WOW! " + str(grade))
		numberOfGoodGrades = numberOfGoodGrades + 1
	totalOfGrades = totalOfGrades + grade
average = totalOfGrades / numberOfGrades
print("Average: " + str(average))
print("Number of good grades: " + str(numberOfGoodGrades))
print("\n")

# Dictionaries: Data types that store associations
capitals = {"Ontario":"Toronto", 
"Canada":"Ottawa", 
"Croatia": "Zagreb"}
print(capitals["Ontario"])
print("\n")

# Iterate with for-loop
for place in capitals:
	print(place)

print("\n")

# 9. Quiz the capitals
# Given the capitals dictionary from before, make a 
# flash card-like quiz, where every location is the 
# question and the capitol is the answer.
for place in capitals:
    answer = input("What is the capitol of " + place + "? ")
    if capitals[place] == answer:
        print("Right answer!")
    else:
        print("Sorry, the answer was " + capitals[place])















