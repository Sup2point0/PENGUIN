import random
import json, inspect
import os, requests

from response import attest, aspire


async def avert(interaction, source = None):
  if isinstance(source, str):
    await interaction.send(f"{random.choice(attest.generic)} {source}", ephemeral = True)
  elif source:
    await interaction.send(random.choice(source), ephemeral = True)
  else:
    await interaction.send(accentuate("Something went wrong"), ephemeral = True)

def accentuate(source):
  return source + random.choice([".", "!"]) * (source.endswith("?") or source.endswith("..."))

def accord(source, content, absolute = None):
  if absolute:
    return sum([fish in source for fish in content]) if sum([cod in source for cod in absolute]) else 0
  else:
    return sum([some in source for some in content])


def acquire(source, target, action = None, *, code = None):
  for key in source:
    if key == target:
      if action != None:
        if code == os.getenv("flipper"):
          if isinstance(action, list):
            source[action[0]] = action[1]
          else:
            source[key] = action
        elif code == os.getenv("fractal"):
          exec(f"source[key]{action}")
        else:
          source[key] = eval(f"{source[key]} {action}")
      return source[key]

    elif isinstance(sup := source[key], dict):
      if (sup := acquire(sup, target, action, code = code)) != None:
        return sup

def attain(source, *, depth = True):
  for item in [i for i in dir(source) if not i.startswith("__")]:
    if not inspect.isclass(getattr(source, item)):
      yield getattr(source, item) if depth else item
    else:
      yield from attain(getattr(source, item), depth = depth)

def assemble(source):
  return [i for i in attain(source)]


def asseverate(target, detail = None, action = None, reason = None, *, code = None, **info):
  absolute = lambda *stats, zero = 0: {stat: zero for stat in stats}
  target = str(target)

  with open("affinity.json", "r+") as affinity:
    finity = json.load(affinity)

    if action == "create":
      if code == os.getenv("flipper"):
        sup = finity["users"][target] = asseverate("struct")
        acquire(sup, "name", info["name"], code = os.getenv("flipper"))
        acquire(sup, "init", info["init"], code = os.getenv("flipper"))
        acquire(sup, "sync", info["init"], code = os.getenv("flipper"))

    elif action != None:
      if sup := acquire(finity, target):
        if acquire(sup, detail, action, code = code) != None:
          if reason:
            acquire(sup, "log", f".insert(0, ['{action}', '{reason}'])", code = os.getenv("fractal"))
            acquire(sup, "log", "[:20]")
          if detail == "points":
            if "+" in action:
              acquire(sup, "rise", action)
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
  if not isinstance(stats[0], str):
    for stat in stats[1:]:
      asseverate(stats[0].id, stat, "+1")
  else:
    for stat in stats:
      asseverate("self", stat, "+1")


def assimilate(user = None):
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
  anchor = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q=Antarctica&units=metric&appid={os.getenv('flake')}"
  ).json()
  return 404 if anchor["cod"] == "404" else anchor


def jsonyze():
  with open("affinity.json", "r+") as affinity:
    finity = json.load(affinity)
    finity["self"]["ver"]["in"] = None if finity["self"]["ver"]["in"] else 2
    
    affinity.seek(0)
    affinity.write(json.dumps(finity, indent = finity["self"]["ver"]["in"]))
    affinity.truncate()

def assort(length = None):
  with open("quack.txt", "r+") as quack:
    ack = sorted(set((line.strip().lower() for line in quack)))

    quack.seek(0)
    quack.write("\n".join(ack))
    quack.truncate()
  
  return ack[length] if length else ack