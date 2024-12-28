import fileinput
from collections import Counter
from utils import ints


def parse_line(line):
  return ints(line)

def simulate(reindeers, upto):
  distances = []
  for (speed, run, rest) in reindeers:  
    curr = upto % (run + rest)
    times = upto // (run + rest)
    distance = times * run * speed + min(curr, run) * speed
    distances.append(distance)
  
  return distances

reindeers = [parse_line(line) for line in fileinput.input()]
upto = 2503

def part_1():
  final_pos = simulate(reindeers, upto)
  answer = max(final_pos)
  print(answer)

def part_2():
  points = Counter()
  for i in range(1, upto + 1):
    positions = simulate(reindeers, i)
    best = max(positions)
    leaders = [i for i in range(len(reindeers)) if positions[i] == best]
    points.update(leaders)
  answer = points.most_common(1)[0][1]
  print(answer)

part_2()