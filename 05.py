import fileinput

vowels = set("aioeu")

def has_consecutive(s):
  for i in range(0, len(s)-1):
    if s[i] == s[i+1]:
      return True
  return False

def is_nice(s):
  vowels_ok = sum(1 for c in s if c in vowels) >= 3
  consecutive_ok = has_consecutive(s)
  forbidden_ok = all(f not in s for f in ['ab', 'cd', 'pq', 'xy'])
  
  return vowels_ok and consecutive_ok and forbidden_ok

def part_1():
  answer = sum(1 for line in map(str.strip, fileinput.input()) if is_nice(line))
  print(answer)

def all_indices(s, sub):
  result = []
  start = 0
  while True:
    i = s.find(sub, start)
    if i == -1:
      break
    result.append(i)
    start = i+1
  return result

def have_nonoverlapping(s, sub):
  indices = all_indices(s, sub)
  return max(indices) - min(indices) >= len(sub)

def have_repeating_with_between(s):
  for i in range(0, len(s)-2):
    if s[i+2] == s[i]:
      return True
  return False
  

def is_nice_2(s):
  pairs = {s[i:i+2] for i in range(0, len(s) - 1)}
  pairs_ok = any(have_nonoverlapping(s, p) for p in pairs)
  
  return pairs_ok and have_repeating_with_between(s)

def part_2():
  answer = sum(1 for line in map(str.strip, fileinput.input()) if is_nice_2(line))
  print(answer)

part_2()