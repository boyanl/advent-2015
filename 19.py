import fileinput
from collections import defaultdict
from heapq import heapify, heappush, heappop

def replacements(s, sub, replacement):
  index = s.find(sub)
  while index != -1:
    yield s[:index] + replacement + s[index + len(sub):]
    index = s.find(sub, index+1)

start = ""
rules = defaultdict(list)
rules_inv = defaultdict(list)

for line in map(str.strip, fileinput.input()):
  if '=>' in line:
    parts = line.split(' => ')
    rules[parts[0]].append(parts[1])
    rules_inv[parts[1]] = parts[0]
  elif len(line):
    start = line


def all_replacements(starts, n=1):
  current = set(starts)
  result = set()
  for _ in range(n):
    result = set()
    for start in current:
      for (s, ns) in rules.items():
        for n in ns:
          result |= set(replacements(start, s, n))
          
    current = result
  return result

def part_1():
  answer = len(all_replacements([start], n=1))
  print(answer)


def part_2():
  max_per_turn = 2 # magically estimated

  pq = [(0, 0, start)]
  heapify(pq)

  visited = set()
  answer = -1
  
  while len(pq) > 0:
    (h, cnt, s) = heappop(pq)
    
    if len(pq) > 1_000_000:
      print(f"H = {h}, cnt = {cnt}, s = {s}, len = {len(s)}")
      pq = pq[:10_000]

    if s == 'e':
      answer = cnt
      break
    if s in visited:
      continue
    
    visited.add(s)
    
    next = set(r for (k, v) in rules_inv.items() for r in replacements(s, k, v))
    for s1 in next:
      if (('e' not in s1) or (s1 == 'e')) and s1 not in visited:
          h_next = cnt + 1 + len(s1) / max_per_turn
          heappush(pq, (h_next, cnt + 1, s1))
  
  print(answer)

part_2()
