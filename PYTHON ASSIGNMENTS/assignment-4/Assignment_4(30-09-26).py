# Topic 1 — Basic if Statements
# 1.
# num = int(input())if num > 0:    print("Positive Number")



# 2.
# age = int(input())if age >= 18:    print("Eligible to Vote")



# 3.
# temp = int(input())if temp > 40:    print("High Temperature")



# 4.
# num = int(input())if num % 5 == 0:    print("Divisible by 5")



# 5.
# amount = int(input())if amount >= 1000:    print("Free Delivery")



# 6.
# ch = input()if ch == "A":    print("You entered A")



# 7.
# password = input()if len(password) >= 8:    print("Strong Length")



# 8.
# num = int(input())if num >= 100 and num <= 999:    print("Three Digit Number")



# Topic 2 — if-else Statements
# 9.
# num = int(input())if num % 2 == 0:    print("Even")else:    print("Odd")



# 10.
# marks = int(input())if marks >= 40:    print("Pass")else:    print("Fail")



# 11.
# age = int(input())if age >= 18:    print("Adult")else:    print("Minor")



# 12.
# num = int(input())if num > 0:    print("Positive")else:    print("Non-Positive")



# 13.
# num = int(input())if num % 3 == 0:    print("Divisible by 3")else:    print("Not Divisible by 3")



# 14.
# correct_password = "python123"password = input()if password == correct_password:    print("Login Successful")else:    print("Invalid Password")



# 15.
# username = input()if username == "admin":    print("Welcome Admin")else:    print("Invalid Username")



# 16.
# a, b = map(int, input().split())if a > b:    print(a)elif b > a:    print(b)else:    print("Both are Equal")



# 17.
# temp = int(input())if temp > 30:    print("Hot")else:    print("Comfortable")



# 18.
# amount = int(input())if amount >= 5000:    print("Discount Available")else:    print("No Discount")



# Topic 3 — if-elif-else
# 19.
# marks = int(input())if marks >= 90:    print("A")elif marks >= 80:    print("B")elif marks >= 70:    print("C")elif marks >= 60:    print("D")else:    print("F")



# 20.
# temp = int(input())if temp >= 40:    print("Very Hot")elif temp >= 30:    print("Hot")elif temp >= 20:    print("Warm")else:    print("Cold")



# 21.
# color = input()if color == "red":    print("Stop")elif color == "yellow":    print("Wait")elif color == "green":    print("Go")else:    print("Invalid Signal")



# 22.
# units = int(input())if units <= 100:    print("Low Usage")elif units <= 300:    print("Medium Usage")elif units <= 500:    print("High Usage")else:    print("Very High Usage")



# 23.
# age = int(input())if age < 5:    print("Free Ticket")elif age <= 12:    print("Child Ticket")elif age <= 59:    print("Regular Ticket")else:    print("Senior Ticket")



# 24.
# bmi = float(input())if bmi < 18.5:    print("Underweight")elif bmi < 25:    print("Normal")elif bmi < 30:    print("Overweight")else:    print("Obese")



# 25.
# month = int(input())if month in (1, 3, 5, 7, 8, 10, 12):    print("31 Days")elif month in (4, 6, 9, 11):    print("30 Days")elif month == 2:    print("28 or 29 Days")else:    print("Invalid Month")



# 26.
# a, b, op = input().split()a = float(a)b = float(b)if op == "+":    print(a + b)elif op == "-":    print(a - b)elif op == "*":    print(a * b)elif op == "/" and b != 0:    print(a / b)else:    print("Invalid Operator")



# 27.
# day = int(input())if day == 1:    print("Monday")elif day == 2:    print("Tuesday")elif day == 3:    print("Wednesday")elif day == 4:    print("Thursday")elif day == 5:    print("Friday")elif day == 6:    print("Saturday")elif day == 7:    print("Sunday")else:    print("Invalid Day")



# 28.
# score = int(input())if score >= 90:    print("Excellent")elif score >= 75:    print("Very Good")elif score >= 60:    print("Good")elif score >= 40:    print("Average")else:    print("Needs Improvement")



# Topic 4 — Logical Conditions
# 29.
# marks, attendance = map(int, input().split())if marks >= 60 and attendance >= 75:    print("Eligible")else:    print("Not Eligible")



# 30.
# marks, income = map(int, input().split())if marks >= 85 or income < 300000:    print("Scholarship Available")else:    print("No Scholarship")



# 31.
# day = input()if day == "Saturday" or day == "Sunday":    print("Weekend")else:    print("Weekday")



# 32.
# username, password = input().split()if username == "student" and password == "python123":    print("Access Granted")else:    print("Access Denied")



# 33.
# city = input()if city == "Ahmedabad" or city == "Gandhinagar":    print("Delivery Available")else:    print("Delivery Unavailable")



# 34.
# num = int(input())if num >= 10 and num <= 50:    print("Inside Range")else:    print("Outside Range")



# 35.
# amount, otp = input().split()amount = int(amount)if amount <= 50000 and otp == "1234":    print("Transaction Approved")else:    print("Transaction Declined")



# Topic 5 — Nested if
# 36.
# username, password = input().split()if username == "admin":    if password == "admin123":        print("Login Successful")    else:        print("Wrong Password")else:    print("Invalid Username")



# 37.
# age, status = input().split()age = int(age)if age >= 18:    if status == "pass":        print("License Approved")    else:        print("Test Not Passed")else:    print("Age Not Eligible")



# 38.
# balance, amount = map(int, input().split())if amount <= balance:    if amount % 100 == 0:        print("Withdrawal Successful")    else:        print("Enter Amount in Multiples of 100")else:    print("Insufficient Balance")



# 39.
# attendance, marks = map(int, input().split())if attendance >= 75:    if marks >= 40:        print("Pass")    else:        print("Fail")else:    print("Not Eligible Due to Attendance")



# 40.
# account, balance = input().split()balance = int(balance)if account == "savings":    if balance >= 1000:        print("Minimum Balance Maintained")    else:        print("Minimum Balance Not Maintained")else:    print("Unsupported Account")



# 41.
# amount, payment = input().split()amount = int(amount)if amount >= 500:    if payment == "card":        print("Card Payment Accepted")    elif payment == "upi":        print("UPI Payment Accepted")    else:        print("Unsupported Payment Method")else:    print("Minimum Order Amount Not Reached")



# 42.
# year, attendance = map(int, input().split())if year == 2 or year == 3 or year == 4:    if attendance >= 75:        print("Room Eligible")    else:        print("Attendance Too Low")else:    print("Not Eligible by Year")



# 43.
# plan, usage = input().split()usage = int(usage)if plan == "basic":    if usage > 100:        print("Recommend Upgrade")    else:        print("Basic Plan Is Sufficient")else:    print("Already on Higher Plan")



# Topic 6 — Nested if-elif-else
# 44.
# a, b, c = map(int, input().split())if a == b and b == c:    print("All are Equal")elif a >= b and a >= c:    if a == b:        print("A and B are Equal and Greatest")    elif a == c:        print("A and C are Equal and Greatest")    else:        print("A is Greatest")elif b >= a and b >= c:    if b == c:        print("B and C are Equal and Greatest")    else:        print("B is Greatest")else:    print("C is Greatest")



# 45.
# marks, attendance = map(int, input().split())if attendance >= 75:    if marks >= 90:        print("Grade A")    elif marks >= 75:        print("Grade B")    elif marks >= 60:        print("Grade C")    elif marks >= 40:        print("Grade D")    else:        print("Grade F")else:    print("Not Eligible")



# 46.
# salary, rating = map(int, input().split())if salary >= 30000:    if rating == 5:        print("Bonus: 20%")    elif rating == 4:        print("Bonus: 15%")    elif rating == 3:        print("Bonus: 10%")    else:        print("Bonus: 5%")else:    print("Not Eligible for Bonus")



# 47.
# age, distance = map(int, input().split())if age < 5:    print("Free")elif age >= 60:    print("Senior")else:    if distance <= 10:        print("Regular - Short Distance")    else:        print("Regular - Long Distance")



# 48.
# stock, status = input().split()stock = int(stock)if stock > 0:    if status == "paid":        print("Order Confirmed")    elif status == "pending":        print("Payment Pending")    else:        print("Invalid Payment Status")else:    print("Out of Stock")



# 49.
# age, ticket = input().split()age = int(age)if age < 5:    print("Free Travel")elif age >= 60:    print("Senior Passenger")else:    if ticket == "AC":        print("AC Ticket")    elif ticket == "Sleeper":        print("Sleeper Ticket")    else:        print("Invalid Ticket Type")



# Topic 7 — match-case
# 50.
# choice = int(input())match choice:    case 1:        print("Add")    case 2:        print("View")    case 3:        print("Update")    case 4:        print("Delete")    case _:        print("Invalid Choice")



# 51.
# day = int(input())match day:    case 1:        print("Monday")    case 2:        print("Tuesday")    case 3:        print("Wednesday")    case 4:        print("Thursday")    case 5:        print("Friday")    case 6:        print("Saturday")    case 7:        print("Sunday")    case _:        print("Invalid Day")



# 52.
# a, b, op = input().split()a = float(a)b = float(b)match op:    case "+":        print(a + b)    case "-":        print(a - b)    case "*":        print(a * b)    case "/" if b != 0:        print(a / b)    case _:        print("Invalid Operator")



# 53.
# color = input()match color:    case "red":        print("Stop")    case "yellow":        print("Wait")    case "green":        print("Go")    case _:        print("Invalid Signal")



# 54.
# grade = input()match grade:    case "A":        print("Excellent Performance")    case "B":        print("Very Good Performance")    case "C":        print("Good Performance")    case "D":        print("Needs Improvement")    case "F":        print("Failed")    case _:        print("Invalid Grade")



# 55.
# code = int(input())match code:    case 1:        print("Check Balance")    case 2:        print("Recharge")    case 3:        print("Data Usage")    case 4:        print("Customer Support")    case _:        print("Invalid Service")



# 56.
# month = int(input())match month:    case 1:        print("January")    case 2:        print("February")    case 3:        print("March")    case 4:        print("April")    case 5:        print("May")    case 6:        print("June")    case 7:        print("July")    case 8:        print("August")    case 9:        print("September")    case 10:        print("October")    case 11:        print("November")    case 12:        print("December")    case _:        print("Invalid Month")



# 57.
# extension = input()match extension:    case "py":        print("Python File")    case "txt":        print("Text File")    case "pdf":        print("PDF File")    case "jpg":        print("Image File")    case _:        print("Unknown File Type")



# Topic 8 — Conditional Statements + Previous Concepts
# 58.
# student_id = input()data = student_id.split("-")print("Degree:", data[0])print("Batch:", data[1])print("Branch:", data[2])print("Roll Number:", data[3])if data[2] == "CSE":    print("CSE Student")else:    print("Non-CSE Student")



# 59.
# email = input()data = email.split("@")domain = data[1]if domain == "gmail.com":    print("Gmail User")else:    print("Other Email Provider")



# 60.
# name = input()words = name.split()username = words[0].lower() + "." + words[2].lower()if "." in username:    print("Valid Username Format")else:    print("Invalid Username Format")



# 61.
# num = int(input())if num < 10:    print("One Digit")elif num < 100:    print("Two Digits")elif num < 1000:    print("Three Digits")else:    print("Four or More Digits")



# 62.
# price, quantity = map(int, input().split())subtotal = price * quantityif subtotal >= 5000:    discount = 20elif subtotal >= 2000:    discount = 10else:    discount = 0final = subtotal - (subtotal * discount / 100)print("Subtotal:", subtotal)print("Discount:", discount, "%")print(f"Final: {final:.2f}")



# 63.
# units = int(input())if units <= 100:    rate = 5elif units <= 300:    rate = 7else:    rate = 10bill = units * rateprint("Units:", units)print("Rate: ₹", rate)print("Bill: ₹", bill)



# 64.
# balance = 10000choice = int(input())match choice:    case 1:        print("Balance:", balance)    case 2:        amount = int(input())        balance += amount        print("Deposit Successful")        print("Balance:", balance)    case 3:        amount = int(input())        if amount <= balance:            balance -= amount            print("Withdrawal Successful")            print("Balance:", balance)        else:            print("Insufficient Balance")    case 4:        print("Exit")    case _:        print("Invalid Choice")



# 65.
# choice, quantity = map(int, input().split())match choice:    case 1:        product = "Pizza"        price = 250    case 2:        product = "Burger"        price = 150    case 3:        product = "Pasta"        price = 200    case 4:        product = "Sandwich"        price = 120    case _:        product = "Invalid"        price = 0if price == 0:    print("Invalid Choice")else:    total = price * quantity    if total >= 500:        discount = total * 10 / 100    else:        discount = 0    final = total - discount    print("Product:", product)    print("Total:", total)    print(f"Discount: {discount:.2f}")    print(f"Final: {final:.2f}")



# 66.
# a, b, c, attendance = map(int, input().split())total = a + b + caverage = total / 3if attendance >= 75:    if average >= 90:        print("Outstanding")    elif average >= 75:        print("Very Good")    elif average >= 60:        print("Good")    elif average >= 40:        print("Pass")    else:        print("Fail")else:    print("Not Eligible")



# 67.
# distance, ride = input().split()distance = float(distance)match ride:    case "normal":        rate = 15    case "premium":        rate = 25    case _:        rate = 0if rate == 0:    print("Invalid Ride Type")else:    fare = distance * rate    if distance > 20:        fare = fare + (fare * 10 / 100)    print(f"Fare: {fare:.2f}")



# 68.
# score, percentage, category = input().split()score = int(score)percentage = int(percentage)match category:    case "general":        if score >= 80 and percentage >= 75:            print("Admission Eligible")        else:            print("Admission Not Eligible")    case "obc":        if score >= 70 and percentage >= 70:            print("Admission Eligible")        else:            print("Admission Not Eligible")    case "sc":        if score >= 60 and percentage >= 60:            print("Admission Eligible")        else:            print("Admission Not Eligible")    case _:        print("Admission Not Eligible")



# Topic 9 — Debugging Conditional Programs
# 69.
# age = int(input("Enter age: "))if age >= 18:    print("Eligible")else:    print("Not Eligible")



# 70.
# marks = int(input("Enter marks: "))if marks >= 90:    print("A")elif marks >= 75:    print("B")elif marks >= 40:    print("Pass")else:    print("Fail")



# Topic 10 — Output Prediction & Execution Flow
# 71.
# marks = 85if marks >= 40:    print("Pass")elif marks >= 75:    print("Very Good")else:    print("Fail")



# Output:
# Pass


# 72.
# marks = 85if marks >= 90:    print("A")elif marks >= 75:    print("B")elif marks >= 40:    print("Pass")else:    print("Fail")



# Outputs:
# - 95 → A
# - 85 → B
# - 50 → Pass
# - 30 → Fail
# 73.
# age = 20has_id = Trueif age >= 18:    if has_id:        print("Entry Allowed")    else:        print("ID Required")else:    print("Underage")



# Outputs:
# - Age 20, ID True → Entry Allowed
# - Age 20, ID False → ID Required
# - Age 16, ID True → Underage
# 74.
# choice = 5match choice:    case 1:        print("Add")    case 2:        print("View")    case 3:        print("Delete")    case _:        print("Invalid Choice")



# Outputs:
# - 1 → Add
# - 3 → Delete
# - 5 → Invalid Choice
# case _ handles all choices that do not match the other cases.

# 75.
# marks = 82attendance = 80if attendance >= 75:    if marks >= 90:        print("Grade A")    elif marks >= 75:        print("Grade B")    elif marks >= 40:        print("Pass")    else:        print("Fail")else:    print("Not Eligible")



# Output:
# Grade B