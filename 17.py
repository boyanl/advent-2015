import fileinput
from collections import Counter
from functools import cache

def make_containers(capacities):
  return frozenset((capacities[i], i) for i in range(len(capacities)))

def subtracted(counts, el):
  return counts - {el}

@cache
def ways(amount, remaining, last=None, length=0):
  result = Counter()
  for el in remaining:
    if not(last is None or el <= last):
      continue

    (c, _) = el
    if c == amount:
      result.update((length+1,))
    elif c < amount:
      result += ways(amount - c, subtracted(remaining, el), last=el, length=length+1)

  return result


# amount = 25
# containers = make_containers([20, 15, 10, 5, 5])
amount = 150
containers = make_containers([int(line) for line in fileinput.input()])

def part_1():
  answer = sum(ways(amount, containers).values())
  print(answer)


def part_2():
  counts = ways(amount, containers)
  min_containers = min(counts.keys())
  answer = counts[min_containers]
  print(answer)

part_1()