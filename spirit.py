from random import randint


games = []

def create(list, weight, item):
  list.append((item, weight))

def select(list):
  count = 0
  for item in list:
    count += item[1]
  select = randint(1, count)

  count = 0
  for item in list:
    count += item[1]
    if count >= select:
      return item[0]

def adventure():
  return select(games)


create(games, 20, "Penguin Dash")
create(games, 60, "Penguin Dash 2")
create(games, 20, "Hide and Sleet")
create(games, 20, "Capture the Krill")
create(games, 10, "Frozen Flurry")
create(games, 60, "Frozen Flurry 2")
create(games, 20, "Frozen Defence")
create(games, 10, "Yeti Hunt")
create(games, 20, "The Sacred Seals")