print("Let's check the strength of your password!")
while True:
    password = input("Enter password: ")
    score = 0

    #pass length 
    if len(password) < 16:
        print("Make it at least 16 characters.")
    else:
        score += 1

    #has upper 
    if any(char.isupper() for char in password):
        score += 1
    else:
        print("Add an uppercase letter.")

    #has lower
    if any(char.islower() for char in password):
        score += 1
    else:
        print("Add a lowercase letter.")

    #has digit
    if any(char.isdigit() for char in password):
        score += 1
    else:
        print("Add a number.")

    #has symbol 
    if any(not char.isalnum() for char in password):
        score += 1
    else:
        print("Add a symbol.")

    # final rating
    if score <= 2:
        print("Weak password")
    elif score == 3 or score == 4:
        print("Medium strength password")
    else:
        print("Strong password!")

    again = input("Check another password? (y/n): ")
    if again.lower() != "y":
        break
