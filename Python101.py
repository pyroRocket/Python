# Strings

print("Hello World!")  # Double quotes
print('Hello World')  # Single quotes
# You cant mix type of quotes ex: print('Hello world")
print("""This is a 
multi line string""")

print("\n")  # new line

# Math
print("Math time: ")
print(67 + 69)  # Add
print(67 - 69)  # Subtract
print(67 * 69)  # Multiply
print(10 / 5)  # Divide
print(20 + 20 - 20 * 20 / 20)  # PEMDAS (Order of operations)
print(20 ** 2)  # Exponents
print(23 % 4)  # Modulo
print(10 // 5)  # truncated division

print("\n")  # new line

# Variables and Methods
print("Fun with variables and methods:")
quote = "Give me liberty or give me death"   # Assigning a variable without declaring type
print(len(quote))  # prints length of variable: quote
print(quote.upper())  # turns string into all uppercase
print(quote.lower())  # turns string into all lowercase
print(quote.title())  # capitalizes the first letter of every word

name = "William"  # String
age = 16  # int int(16)
gpa = 5.7  # float float(5.0)

print(int(age))
print(int(gpa))  # Truncation

print("My name is" + name + " and I am " + str(age) + " years old.")

print("\n")  # new line

age += 1  # age = age + 1
print(age)

birthday = 3
age += birthday  # age = age + birthday
print(age)

print("\n")  # new line

# Functions
print("Time for FUNctions")


def whoAmI():
    otherName = "Dogan"
    otherAge = 12
    print("My name is " + otherName + " and I am " + str(otherAge) + " years old.")


whoAmI()


# Functions with param
def addOneHundred(num):
    num += 100
    print(num)


addOneHundred(1)


def add(x, y):
    print(x + y)


add(3, 7)


def multiply(x, y):
    return x * y


print(multiply(3, 9))


def squareRoot(x):
    return x ** .5


print(squareRoot(4))

print("\n")  # new line

# Boo lean expressions
print("Boolean Expressions:")
bool1 = True
bool2 = 3 * 3 == 9
bool3 = False
bool4 = 3 * 3 != 9

print(bool1, bool2, bool3, bool4)
print(type(bool1))

# Relational operators
greaterThan = 7 > 5
lessThan = 5 < 7
greaterThanEqualTo = 7 >= 7
lessThanEqualTo = 5 <= 5

print(greaterThan, lessThan, greaterThanEqualTo, lessThanEqualTo)

testAnd = (7 > 5) and (5 < 7)
testOr = (7 > 5) or (5 > 6)
testNot = not True

print(testAnd, testOr, testNot)

print("\n")  # new line

# Conditional Statements
print("Conditional statements:")


def soda(money):
    if money >= 2:
        return "You can afford a soda!"
    else:
        return "No soda for you :("


print(soda(3))
print(soda(1))


def alcohol(age, money):
    if (age >= 21) and (money >= 5):
        return "Time to get tipsy!"
    elif (age >= 21) and (money < 5):
        return "Come back when you have the money"
    elif (age < 21) and (money >= 5):
        return "Nice try kid."
    else:
        return "You are too young and too broke"


print(alcohol(21, 5))
print(alcohol(21, 4))
print(alcohol(20, 6))
print(alcohol(19, 4))

print("\n")  # new line

# Lists
print("Lists use brackets")
movies = ["Deadpool", "Breaking Bad", "Mission Impossible", "El Camino"]

print(movies[0])
print(movies[0:2])  # Up to but not including 2
print(movies[1:])
print(movies[:2])
print(movies[-1])  # length -1 movies[length-1]
print(movies[-2])  # movies[length-2]
print(len(movies))

movies.append("JAWS")
print(movies)

movies.pop()  # remove last element
print(movies)

movies.pop(1)
print(movies)

movies = ["Deadpool", "Breaking Bad", "Mission Impossible", "El Camino"]
person = ["Katman", "Katman", "Dogan", "Dogan"]
combined = zip(movies, person)

print(list(combined))

print("\n")  # new line

# Tuples
print("Tuples have parenthesis and cannot change:")
grades = ('A', 'B', 'C', 'D', 'F')
print(grades[1])

print("\n")  # new line

# Looping
print("For loops - start to finish of iterate:")
fruits = ["apples", "bananas", "pears", "oranges"]
for item in fruits:
    print(item)

print("While loops - execute while true:")
i = 1
while i < 10:
    print(i)
    i += 1

