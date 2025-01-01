from utils import ints

initial = 20151125
p = 252533
m = 33554393

def triangle(n):
  return n*(n+1)//2

def sequence_number(row, col):
  s = row+col
  before = triangle(s-2)
  n = before + (s - row)
  return n

def fastpow_mod(p, n, m):
  acc = p
  result = 1
  while n > 0:
    if n % 2 == 1:
      result = (result * acc) % m
    acc = (acc * acc) % m
    n //= 2


  return result
    
def at(row, col):
  n = sequence_number(row, col)
  return (initial * fastpow_mod(p, n-1, m)) % m


row, col = ints(input())
answer = at(row, col)
print(answer)