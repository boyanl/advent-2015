import json
import numbers
from utils import ints

def sum_ints(json):
  return sum(ints(json))
def part_1():
  answer = sum_ints(input())
  print(answer)

def sum_ignoring_red(obj):
  if isinstance(obj, numbers.Number):
    return obj
  elif isinstance(obj, list):
    return sum(sum_ignoring_red(x) for x in obj)
  elif isinstance(obj, dict):
    have_red = 'red' in obj.values()
    return 0 if have_red else sum(sum_ignoring_red(val) for val in obj.values())
  
  return 0


def part_2():
  parsed = json.loads(input())
  answer = sum_ignoring_red(parsed)
  print(answer)

part_2()