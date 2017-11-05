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

print('\nContainers (Array\'s)')
xs = [3, 1, 2]
print(xs, xs[2])
print(xs[-1])
xs[2] = 'foo'
print(xs)
xs.append('bar')
print(xs)
x = xs.pop()
print(x, xs)

print('\nSlicing with List\'s')
num = list(range(5))
print(num)
print(num[2:4])
print(num[2:])
print(num[:2])
print(num[:-1])
num[2:4] = [8, 9]
print(num)

print('\nLoops')
animals = ['cats', 'dogs', 'monkey']
for idx, animal in enumerate(animals):
    print('#%d: %s' % (idx + 1, animal))

print('\nList - Long way')
nums = list(range(5))
squares = []
for x in nums:
    squares.append(x ** 2)
print(squares)

print('\nList - comprehension')
nums = list(range(5))
squares = [x ** 2 for x in nums]
print(squares)

print('\nList - comprehension with conditionals')
nums = list(range(5))
squares = [x ** 2 for x in nums if x % 2 == 0]
print(squares)

print('Dictionaries')
d = {'cat': 'cute', 'dog': 'furry'}
print(d['cat'])
print('cat' in d)
d['fish'] = 'wet'
print(d['fish'])
# print(d['monkey']) <- blows up!
print(d.get('monkey','Monkey not found'))
print(d.get('fish', 'Fish not found'))
del d['fish']
print(d.get('fish', 'Fish not found'))

print('\nLast - Classes')
class Greeter(object):
    # Constructor
    def __init__(self, name):
        self.name = name

    def greet(self, loud=False):
        if loud:
            print('HELLO %s' % (self.name.upper()))
        else:
            print('Hello %s' % (self.name))

g = Greeter('world')
g.greet()
g.greet(True)