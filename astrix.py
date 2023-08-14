'''
Game scripts
'''

import random, math

from response import aspire
from weightedlist import WeightedList as wl


def prime(num):
  if num == 2:
    return True
  elif num % 2 == 0 or num == 1:
    return False
  else:
    return all(num % i != 0 for i in range(3, 1 + int(num ** 0.5), 2))

def accuryze(guess, right, *, top, guesses = None):
  lx = lambda el = False: (wl((48, "."), (52, "!")) + wl((24, "..."))).select()
  right = int(right)
  dist = 20 * (right - int(guess)) / top
  dist = round(math.copysign(abs(dist) + math.log(top, 10), dist))

  sup = random.randint(1, 200)
  if sup >= 111:
    return aspire.wrong.select() + lx()
  if sup in range(1, 10) and right % 2 == 0:
    return "The number is even" + lx()
  elif sup in range(10, 20) and right % 2 == 1:
    return "The number is odd" + lx()
  elif sup in range(20, 25) and right % 3 > 0:
    return "The number is not divisible by 3" + lx()
  elif sup in range(25, 27) and right % 3 == 0:
    return "The number is divisible by 3" + lx()
  elif sup in range(50, 55) and not (math.sqrt(right)).is_integer():
    return "The number is not a square number" + lx()
  elif sup in [64, 81] and (math.sqrt(right)).is_integer():
    return "The number is a square number" + lx()
  elif sup in range(97, 101) and not prime(right):
    return "The number is not a prime number" + lx()
  elif sup in [97, 199] and prime(right):
    return "The number is a prime number" + lx()

  if 1 >= abs(dist):
    return "Almost!"
  if abs(dist) == 2:
    return random.choice(["Really", "Very"]) + " close" + lx(True)
  if abs(dist) == 3:
    return "Close" + lx()
  if 5 >= dist > 0:
    return "A bit higher" + lx()
  if 0 > dist >= -5:
    return "A bit lower" + lx()
  if 9 >= dist > 0:
    return "Much " + random.choice(["higher", "too low"]) + lx()
  if 0 > dist >= -9:
    return "Much " + random.choice(["lower", "too high"]) + lx()
  if abs(dist) > 24 and random.randint(1, 3) == 1:
    return "Nowhere near!"
  if dist >= 12:
    return "Way " + random.choice(["higher", "too low"]) + "!"
  if -12 >= dist:
    return "Way " + random.choice(["lower", "too high"]) + "!"
  if dist > 0:
    return random.choice(["Higher", "Too low"]) + lx()
  if dist < 0:
    return random.choice(["Lower", "Too high"]) + lx()