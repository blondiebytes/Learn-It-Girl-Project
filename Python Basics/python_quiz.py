# My Quiz (in Pythy Python)

# 1. Ask differen questions via console
# 	a. One yes/no questions
#	b. One multiple choice
#	c. One question with a single number or word answer (like before)

# Plan:
# Q1: Is my favorite color purple?
# A1: No
# Responses:
# Right--> Correct! You know me so well! My favorite color is hot pink.
# Wrong --> Wrong! You don't know me even a little bit! My favorite color is hot pink. 

# Q2: How much do I like tap dancing?
# a. You have never tap danced before.
# b. You like it a little.
# c. You think tap dancing is the most incredible thing ever 
# (almost as awesome as coding).
# A2: c
# Responses:
# Wrong -->  Wrong! I love tap dancing so much. 
# Right --> You are so right! Tap is life. 

# Q3: Where did I grow up? (City, US State Initials)
# A3: Sugar Land, TX
# Responses:
# Wrong --> Wrong, you know nothing Jon Snow! I grew up in Sugar Land, TX.
# Right --> Correct! You seriously could be my best friend!

q1 = "Is my favorite color purple?"
q2 = """How much do I like tap dancing?
a. You have never tap danced before.
b. You like it a little.
c. You think tap dancing is the most incredible thing ever (almost as awesome as coding)."""
q3 = "Where did I grow up? (City, US State Initials)"
questions = [q1, q2, q3]


answers = ["no", "c", "sugar land, tx"]

c1 = "Correct! You know me so well! My favorite color is hot pink."
c2 = "You are so right! Tap is life."
c3 = "Correct! You seriously could be my best friend!"
correctResponses = [c1, c2, c3]

w1 = "Wrong! You don't know me even a little bit! My favorite color is hot pink."
w2 = "Wrong! I love tap dancing so much."
w3 = "Wrong, you know nothing Jon Snow! I grew up in Sugar Land, TX."
wrongResponses = [w1, w2, w3]

count = 0
numberOfCorrectAnswers = 0
for q in questions :
	# Is there a way to add padding between printing out q
	# and where you grab the input??
	answer = input(q)
	if answer.lower() == answers[count]:
		print(correctResponses[count])
		numberOfCorrectAnswers = numberOfCorrectAnswers + 1
	else:
		print(wrongResponses[count])
	count = count + 1
	print("\n")

if (numberOfCorrectAnswers > 0):
	print("Congrats! You got", numberOfCorrectAnswers, "correct!")
else
	print("Sadly, you got all of the questions wrong.")


# TO DO:
# Add in enumerate stuff
# Look up elif
# Visualize results
# How to read and write from a file in Python?
