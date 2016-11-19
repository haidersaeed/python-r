# basic structure


# print function
print('Hello' + 'World')
print('Hello', 'World', 'Again')


# variable and type casting
x = int('5') + float('5.5')
print('Result', x)

y,z = (5,10)
print('var y and z are:', y,z)


# while loop
x = 0
while x < 5:
    print(x)
    x += 1


# for loop
myList = [4,5,6,7,3,7,4,20]
print('List loop')
for x in myList:
    print(x)


# for loop for range
print('Range loop')
for x in range(1,11):
    print(x)


# conditional statements
x,y,z = (3,4,5)
if x > y:
    print(x,'is greater than',y)
elif y > z:
    print(y,'is greater than',z)
else:
    print(z,'is greater than',x,'and', y)


# function and global variable
x = 5
def increament_by_five():
    global x
    x+=5
    return x

xVal = increament_by_five()
print('Incremented x value is:',xVal)
print('New x value is incremented:',x)


# function parameters
def add_numbers(x, y):
    return x+y

xResult = add_numbers(5,10)
print('5 + 10 is:', xResult)


'''
    File IO
    For writing in file 'w'
    FOr appending / editing in file 'a'
    FOr reading file 'r'
'''

# writing to file
fileName = 'file1.txt'
textContent = 'This is a sample data in line one.'
textContent += '\nThis is a sample data in line two.'
textContent += '\nThis is a sample data in line three.'

fileHandler = open(fileName, 'w')
fileHandler.write(textContent)
fileHandler.close()

# editing the file
newTextContent = '\n'
newTextContent += '\nThis is a sample data in line four.'
newTextContent += '\nThis is a sample data in line five.'

fileHandler = open(fileName, 'a')
fileHandler.write(newTextContent)
fileHandler.close()

# reading file by lines
fileContent = open(fileName, 'r').readlines()
print('File Content')

for line in fileContent:
    print(line, end='')


'''
    Creating a basic class
'''

class calculator:

    def add(x,y):
        return x+y

    def subtract(x, y):
        return x - y

# Using the above class
result = calculator.add(5,10)
print('Class add method result:',result)

result = calculator.subtract(5,10)
print('Class subtract method result:',result)


# User input
# x = input('Please enter your name: ')
#print('Hello', x)


# tuples
x = (2,3,4)
print('Value in index 1 is:',x[1])


# lists
myList = [2,3,7,11,7,20]
print('Original list:', myList)

myList.append(25)
print('25 added at the end of myList:', myList)

myList.insert(2,30)
print('30 added at 3rd index in myList:', myList)

myList.remove(3)
print('Value 3 removed from myList:', myList)

myListSlice = myList[2:4]
print('Slice myList:', myListSlice)

print('Total number of 7 in myList:', myList.count(7))

myList.sort()
print('myList is sorted now:',myList)


# Dictionaries
userDetails = {'firstname':'Haider', 'lastname':'Saeed', 'email':'email@example.com'}
print(userDetails['firstname'],userDetails['lastname'])