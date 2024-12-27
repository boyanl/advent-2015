import fileinput

def length_diff(s):
  return len(s) - len(eval(s))


def part_1():
  answer = sum(length_diff(line) for line in map(str.strip, fileinput.input()))
  print(answer)
  

def expand(s):
  return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'

def part_2():
  answer = sum(length_diff(expand(line)) for line in map(str.strip, fileinput.input()))
  print(answer)

part_2()