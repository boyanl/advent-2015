import fileinput
from utils import ints

boxes = [ints(line) for line in fileinput.input()]

def part_1():
  answer = sum(2*w*l + 2*l*h + 2*w*h + min(w*l, l*h, w*h) for (w, l, h) in boxes)
  print(answer)

def part_2():
  perimeter = lambda a, b: 2*a + 2*b
  answer = sum(min(perimeter(w, l), perimeter(l, h), perimeter(w, h)) + w*l*h for (w, l, h) in boxes)
  print(answer)


part_2()