import fileinput
from pos import Pos, UP, DOWN, LEFT, RIGHT

def neighbours(state, p):
  result = []
  for n in [p+UP, p+UP+LEFT, p+UP+RIGHT, p+DOWN, p+DOWN+LEFT, p+DOWN+RIGHT, p+LEFT, p+RIGHT]:
    if 0 <= n.x < len(state[0]) and 0 <= n.y < len(state):
      result.append(n)
  
  return result

def at(state, p):
  return state[p.y][p.x]

def print_state(state):
  for line in state:
    print("".join(line))
  print()

def evolve(state):
  n, m = len(state), len(state[0])
  result = []
  for y in range(n):
    row = []
    for x in range(m):
      p = Pos(x=x, y=y)
      alive = sum(1 for neighb in neighbours(state, p) if at(state, neighb) == '#')
      
      if state[y][x] == '#':
        row.append('#' if alive in (2, 3) else '.')
      else:
        assert state[y][x] == '.'
        row.append('#' if alive == 3 else '.')
        
    result.append(row)

  return result

def light_corners(state):
  n, m = len(state), len(state[0])
  state[0][0] = state[n-1][0] = state[0][m-1] = state[n-1][m-1] = '#'

state = [list(line) for line in map(str.strip, fileinput.input())]
steps = 100

def part_1():
  current = state
  for _ in range(steps):
    current = evolve(current)

  answer = sum(line.count('#') for line in current)
  print(answer)

  
def part_2():
  current = state
  light_corners(current)
  for _ in range(steps):
    current = evolve(current)
    light_corners(current)

  answer = sum(line.count('#') for line in current)
  print(answer)

part_2() 