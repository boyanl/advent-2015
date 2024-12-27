
chars = "abcdefghijklmnopqrstuvwxyz"
def next_char(c):
  i = chars.index(c)
  return chars[(i+1)%len(chars)]

def pairs_same(s):
  return [(i, i+1) for i in range(len(s)-1) if s[i] == s[i+1]]

def is_valid(p):
  have_increasing = any(p[i] <= 'x' and next_char(p[i]) == p[i+1] and next_char(p[i+1]) == p[i+2] for i in range(len(p)-3))
  no_forbidden = len({'i', 'l', 'o'}  & set(p)) == 0
  pairs = pairs_same(p)
  have_pairs = len(pairs) >= 2 and pairs[-1][0] - pairs[0][0] >= 2
  
  return have_increasing and no_forbidden and have_pairs

def test_pass(p):
  print(is_valid(p))

def next_pass(p):
  result = list(p)
  i = len(p)-1

  while i >= 0:
    result[i] = next_char(result[i])
    if result[i] != 'a':
      break
    i -= 1
  return result

def find_next_valid(p):
  result = next_pass(p)
  while not is_valid(result):
    result = next_pass(result)
  return "".join(result)
  

input = 'cqjxjnds'
# input = 'abcdefgh'

def part_1():
  answer = find_next_valid(input)
  print(answer)

def part_2():
  answer = find_next_valid(input)
  answer = find_next_valid(answer)
  print(answer)

part_2()