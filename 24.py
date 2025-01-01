import fileinput
from functools import cache
from heapq import heapify, heappush, heappop

def remaining_estimate(sums, remaining):
  if remaining == 0:
    return 0

  return next(i+1 for i in range(len(sums)) if sums[i] >= remaining)

def is_set(mask, i):
  return (mask & (1 << i)) != 0

def with_set(mask, i):
  return mask | (1 << i)

def best_configuration(items, weight):
  reverse_sorted = sorted(items, reverse=True)
  sums = [sum(reverse_sorted[:(i+1)]) for i in range(len(items))]
  
  q = [(remaining_estimate(sums, weight), 0, 1, 0, 0)]
  while len(q) > 0:
    (h, cnt, entanglement, taken_mask, total) = heappop(q)
    if total == weight:
      return (cnt, entanglement, [items[i] for i in range(len(items)) if is_set(taken_mask, i)])
    
    if len(q) > 10_000_000:
      q = q[:1_000_000]
    
    remaining = weight - total
    for i in range(len(items)):
      if items[i] <= remaining and not is_set(taken_mask, i):
        estimate = cnt + 1 + remaining_estimate(sums, remaining - items[i])
        heappush(q, (estimate, cnt + 1, entanglement * items[i], with_set(taken_mask, i), total + items[i]))
  
  return (-1, -1)

items = [int(line) for line in fileinput.input()]

def part_1():
  target_weight = sum(items) // 3

  config = best_configuration(items, target_weight)
  print(config)
  answer = config[1]
  print(answer)

def part_2():
  target_weight = sum(items) // 4

  config = best_configuration(items, target_weight)
  print(config)
  answer = config[1]
  print(answer)

part_2()