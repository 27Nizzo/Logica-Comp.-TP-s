from z3 import *

x = BitVec('x', 8)

constraints = [x & 0b11110000 == 0b10100000]

solve(*constraints)