# Basics Part 3

# Functions: a piece of code we might want to run 
# multiple times

def say_hello_to(name) :
	greeting = "Hello " + name
	return greeting

print(say_hello_to("everyone!"))

who = "us"
print(say_hello_to(who))
greet = "everybody!"
print(say_hello_to(greet))
text = "world in peace!"
output = say_hello_to(text)
print(output)
print("\n")

# 1. What is the value of output in eaach of these lines?
# a) output = say_hello_to("") --> "Hello "
# b) output = say_hello_to(1) --> ERROR Num not string
# c) output = say_hello_to() --> ERROR - no value for param
#print(say_hello_to(""))
#print(say_hello_to(1))
#print(say_hello_to())

# 2. Print the number of characters in the word 
# 'MORPHOGENESIS'
word = 'MORPHOGENESIS' # Do single VS double quotes matter ever??
length = 0
for letter in word:
	length = length + 1
print(length)
print("\n")

# 3. What do these three lines of code return given...
def count_letters(word):
	length = 0
	for letter in word:
		length = length + 1
	return length

print(count_letters('1')) # --> 1
print(count_letters('')) # --> 0
#print(count_letters(100)) # --> Error! TypeError: 'int' object is not iterable
print("\n")

# 4. Fahrenheit to Celsius
def fahr_to_cels(temp_f):
	temp_c = (temp_f-32)*5/9
	return temp_c

temp_fahrenheit = 100
temp_celsius = fahr_to_cels(temp_fahrenheit)
print(temp_fahrenheit, 'Fahrenheit is', temp_celsius, 'Celsius!')
# 100 Fahrenheit is 87.55555555555556 Celsius!
print("\n")

# 5. Find smaller number!
def smaller(a, b):
	min_num = a
	if (a > b):
		min_num = b
	return min_num

smaller_num = smaller(5, 2)
print(smaller_num)
print(smaller(-1, 10))

# Moare functions!!
def fruit_salad(fruit1="apples", fruit2="pears", fruit3="oranges"):
	your_fruit_salad = fruit1 + " " + fruit2 + " " + fruit3
	return your_fruit_salad

print(fruit_salad()) # --> apples pears oranges
# We can replace default fruits
print(fruit_salad(fruit2="cheeries"))
# Passing them in any order
print(fruit_salad(fruit3="melon", fruit1="kiwi"))

# 6. Write a function which tells you whether a number is negative, 
# call it is_negative
def is_negative(num):
	s = str(num)
	if num > 0:
		s = s + " is not negative"
	else: 
		if num < 0 :
			s = s + " is negative"
		else:
			s = s + " is zero"
	return s


print(is_negative(12)) # 12 is not negative!
print(is_negative(-10)) # -10 is negative
print(is_negative(0)) # 0 is zero



























