# Simon Ramsey
# CS315 - Algorithms and Analysis
# Homework 1 - Secret Santa, Multiplication without operator, Multiplication Recursively

import sys

# changed the maximum recursion depth to 1,000,000
sys.setrecursionlimit(10**6)

def multiply_without_operator(a: int, b: int) -> int:
  result: int = 0
  for i in range(b):
    result += a
  
  return result

# if an input for b of over 15000 is given it throws a max recursion depth error
# can fix this with some clever bitwise operation, or you can just change the max recursion depth because we know it'll never loop infinitely
def multiply_recursively(a: int, b: int) -> int:
  if b == 0: return 0
  else: return a + multiply_recursively(a, b - 1)

# both the recursive and iterative methods do basically the same thing, just in different ways
# the recursive solution is just shut down by the system because it believes it to be looping infinitely
print(multiply_without_operator(15000, 15000))
print(multiply_recursively(15000, 15000))