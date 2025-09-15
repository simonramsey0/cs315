# Simon Ramsey
# CS315 - Algorithms and Analysis
# Homework 1 - Secret Santa, Multiplication without operator, Multiplication Recursively

from itertools import permutations
import json
import os

def secret_santa(participants: list, invalid_combinations: set[tuple]) -> list:
  all_permutations = permutations(participants)

  acceptable_combinations = []

  for p in all_permutations:
    valid = True
    zipped_list = list(zip(participants, p)) # combine each permutation with the original list of participants to ensure every possible group of pairings is considered

    # check every pairing in the zipped list for validity
    for i, j in zipped_list:
      if (i, j) in invalid_combinations or i == j:
        valid = False
        break
    
    if valid:
      acceptable_combinations.append(list(zipped_list))

  return acceptable_combinations

# if the output file already exists then delete it
if os.path.exists("output.txt"):
    os.remove("output.txt")

# load input data from json file
file = open("input.json", "r")
data = json.load(file)
file.close()

participants = data["participants"]
invalid_combinations = set(tuple(pair) for pair in data["invalid_combinations"]) # convert list of lists to set of tuples for easier comparison
combinations = secret_santa(participants, invalid_combinations)

# write all permissable combinations to the output text file
file = open("output.txt", "w")
for c in combinations:
  for pair in c:
    file.write(f"({pair[0]} gives to {pair[1]}), ")
  file.write("\n")
file.close()