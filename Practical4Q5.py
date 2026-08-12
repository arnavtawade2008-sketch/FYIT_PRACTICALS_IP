# Input a number
num = int(input("Enter a number: "))

# Print multiplication table
print("\nMultiplication Table of", num)
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
