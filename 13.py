import fileinput
from itertools import permutations

def parse_line(line):
  parts = line.strip().split()
  person1 = parts[0]
  person2 = parts[-1][:-1]
  gain = int(parts[3]) if parts[2] == 'gain' else -int(parts[3])

  return (person1, person2, gain)

def calculate_happiness(arrangement, rules):
  n = len(arrangement)
  result = 0
  for i in range(n):
    p0, p1, p2 = arrangement[(i+n-1)%n], arrangement[i], arrangement[(i+1)%n]
    result += rules[(p1, p0)] + rules[(p1, p2)]

  return result

def people(rules):
  return {pair[0] for pair in rules.keys()}


rules = {}
for line in fileinput.input():
  (p1, p2, c) = parse_line(line)
  rules[(p1, p2)] = c

def part_1():
  answer = max(calculate_happiness(arrangement, rules) for arrangement in permutations(people(rules)))
  print(answer)

def part_2():
  rules_new = rules.copy() 
  for p in people(rules):
    rules_new[(p, 'me')] = rules_new[('me', p)] = 0
  
  answer = max(calculate_happiness(arrangement, rules_new) for arrangement in permutations(people(rules_new)))
  print(answer)

part_2()