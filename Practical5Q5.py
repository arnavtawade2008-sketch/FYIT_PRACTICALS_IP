#Q5
# Input a number
n = int(input("Enter a number: "))

# Find the first number divisible by n
for i in range(2, 101):
    if n % i == 0:
        print("First number divisible by", n, "is", i)
        break
