#list in Python: []. Can be a mix of different data types.
#certain data types use indexing, like strings and lists. In Python, it always starts at 0.
# print([3, 'String inside list', 4.5, False])

#string manipulation
# split a string by whitespace
# print('We are working in PyCharm'.split(' '))

# replace the exclamation point with a period
# print('We are working in PyCharm!'.replace('!', '.'))

# find the location of a certain character. Only for 1 instance. If we want more, we need to loop it.
# print('looking for a character'.find('o'))

# strip whitespace (or other characters) from a string
# print('      stripping whitespace   '.strip())
# print('wwwwwmerry christmas'.lstrip('w'))
# print('happy hanukkah??????'.rstrip('?'))

#variables
x = 5
# print(x)

# create a float variable
y = 3.3
# print(y)

z = x + y
# print(z)

# boolean
switch = False

# list as a variable
sports = ['Baseball', 'Football', 'Basketball', 'Hockey']
# print(sports)
# print(sports[0])
# print(sports[2])

# error--out of range
# print(sports[4])

celtics = sports[2]
# print(celtics)
# print('The Celtics play ' + celtics + '.')

name = "John Smith"
# print(name[0])
# print(name[5])
# print(name[0:4])

# take 2 variables and create a full name
first_name = "John"
last_name = "Smith"
# print(first_name + ' ' + last_name)
# or:
full_name = first_name + ' ' + last_name
# print(full_name)

print('First Name: {} \nLast Name: {}'.format(first_name, last_name))


