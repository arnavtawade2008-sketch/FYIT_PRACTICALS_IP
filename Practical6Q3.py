# Pract6-Q3
# Creating a Matrix
rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))

matrix = []

# Matrix Elements
print("Enter matrix elements: ")
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    matrix.append(row)

# Sum of rows
print("\nRow Sums")
for row in matrix:
    print(sum(row))

# Sum of columns
print("\nColumn Sums")
for j in range(cols):
    total = 0
    for i in range(rows):
        total += matrix[i][j]
    print(total)
