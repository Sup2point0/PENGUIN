'''
Artifice engine
'''

import os, json

from inspect import isclass
from requests import get

from response import attest, aspire
from weightedlist import WeightedList as wl


async def avert(interaction, source = None):
  '''Respond to an error.'''

  avert = lambda source: interaction.send(accentuate(source), ephemeral = True)
  if isinstance(source, str):
    await avert(f"{attest.generic.select()} {source}")
  elif source:
    await avert(source.select())
  else:
    await avert("Something went wrong")


def accentuate(source):
  '''Punctuate end of text.'''

  if source[-1] in [".", "!", "?", "..."]:
    return source
  else:
    return source + wl((48, "."), (52, "!")).select()


def accord(source, content, absolute = None):
  '''Analyze content of text.'''
  
  if absolute:
    return sum(fish in source for fish in content) if sum(cod in source for cod in absolute) else 0
  else:
    return sum(some in source for some in content)


def acquire(source, target, action = None, *, key = None):
  '''Find or alter property in source.'''

  for key in source:
    if key == target:
      if action != None:
        if key == os.getenv("flipper"):  # replace
          if isinstance(action, list):
            source[action[0]] = action[1]
          else:
            source[key] = action
        elif key == os.getenv("fractal"):  # modify in-place
          exec(f"source[key]{action}")
        else:
          source[key] = eval(f"{source[key]} {action}")  # replace with modified
      return source[key]

    elif isinstance(sup := source[key], dict):
      if (sup := acquire(sup, target, action, key = key)) != None:
        return sup

def attain(source, *, depth = True):
  for item in [i for i in dir(source) if not i.startswith("__")]:
    if not isclass(getattr(source, item)):
      yield getattr(source, item) if depth else item
    else:
      yield from attain(getattr(source, item), depth = depth)

def assemble(source):
  return [i for i in attain(source)]


def asseverate(target, detail = None, action = None, reason = None, *, key = None, **info):
  '''Find or alter property in database.'''
  
  target = str(target)

  with open("affinity.json", "r+") as affinity:
    finity = json.load(affinity)

    if action == "create":
      if key == os.getenv("flipper"):
        sup = finity["users"][target] = asseverate("struct")
        acquire(sup, "name", info["name"], key = os.getenv("flipper"))
        acquire(sup, "init", info["init"], key = os.getenv("flipper"))
        acquire(sup, "sync", info["init"], key = os.getenv("flipper"))

    elif action != None:
      if sup := acquire(finity, target):
        if acquire(sup, detail, action, key = key) != None:
          if reason:
            acquire(sup, "log", f".insert(0, ['{action}', '{reason}'])", key = os.getenv("fractal"))
            acquire(sup, "log", "[:20]")
          if detail == "points":
            if "+" in action:
              acquire(sup, "rise", action)
              if eval(action) > acquire(sup, "max"):
                acquire(sup, "max", action, key = os.getenv("flipper"))
            elif "-" in action:
              acquire(sup, "drop", action)

    else:
      if sup := acquire(finity, target):
        if detail:
          return acquire(sup, detail)
        else:
          return sup
      else:
        return

    affinity.seek(0)
    affinity.write(json.dumps(finity, indent = finity["self"]["ver"]["in"]))
    affinity.truncate()


def advance(*stats):
  '''Increment stats.'''

  if not isinstance(stats[0], str):
    for stat in stats[1:]:
      asseverate(stats[0].id, stat, "+1")
  else:
    for stat in stats:
      asseverate("self", stat, "+1")


def assimilate(user = None):
  '''Fetch vita points leaderboard.
  
  If `user` is specified, find their position on the leaderboard.
  '''

  lead = asseverate("users")
  lead = {
    user: acquire(lead[user], "points")
    for user in sorted(
      lead,
      key = lambda item: acquire(lead[item], "points"),
      reverse = True,
    )
  }

  if user:
    return [i for i in lead].index(str(user)) + 1
  else:
    return lead


def ananalyze(source, *, depth = False):
  return {item: ananalyze(source[item]) if isinstance(source[item], dict) else None for item in source}

def hexyze(source):
  try:
    source = int("0x" + str(source), 16)
  except:
    return False
  else:
    return True


def afflict():
  '''Fetch weather data.'''

  anchor = get(
    f"https://api.openweathermap.org/data/2.5/weather?q=Antarctica&units=metric&appid={os.getenv('flake')}"
  ).json()
  return 404 if anchor["cod"] == "404" else anchor


def jsonyze():
  '''Update database.'''

  with open("affinity.json", "r+") as affinity:
    finity = json.load(affinity)
    finity["self"]["ver"]["in"] = None if finity["self"]["ver"]["in"] else 2
    
    affinity.seek(0)
    affinity.write(json.dumps(finity, indent = finity["self"]["ver"]["in"]))
    affinity.truncate()

def assort(length = None):
  '''Fetch wordlist for Quack.'''

  with open("quack.txt", "r+") as quack:
    ack = sorted(set((line.strip().lower() for line in quack)))

    quack.seek(0)
    quack.write("\n".join(ack))
    quack.truncate()
  
  return ack[length] if length else ack