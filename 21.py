import fileinput
import math
from collections import namedtuple, defaultdict, Counter
from itertools import product, combinations
from utils import ints


Stats = namedtuple('Stats', ['damage', 'armor'])
Character = namedtuple('Character', ['hp', 'damage', 'armor'])
Item = namedtuple('Item', ['name', 'slot', 'cost', 'damage','armor'])

def parse_shop(description):
  result = defaultdict(list)
  for line in description.splitlines():
    line = line.strip()
    if "Cost" in line:
      category = line.split()[0][:-1]
    elif len(line) > 0:
      parts = line.split()
      cost, damage, armor = int(parts[-3]), int(parts[-2]), int(parts[-1])
      name = " ".join(parts[:-3])
      item = Item(name=name, slot=category, cost=cost, damage=damage, armor=armor)
      result[category].append(item)
  
  return result

def parse_boss():
  for line in fileinput.input():
    if 'Hit Points' in line:
      hp = ints(line)[0]
    elif 'Damage' in line:
      damage = ints(line)[0]
    elif 'Armor' in line:
      armor = ints(line)[0]
    
  return Character(hp=hp, damage=damage, armor=armor)

def armor_needed_to_beat(you, boss):
  assert you.damage > 0
  result = math.ceil(boss.damage - (you.hp/boss.hp) * max(1, you.damage - boss.armor))
  return max(result, 0) if result < boss.damage else None

def can_beat(you, boss):
  dmg_you = max(1, you.damage - boss.armor)
  dmg_boss = max(1, boss.damage - you.armor)
  print(f"You (effective dmg) = {dmg_you}, boss (effective dmg) = {dmg_boss}")

  rounds_kill_boss = math.ceil(boss.hp / dmg_you)
  rounds_kill_you = math.ceil(you.hp / dmg_boss)
  print(f"Rounds to kill boss = {rounds_kill_boss}, rounds to kill you = {rounds_kill_you}")

  return rounds_kill_boss <= rounds_kill_you

def armor_cost_least(armor, shop, slots = Counter(['Armor', 'Rings', 'Rings']), items_taken = set()):
  if armor == 0:
    return (0, set())

  items = [item for items in shop.values() for item in items]
  result = (float("inf"), set())
  for item in items:
    if 0 < item.armor <= armor and item.slot in slots and slots[item.slot] > 0 and item not in items_taken:
      (cost_rem, items_taken_rem) = armor_cost_least(armor - item.armor, shop, slots - Counter([item.slot]), items_taken | {item})
      if item.cost + cost_rem < result[0]:
        result = (item.cost + cost_rem, items_taken | {item} | items_taken_rem)

  return result

def cheapest_win(you, boss, shop):
  best = None
  rings_options = [None, None] + shop['Rings'] # repeat 'None' so we can directly take combinations and have the option of no rings
  for weapon in shop['Weapons']:
    for rings in combinations(rings_options, 2):
      damage = weapon.damage
      cost = weapon.cost
      slots_remaining = Counter(['Armor', 'Rings', 'Rings'])
      equipped = [weapon]

      for ring in rings:
        if ring is not None:
          damage += ring.damage
          cost += ring.cost
          slots_remaining -= Counter(['Rings'])
          equipped += [ring]

      upgraded_you = you._replace(damage = damage)
      armor_wanted = armor_needed_to_beat(upgraded_you, boss)
      
      if armor_wanted is not None:
        (additional_cost, armor_items) = armor_cost_least(armor_wanted, shop, slots_remaining)
        if best is None or additional_cost + cost < best:
          best = additional_cost + cost
          best_items = equipped + list(armor_items)

  return (best, best_items)

shop = parse_shop("""
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
""")
boss = parse_boss()
you = Character(hp=100, damage=0, armor=0)

def part_1():
  answer = cheapest_win(you, boss, shop)
  print(answer)


def armor_cost_most(armor, shop, slots = Counter(['Armor', 'Rings', 'Rings'])):
  if armor == 0:
    return (0, [])

  items = [item for items in shop.values() for item in items]
  result = (float("-inf"), [])
  for item in items:
    if 0 < item.armor <= armor and item.slot in slots and slots[item.slot] > 0:
      (cost_rem, items_taken) = armor_cost_most(armor - item.armor, shop, slots - Counter([item.slot]))
      if item.cost + cost_rem > result[0]:
        result = (item.cost + cost_rem, items_taken + [item])

  return result

def most_expensive_loss(you, boss, shop):
  best = None

  rings_options = [None, None] + [ring for ring in shop['Rings'] if ring.damage > 0] # repeat 'None' so we can directly take combinations and have the option of no rings
   
  for weapon in shop['Weapons']:
    for rings in combinations(rings_options, 2):
      damage = weapon.damage
      cost = weapon.cost
      slots_remaining = Counter(['Armor', 'Rings', 'Rings'])
      equipped = [weapon]

      for ring in rings:
        if ring is not None:
          damage += ring.damage
          cost += ring.cost
          slots_remaining -= Counter(['Rings'])
          equipped += [ring]

      upgraded_you = you._replace(damage = damage)
      armor_wanted = armor_needed_to_beat(upgraded_you, boss)
      can_lose = armor_wanted is None or armor_wanted > 0
      
      if can_lose:
        (additional_cost, armor_items) = armor_cost_most(armor_wanted-1, shop, slots_remaining)
        if best is None or additional_cost + cost > best:
          best = additional_cost + cost
          best_items = equipped + armor_items

  return (best, best_items)

def part_2():
  answer = most_expensive_loss(you, boss, shop)
  print(answer)

part_2()