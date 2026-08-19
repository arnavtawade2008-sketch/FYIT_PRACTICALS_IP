# Set the correct password
correct_password = "python123"

# Allow 3 attempts
for i in range(1, 4):
    password = input("Enter password: ")

    if password == correct_password:
        print("Login Successful!")
        break
    else:
        print("Incorrect password.")

# If all attempts are used
else:
    print("Login Failed! You have used all 3 attempts.")
