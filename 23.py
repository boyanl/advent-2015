import fileinput

def parse_instr(line):
  idx = line.index(' ')
  instr, rest = line[:idx], line[idx+1:]
  args = rest.split(", ")
  return (instr, args)

def execute(program, state):
  current = state.copy()
  ip = 0
  
  while 0 <= ip < len(program):
    (op, args) = program[ip]
    target = args[0]

    match op:
      case 'hlf':
        current[target] = current[target] // 2
      case 'tpl':
        current[target] = current[target] * 3
      case 'inc':
        current[target] += 1
      case 'jmp':
        amount = int(target)
        ip += amount - 1 # -1 since the ip will be incremented later anyway
      case 'jie':
        amount = int(args[1])
        if current[target] % 2 == 0:
          ip += amount - 1
      case 'jio':
        amount = int(args[1])
        if current[target] == 1:
          ip += amount - 1
    
    ip += 1
  
  return current
        


instructions = [parse_instr(line) for line in map(str.strip, fileinput.input())]
def part_1():
  state = execute(instructions, {'a': 0, 'b': 0})
  print(state['b'])

def part_2():
  state = execute(instructions, {'a': 1, 'b': 0})
  print(state['b'])

part_2()