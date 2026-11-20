# Q1–Q18
# 1.
# a = 15b = 20print(a < b)print(a > b)print(a == b)print(a != b)print(a <= b)print(a >= b)



# 2.
# x = 10y = 10print(x == y)print(x != y)print(x < y)print(x <= y)print(x >= y)



# 3.
# a = 10b = 5print(a + b == 15)print(a * b > 40)print(a - b != 5)print(a // b == 2)



# 4.
# print("Python" == "Python")print("Python" == "python")print("Hello" != "hello")



# Strings are case-sensitive.

# 5.
# x = 20x += 10x -= 5x *= 2x //= 5print(x)



# 6.
# marks = 50marks += 10marks -= 5marks *= 2print(marks)



# 7.
# text = "Python Programming"print("Python" in text)print("Java" in text)print("Python" not in text)



# 8.
# word = "computer"print("p" in word)print("x" in word)print("c" not in word)



# 9.
# text = "Python"print("P" in text)print("p" in text)print("Python" in text)print("python" in text)



# 10.
# text = input()print("a" in text)



# 11.
# email = input()print("@" in email)



# 12.
# print(ord("A"))print(ord("a"))print(ord("Z"))print(ord("z"))print(ord("0"))print(ord("9"))print(ord("@"))



# 13.
# print(chr(65))print(chr(66))print(chr(97))print(chr(98))print(chr(48))print(chr(57))print(chr(64))



# 14.
# print(ord("A"))print(ord("a"))print(ord("B"))print(ord("b"))



# Lowercase letters have larger codes. The difference is 32.

# 15.
# ch = input()print(ord(ch))



# 16.
# ch = input()print(chr(ord(ch) + 1))



# 17.
# print("A" < "B")print("a" < "b")print("A" < "a")print("0" < "9")



# 18.
# print(chr(9731))print(chr(9829))print(chr(8377))print(ord(chr(9731)))print(ord(chr(9829)))print(ord(chr(8377)))



# Q19–Q41
# 19.
# text = "PYTHON"print(text[0])print(text[1])print(text[-1])print(text[-2])



# 20.
# text = "COMPUTER"print(text[0])print(text[3])print(text[-1])print(text[-3])



# 21.
# text = "PYTHON"print(text[0])print(text[2])print(text[-1])print(text[-2])



# 22.
# word = input()print(word[0])print(word[-1])



# 23.
# word = "PROGRAM"print(word[0])print(word[2])print(word[-1])print(word[-4])



# 24.
# text = "PYTHON"print(text[0:3])print(text[2:5])print(text[1:6])



# 25.
# text = "PROGRAMMING"print(text[:4])print(text[4:])print(text[:])



# 26.
# text = "COMPUTER"print(text[-5:])print(text[:-3])print(text[-6:-2])



# 27.
# text = "PYTHON"print(text[::2])print(text[1::2])print(text[::-1])



# 28.
# text = input()print(text[::-1])



# 29.
# text = input()print(text[::2])



# 30.
# text = input()print(text[:3])print(text[-3:])



# 31.
# text = "ABCDEFGHIJ"print(text[2:8:2])print(text[8:2:-2])print(text[::-2])



# 32.
# text = "BTECH-CSE-2026"print(text[:5])print(text[6:9])print(text[10:])



# 33.
# text = "Python is easy"print(text.split())



# 34.
# data = "apple,banana,mango"print(data.split(","))



# 35.
# text = "Python is easy"print(text.split(","))



# 36.
# name = input()words = name.split()print(words[0])print(words[1])print(words[2])



# 37.
# first_name, last_name = input().split()print("First Name:", first_name)print("Last Name:", last_name)



# 38.
# a, b, c = map(int, input().split())print(a + b + c)



# 39.
# data = input().split(",")print("Name:", data[0])print("Age:", data[1])print("Course:", data[2])print("City:", data[3])



# 40.
# email = input()data = email.split("@")print("Username:", data[0])print("Domain:", data[1])



# 41.
# text = input()words = text.split()print("First word:", words[0])print("Last word:", words[-1])print("Total words:", len(words))



# Q42–Q59
# 42.
# print("Hello\nWorld")



# 43.
# print("Name:\tRahul")print("Age:\t20")print("City:\tAhmedabad")



# 44.
# print("C:\\Python\\Programs")



# 45.
# print('It\'s Python')



# 46.
# print("He said \"Hello\"")



# 47.
# print("Python\nProgramming")



# 48.
# print("Student Details\n")print("Name:\tRahul")print("Age:\t20")print("Course:\tB.Tech")



# 49.
# print("2026", "09", "09", sep="-")



# 50.
# print("Hello", end=" ")print("Python")



# 51.
# print(10, 20, 30, sep="-")print(40, 50, 60, sep="-")



# 52.
# name = input()age = input()city = input()course = input()print(f"Name: {name}")print(f"Age: {age}")print(f"City: {city}")print(f"Course: {course}")



# 53.
# price = float(input())print(f"{price:.2f}")



# 54.
# age = int(input("Enter age: "))print("Age after 5 years:", age + 5)



# 55.
# print("It's Python")



# 56.
# text = "Python"print(text[1:4])



# 57.
# a, b = input().split()print(a, b)



# 58.
# a, b = input().split()print(int(a) + int(b))



# 59.
# print(r"C:\new\test")



# Q60–Q70
# 60.
# name = input()a, b, c = map(int, input().split())total = a + b + caverage = total / 3print(f"Name: {name}")print(f"Total: {total}")print(f"Average: {average:.2f}")



# 61.
# student_id = input()data = student_id.split("-")degree = data[0]batch = data[1]branch = data[2]roll = int(student_id[-3:])print("Degree:", degree)print("Batch:", batch)print("Branch:", branch)print("Roll Number:", roll)



# 62.
# name = input()words = name.split()username = words[0].lower() + "." + words[2].lower()print(username)



# 63.
# text = input()words = text.split()print("First word:", words[0])print("Last word:", words[-1])print("Total words:", len(words))



# 64.
# email = input()data = email.split("@")print("@ Present:", "@" in email)print("Username:", data[0])print("Domain:", data[1])



# 65.
# ch = input()print("Character:", ch)print("Code:", ord(ch))print("Previous:", chr(ord(ch) - 1))print("Next:", chr(ord(ch) + 1))



# 66.
# product = input()price = float(input())quantity = int(input())discount = float(input())subtotal = price * quantitydiscount_amount = subtotal * discount / 100total = subtotal - discount_amountprint(f"Product: {product}")print(f"Price: {price:.2f}")print(f"Quantity: {quantity}")print(f"Subtotal: {subtotal:.2f}")print(f"Discount: {discount_amount:.2f}")print(f"Final Total: {total:.2f}")



# 67.
# date = input()data = date.split("-")print("Day:", data[0])print("Month:", data[1])print("Year:", data[2])print("Year using slicing:", date[6:])



# 68.
# text = input()words = text.split()print("First Word:", words[0])print("Second Word:", words[1])print("First Word Reversed:", words[0][::-1])print("Second Word Reversed:", words[1][::-1])



# 69.
# student = input()data = student.split("-")degree = data[0]batch = data[1]branch = data[2]roll = data[3]print("Degree:", degree)print("Batch:", batch)print("Branch:", branch)print("Roll:", roll)print("Code:", degree + "/" + branch + "/" + roll)



# 70.
# name = input()words = name.split()first = words[0]last = words[-1]print(f"Original: {name}")print(f"First Name: {first}")print(f"Last Name: {last}")print(f"First Name (Upper Part): {first[:3].upper()}")print(f"Last Name (Lower Part): {last[-3:].lower()}")print(f"Full Name Reversed: {name[::-1]}")