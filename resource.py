from recog import item


class ancede:

  def act(command = None, init = False, ctx = None):
    if ctx:
      return f"used a context command{' for the first time' * init}"
    else:
      return f"used {f'`{command}`' if command else 'a command'}{' for the first time' * init}"

  def game():
    return "played a game"

  def secret(shard = "a secret shard"):
    return f"found {shard}"

  def crack(crypt = "a secret crypt"):
    return f"cracked {crypt}"


atavist = [{
  "vita points":         "points",
  "presence":            "live",
  "messages sent":       "sent",
  "reactions":           "react",
  "command activations": "act",
  "context commands":    "ctx",
  "errors raised":       "err",
  "restricted attempts": "acc",
  "games played":        "played",
  "highest position":    "top",
}, {
  "identity views":      "view",
  "lifetime points":     "rise",
  "lifetime lost":       "drop",
  "messages sent":       "sent",
  "reactions":           "react",
  "command activations": "act",
  "/help commands":      "/help",
  "/play commands":      "/play",
  "/vita commands":      "/vita",
  "direct messages":     "dir",
  "context commands":    "ctx",
  "errors raised":       "err",
  "restricted attempts": "acc",
  "games played":        "play",
  "games won":           "win",
  "games lost":          "lose",
  "games timed out":     "out",
  "whoosh moments":      "whoosh",
}]


atticate = [
  922420426175557632,
]


allocale = [{
  "Aventurina": "Aventurina District",
  "Ross City":  "Ross City, Aventurina",
  "Archadia":   "Archadia District",
  "Atalla":     "Atalla District",
  "Atla":       "Atla, Atalla",
  "Ascerta":    "Ascerta District",
  "Axona":      "Axona, Ascerta",
  "Aleta":      "Aleta, Ascerta",
  
  "Titeria":   "Titeria District",
  "Tyrestra":  "Tyrestra District",

  "Divelda":   "Divelda District",
  "Novada":    "Novada, Divelda",
  "Teneca":    "Teneca, Divelda",
  "Yena":      "Yena, Divelda",
  "Dessica":   "Dessica District",
  "Escharcha": "Escharcha, Dessica",
  "Panaxa":    "Panaxa, Dessica",
  "Discenda":  "Discenda District",
  "Vanqua":    "Vanqua, Discenda",
  "Helada":    "Helada, Discenda",
}, [
  "Rubicon Valley",
  "CARROT",
]]


aricept = [
  "Scott University", "Amundsen College", "Ross Academy",
  "NioTech", "ROAG", "Lakara",
  "Evelyn", "ISAB",
]


class advent:

  Year = item(
    title = "Antarctican New Year",
    caption = "Arteria Prime",
    decate = 93,
    content = """
    """,
  )

  Invict = item(
    title = "Invict Day",
    caption = "Vepida Prime",
    decate = 349,
    content = """
    """,
  )

  Discovery = item(
    title = "Discovery Day",
    caption = "Aeva 8",
    decate = 27,
    content = """
    """,
  )

  Tersolle = item(
    title = "Tersolle",
    caption = "Aeva 19",
    decate = 38,
    content = """
    """,
  )

  Falcon = item(
    title = "Falcon’s Noon",
    caption = "Verena 33",
    decate = 89,
    content = """
    """,
  )