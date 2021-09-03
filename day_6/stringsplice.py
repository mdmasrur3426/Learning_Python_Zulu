### Multi Line String

multiString = "Hi! I am Rumman. \n" \
              "Favourite food: Beef Chap. \n" \
              "Favourite Series: Community"

print(multiString)

### Length of String

print(len(multiString))

### Check of a string have a word

myString = input("Write a string:")
myWord = (input("Write a word to check in string:")).lower()

if myWord in myString:
    print(myWord, "is in the string.")
else:
    print(myWord, "is not in the string.")

### Subsring

print(myString[1:6])
print(myString[0:9:2])

### Upper case and lowercase

print(myString.upper())
print(myString.lower())

### Replace substring with another substring

myCountry = "Bangladesh"
print(myCountry.replace("Bangla", "Canada"))


### Split
x = myString.split()
print(x)

###OUTPUT
# myString = "This is big split"
# ['This', 'is', 'big', 'split']

### Sting Concatenation

stringOne = "Noah loves "
stringTwo = "drill videos"
z = stringOne + stringTwo

print(z)





