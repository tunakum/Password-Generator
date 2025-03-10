import random
import string
while True:
    print("Welcome to Password Generator")
    try:
        passLength = int(input("Please enter the length of your password (minimum 8, maximum 128):"))
        
        if passLength < 0:
            print("Only positive numbers between 8-128 !!!!")
            continue
        
        if passLength < 8:
            print("Too short, minimum 8 characters!!!")
            continue
        elif passLength > 128:
            print("Too long, maximum 128 characters!!!")
            continue
    except ValueError:
        print("Please only enter a number!!!")
        continue
        
    upperLetters = string.ascii_uppercase
    lowerLetters = string.ascii_lowercase
    digits = string.digits
    specialCharacters = string.punctuation
    
    password = [random.choice(upperLetters), random.choice(lowerLetters), random.choice(digits), random.choice(specialCharacters)]

    allCombined = upperLetters + lowerLetters + digits + specialCharacters

    password += random.choices(allCombined,k= passLength - 4)

    random.shuffle(password)
    password = "".join(password)

    print(f"Your generated password is: {password}")
    break