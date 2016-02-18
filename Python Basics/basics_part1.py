#This file is a python script (VS just working in terminal)

# PRINTING: Python saying 'hi'
print("Good evening everyone!")
print("Good evening at 8pm!")

# MATH COMMANDS: Python as a calculator
print(10 + 5)
print(10 * 20)
print(10 - (2+3))


# Some excerises
# -----------------

# 1: How much is 1234 CAD in EUR? And in GBP?
# (1 CAD = 0.65 EUR, 1 CAD = 0.49 GBP)

cad = 1234
eur = cad * 0.65
print("1234 CAD is {} in EUR".format(eur))

gbp = cad * 0.49
print("1234 CAD is {} in GBP".format(gbp))

# 2. What do you expect to see when you type
# type following divisions?

# Guess: prints 0..rounded down?
# Reality: prints 0.333333333
print(1/3)

# Guess: probably gives "cannot divide by 
# zero error
# Reality: Errors with "ZeroDivisionError: 
# division by zero"
print(1/0) #this will error and the rest will not process

# Make a script with 10-43 and print "I'm done"
print(10-43)
print("I'm done")




