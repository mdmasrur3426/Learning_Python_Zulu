myNumber = 123
myString = '456'
myList = [7, 8, 9]
myTuple = (10, 11)
myTupleDict = ('name', 'rumman')
myDictionary = {'name': 'noah', 'age': '5', 'activity': 'fart'}

print("*******Integer*********")
print("My number is:", myNumber)
print('\n')

print("*******String*********")
print("My string is:", myString)
print('\n')

print("*******List*********")
print("My list is:", myList)
print('\n')

print("*******Tuple*********")
print("My tuple is:", myTuple)
print('\n')

print("*******Dictionary*********")
print("My dictionary is:", myDictionary)
print('\n')

print("*******String-->Integer*********")
intCon = int(myString)
print(intCon)
print("Type is:", type(intCon))
print('\n')

print("*******String-->Tuple*********")
tupCon = tuple(myString)
print(tupCon)
print("Type is:", type(tupCon))
print('\n')

print("*******Tuple-->Dictionary*********")
dicCon = dict(myTupleDict)
print(dicCon)
print("Type is:", type(dicCon))
print('\n')

print("*******Integer-->String*********")
strCon = str(myNumber)
print(strCon)
print("Type is:", type(strCon))
print('\n')


