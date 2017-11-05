"""
Some basic data types in python3
"""
print('Int\'s')
x = 3
print(type(x), ' = <class \'int\'>')
print(x, ' = 3')
print(x + 1, ' = 4')
print(x - 1, ' = 2')
print(x * 2, ' = 6')
print(x ** 2, ' = 9')

x += 1
print(x, ' = 4')

x *= 2
print(x, ' = 8')

print('\nFloat\'s')
y = 2.5
print(type(y), ' = <class \'float\'>')
print(y, y + 1, y * 2, y ** 2)
print('2.5 3.5 5.0 6.25')

print('\nBoolean Logic')
t = True
f = False
print(type(t), ' = <class \'bool\'>')
print(t and f, ' = False')
print(t or f, ' = True')
print(not t, ' = False')
print(t != f, ' = True')

print('\nString\'s')
hello='hello'
world='world'
print(hello, '= hello')
print(len(hello), '= 5')
hw = hello + ' ' + world
print(hw, '= hello world')
hw12 = '%s %s %d' % (hello, world, 12)
print(hw12, '= hello world 12')

print('\nString methods')
s = 'hello'
print(s.capitalize())
print(s.upper())
print(s.rjust(7))
print(s.center(7))
print(s.replace('l', '(ell)'))
print('     world'.strip())