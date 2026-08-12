# For loop
# Input a number
num = int(input("Enter a number: "))
factorial = 1
# calculate factorial
for i in range(1, num + 1):
    factorial = factorial * i
    print("Factorial = ", factorial)

i = 1
# Calculate factorial the same with while
while i <= num:
    factorial = factorial * 1
    i = i + 1
print("Factorial =", factorial)
