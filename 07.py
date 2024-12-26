import fileinput
from functools import cache

rules = {}
known = {}

for line in map(str.strip, fileinput.input()):
  parts = line.split(' -> ')
  left = parts[0].split()
  right = parts[1]
  
  rules[right] = left

def evaluate(s):
  if s in known:
    return known[s]

  if s.isdigit():
    res = int(s)
  
  else:
    rule = rules[s]
    mask = 0xffff
    if len(rule) == 1:
      res = evaluate(rule[0])
    elif len(rule) == 2:
      op, right = rule
      assert op == 'NOT'
      res = ~evaluate(right) & mask
    else:
      (left, op, right) = rules[s]
      l, r = evaluate(left), evaluate(right)
      if op == 'AND':
        res = l & r
      elif op == 'OR':
        res = l | r
      elif op == 'LSHIFT':
        res = (l << r) & mask
      elif op == 'RSHIFT':
        res = l >> r
      else:
        assert False, op

  known[s] = res
  return res

def part_1():
  print(evaluate('a'))

def part_2():
  val_a = evaluate('a')
  rules['b'] = (str(val_a),)

  known.clear()
  print(evaluate('a'))

part_2()