PASSWORD_LENGTH = 10

password = input("Enter Password: ")

while len(password) < PASSWORD_LENGTH:
    print("Password doesn't meet the minimum length")
    password = input("Enter Password: ")

for i in range(len(password)):
    print("*", end=" ")