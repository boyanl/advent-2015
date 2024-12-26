import fileinput
from pos import Pos, DIRS_MAP

def distinct_locations(line):
  current = Pos(x=0, y=0)
  positions = {current}
  for d in line:
    current += DIRS_MAP[d]
    positions.add(current)
  
  return positions
  
def part_1():
  for line in map(str.strip, fileinput.input()):
    answer = len(distinct_locations(line))
    print(answer)
    

def part_2():
  for line in map(str.strip, fileinput.input()):
    evens = line[0::2]
    odds = line[1::2]
    answer = len(distinct_locations(evens) | distinct_locations(odds))
    print(answer)

part_2()