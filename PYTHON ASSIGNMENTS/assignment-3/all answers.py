# Topic-1 — Comparison Operators
# Q1 to Q4


# Q1 — Predict the Output
a = 15
b = 20

print(a < b)
print(a > b)
print(a == b)
print(a != b)
print(a <= b)
print(a >= b)

# Output:
# True
# False
# False
# True
# True
# False


# Q2 — Compare Expressions
x = 10
y = 10

print(x == y)
print(x != y)
print(x < y)
print(x <= y)
print(x >= y)

# Output:
# True
# False
# False
# True
# True

# == is used for comparison.
# = is used for assignment.


# Q3 — Comparison with Arithmetic
a = 10
b = 5

print(a + b == 15)
print(a * b > 40)
print(a - b != 5)
print(a // b == 2)

# Output:
# True
# True
# False
# True


# Q4 — String Comparison
print("Python" == "Python")
print("Python" == "python")
print("Hello" != "hello")

# Output:
# True
# False
# True

# String comparison is case-sensitive.
# "Python" and "python" are considered different strings.
#====================================================================

# Topic-2 — Assignment Operators
# Q5 to Q6


# Q5 — Trace the Value
x = 20

x += 10
print("After += 10:", x)   # 30

x -= 5
print("After -= 5:", x)    # 25

x *= 2
print("After *= 2:", x)    # 50

x //= 5
print("After //= 5:", x)   # 10

print("Final Value:", x)   # 10


# Q6 — Assignment Operator Practice
marks = 50

marks += 10
marks -= 5
marks *= 2

print("Final Marks:", marks)
# Output: Final Marks: 110
#============================================

# Topic-3 — Membership Operators with Strings
# Q7 to Q11


# Q7 — Basic Membership
text = "Python Programming"

print("Python" in text)
print("Java" in text)
print("Python" not in text)

# Output:
# True
# False
# False


# Q8 — Character Membership
word = "computer"

print("p" in word)
print("x" in word)
print("c" not in word)

# Output:
# True
# False
# False


# Q9 — Case Sensitivity in Membership
text = "Python"

print("P" in text)
print("p" in text)
print("Python" in text)
print("python" in text)

# Output:
# True
# False
# True
# False

# Membership checking is case-sensitive.
# Uppercase and lowercase characters are treated as different.


# Q10 — Membership with User Input
text = input("Enter a word or sentence: ")

print("a" in text)


# Q11 — Email Symbol Check
email = input("Enter your email: ")

print("@" in email)
#=============================================

# Topic-4 — ASCII and Unicode
# Q12 to Q18


# Q12 — Find Character Codes
print(ord("A"))
print(ord("a"))
print(ord("Z"))
print(ord("z"))
print(ord("0"))
print(ord("9"))
print(ord("@"))

# Output:
# 65
# 97
# 90
# 122
# 48
# 57
# 64


# Q13 — Convert Codes to Characters
print(chr(65))
print(chr(66))
print(chr(97))
print(chr(98))
print(chr(48))
print(chr(57))
print(chr(64))

# Output:
# A
# B
# a
# b
# 0
# 9
# @


# Q14 — Uppercase and Lowercase
print(ord("A"))
print(ord("a"))
print(ord("B"))
print(ord("b"))

# A = 65, a = 97
# B = 66, b = 98
#
# 1. ord("a") is larger than ord("A")
# 2. Difference = 97 - 65 = 32
# 3. Yes, the difference is also 32 for B and b.


# Q15 — Character Code Program
character = input("Enter a character: ")

print(ord(character))


# Q16 — Next Character
character = input("Enter an uppercase letter: ")

next_character = chr(ord(character) + 1)

print(next_character)


# Q17 — Character Comparison and Unicode
print("A" < "B")
print("a" < "b")
print("A" < "a")
print("0" < "9")

# Output:
# True
# True
# True
# True
#
# Unicode values:
# A = 65, B = 66
# a = 97, b = 98
# 0 = 48, 9 = 57


# Q18 — Unicode Character Challenge
print(chr(9731))
print(chr(9829))
print(chr(8377))

# Output:
# ☃
# ♥
# ₹

# Verify using ord()
print(ord("☃"))
print(ord("♥"))
print(ord("₹"))

# Output:
# 9731
# 9829
# 8377
#====================================

# Topic-5 — String Indexing
# Q19 to Q23


# Q19 — Basic Indexing
text = "PYTHON"

print("First Character:", text[0])
print("Second Character:", text[1])
print("Last Character:", text[-1])
print("Second-Last Character:", text[-2])


# Q20 — Positive and Negative Indexing
text = "COMPUTER"

print("Index 0:", text[0])
print("Index 3:", text[3])
print("Index -1:", text[-1])
print("Index -3:", text[-3])


# Q21 — Predict the Output
text = "PYTHON"

print(text[0])
print(text[2])
print(text[-1])
print(text[-2])

# Output:
# P
# T
# N
# O


# Q22 — Indexing a User Input
word = input("Enter a word: ")

print("First Character:", word[0])
print("Last Character:", word[-1])


# Q23 — Think Carefully About Indexing
word = "PROGRAM"

print("word[0]:", word[0])
print("word[2]:", word[2])
print("word[-1]:", word[-1])
print("word[-4]:", word[-4])

# Output:
# word[0]: P
# word[2]: O
# word[-1]: M
# word[-4]: G
#=========================================

# Topic-6 — String Slicing
# Q24 to Q32


# Q24 — Basic Slicing
text = "PYTHON"

print(text[0:3])
print(text[2:5])
print(text[1:6])

# Output:
# PYT
# THO
# YTHON


# Q25 — Start and Stop
text = "PROGRAMMING"

print(text[:4])
print(text[4:])
print(text[:])

# Output:
# PROG
# RAMMING
# PROGRAMMING


# Q26 — Negative Slicing
text = "COMPUTER"

print(text[-5:])
print(text[:-3])
print(text[-6:-2])

# Output:
# PUTER
# COMPU
# MPUT


# Q27 — Step in Slicing
text = "PYTHON"

print(text[::2])
print(text[1::2])
print(text[::-1])

# Output:
# PTO
# YHN
# NOHTYP


# Q28 — Reverse a String
text = input("Enter a string: ")

print(text[::-1])


# Q29 — Alternate Characters
text = input("Enter a string: ")

print(text[::2])


# Q30 — Extract First and Last Three Characters
text = input("Enter a string: ")

print("First Three:", text[:3])
print("Last Three:", text[-3:])


# Q31 — Slicing Challenge
text = "ABCDEFGHIJ"

print(text[2:8:2])
print(text[8:2:-2])
print(text[::-2])

# Output:
# CE G -> CEG
# IGE
# JHFDB
#
# text[2:8:2]
# Start = 2
# Stop = 8
# Step = 2
#
# text[8:2:-2]
# Start = 8
# Stop = 2
# Step = -2
#
# text[::-2]
# Start = beginning (default)
# Stop = end (default)
# Step = -2


# Q32 — Slice Without Counting from the Beginning
text = "BTECH-CSE-2026"

btech = text[:5]
cse = text[6:9]
year = text[10:]

print("BTECH:", btech)
print("CSE:", cse)
print("2026:", year)
#=================================================

# Topic-7 — String split()
# Q33 to Q41


# Q33 — Basic split()
text = "Python is easy"

print(text.split())

# Output:
# ['Python', 'is', 'easy']
# By default, split() separates words using whitespace (spaces).


# Q34 — Custom Separator
data = "apple,banana,mango"

print(data.split(","))

# Output:
# ['apple', 'banana', 'mango']


# Q35 — Separator Not Present
text = "Python is easy"

print(text.split(","))

# Output:
# ['Python is easy']
# It does not split at spaces because "," was specified as the separator.


# Q36 — Split a Full Name
name = input("Enter full name: ")

words = name.split()

for word in words:
    print(word)


# Q37 — Multiple Inputs Using split()
first_name, last_name = input("Enter first and last name: ").split()

print("First Name:", first_name)
print("Last Name:", last_name)


# Q38 — Three Numeric Inputs
a, b, c = input("Enter three numbers: ").split()

a = int(a)
b = int(b)
c = int(c)

print("Sum:", a + b + c)


# Q39 — Student Record
data = input("Enter student record: ")

name, age, course, city = data.split(",")

print("Name:", name)
print("Age:", age)
print("Course:", course)
print("City:", city)


# Q40 — Email Analyzer
email = input("Enter email: ")

username, domain = email.split("@")

print("Username:", username)
print("Domain:", domain)


# Q41 — Sentence Analyzer
sentence = input("Enter a sentence: ")

words = sentence.split()

print("First word:", words[0])
print("Last word:", words[-1])
print("Total words:", len(words))
#===========================================

# Topic-8 — Escape Sequences

# Q42. New Line
print("Hello\nWorld")


# Q43. Tab
print("Name:\tRahul")
print("Age:\t20")
print("City:\tAhmedabad")


# Q44. Backslash
print("C:\\Python\\Programs")


# Q45. Single Quote
print("It\'s Python")


# Q46. Double Quote
print("He said \"Hello\"")


# Q47. Predict the Output
print("Python\nProgramming")


# Q48. Combined Escape Sequences
print("Student Details\n")
print("Name:\tRahul")
print("Age:\t20")
print("Course:\tB.Tech")
#=================================

# Topic-9 — print(), sep, end, and f-Strings

# Q49. sep
print("2026", "09", "09", sep="-")
# Output: 2026-09-09


# Q50. end
print("Hello", end=" ")
print("Python")
# Output: Hello Python


# Q51. sep and end
print(10, 20, 30, sep="-", end="\n")
print(40, 50, 60, sep="-")


# Q52. Student Introduction
name = input("Enter name: ")
age = input("Enter age: ")
city = input("Enter city: ")
course = input("Enter course: ")

print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Course: {course}")


# Q53. Formatted Price
price = float(input("Enter price: "))
print(f"{price:.2f}")
#=====================================

# Topic-10 — Debugging

# Q54. String and Integer
age = int(input("Enter age: "))
print("Age after 5 years:", age + 5)


# Q55. Incorrect Quotes
print("It's Python")


# Q56. Incorrect Slicing Syntax
text = "Python"
print(text[1:4])


# Q57. Incorrect split() Separator
# The input uses a space, but split(",") expects a comma.
a, b = input().split()
print(a, b)


# Q58. String Addition vs Numeric Addition
a, b = input().split()

# Original program prints: 1020
print(a + b)

# Numeric addition
a = int(a)
b = int(b)
print(a + b)


# Q59. Escape Sequence Debugging
# \n means new line and \t means tab.
# Use double backslashes to display actual backslashes.
print("C:\\new\\test")
#========================================================

# Topic-11 — Integrated Problems


# Q60. Student Result Information
name = input("Enter student name: ")
marks = input("Enter three marks: ").split()

m1 = int(marks[0])
m2 = int(marks[1])
m3 = int(marks[2])

total = m1 + m2 + m3
average = total / 3

print(f"Name: {name}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")


# Q61. Student ID Analyzer
student_id = input("Enter Student ID: ")

parts = student_id.split("-")

degree = parts[0]
batch = parts[1]
branch = parts[2]
roll = int(parts[3])

last_three = student_id[-3:]

print(f"Degree: {degree}")
print(f"Batch: {batch}")
print(f"Branch: {branch}")
print(f"Roll Number: {roll}")


# Q62. Username Generator
full_name = input("Enter full name: ").split()

first_name = full_name[0]
last_name = full_name[2]

username = first_name.lower() + "." + last_name.lower()

print(username)


# Q63. Sentence Information
sentence = input("Enter a sentence: ")
words = sentence.split()

print(f"First word: {words[0]}")
print(f"Last word: {words[-1]}")
print(f"Number of words: {len(words)}")


# Q64. Email Analyzer + Membership
email = input("Enter email: ")

print(f"@ Present: {'@' in email}")

username, domain = email.split("@")

print(f"Username: {username}")
print(f"Domain: {domain}")


# Q65. Character Analyzer
character = input("Enter one character: ")

code = ord(character)
previous = chr(code - 1)
next_character = chr(code + 1)

print(f"Character: {character}")
print(f"Code: {code}")
print(f"Previous: {previous}")
print(f"Next: {next_character}")


# Q66. Product Bill
product = input("Enter product name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
discount_percentage = float(input("Enter discount percentage: "))

subtotal = price * quantity
discount = subtotal * discount_percentage / 100
final_total = subtotal - discount

print(f"Product: {product}")
print(f"Price: {price:.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: {subtotal:.2f}")
print(f"Discount: {discount:.2f}")
print(f"Final Total: {final_total:.2f}")


# Q67. Date Analyzer
date = input("Enter date: ")

parts = date.split("-")

day = parts[0]
month = parts[1]
year = parts[2]

year_slice = date[-4:]

print(f"Day: {day}")
print(f"Month: {month}")
print(f"Year: {year}")
print(f"Year using slicing: {year_slice}")


# Q68. String Transformation Challenge
text = input("Enter two words: ")

words = text.split()

first_word = words[0]
second_word = words[1]

print(f"First Word: {first_word}")
print(f"Second Word: {second_word}")
print(f"First Word Reversed: {first_word[::-1]}")
print(f"Second Word Reversed: {second_word[::-1]}")


# Q69. Final Challenge — Student Code Formatter
student_code = input("Enter student code: ")

parts = student_code.split("-")

degree = parts[0]
batch = parts[1]
branch = parts[2]
roll = parts[3]

code = f"{degree}/{branch}/{roll}"

print(f"Degree: {degree}")
print(f"Batch: {batch}")
print(f"Branch: {branch}")
print(f"Roll: {roll}")
print(f"Code: {code}")


# Q70. Final String + Input/Output Challenge
full_name = input("Enter full name: ")

words = full_name.split()

first_name = words[0]
last_name = words[-1]

first_upper = first_name[:3].upper()
last_lower = last_name[1:4].lower()

reversed_name = full_name[::-1]

print(f"Original: {full_name}")
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"First Name (Upper Part): {first_upper}")
print(f"Last Name (Lower Part): {last_lower}")
print(f"Full Name Reversed: {reversed_name}")