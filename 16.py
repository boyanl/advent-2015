import fileinput

def parse_pair(part):
  parts = part.split(": ")
  return (parts[0], int(parts[1]))

def parse_aunt(things):
  things = map(parse_pair, things.replace(", ", "\n").splitlines())
  return dict(things)

 
wanted = parse_aunt("""children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1""")

possible_aunts = {}
for line in fileinput.input():
  idx = line.find(':')
  name, rest = line[:idx].strip(), line[idx+1:].strip()
  possible_aunts[name] = parse_aunt(rest)

def matches_1(want, have):
  return all(k not in have or have[k] == v for (k, v) in want.items())
  
def part_1():
  answer = next(name for (name, aunt) in possible_aunts.items() if matches_1(wanted, aunt))
  print(answer)


def matches_2(want, have):
  for (k, v) in want.items():
    ok = k not in have
    match k:
      case 'cats' | 'trees':
        ok = ok or have[k] > want[k]
      case 'pomeranians' | 'goldfish':
        ok = ok or have[k] < want[k]
      case _:
        ok = ok or have[k] == want[k]

    if not ok:
      return False

  return True
  
def part_2():
  answer = next((name, aunt) for (name, aunt) in possible_aunts.items() if matches_2(wanted, aunt))
  print(answer)

part_2()