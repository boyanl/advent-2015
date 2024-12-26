from hashlib import md5
import itertools

def md5_str(s):
  return md5(str.encode(s)).hexdigest()

def find_suffix(secret, zeros_cnt):
  for i in itertools.count():
    if md5_str(secret + str(i)).startswith('0' * zeros_cnt):
      return i

# secret = input()
secret = 'bgvyzdsv'

def part_1():
  answer = find_suffix(secret, 5)
  print(answer)

def part_2():
  answer = find_suffix(secret, 6)
  print(answer)
  
part_2()