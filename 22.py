import fileinput
from utils import ints
from collections import namedtuple
from functools import cache


Player = namedtuple('Character', ['hp', 'armor', 'mana'])
Boss = namedtuple('Boss', ['hp', 'damage'])
mana_costs = {'magic missile': 53, 'drain': 73, 'shield': 113, 'poison': 173, 'recharge': 229}
spells = mana_costs.keys()
effect_durations = {'shield': 6, 'poison': 6, 'recharge': 5}

def parse_boss():
  for line in fileinput.input():
    if 'Hit Points' in line:
      hp = ints(line)[0]
    elif 'Damage' in line:
      damage = ints(line)[0]
      
  return Boss(hp=hp, damage=damage)

def other(turn):
  return 'boss' if turn == 'you' else 'you'

def not_have(spell, effects):
  for (name, r) in effects:
    if name == spell and r > 0:
      return False
  return True

State = namedtuple('State', ['you', 'boss', 'effects', 'turn', 'winner'])
def do_turn(state, is_hard, spell=None):
  (you, boss, effects, turn, _) = state
  
  if turn == 'you' and is_hard:
    you = you._replace(hp = you.hp - 1)
    if you.hp <= 0:
      return State(you=you, boss=boss, effects=effects, turn=turn, winner='boss')
  
  # Apply effects
  effect_names = set(map(lambda x: x[0], effects))
  if 'shield' in effect_names:
    you = you._replace(armor=7)
  else:
    you = you._replace(armor=0)
  
  if 'poison' in effect_names:
    boss = boss._replace(hp=boss.hp-3)
    
  if 'recharge' in effect_names:
    you = you._replace(mana=you.mana+101)
  
  effects = frozenset({(name, remaining - 1) for (name, remaining) in effects if remaining > 1})

  if boss.hp <= 0:
    return State(you=you, boss=boss, effects=effects,turn=turn, winner='you')
  
  if turn == 'boss':
    assert spell is None
    dmg = max(boss.damage - you.armor, 1)
    you = you._replace(hp = you.hp - dmg)
    
    return State(you=you, boss=boss, effects=effects, turn=other(turn), winner='boss' if you.hp <= 0 else None)


  spell_cost = mana_costs[spell]
  assert you.mana >= spell_cost
  you = you._replace(mana = you.mana - spell_cost)
  
  match spell:
    case 'magic missile': 
      boss = boss._replace(hp=boss.hp - 4)
    case 'drain':
      boss = boss._replace(hp=boss.hp - 2)
      you = you._replace(hp=you.hp + 2)
    case 'shield' | 'poison' | 'recharge':
      assert not_have(spell, effects)
      effects |= {(spell, effect_durations[spell])}

  return State(you=you, boss=boss, effects=effects,turn=other(turn), winner='you' if boss.hp <= 0 else None)

@cache
def cheapest_win(state, is_hard=False):
  if state.turn == 'boss':
    state = do_turn(state, is_hard)
  
  if state.winner is not None:
    return 0 if state.winner == 'you' else float("inf")

  return min([mana_costs[spell] + cheapest_win(do_turn(state, is_hard, spell), is_hard=is_hard) for spell in spells if mana_costs[spell] <= state.you.mana and (not_have(spell, state.effects) or (spell, 1) in state.effects)], default=float("inf"))

you = Player(hp=50, armor=0, mana=500)
boss = parse_boss()
# you = Player(hp=10, armor=0, mana=250)
# boss = Boss(hp=14, damage=8)

state = State(you = you, boss=boss, effects = frozenset(), turn = 'you', winner=None)

def part_1():
  print(cheapest_win(state, is_hard=False))

def part_2():
  print(cheapest_win(state, is_hard=True))

part_2()