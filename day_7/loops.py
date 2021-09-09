# input will be number between 1-10 and string will be name
# It will print the string n times. Here n is the number from input
# Check if the string and number is valid
while True:

    myNumber = int(input("Enter a number between 1 & 10:"))

    if myNumber > 10:
        print("Invalid Entry, please try again.")
        continue
    elif myNumber < 1:
        print("Invalid Entry, please try again.")
        continue
    else:
        myString = input("Enter your name:")
        if len(myString) <= 1:
            print("Enter a valid name.")
            continue
        else:
            for n in range(0, myNumber):
                print(myString)

        break
