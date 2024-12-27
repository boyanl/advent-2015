import fileinput
from collections import defaultdict
from functools import cache

distances = defaultdict(list)
for line in fileinput.input():
  parts = line.split()
  from_name, to_name = parts[0], parts[2]
  distance = int(parts[4])
  
  distances[from_name].append((to_name, distance))
  distances[to_name].append((from_name, distance))

@cache
def calculate_shortest(current, remaining):
  if len(remaining) == 0:
    return 0
  return min(d + calculate_shortest(next, remaining - {next}) for (next, d) in distances[current] if next in remaining)
  
def part_1():
  remaining = frozenset(distances.keys())
  answer = min(calculate_shortest(start, remaining - {start}) for start in distances.keys())
  print(answer)

@cache
def calculate_longest(current, remaining):
  if len(remaining) == 0:
    return 0
  return max(d + calculate_longest(next, remaining - {next}) for (next, d) in distances[current] if next in remaining)

def part_2():
  remaining = frozenset(distances.keys())
  answer = max(calculate_longest(start, remaining - {start}) for start in distances.keys())
  print(answer)

part_2()