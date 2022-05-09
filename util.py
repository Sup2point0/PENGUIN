from nextcord import Embed
from datetime import datetime
from textwrap import dedent

from weightedlist import WeightedList


line = "‾" * 20
pink = 0xf27281
grey = 0x464d59
home = 922420426175557632

decates = WeightedList(
  (37, "Arteria"), (36, "Vitida"),
  (37, "Arrikta"), (36, "Valia"),
  (37, "Aliquanda"), (36, "Verita"),
  (37, "Arteva"), (36, "Vepida"),
  (37, "Aeva"), (36, "Verena"),
)

alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


class icons:
  tick = "<:resTick:923155527696019476>"
  cross = "<:resCross:923155537296764929>"
  this = "<:resThis:925411693524316191>"
  
  up = "<:voteUp:922794109142450176>"
  none = "<:voteNone:922794146551439360>"
  down = "<:voteDown:922794121008128061>"

  sound = "<:icoSpeech:928691121708728390>"
  value = "<:icoSymbol:938538528122470440>"
  clock = "<:icoTime:938538551371505684>"

class menu:
  up = "<:uiArrowUp:964254558563991564>"
  down = "<:uiArrowDown:964254573076316190>"
  left = ""
  right = ""

  sync = "<:uiActionReload:964483722227384330>"
  tick = "<:uiActionTick:964479771566276608>"

  cryst = [
    "<:crystLL:947936646261768263>",
    "<:crystLR:947936658228121632>",
    "<:crystRL:947936671016550400>",
    "<:crystRR:947936682416676944>",
  ]


def avast(content, *, line = 1):
  return dedent(content).strip() + "\n\u200b" * line

def embed(source, fields = True, colour = True, struct = False):
  content = Embed(
    title = source.title,
    description = avast(f"""
      {f'''{source.caption}
      {line}''' if hasattr(source, "caption") else ""}
      {source.content}
    """, line = hasattr(source, "fields") if fields else False),
    colour = (
      pink if colour == True
      else colour if colour else grey
    )
  )

  if hasattr(source, "fields") and fields:
    for field in source.fields:
      content.add_field(
        name = f"{menu.cryst[0]}{menu.cryst[1]}  {field.title}  {menu.cryst[2]}{menu.cryst[3]}" if struct else field.title,
        value = avast(f"{line * 2}\n" * struct + field.content, line = True), inline = False
      )

  if hasattr(source, "surplus"):
    content.set_footer(text = source.surplus)
  elif hasattr(source, "other"):
    content.set_footer(text = f"See also: {source.other}")

  return content


def now():
  return datetime.now().timetuple()

def antect(day = None):
  if not day: day = datetime.now()
  idx = (day.timetuple().tm_yday + 273) % 365 + 1
  return decates[idx].value, idx

def display(unix):
  if unix / 86400 >= 1:
    if unix // 360 % 360 >= 0:
      return f"{int(unix // 86400)}d {int(unix // 3600 % 24)}h"
    return f"{int(unix // 86400)}d"
  elif unix / 60 >= 60:
    if unix // 60 % 60 > 0:
      return f"{int(unix // 3600)}h {int(unix // 60 % 60)} min"
    return f"{int(unix // 3600)}h"
  elif unix >= 60:
    return f"{int(unix // 60)} min"
  else:
    return "just a few seconds"