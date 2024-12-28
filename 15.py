import fileinput
from utils import ints
from functools import reduce
import itertools

ingredients = [ints(line) for line in fileinput.input()]

def product(xs):
  return reduce(lambda a, b: a*b, xs)

def total_score(amounts):
  assert len(amounts) == len(ingredients)
  props_count = len(ingredients[0]) - 1

  return product(max(sum(ingredients[j][i]*amounts[j] for j in range(len(ingredients))), 0) for i in range(0, props_count))

def best_score_sans_calories():
  domain = [list(range(0, 101))] * (len(ingredients) - 1) # amount of last ingredient is always 100 - (sum of the rest) if that is >= 0
  return max(total_score(amounts) for amounts_nolast in itertools.product(*domain) for amounts in [amounts_nolast + (100-sum(amounts_nolast),)]if sum(amounts_nolast) <= 100)

def part_1():
  answer = best_score_sans_calories()
  print(answer)
  
def calories_for(amounts):
  return sum(amounts[i]*ingredients[i][-1] for i in range(len(ingredients)))

def best_score_for_calories(calories):
  domain = [list(range(0, 101))] * (len(ingredients) - 1) # amount of last ingredient is always 100 - (sum of the rest) if that is >= 0

  return max(total_score(amounts) for amounts_nolast in itertools.product(*domain) for amounts in [amounts_nolast + (100-sum(amounts_nolast),)] if sum(amounts_nolast) <= 100 and calories_for(amounts) == calories)

def part_2():
  answer = best_score_for_calories(500)
  print(answer)

part_2()