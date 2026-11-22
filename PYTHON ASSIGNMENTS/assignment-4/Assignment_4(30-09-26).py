# TOPIC 1 — BASIC if STATEMENTS (Q1–Q8)



# Q1. 
number = int(input("Enter a number: "))
if number > 0:
    print("Positive Number")


# Q2. 
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to Vote")


# Q3. 
temperature = float(input("Enter temperature: "))
if temperature > 40:
    print("High Temperature")


# Q4.
number = int(input("Enter a number: "))
if number % 5 == 0:
    print("Divisible by 5")


# Q5.
amount = float(input("Enter order amount: "))
if amount >= 1000:
    print("Free Delivery")


# Q6.
character = input("Enter one character: ")
if character == "A":
    print("You entered A")


# Q7. 
password = input("Enter password: ")
if len(password) >= 8:
    print("Strong Length")


# Q8.
number = int(input("Enter a number: "))
if number >= 100 and number <= 999:
    print("Three Digit Number")
#============================================

# Topic-2 — if-else Statements


# Q9. Even or Odd

num = int(input("Enter an integer: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Q10. Pass or Fail

marks = int(input("Enter marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")


# Q11. Adult or Minor

age = int(input("Enter age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")


# Q12. Number Sign

num = int(input("Enter an integer: "))

if num > 0:
    print("Positive")
else:
    print("Non-Positive")


# Q13. Divisible by 3

num = int(input("Enter an integer: "))

if num % 3 == 0:
    print("Divisible by 3")
else:
    print("Not Divisible by 3")


# Q14. Login Password

correct_password = "python123"
password = input("Enter password: ")

if password == correct_password:
    print("Login Successful")
else:
    print("Invalid Password")


# Q15. Username Check

username = input("Enter username: ")

if username == "admin":
    print("Welcome Admin")
else:
    print("Invalid Username")


# Q16. Greater Between Two Numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a)
elif b > a:
    print(b)
else:
    print("Both are Equal")


# Q17. Hot or Comfortable

temperature = int(input("Enter temperature: "))

if temperature > 30:
    print("Hot")
else:
    print("Comfortable")


# Q18. Shopping Discount Eligibility

amount = int(input("Enter shopping amount: "))

if amount >= 5000:
    print("Discount Available")
else:
    print("No Discount")
#================================================

# Topic-3: if-elif-else

# Q19.

marks = int(input("Enter marks: "))

if marks >= 90 and marks <= 100:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
elif marks >= 0:
    print("F")
else:
    print("Invalid Marks")


# Q20. 

temperature = int(input("Enter temperature: "))

if temperature >= 40:
    print("Very Hot")
elif temperature >= 30:
    print("Hot")
elif temperature >= 20:
    print("Warm")
else:
    print("Cold")


# Q21. 

signal = input("Enter signal color: ")

if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Wait")
elif signal == "green":
    print("Go")
else:
    print("Invalid Signal")


# Q22.

units = int(input("Enter electricity units: "))

if units >= 0 and units <= 100:
    print("Low Usage")
elif units <= 300 and units > 100:
    print("Medium Usage")
elif units <= 500 and units > 300:
    print("High Usage")
elif units > 500:
    print("Very High Usage")
else:
    print("Invalid Units")


# Q23.

age = int(input("Enter age: "))

if age < 5:
    print("Free Ticket")
elif age <= 12:
    print("Child Ticket")
elif age <= 59:
    print("Regular Ticket")
else:
    print("Senior Ticket")


# Q24.

bmi = float(input("Enter BMI: "))

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")


# Q25. 
month = int(input("Enter month number: "))

if month in (1, 3, 5, 7, 8, 10, 12):
    print("31 Days")
elif month in (4, 6, 9, 11):
    print("30 Days")
elif month == 2:
    print("28 or 29 Days")
else:
    print("Invalid Month")


# Q26.

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    if b != 0:
        print(a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid Operator")


# Q27. 

day = int(input("Enter day number: "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid Day")


# Q28. 

score = int(input("Enter score: "))

if score >= 90 and score <= 100:
    print("Excellent")
elif score >= 75:
    print("Very Good")
elif score >= 60:
    print("Good")
elif score >= 40:
    print("Average")
elif score >= 0:
    print("Needs Improvement")
else:
    print("Invalid Score")
#=======================================

# Topic-4: Logical Conditions

# Question-29

marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance: "))

if marks >= 60 and attendance >= 75:
    print("Eligible")
else:
    print("Not Eligible")


# Question-30

marks = int(input("Enter marks: "))
income = int(input("Enter family income: "))

if marks >= 85 or income < 300000:
    print("Scholarship Available")
else:
    print("No Scholarship")


# Question-31

day = input("Enter day: ")

if day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Weekday")


# Question-32

username = input("Enter username: ")
password = input("Enter password: ")

if username == "student" and password == "python123":
    print("Access Granted")
else:
    print("Access Denied")


# Question-33

city = input("Enter city: ")

if city == "Ahmedabad" or city == "Gandhinagar":
    print("Delivery Available")
else:
    print("Delivery Unavailable")


# Question-34

num = int(input("Enter an integer: "))

if num >= 10 and num <= 50:
    print("Inside Range")
else:
    print("Outside Range")


# Question-35

amount = int(input("Enter transaction amount: "))
otp = input("Enter OTP: ")

if amount <= 50000 and otp == "1234":
    print("Transaction Approved")
else:
    print("Transaction Declined")
#===================================================

# Topic-5: Nested if

# Question-36.

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "admin123":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")


# Question-37. 

age = int(input("Enter age: "))
test_status = input("Enter test status: ")

if age >= 18:
    if test_status == "pass":
        print("License Approved")
    else:
        print("Test Not Passed")
else:
    print("Age Not Eligible")


# Question-38. 

balance = int(input("Enter account balance: "))
amount = int(input("Enter withdrawal amount: "))

if amount <= balance:
    if amount % 100 == 0:
        print("Withdrawal Successful")
    else:
        print("Enter Amount in Multiples of 100")
else:
    print("Insufficient Balance")


# Question-39. 

attendance = int(input("Enter attendance: "))
marks = int(input("Enter marks: "))

if attendance >= 75:
    if marks >= 40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Not Eligible Due to Attendance")


# Question-40. 

account_type = input("Enter account type: ")
balance = int(input("Enter balance: "))

if account_type == "savings":
    if balance >= 1000:
        print("Minimum Balance Maintained")
    else:
        print("Minimum Balance Not Maintained")
else:
    print("Unsupported Account")


# Question-41. 

amount = int(input("Enter order amount: "))
payment = input("Enter payment method: ")

if amount >= 500:
    if payment == "card":
        print("Card Payment Accepted")
    elif payment == "upi":
        print("UPI Payment Accepted")
    else:
        print("Unsupported Payment Method")
else:
    print("Minimum Order Amount Not Reached")


# Question-42. 

year = int(input("Enter year of study: "))
attendance = int(input("Enter attendance: "))

if year >= 2 and year <= 4:
    if attendance >= 75:
        print("Room Eligible")
    else:
        print("Attendance Too Low")
else:
    print("Not Eligible by Year")


# Question-43. 

plan = input("Enter current plan: ")
usage = int(input("Enter monthly usage in GB: "))

if plan == "basic":
    if usage > 100:
        print("Recommend Upgrade")
    else:
        print("Basic Plan Is Sufficient")
else:
    print("Already on Higher Plan")
#=================================================

# Topic-6: Nested if-elif-else

# Question-44. 

a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

if a == b and b == c:
    print("All are Equal")
elif a >= b and a >= c:
    if a == b:
        print("A and B are Equal and Greatest")
    elif a == c:
        print("A and C are Equal and Greatest")
    else:
        print("A is Greatest")
elif b >= a and b >= c:
    if b == c:
        print("B and C are Equal and Greatest")
    else:
        print("B is Greatest")
else:
    print("C is Greatest")


# Question-45.

marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance: "))

if attendance >= 75:
    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 60:
        print("Grade C")
    elif marks >= 40:
        print("Grade D")
    else:
        print("Grade F")
else:
    print("Not Eligible")


# Question-46. 

salary = int(input("Enter salary: "))
rating = int(input("Enter performance rating: "))

if salary >= 30000:
    if rating == 5:
        print("Bonus: 20%")
    elif rating == 4:
        print("Bonus: 15%")
    elif rating == 3:
        print("Bonus: 10%")
    else:
        print("Bonus: 5%")
else:
    print("Not Eligible for Bonus")


# Question-47. 

age = int(input("Enter age: "))
distance = int(input("Enter distance: "))

if age < 5:
    print("Free")
elif age >= 60:
    print("Senior")
else:
    if distance <= 10:
        print("Regular - Short Distance")
    else:
        print("Regular - Long Distance")


# Question-48. 

stock = int(input("Enter stock: "))
payment = input("Enter payment status: ")

if stock > 0:
    if payment == "paid":
        print("Order Confirmed")
    elif payment == "pending":
        print("Payment Pending")
    else:
        print("Invalid Payment Status")
else:
    print("Out of Stock")


# Question-49.

age = int(input("Enter age: "))
ticket = input("Enter ticket type: ")

if age < 5:
    print("Free Travel")
elif age >= 60:
    print("Senior Passenger")
else:
    if ticket == "AC":
        print("AC Ticket")
    elif ticket == "Sleeper":
        print("Sleeper Ticket")
    else:
        print("Invalid Ticket Type")
#=========================================

# Topic-7 — match-case


# Question-50
choice = int(input("Enter menu number: "))

match choice:
    case 1:
        print("Add")
    case 2:
        print("View")
    case 3:
        print("Update")
    case 4:
        print("Delete")
    case _:
        print("Invalid Choice")


# Question-51
day = int(input("Enter day number: "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid Day")


# Question-52
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter operator: ")

match operator:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        if b != 0:
            print(a / b)
        else:
            print("Cannot divide by zero")
    case _:
        print("Invalid Operator")


# Question-53
color = input("Enter signal color: ").lower()

match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")
    case _:
        print("Invalid Signal")


# Question-54
grade = input("Enter grade: ").upper()

match grade:
    case "A":
        print("Excellent Performance")
    case "B":
        print("Very Good Performance")
    case "C":
        print("Good Performance")
    case "D":
        print("Needs Improvement")
    case "F":
        print("Failed")
    case _:
        print("Invalid Grade")


# Question-55
service = int(input("Enter service code: "))

match service:
    case 1:
        print("Check Balance")
    case 2:
        print("Recharge")
    case 3:
        print("Data Usage")
    case 4:
        print("Customer Support")
    case _:
        print("Invalid Service")


# Question-56
month = int(input("Enter month number: "))

match month:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    case _:
        print("Invalid Month")


# Question-57
extension = input("Enter file extension: ").lower()

match extension:
    case "py":
        print("Python File")
    case "txt":
        print("Text File")
    case "pdf":
        print("PDF File")
    case "jpg":
        print("Image File")
    case _:
        print("Unknown File Type")
#====================================================

# Topic-8 — Conditional Statements + Previous Concepts

# Question-58
student_id = input("Enter Student ID: ")
parts = student_id.split("-")

degree = parts[0]
batch = parts[1]
branch = parts[2]
roll_number = parts[3]

if branch == "CSE":
    print("CSE Student")
else:
    print("Non-CSE Student")


# Question-59
email = input("Enter email: ")
parts = email.split("@")
domain = parts[1]

if domain == "gmail.com":
    print("Gmail User")
else:
    print("Other Email Provider")


# Question-60
name = input("Enter full name: ")
parts = name.split()

username = parts[0].lower() + "." + parts[2].lower()

if "." in username:
    print("Valid Username Format")
else:
    print("Invalid Username Format")


# Question-61
num = int(input("Enter a positive integer: "))

if num < 10:
    print("One Digit")
elif num < 100:
    print("Two Digits")
elif num < 1000:
    print("Three Digits")
else:
    print("Four or More Digits")


# Question-62
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

subtotal = price * quantity

if subtotal >= 5000:
    discount_percent = 20
elif subtotal >= 2000:
    discount_percent = 10
else:
    discount_percent = 0

discount = subtotal * discount_percent / 100
final_amount = subtotal - discount

print("Subtotal:", subtotal)
print("Discount:", str(discount_percent) + "%")
print("Final: {:.2f}".format(final_amount))


# Question-63
units = int(input("Enter units consumed: "))

if units <= 100:
    rate = 5
elif units <= 300:
    rate = 7
else:
    rate = 10

bill = units * rate

print("Units:", units)
print("Rate: ₹" + str(rate))
print("Bill: ₹" + str(bill))


# Question-64
balance = 10000

print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Balance:", balance)

    case 2:
        amount = int(input("Enter deposit amount: "))
        balance += amount
        print("Deposit Successful, Balance:", balance)

    case 3:
        amount = int(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print("Withdrawal Successful, Balance:", balance)
        else:
            print("Insufficient Balance")

    case 4:
        print("Exit")

    case _:
        print("Invalid Choice")


# Question-65
print("1. Pizza - ₹250")
print("2. Burger - ₹150")
print("3. Pasta - ₹200")
print("4. Sandwich - ₹120")

choice = int(input("Enter food choice: "))
quantity = int(input("Enter quantity: "))

match choice:
    case 1:
        item_price = 250
    case 2:
        item_price = 150
    case 3:
        item_price = 200
    case 4:
        item_price = 120
    case _:
        item_price = 0
        print("Invalid Choice")

if item_price > 0:
    total = item_price * quantity

    if total >= 500:
        discount = total * 0.10
    else:
        discount = 0

    final_amount = total - discount

    print("Total:", total)
    print("Discount: {:.2f}".format(discount))
    print("Final: {:.2f}".format(final_amount))


# Question-66
m1 = int(input("Enter marks for subject 1: "))
m2 = int(input("Enter marks for subject 2: "))
m3 = int(input("Enter marks for subject 3: "))
attendance = int(input("Enter attendance percentage: "))

total = m1 + m2 + m3
average = total / 3

if attendance >= 75:
    if average >= 90:
        print("Outstanding")
    elif average >= 75:
        print("Very Good")
    elif average >= 60:
        print("Good")
    elif average >= 40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Not Eligible")


# Question-67
distance = float(input("Enter distance in km: "))
ride_type = input("Enter ride type: ").lower()

match ride_type:
    case "normal":
        rate = 15
    case "premium":
        rate = 25
    case _:
        rate = 0
        print("Invalid Ride Type")

if rate > 0:
    fare = distance * rate

    if distance > 20:
        fare = fare + fare * 0.10

    print("Fare: {:.2f}".format(fare))


# Question-68
score = int(input("Enter entrance score: "))
percentage = float(input("Enter 12th percentage: "))
category = input("Enter category: ").lower()

match category:
    case "general":
        if score >= 80:
            if percentage >= 75:
                print("Admission Eligible")
            else:
                print("Admission Not Eligible")
        else:
            print("Admission Not Eligible")

    case "obc":
        if score >= 70:
            if percentage >= 70:
                print("Admission Eligible")
            else:
                print("Admission Not Eligible")
        else:
            print("Admission Not Eligible")

    case "sc":
        if score >= 60:
            if percentage >= 60:
                print("Admission Eligible")
            else:
                print("Admission Not Eligible")
        else:
            print("Admission Not Eligible")

    case _:
        print("Admission Not Eligible")
#================================================

# Topic-9 — Debugging Conditional Programs

# Question-69
age = int(input("Enter age: "))

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")


# Question-70
marks = int(input("Enter marks: "))

if marks >= 40:
    if marks >= 90:
        print("A")
    elif marks >= 75:
        print("B")
    else:
        print("Pass")
else:
    print("Fail")
#=================================================

# Topic-10 - Output Prediction & Execution

# Question-71
marks = 85

if marks >= 40:
    print("Pass")
elif marks >= 75:
    print("Very Good")
else:
    print("Fail")

# Output: Pass



# Question-72
marks = int(input("Enter marks: "))

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")

# Outputs:
# 95 -> A
# 85 -> B
# 50 -> Pass
# 30 -> Fail



# Question-73
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry Allowed")
    else:
        print("ID Required")
else:
    print("Underage")

# Output: Entry Allowed

# If age = 20 and has_id = False:
# Output: ID Required

# If age = 16 and has_id = True:
# Output: Underage


# Question-74
choice = 5

match choice:
    case 1:
        print("Add")
    case 2:
        print("View")
    case 3:
        print("Delete")
    case _:
        print("Invalid Choice")

# Outputs:
# 1 -> Add
# 3 -> Delete
# 5 -> Invalid Choice



# Question-75
marks = 82
attendance = 80

if attendance >= 75:
    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Not Eligible")

# Outputs:
# 82 80 -> Grade B
# 92 80 -> Grade A
# 55 80 -> Pass
# 92 60 -> Not Eligible
