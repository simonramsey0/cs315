# Simon Ramsey
# CS315 - Algorithms and Analysis
# Homework 1 - Secret Santa, Multiplication without operator, Multiplication Recursively

from itertools import permutations

def secret_santa(participants: list, invalid_combinations: list[tuple]) -> None:
  for p in permutations(participants):
    if p not in invalid_combinations:
      print(p)