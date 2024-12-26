import re

def ints(text):
  return tuple(map(int, re.findall('-?[0-9]+', text)))