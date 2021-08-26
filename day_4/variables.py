#Using ast for String to Dictionary
import ast
# Assigning all the Datatypes
myInt = 123
myFloat = 123.456
myString = '456'
myList = [7, 8, 9]
myTuple = (10, 11)
myTupleDict = [('name', 'rumman')]
myStrDict = '{"Name" : "Shahed", "Food" : "Pho"}'
myDictionary = {'name': 'noah', 'age': '5', 'activity': 'fart'}

# Printing all the Datatypes
print("*******Integer*********")
print("My number is:", myInt)
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

# Converting String to Integer and printing the datatype of the output
print("*******String-->Integer*********")
str2int = int(myString)
print(str2int)
print("Type is:", type(str2int))
print('\n')

# Converting String to List and printing the datatype of the output
print("*******String-->List*********")
str2lst = list(myString)
print(str2lst)
print("Type is:", type(str2lst))
print('\n')

# Converting String to Tuple and printing the datatype of the output
print("*******String-->Tuple*********")
str2tup = tuple(myString)
print(str2tup)
print("Type is:", type(str2tup))
print('\n')

# Converting String to dictionary and printing the datatype of the output
print("*******String-->Dictionary*********")
str2dict = ast.literal_eval(myStrDict)
print(str2dict)
print("Type is:", type(str2dict))
print('\n')

# Converting Integer to String and printing the datatype of the output
print("*******Integer-->String*********")
int2str = str(myInt)
print(int2str)
print("Type is:", type(int2str))
print('\n')

# Converting Integer to Float and printing the datatype of the output
print("*******Integer-->Float*********")
int2flt = float(myInt)
print(int2flt)
print("Type is:", type(int2flt))
print('\n')

# Converting Integer to List and printing the datatype of the output
print("*******Integer-->List*********")
int2lst = [int(x) for x in str(myInt)]
print(int2lst)
print("Type is:", type(int2lst))
print('\n')

# Converting Tuple to Dictionary and printing the datatype of the output
print("*******Tuple-->Dictionary*********")
tup2dic = dict(myTupleDict)
print(tup2dic)
print("Type is:", type(tup2dic))
print('\n')



