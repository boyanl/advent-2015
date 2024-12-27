from functools import cache


def runs(s):
  if len(s) == 0:
    return []
  
  result = []
  i = 0
  while i < len(s):
    c = s[i]
    n = 0
    while i < len(s) and s[i] == c:
      i += 1
      n += 1

    result.append((n, c))
  
  return result


@cache
def describe(s):
  if len(s) == 0:
    return ''
  if len(s) == 1:
    return '1' + s

  return "".join(str(n) + c for (n, c) in runs(s))

def describe_times(s, n):
  current = s
  for _ in range(n):
    current = describe(current)
  
  return current
   

inp = '1321131112'

def part_1():
  answer = len(describe_times(inp, 40))
  print(answer)

def part_2():
  answer = len(describe_times(inp, 50))
  print(answer)
  
part_2()