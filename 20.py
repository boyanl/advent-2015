import itertools
import math

def sieve(upto):
  is_prime = [True] * upto
  for i in range(2, upto+1):
    for j in range(i*i, upto, i):
      is_prime[j] = False
      
  return list(i for i in range(2, upto) if is_prime[i])

input = 34000000


def factorization(n, primes):
  r = n
  stop = math.ceil(math.sqrt(n))
  result = {}
  for p in primes:
    if p > stop:
      break
    
    times = 0
    while r % p == 0:
      r //= p
      times += 1
    
    if times > 0:
      result[p] = times
  
  if r > 1:
    result[r] = 1
  
  return result

def divisors_sum(n, primes):
  result = 1
  for (p, m) in factorization(n, primes).items():
    result *= (p ** (m+1) - 1)//(p - 1)
  return result
    
def presents_1(house, primes):
  return divisors_sum(house, primes) * 10

def part_1():
  times_per_elf = 10
  upto = input // times_per_elf
  primes = sieve(upto)
  answer = next(n for n in range(50, upto) if presents_1(n, primes) >= input)
  print(answer)


def product(ns):
  result = 1
  for n in ns:
    result *= n
  return result

def divisors(n, primes):
  factors = factorization(n, primes)
  ps = list(factors.keys())
  powers = [factors[p] for p in ps]
  result = []
  for current_pows in itertools.product(*[range(0, n+1) for n in powers]):
    d = product([ps[i] ** current_pows[i] for i in range(len(powers))])
    result.append(d)
  return result

def presents_2(house, primes):
  result = 0
  for elf in divisors(house, primes):
    if house // elf <= 50:
      result += 11 * elf
  return result

def part_2():
  primes = sieve(1_000_000)
  answer = next(n for n in range(50, input) if presents_2(n, primes) >= input)
  print(answer)
      
part_2()