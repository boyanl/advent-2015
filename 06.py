import fileinput
from utils import ints

n = 1000
grid = [[0] * n for i in range(n)]
instructions = []

for line in map(str.strip, fileinput.input()):
  op = ''
  if 'toggle' in line:
    op = 'toggle'
  elif 'turn on' in line:
    op = 'turn on'
  elif 'turn off' in line:
    op = 'turn off' 
  
  coords = ints(line)
  start = (coords[0], coords[1])
  end = (coords[2], coords[3])
  
  instructions.append((op, start, end))
  
  
def execute_1(instructions):
  for (op, start, end) in instructions:
    for i in range(start[0], end[0]+1):
      for j in range(start[1], end[1]+1):
        if op == 'toggle':
          grid[i][j] = 1 - grid[i][j]
        elif op == 'turn on':
          grid[i][j] = 1
        else:
          grid[i][j] = 0

  return sum(1 for i in range(n) for j in range(n) if grid[i][j] == 1)
  
def part_1():
  answer = execute_1(instructions)
  print(answer)

def execute_2(instructions):
  for (op, start, end) in instructions:
    for i in range(start[0], end[0]+1):
      for j in range(start[1], end[1]+1):
        if op == 'toggle':
          grid[i][j] += 2
        elif op == 'turn on':
          grid[i][j] += 1
        else:
          grid[i][j] = max(0, grid[i][j] - 1)

  return sum(grid[i][j] for i in range(n) for j in range(n))

def part_2():
  answer = execute_2(instructions)
  print(answer)

part_2()