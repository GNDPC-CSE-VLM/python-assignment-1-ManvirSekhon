# Assignment 1 – Section B
# Write your answers below each question

# Q11: Swap variables
# Your code here


a = 10
b = 20

print("Before swapping:")
print("a =", a, "b =", b)

temp = a
a = b
b = temp

print("\nAfter swapping with temporary variable:")
print("a =", a, "b =", b)



# Q12: Number pattern
# Your code here


for i in range(6):
    for j in range(6):
        print(6, end=" ")
    print()




# Q13: Factorial OR Password System
# Your code here


# A
# Factorial using a loop

num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial of", num, "is", fact)



# B
# Password system with 3 attempts

correct_password = "admin123"
attempts = 3

for i in range(attempts):
    password = input("Enter password: ")
    if password == correct_password:
        print("Access Granted")
        break
    else:
        print("Incorrect password.")
else:
    print("Access Denied")
