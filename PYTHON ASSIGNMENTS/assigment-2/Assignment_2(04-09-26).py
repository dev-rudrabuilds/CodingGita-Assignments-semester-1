# Topic 1: Type Casting
# 1.
# age = "25"age = int(age)print(age)print(type(age))



# 2.
# marks = "75.5"marks = float(marks)print(marks)print(type(marks))



# 3.
# number = 50number = float(number)print(number)print(type(number))



# 4.
# marks = 85.9marks = int(marks)print(marks)



# 5.
# roll_number = 101roll_number = str(roll_number)print(roll_number)print(type(roll_number))



# 6.
# a = int("18")b = float("92.5")c = str(100)d = int(45.8)print(a, type(a))print(b, type(b))print(c, type(c))print(d, type(d))



# 7.
# 20
# 10
# 25
# <class 'int'>
# <class 'int'>
# <class 'str'>


# 8.
# age = "19"new_age = int(age) + 1print("Age:", new_age)



# 9.
# marks = int("85")print("Final Marks:", marks + 5)



# 10.
# price = float("1499.50")total = price + 99.50print("Total Amount:", total)



# Topic 2: Arithmetic Operators
# 11.
# a = 20b = 6print(a + b)print(a - b)print(a * b)print(a / b)print(a // b)print(a % b)print(a ** b)



# 12.
# 3.4
# 3
# 2


# / gives division, // gives floor division, % gives remainder.

# 13.
# 20


# result = (10 + 5) * 2print(result)



# 14.
# 10


# result = 20 - (4 * 3) + 2print(result)



# 15.
# 8
# 9
# 100


# side = 5area = side ** 2print(area)



# 16.
# notebook = 80pen = 20pencil = 10print("Total Amount:", notebook + pen + pencil)



# 17.
# notebook = 3 * 50pen = 2 * 15calculator = 1 * 500print("Notebook Cost:", notebook)print("Pen Cost:", pen)print("Calculator Cost:", calculator)print("Total Bill:", notebook + pen + calculator)



# 18.
# students = 47print("Complete Groups:", students // 5)print("Students Left:", students % 5)



# 19.
# total = 85 + 78 + 92average = total / 3print("Total:", total)print("Average:", average)



# 20.
# total = 78 + 85 + 92 + 81 + 74percentage = total / 5print("Total Marks:", total)print("Percentage:", percentage)



# Topic 3: Digit Extraction
# 21.
# number = 583print("Ones Digit:", number % 10)



# 22.
# number = 583print("Tens Digit:", (number // 10) % 10)



# 23.
# number = 583print("Hundreds Digit:", number // 100)



# 24.
# number = 746print("Ones Digit:", number % 10)print("Tens Digit:", (number // 10) % 10)print("Hundreds Digit:", number // 100)



# 25.
# number = 5829print("Ones Digit:", number % 10)print("Tens Digit:", (number // 10) % 10)print("Hundreds Digit:", (number // 100) % 10)print("Thousands Digit:", number // 1000)



# 26.
# number = 583a = number % 10b = (number // 10) % 10c = number // 100print("Sum of Digits:", a + b + c)



# 27.
# number = 4726a = number % 10b = (number // 10) % 10c = (number // 100) % 10d = number // 1000print("Sum of Digits:", a + b + c + d)



# 28.
# number = 234a = number % 10b = (number // 10) % 10c = number // 100print("Product of Digits:", a * b * c)



# 29.
# number = 583reverse = (number % 10) * 100 + ((number // 10) % 10) * 10 + number // 100print("Original Number:", number)print("Reversed Number:", reverse)



# 30.
# number = 4726reverse = (number % 10) * 1000 + ((number // 10) % 10) * 100 + ((number // 100) % 10) * 10 + number // 1000print("Original Number:", number)print("Reversed Number:", reverse)



# 31.
# number = 5834print("Thousands Place:", (number // 1000) * 1000)print("Hundreds Place:", ((number // 100) % 10) * 100)print("Tens Place:", ((number // 10) % 10) * 10)print("Ones Place:", number % 10)



# 32.
# number = 583difference = (number // 100) - (number % 10)print("Difference:", difference)



# 33.
# number = 583ones = number % 10print("Ones Digit:", ones)



# 34.
# number = 9365print("Thousands Digit:", number // 1000)print("Hundreds Digit:", (number // 100) % 10)print("Tens Digit:", (number // 10) % 10)print("Ones Digit:", number % 10)



# 35.
# hundreds = 5tens = 8ones = 3number = hundreds * 100 + tens * 10 + onesprint("Number:", number)



# Topic 4: Real-Life Arithmetic Problems
# 36.
# principal = 10000rate = 5time = 2si = (principal * rate * time) / 100print("Simple Interest:", si)



# 37.
# length = 15width = 8print("Area:", length * width)print("Perimeter:", 2 * (length + width))



# 38.
# pi = 3.14r = 7area = pi * r ** 2print("Area:", area)



# 39.
# celsius = 35fahrenheit = (celsius * 9 / 5) + 32print("Fahrenheit:", fahrenheit)



# 40.
# total_seconds = 367print("Minutes:", total_seconds // 60)print("Seconds:", total_seconds % 60)



# 41.
# total_seconds = 7384hours = total_seconds // 3600minutes = (total_seconds % 3600) // 60seconds = total_seconds % 60print("Hours:", hours)print("Minutes:", minutes)print("Seconds:", seconds)



# 42.
# gross = 25000 + 5000 + 2500net = gross - 3000print("Gross Salary:", gross)print("Net Salary:", net)



# 43.
# distance = 120fuel = distance / 20cost = fuel * 100print("Fuel Required:", fuel)print("Total Fuel Cost:", cost)



# 44.
# price = float("2500")discount = float("10")discount_amount = price * discount / 100final_price = price - discount_amountprint("Discount Amount:", discount_amount)print("Final Price:", final_price)



# Topic 5: Type Casting + Arithmetic
# 45.
# price = int("1200")quantity = int("4")print("Price:", price)print("Quantity:", quantity)print("Total Price:", price * quantity)



# 46.
# python_marks = int("85")math_marks = int("78")physics_marks = int("91")total = python_marks + math_marks + physics_marksprint("Total:", total)print("Average:", total / 3)



# 47.
# price = int("1500")quantity = int("2")tax_rate = int("5")subtotal = price * quantitytax = subtotal * tax_rate / 100print("Subtotal:", subtotal)print("Tax Amount:", tax)print("Final Bill:", subtotal + tax)



# 48.
# price = 2000discount = price * 15 / 100after_discount = price - discountgst = after_discount * 18 / 100final_price = after_discount + gstprint("Discount Amount:", discount)print("Price After Discount:", after_discount)print("GST Amount:", gst)print("Final Price:", final_price)



# 49.
# price = int("500")quantity = 3total = price * quantityprint("Total:", total)



# 50.
# marks1 = int("80")marks2 = int("75")marks3 = int("90")total = marks1 + marks2 + marks3print("Total Marks:", total)



# Topic 6: Output Prediction
# 51.
# 50
# 50
# <class 'str'>
# <class 'int'>


# 52.
# 99.99
# 99


# int() removes the decimal part.

# 53.
# 17
# 7
# 60
# 2.4
# 2
# 2


# 54.
# 20
# 30
# 7.0
# 2.5


# Parentheses calculate the enclosed expression first.

# 55.
# 4
# 8
# 6


# - a = Ones
# - c = Tens
# - d = Hundreds
# Topic 7: Mixed Debugging
# 56.
# student_name = "Ravi"marks = "85"total = int(marks) + 5print("Student:", student_name)print("Marks:", total)print("Type:", type(total))



# 57.
# number = 746ones = number % 10tens = (number // 10) % 10hundreds = number // 100print("Ones:", ones)print("Tens:", tens)print("Hundreds:", hundreds)



# 58.
# price = int("2000")discount = int("15")discount_amount = price * discount / 100final_price = price - discount_amountprint("Discount:", discount_amount)print("Final Price:", final_price)



# 59.
# student_name = "Rahul"marks1 = int("85")marks2 = int("90")marks3 = int("78")total = marks1 + marks2 + marks3average = total / 3print("Student:", student_name)print("Total Marks:", total)print("Average:", average)print("Marks Type:", type(total))



# 60.
# number = 5836thousands = number // 1000hundreds = (number // 100) % 10tens = (number // 10) % 10ones = number % 10total = thousands + hundreds + tens + onesreverse = ones * 1000 + tens * 100 + hundreds * 10 + thousandsprint("Thousands:", thousands)print("Hundreds:", hundreds)print("Tens:", tens)print("Ones:", ones)print("Sum:", total)print("Reversed:", reverse)price = int("1250")quantity = int("4")discount = int("10")subtotal = price * quantitydiscount_amount = subtotal * discount / 100final_amount = subtotal - discount_amountprint("Subtotal:", subtotal)print("Discount Amount:", discount_amount)print("Final Amount:", final_amount)