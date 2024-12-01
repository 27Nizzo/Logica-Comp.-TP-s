from z3 import *

x = Int('x')
y = Int('y')

constrains = [x + y == 10, x > y]


solve(*constrains)

