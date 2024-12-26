import fileinput

def part_1():
  for line in fileinput.input():
    answer = line.count('(') - line.count(')')
    print(answer)

def part_2():
  for line in fileinput.input():
    level = 0
    for (j, c) in enumerate(line):
      level += 1 if c == '(' else -1
      if level == -1:
        print(j+1)
        break


part_2()