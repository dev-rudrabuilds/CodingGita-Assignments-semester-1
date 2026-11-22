# Level 1 — Loop Thinking & range()

# Question-1
for i in range(2, 15, 3):
    print(i)


# Question-2
for i in range(15, 2, -3):
    print(i)


# Question-3
count = 0
for i in range(4, 31, 5):
    print(i)
    count += 1
print("Iterations:", count)


# Question-4
for i in range(3, 19, 3):
    print(i)


# Question-5
for i in range(5, 11):
    print(i, 20 - i)


# Question-6
for i in range(1, 7):
    print(i, i ** 2, i ** 3)
#=================================

# Level 2 — Counting & Accumulation

# Question-7
start = int(input("Enter start: "))
end = int(input("Enter end: "))
total = 0

for i in range(start, end + 1):
    total += i

print(total)


# Question-8
n = int(input("Enter N: "))
count = 0

for i in range(1, n + 1):
    if i % 3 == 0:
        count += 1

print(count)


# Question-9
n = int(input("Enter N: "))
total = 0

for i in range(1, n + 1):
    if i % 4 == 0:
        total += i

print(total)


# Question-10
n = int(input("Enter N: "))
count = 0

for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        count += 1

print(count)


# Question-11
n = int(input("Enter N: "))
total = 0

for i in range(1, n + 1):
    if i % 3 != 0:
        total += i

print(total)


# Question-12
n = int(input("Enter N: "))
even = 0
odd = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even =", even, "Odd =", odd)


# Question-13
n = int(input("Enter N: "))
total = 0

for i in range(1, n + 1):
    total += i
    print(total)


# Question-14
n = int(input("Enter N: "))
product = 1

for i in range(1, n + 1):
    product *= i
    print(product)
#================================

# Level 3 — Factorial & Product Logic

# Question-15
n = int(input("Enter N: "))
fact = 1

for i in range(1, n + 1):
    fact *= i

print(fact)


# Question-16
n = int(input("Enter N: "))
fact = 1

for i in range(1, n + 1):
    fact *= i
    print(i, "! =", fact)


# Question-17
n = int(input("Enter N: "))
product = 1

for i in range(2, n + 1, 2):
    product *= i

print(product)


# Question-18
n = int(input("Enter N: "))
product = 1

for i in range(1, n + 1, 2):
    product *= i

print(product)


# Question-19
n = int(input("Enter an even number: "))
product = 1

for i in range(n, 0, -2):
    product *= i

print(product)


# Question-20
n = int(input("Enter N: "))
total = 0

for i in range(1, n + 1):
    total += i ** 2

print(total)


# Question-21
n = int(input("Enter N: "))
total = 0

for i in range(1, n + 1):
    total += i ** 3

print(total)


# Question-22
n = int(input("Enter N: "))
fact = 1
total = 0

for i in range(1, n + 1):
    fact *= i
    total += fact

print(total)
#================================

# Level 4 — Number & Digit Logic

# Question-23
n = int(input("Enter a positive integer: "))
count = 0

for i in range(1, n + 1):
    if n == 0:
        count = 1
        break
    count += 1
    n //= 10

print(count)


# Question-24
n = abs(int(input("Enter a number: ")))
total = 0

for i in range(len(str(n))):
    total += n % 10
    n //= 10

print(total)


# Question-25
n = abs(int(input("Enter a number: ")))
product = 1

for i in range(len(str(n))):
    product *= n % 10
    n //= 10

print(product)


# Question-26
n = abs(int(input("Enter a number: ")))
count = 0

for i in range(len(str(n))):
    digit = n % 10
    if digit % 2 == 0:
        count += 1
    n //= 10

print(count)


# Question-27
n = abs(int(input("Enter a number: ")))
total = 0

for i in range(len(str(n))):
    digit = n % 10
    if digit % 2 == 0:
        total += digit
    n //= 10

print(total)


# Question-28
n = int(input("Enter a number: "))
n = abs(n)
largest = 0

for i in range(len(str(n))):
    digit = n % 10
    if digit > largest:
        largest = digit
    n //= 10

print(largest)


# Question-29
n = abs(int(input("Enter a number: ")))
smallest = 9

for i in range(len(str(n))):
    digit = n % 10
    if digit < smallest:
        smallest = digit
    n //= 10

print(smallest)


# Question-30
n = int(input("Enter a positive integer: "))
reverse = 0

for i in range(len(str(n))):
    reverse = reverse * 10 + n % 10
    n //= 10

print(reverse)


# Question-31
n = int(input("Enter a number: "))
original = n
reverse = 0

for i in range(len(str(n))):
    reverse = reverse * 10 + n % 10
    n //= 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")


# Question-32
n = abs(int(input("Enter a number: ")))
target = int(input("Enter target digit: "))
count = 0

for i in range(len(str(n))):
    if n % 10 == target:
        count += 1
    n //= 10

print(count)


# Question-33
n = int(input("Enter a positive integer: "))

for i in range(len(str(n))):
    if n < 10:
        break
    n //= 10

print(n)


# Question-34
n = abs(int(input("Enter a number: ")))
largest = 0
smallest = 9

for i in range(len(str(n))):
    digit = n % 10
    if digit > largest:
        largest = digit
    if digit < smallest:
        smallest = digit
    n //= 10

print(largest - smallest)


# Question-35
n = int(input("Enter a positive integer: "))
position = 1

for i in range(len(str(n))):
    print(n % 10, position)
    n //= 10
    position += 1


# Question-36
n = int(input("Enter a three-digit number: "))
original = n
total = 0

for i in range(3):
    digit = n % 10
    total += digit ** 3
    n //= 10

if total == original:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
#=================================

# Level 5 — String & Character Logic

# Question-37
text = input("Enter a string: ")

for i in range(len(text)):
    print(i, text[i])


# Question-38
text = input("Enter a string: ")
count = 0

for ch in text:
    count += 1

print(count)


# Question-39
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for ch in text:
    if ch.isalpha():
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels =", vowel_count, "Consonants =", consonant_count)


# Question-40
text = input("Enter a string: ")
target = input("Enter target character: ")
count = 0

for ch in text:
    if ch == target:
        count += 1

print(count)


# Question-41
text = input("Enter a string: ")
target = input("Enter target character: ")
position = -1

for i in range(len(text)):
    if text[i] == target and position == -1:
        position = i

if position == -1:
    print("Not Found")
else:
    print(position)


# Question-42
text = input("Enter a string: ")
upper = 0
lower = 0

for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase =", upper, "Lowercase =", lower)


# Question-43
text = input("Enter a string: ")

for ch in text:
    print(ch, ord(ch))


# Question-44
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
result = ""

for ch in text:
    if ch not in vowels:
        result += ch

print(result)
#=====================================

# Level 6 — Midpoint, Half & String Logic

# Question-45
text = input("Enter an odd-length string: ")
middle = len(text) // 2
print(text[middle])


# Question-46
text = input("Enter an even-length string: ")
middle = len(text) // 2

print("First Half:", text[:middle])
print("Second Half:", text[middle:])


# Question-47
text = input("Enter a string: ")
length = len(text)
first = ""
second = ""
middle = ""

for i in range(length):
    if i < length // 2:
        first += text[i]
    elif length % 2 == 1 and i == length // 2:
        middle = text[i]
    else:
        second += text[i]

print("First Half:", first)
if length % 2 == 1:
    print("Middle:", middle)
print("Second Half:", second)


# Question-48
text = input("Enter an even-length string: ")
length = len(text)
equal = True

for i in range(length // 2):
    if text[i] != text[i + length // 2]:
        equal = False

if equal:
    print("Equal Halves")
else:
    print("Different Halves")


# Question-49
text = input("Enter a string: ")
symmetric = True

for i in range(len(text) // 2):
    if text[i] != text[len(text) - 1 - i]:
        symmetric = False

if symmetric:
    print("Symmetric")
else:
    print("Not Symmetric")


# Question-50
text = input("Enter a string: ")

for i in range(len(text)):
    if i % 2 == 0:
        print(text[i], end="")


# Question-51
text = input("Enter a string: ")
even = 0
odd = 0

for i in range(len(text)):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even Index =", even, "Odd Index =", odd)


# Question-52
text = input("Enter an even-length string: ")
result = ""

for i in range(0, len(text), 2):
    result += text[i + 1] + text[i]

print(result)
#====================================================

# Level 7 — Tricky Single-Loop Problems

# Question-53
n = abs(int(input("Enter a number: ")))
largest = -1
second = -1

for i in range(n):
    if n == 0:
        break
    digit = n % 10

    if digit > largest:
        second = largest
        largest = digit
    elif digit < largest and digit > second:
        second = digit

    n //= 10

if second == -1:
    print("No second largest distinct digit")
else:
    print(second)


# Question-54
text = input("Enter a string: ")

current = 0
best = 0
previous = ""

for ch in text:
    if ch == previous:
        current += 1
    else:
        current = 1
        previous = ch

    if current > best:
        best = current

print(best)


# Question-55
text = input("Enter a string: ")
target = input("Enter target character: ")
count = 0
length = 0

for ch in text:
    length += 1
    if ch == target:
        count += 1

if length > 0:
    frequency = count / length * 100
else:
    frequency = 0

print("Count =", count)
print("Frequency = {:.2f}%".format(frequency))


# Question-56
n = int(input("Enter a positive integer: "))
total = 0

for i in range(n):
    if n == 0:
        break
    total += n % 10
    print(total)
    n //= 10


# Question-57
n = int(input("Enter a positive integer: "))
even = 0
odd = 0

for i in range(n):
    if n == 0:
        break

    digit = n % 10

    if digit % 2 == 0:
        even += 1
    else:
        odd += 1

    n //= 10

if even > odd:
    print("More Even Digits")
elif odd > even:
    print("More Odd Digits")
else:
    print("Equal")


# Question-58
n = int(input("Enter a positive integer: "))
total = 0
sign = 1

for i in range(n):
    if n == 0:
        break

    digit = n % 10
    total += digit * sign
    sign *= -1
    n //= 10

print(total)


# Question-59
total = 0

for i in range(1, 6):
    total = total + i * 2
    print(total)


# Question-60
count = 0

for i in range(1, 11):
    if i % 2 == 0:
        count += 1

print(count)


# Question-61
total = 0

for i in range(1, 6):
    total += i

print(total)


# Question-62
n = int(input("Enter number of days: "))
total = 0
highest = None
lowest = None

for i in range(n):
    expense = float(input("Enter expense: "))
    total += expense

    if highest is None or expense > highest:
        highest = expense
    if lowest is None or expense < lowest:
        lowest = expense

print("Total:", total)
print("Highest:", highest)
print("Lowest:", lowest)


# Question-63
n = int(input("Enter number of subjects: "))
total = 0
highest = None
lowest = None

for i in range(n):
    marks = float(input("Enter marks: "))
    total += marks

    if highest is None or marks > highest:
        highest = marks
    if lowest is None or marks < lowest:
        lowest = marks

if n > 0:
    print("Total:", total)
    print("Average:", total / n)
    print("Highest:", highest)
    print("Lowest:", lowest)


# Question-64
n = int(input("Enter working days: "))
present = 0
absent = 0

for i in range(n):
    status = input("Enter P or A: ").upper()

    if status == "P":
        present += 1
    elif status == "A":
        absent += 1

if n > 0:
    attendance = present / n * 100
else:
    attendance = 0

print("Present:", present)
print("Absent:", absent)
print("Attendance: {:.2f}%".format(attendance))


# Question-65
n = int(input("Enter number of days: "))
total = 0
days_above = 0

for i in range(n):
    units = int(input("Enter units: "))
    total += units

    if units > 10:
        days_above += 1

print("Total Units:", total)
print("Days Above 10:", days_above)


# Question-66
n = int(input("Enter number of products: "))
total = 0
count = 0

for i in range(n):
    price = float(input("Enter price: "))
    total += price

    if price > 1000:
        count += 1

print("Total Bill:", total)
print("Products Above 1000:", count)


# Question-67
n = int(input("Enter number of attempts: "))
successful = 0
failed = 0

for i in range(n):
    status = input("Enter success or failed: ").lower()

    if status == "success":
        successful += 1
    elif status == "failed":
        failed += 1

if n > 0:
    rate = successful / n * 100
else:
    rate = 0

print("Successful:", successful)
print("Failed:", failed)
print("Success Rate:", rate, "%")
#========================================

# Level 8 — Real-Life Single-Loop Problems

# Question-62
n = int(input("Enter number of days: "))
total = 0
highest = None
lowest = None

for i in range(n):
    expense = float(input("Enter expense: "))
    total += expense

    if highest is None or expense > highest:
        highest = expense
    if lowest is None or expense < lowest:
        lowest = expense

print("Total:", total)
print("Highest:", highest)
print("Lowest:", lowest)


# Question-63
n = int(input("Enter number of subjects: "))
total = 0
highest = None
lowest = None

for i in range(n):
    marks = float(input("Enter marks: "))
    total += marks

    if highest is None or marks > highest:
        highest = marks
    if lowest is None or marks < lowest:
        lowest = marks

if n > 0:
    print("Total:", total)
    print("Average:", total / n)
    print("Highest:", highest)
    print("Lowest:", lowest)


# Question-64
n = int(input("Enter working days: "))
present = 0
absent = 0

for i in range(n):
    status = input("Enter P or A: ").upper()

    if status == "P":
        present += 1
    elif status == "A":
        absent += 1

attendance = present / n * 100 if n > 0 else 0

print("Present:", present)
print("Absent:", absent)
print("Attendance: {:.2f}%".format(attendance))


# Question-65
n = int(input("Enter number of days: "))
total = 0
days_above = 0

for i in range(n):
    units = int(input("Enter units: "))
    total += units

    if units > 10:
        days_above += 1

print("Total Units:", total)
print("Days Above 10:", days_above)


# Question-66
n = int(input("Enter number of products: "))
total = 0
count = 0

for i in range(n):
    price = float(input("Enter price: "))
    total += price

    if price > 1000:
        count += 1

print("Total Bill:", total)
print("Products Above 1000:", count)


# Question-67
n = int(input("Enter number of attempts: "))
successful = 0
failed = 0

for i in range(n):
    status = input("Enter success or failed: ").lower()

    if status == "success":
        successful += 1
    elif status == "failed":
        failed += 1

rate = successful / n * 100 if n > 0 else 0

print("Successful:", successful)
print("Failed:", failed)
print("Success Rate: {:.1f}%".format(rate))
#=============================================

# Level 9 — Final Challenges

# Question-68
n = int(input("Enter a positive integer: "))
digits = 0
total = 0
largest = 0
smallest = 9
even = 0
odd = 0

for i in range(n):
    if n == 0:
        break

    digit = n % 10
    digits += 1
    total += digit

    if digit > largest:
        largest = digit
    if digit < smallest:
        smallest = digit

    if digit % 2 == 0:
        even += 1
    else:
        odd += 1

    n //= 10

print("Digits:", digits)
print("Sum:", total)
print("Largest:", largest)
print("Smallest:", smallest)
print("Even Digits:", even)
print("Odd Digits:", odd)


# Question-69
text = input("Enter a string: ")
vowels = "aeiouAEIOU"

total = 0
vowel_count = 0
consonants = 0
uppercase = 0
lowercase = 0
even_index = 0

for i in range(len(text)):
    ch = text[i]
    total += 1

    if i % 2 == 0:
        even_index += 1

    if ch.isalpha():
        if ch in vowels:
            vowel_count += 1
        else:
            consonants += 1

        if ch.isupper():
            uppercase += 1
        elif ch.islower():
            lowercase += 1

print("Total Characters:", total)
print("Vowels:", vowel_count)
print("Consonants:", consonants)
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Even Index Characters:", even_index)