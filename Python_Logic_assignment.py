# Scott Johnson
# October 17, 2026
# Python Logic assignment

# 1. Basic Selection Structure
# age = int(input("Enter your age: "))
# if age >= 18:
#   print("You are eligible to vote.")
# else:
#    print("You are not eligible to vote.")

# My example - gas left in car
car = int(input("enter gallons left in tank: "))
if car == 0:
    print ("how is the car driving")
elif car < 3:
    print ("Find nearest gas station")
else:
    print ("you have enough gas")

print()
# 2. Relational operators
#  print("2. Relational Operators")
#  num1 = float(input("Enter the first number: "))
#  num2 = float(input("Enter the second number: "))
#  print(f"{num1} == {num2}: {num1 == num2}")
#  print(f"{num1} != {num2}: {num1 != num2}")
#  print(f"{num1} < {num2}: {num1 < num2}")
#  print(f"{num1} > {num2}: {num1 > num2}")
#  print(f"{num1} <= {num2}: {num1 <= num2}")
#  print(f"{num1} >= {num2}: {num1 >= num2}")

# My example - does the pc have enough ram
ram = int(input("How much RAM does the PC have (GB)? "))
needed = int(input("How much RAM does the program need (GB)? "))
print("ram == needed:", ram == needed)
print("ram != needed:", ram != needed)
print("ram < needed:", ram < needed)
print("ram > needed:", ram > needed)
print("ram <= needed:", ram <= needed)
print("ram >= needed:", ram >= needed)
if ram >= needed:
    print("PC has enough RAM")
else:
    print("PC needs more RAM")

print()
# 3. AND logic - both have to be true
# print("3. AND Logic")
# score = float(input("Enter your test score: "))
# attendance = float(input("Enter your attendance percentage: "))
# if score >= 70 and attendance >= 80:
#    print("You pass the course.")
# else:
#    print("You do not pass the course.")

# my example - is the device compliant
bitlocker = input("Is BitLocker on? (yes/no): ").lower()
days = int(input("Days since last Windows update: "))
if bitlocker == "yes" and days <= 30:
    print("Device is compliant")
else:
    print("Device is NOT compliant")

print()
# 4. OR logic - only one has to be true
# print("4. OR Logic")
# has_student_id = input("Do you have a student ID? (yes/no): ").lower()
# has_library_card = input("Do you have a library card? (yes/no): ").lower()
# if has_student_id == "yes" or has_library_card == "yes":
#     print("You may enter the library.")
# else:
#    print("Access denied. You need a student ID or library card.")

# my example - escalate a ticket
priority = input("Ticket priority (low/medium/high): ").lower()
users = int(input("How many users are affected? "))
if priority == "high" or users >= 10:
    print("Escalate to Tier 2")
else:
    print("Tier 1 can handle it")

print()
# 5. NOT logic
# print("5. NOT Logic")
# is_banned = input("Are you banned from the system? (yes/no): ").lower()
# if not is_banned == "yes":
#    print("You may access the system.")
# else:
#    print("Access denied due to ban.")

# my example - locked out account
locked = input("Is the account locked out? (yes/no): ").lower()
if not locked == "yes":
    print("User can sign in")
else:
    print("Account is locked, unlock it first")

print()
# 6. AND/OR with precedence
# print("6. AND/OR with Precedence")
# gpa = float(input("Enter your GPA: "))
# volunteer_hours = int(input("Enter your volunteer hours: "))
# leadership = input("Do you hold a leadership role? (yes/no): ").lower()
# if gpa >= 3.5 and (volunteer_hours >= 50 or leadership == "yes"):
#     print("You qualify for the scholarship.")
# else:
#    print("You do not qualify for the scholarship.")

# my example - vpn access
# and goes before or, so the parentheses make the or part run first
active = input("Is the account active? (yes/no): ").lower()
laptop = input("Company laptop? (yes/no): ").lower()
mfa = input("Signed in with MFA? (yes/no): ").lower()
if active == "yes" and (laptop == "yes" or mfa == "yes"):
    print("VPN access granted")
else:
    print("VPN access denied")

