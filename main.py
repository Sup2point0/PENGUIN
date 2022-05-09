version = 28.2


import nextcord as discord
from nextcord import Embed as embed
from nextcord import SlashOption as pool
from nextcord import SelectOption as slot
from nextcord import ButtonStyle as style

from nextcord import ui
from nextcord.ui import View, Modal, button
from nextcord.ext import commands, tasks

import random, math
import json, textwrap
import time, datetime
import asyncio, os
import functools, copy

from vitals import huddle
from spirit import adventure

from recog import affluence
from recom import adept, ascept
from recon import ancest, assist, aspect, arcane
from recol import absorb, avail, attent, articept
from response import attest, aspire, accede, ascent

import recog
import artifice as arti
import resource as res
import util as uti
import astrix


penguin = commands.Bot(command_prefix = "~", intents = discord.Intents.all())
penguin.remove_command("help")

home = None
current = []



# points
def accumulate(act = 2, init = 20, call = None, *, ctx = None, req = 0):
  def activate(func):
    
    @ functools.wraps(func)
    async def wrap(interaction, *args, **kwargs):
      user = interaction.author if isinstance(interaction, commands.Context) else interaction.user
      arti.advance("rec")

      try:
        if req and arti.asseverate(user.id, "rise") < req:
          raise UserWarning
        
        await func(interaction, *args, **kwargs)

      except:
        arti.advance("err")
        arti.advance(user, "err")
        
        try:
          raise
        except commands.errors.MissingPermissions:
          await arti.avert(interaction, attest.restrict)
          arti.advance("acc")
          arti.advance(user, "acc")
        except NotImplementedError:
          await arti.avert(interaction, attest.future)
          arti.advance("acc")
          arti.advance(user, "acc")
        except UserWarning:
          await arti.avert(interaction, attest.require)
          arti.advance("acc")
          arti.advance(user, "acc")
        
        except:
          if not interaction.response.is_done():
            await arti.avert(interaction)
        finally:
          raise
      
      arti.advance("act")
      arti.advance(user, "act")
      if ctx:
        arti.advance("ctx")
        arti.advance(user, "ctx")

      if arti.asseverate(user.id):
        first = call not in arti.asseverate(user.id, "used")
      else:
        first = None
      if first:
        arti.asseverate(user.id, "used", f"+['{call}']")
      
      if isinstance(interaction, discord.Interaction):
        if (sup := init if first else act):
          arti.asseverate(user.id, "points", f"+{sup}", reason = res.ancede.act(call, init = first), ctx = ctx)
        
    return wrap
  return activate
  

# expand
def expand(id):
  @ discord.ui.button(label = "Expand", emoji = uti.menu.down, style = style.blurple, custom_id = id)
  async def size(self, button, interaction):
    if self.state:
      self.state = False
      button.label = "Expand"
      button.emoji = uti.menu.down
      content = copy.deepcopy(self.content)
      if len(self.content.description) < 4:
        content.fields = content.fields[0]
      else:
        content.clear_fields()
    else:
      self.state = True
      button.label = "Collapse"
      button.emoji = uti.menu.up
      content = self.content
    
    await interaction.edit(embed = content, view = self)

  return size

# update
def update(id, source):
  @ discord.ui.button(label = "Update", emoji = uti.menu.sync, style = style.blurple, custom_id = id)
  async def sync(self, button, interaction):
    try:
      self.content = source()
    except:
      await arti.avert(interaction)
      return

    if self.state:
      content = self.content
    else:
      content = copy.deepcopy(self.content)
      content.clear_fields()
    button.emoji = uti.menu.tick
    await interaction.edit(embed = content, view = self)
    
    await asyncio.sleep(2)
    button.emoji = uti.menu.sync
    await interaction.edit(view = self)
  
  return sync
  

# wakening
@ penguin.event
async def on_ready():
  await swim(None)
  arti.assort()
  
  global home, version
  home = penguin.get_guild(922420426175557632)
  if arti.asseverate("self", "sub") != version:
    arti.asseverate("self", "sub", version, code = os.getenv("flipper"))
    arti.asseverate("self", "up", round(time.time()), code = os.getenv("flipper"))
  version = f"{arti.asseverate('self', 'sup')}.{version}"
  
  arti.advance("res")
  print("Penguin's woken up!")

  # act = lambda view: self.add_item(view)
  # act(await stuff(None))
  # act(await start(None))
  # act(await command(None))
  # act(await cast(None))
  # act(await cal(None))


# ping
@ penguin.command()
@ accumulate(1, 1, "~ping")
async def ping(ctx):
  sup = False
  if time.time() - arti.asseverate("self", "pong") > random.randrange(1200, 7500, 300):
    if random.randint(1, 12) == 12:
      sup = random.randint(2, 20)
      arti.asseverate(ctx.author, "points", f"+{sup}", "pinged a lucky ping")
      sup = True
  
  await ctx.channel.send(random.choice(accede.affirm[int(sup)]))
  arti.advance("ping")
  arti.asseverate("self", "pong", round(time.time()), code = os.getenv("flipper"))



# help (root)
@ penguin.slash_command()
async def help(interaction):
  pass


# info and about
@ help.subcommand(description = "all about me!")
@ accumulate(1, 10, "/help info")
async def info(interaction):
  await interaction.send(ephemeral = True, embed = embed(title = "About Me", description = uti.avast(f"""
    Help and Info
    {uti.line}
    Hey, I’m PENGUIN! Your playful & energetic new general utility & information network bot, though you can just call me Penguin.

    I can tell you all about Antarctica, play games, and so much more!

    Need help getting started? You can use `/help start` to see what things to try out first, or `/help all` to find out what I can do!
  """, line = 0), colour = uti.pink).set_footer(text = f"Updated as of v{version}"))
  

# all commands
@ help.subcommand("all", description = "see what I can do")
@ accumulate(1, 10, "/help all")
async def stuff(interaction, category: int = pool(description = "pick a specific category of commands", choices = {
  "/help ...": 0, "/util ...": 1, "/index ...": 2, "/info ...": 3, "/play ...": 4, "/vita ...": 5,
}, required = False)):
  content = uti.embed(avail.help.fields[category] if category else avail.help).set_footer(text = f"Updated as of v{version}")
  
  class visual(View):
    def __init__(self):
      super().__init__(timeout = None)
      self.state = False
      self.content = content

    expand = expand("stxp.hpal")

  if interaction is None: return visual()
  await interaction.send(embed = content, view = None if category else visual(), ephemeral = True)


# where to start
@ help.subcommand(description = "help getting started")
@ accumulate(1, 10, "/help start")
async def start(interaction):
  content = uti.embed(avail.start).set_footer(text = f"Updated as of v{version}")

  class visual(View):
    def __init__(self):
      super().__init__(timeout = None)
      self.state = False
      self.content = content

    expand = expand("stxp.hpst")

  if interaction is None: return visual()
  await interaction.send(embed = content, view = visual(), ephemeral = True)


# specific command help
@ help.subcommand(description = "detailed & extensive help with a specific command")
@ accumulate(call = "/help command")
async def command(interaction, command = pool(description = "pick a command, or find out about a random command", required = False)):
  if command:
    query = command.lower()
    query = query[int(query[0] not in uti.alpha):]
    query = query.split()[-1]
    if query not in arti.attain(adept, depth = False):
      await arti.avert(interaction, attest.index)
      return
    item = [i for i in arti.attain(adept, depth = False)].index(query)
    item = arti.assemble(adept)[item]
  else:
    item = random.choice(arti.assemble(adept))

  content = uti.embed(item)

  class visual(View):
    def __init__(self):
      super().__init__(timeout = None)
      self.state = False
      self.content = content

    expand = expand("stxp.hpcd")

  if interaction is None: return visual()
  await interaction.send(embed = content, view = visual(), ephemeral = True)

# autofill
@ command.on_autocomplete("command")
async def fill_command(interaction, query):
  full = [i.title for i in arti.attain(adept)]
  if query and not query == "/":
    query = query.lower()[int(query.startswith("/")):]
    fill = [i for i in full if i[int(i.startswith("/")):].startswith(query)]
    if len(fill) < 5 and len(query) >= 3:
      fill += [i for i in full if query in i and i not in fill]
    await interaction.response.send_autocomplete(fill[:12])
  else:
    await interaction.response.send_autocomplete(random.sample(full, 12))


# tips
@ help.subcommand(description = "tells you a random helpful tip")
@ accumulate(call = "/help tip")
async def tip(interaction):
  await interaction.send(random.choice(assist))



# status timings
@ penguin.command()
async def dinnertime(ctx):
  global last, next
  now = time.time()
  await ctx.channel.send(
    f"I'll play for {int((next - (now - last)) / 60)} more minutes! (and {(next - int(now - last)) % 60} seconds)")
  
def reset():
  global last, next
  last = time.time()
  next = random.randint(2, 20) * 60

# status switch
@ penguin.command()
async def swim(ctx, state = "play", status = None, chance = 1):
  if random.randint(1, chance) != chance:
    return

  if state == "play":
    await penguin.change_presence(activity = discord.Game(name = (status if status else adventure())))
  elif state == "watch":
    await penguin.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = status))
  elif state == "listen":
    await penguin.change_presence(activity = discord.Activity(type = discord.ActivityType.listening, name = status))
  
  reset()
  if ctx: await ctx.message.add_reaction(uti.icons.tick)
  arti.advance("stas")



# utility (root)
@ penguin.slash_command()
async def util(interation):
  pass


# weather forecast
@ util.subcommand(description = adept.util.cast.desc.full)
@ accumulate(4, 40, "/util cast")
async def cast(interaction, detail = pool(description = "pick a specific detail of the forecast", choices = [
  "temperature", "pressure", "humidity", "visibility",
], required = False)):
  if (cast := arti.afflict()) == 404:
    await arti.avert(interaction, "fetching the data")
    return

  if detail:
    if detail == "temperature":
      await interaction.send(f"It's currently {round(cast('temp') + random.uniform(-0.2, 0.2), 1)}°C!")
    elif detail == "pressure":
      await interaction.send(f"")
    elif detail == "humidity":
      await interaction.send(f"")
    elif detail == "visibliity":
      await interaction.send(f"")
    elif detail == "debug json":
      await interaction.send(f"""```json
        {json.dumps(cast, indent = 2).strip()}
      ```""", ephemeral = True)
    return

  try:
    decate = uti.antect()

    def content():
      cast = arti.afflict()
      cast = lambda detail: arti.acquire(cast, detail)
      return (embed(title = "Weather Forecast", description = uti.avast(f"""
        {decate[0]} {decate[1]}
        {uti.line}
        Quite cold today, unsurprisingly.
      """), colour = uti.pink)
      .add_field(name = "Temperature", value = uti.avast(f"""
        Current: {round(cast("temp") + random.uniform(-0.2, 0.2), 1)}°C
        Feels Like: {round(cast("feels_like") + random.uniform(-0.2, 0.2), 1)}°C
      """), inline = False)
      .add_field(name = "Atmosphere", value = uti.avast(f"""
        Pressure: {cast("pressure") + random.randint(-2, 2)} hPa
        Humidity: {cast("humidity")}%
        Visibility: {round(cast("visibility") / 1000 + random.uniform(-0.1, 0.1), 1)} km
      """), inline = False)
      .add_field(name = "Wind", value = uti.avast(f"""
        Speed: {round(cast("speed") * 2.23694 + random.uniform(-0.2, 0.2), 1)} mph
        Direction: {cast("deg")}°
      """), inline = False)
      .add_field(name = "Day", value = uti.avast(f"""
        Sunrise: <t:{cast("sunrise")}:T>
        Sunset: <t:{cast("sunset")}:T>
        \n{uti.line}
      """, line = 0), inline = False)
      .set_thumbnail(url = "https://cdn.discordapp.com/attachments/925419481205968916/939910472067579914/Suncloud.png")
      .set_footer(text = "Data from OpenWeatherMap.org")
      )

    class visual(View):
      def __init__(self):
        super().__init__(timeout = None)
        self.state = False
        self.content = content()

      expand = expand("stxp.utcs")
      update = update("dysy.utcs", content)

      @ button(label = "View Detail", style = style.blurple, custom_id = "stcsdt")
      async def stat(self, button, interaction):
        pass

    if interaction is None: return visual()
    await interaction.send(embed = content(), view = visual())

  except:
    await arti.avert(interaction, "with the embed")
    raise


# convert current
@ util.subcommand(description = adept.util.decate.desc.full)
@ accumulate(call = "/util decate")
async def decate(interaction):
  decate = uti.antect()
  await interaction.send(f"Today's {decate[0]} {decate[1]}!")

# convert date
@ util.subcommand(description = adept.util.antect.desc.full)
@ accumulate(init = 25, call = "/util antect")
async def antect(interaction, month: int = pool(description = "month", choices = {
  "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12,
}, required = True),
day: int = pool(description = "date", min_value = 1, max_value = 31, required = True)):
  try:
    day = datetime.date(42, month, day)
  except:
    await arti.avert(interaction, attest.date)
    raise
  decate = uti.antect(day)
  await interaction.send(f"That would be {decate[0]} {decate[1]}!")


# calendar
@ util.subcommand(description = adept.util.cal.desc.full)
@ accumulate(3, 30, "/util cal")
async def cal(interaction):
  def content():
    events = sorted(arti.attain(res.advent), key = lambda event: event.decate)
    events = [i for i in events if i.decate >= uti.now().tm_yday] + [i for i in events if i.decate < uti.now().tm_yday]

    return uti.embed(recog.item(title = "Events Calendar", content = "", fields = [
      recog.item.field(event.title, uti.avast(f"""
        {event.caption}
        {uti.line}
        {event.content}
      """, line = 0)) for event in events
    ])).set_footer(text = f"Showing {len(events)} events")

  class visual(View):
    def __init__(self):
      super().__init__(timeout = None)
      self.state = False
      self.content = content()

    expand = expand("stxp.utcl")
    update = update("stsy.utcl", content)
  
  if interaction is None: return visual()
  await interaction.send(embed = content(), view = visual())


# suggestion
@ util.subcommand(description = adept.util.idea.desc.full)
@ accumulate(3, 25, "/util idea")
async def idea(interaction, title, idea,
  category = pool(description = "pick a category to help organyze ideas", choices = [
    "addition", "modification", "server", "rank", "lore", "Penguin", "game"
  ], required = False, default = "uncategoryzed"),
  anonymous = pool(description = "submit an anonymous idea", choices = {"enabled": "True"}, required = False, default = "False")
):
  content = embed(title = title, description = idea,
    colour = sup if (sup := int("0x" + arti.asseverate(interaction.user.id, "col"), 16)) != 0x2070c1 else uti.pink
  ).set_footer(text = category.capitalize())
  ###
  if not eval(anonymous):
    content.set_author(name = f"Idea from {interaction.user.display_name}", icon_url = interaction.user.avatar.url)

  try:
    root = await penguin.get_channel(944638572789628978).send(embed = content)
  except:
    await arti.avert(interaction, "submitting the idea!")
    raise
  await interaction.send(f"{uti.icons.tick} Idea successfully submitted!", ephemeral = True)

  rise = await root.create_thread(name = "Idea Discussion", auto_archive_duration = 1440)
  join = await rise.send(interaction.user.mention)
  await join.delete()

  await root.add_reaction(uti.icons.up)
  await root.add_reaction(uti.icons.none)
  await root.add_reaction(uti.icons.down)


# dictionary
@ util.subcommand(description = adept.util.dict.desc.full)
@ accumulate(init = 25, call = "/util define")
async def define(interaction, word):
  class visual(View):
    def __init__(self):
      super().__init__(timeout = None)
      self.state = False
      self.content = ...

    expand = expand("stxp.utdf")

  if interaction is None: return visual()

  if word not in affluence:
    await arti.avert(interaction, attest.index)

  await interaction.send(embed = uti.embed(affluence[word]), view = visual())



# index (root)
@ penguin.slash_command()
async def index(interaction):
  pass

lt = lambda item: ancest[item].value
ls = lambda item: lt(item).alias if hasattr(lt(item), "alias") else item
lx = lambda item: lt(item).index


# view index
@ index.subcommand(description = adept.index.view.desc.full)
@ accumulate(call = "/index view")
async def view(interaction):
  index = [ls(i) for i in sorted(ancest) if lx(i)]
  idx = len(index)

  class visual(View):
    def __init__(self):
      super().__init__(timeout = None)
      self.state = False

    expand = expand("stxp.idxv")
  
  if interaction is None: return visual()
  await interaction.send(embed = embed(title = "Index", description = "\n".join(index), colour = uti.grey
    ).set_footer(text = f"{idx} item{'s' * (idx != 1)} {'found' * (idx == 0)}"), view = visual())


# filter index
@ index.subcommand(description = adept.index.filter.desc.full)
@ accumulate(3, 25, "/index filter")
async def filter(interaction, sort = pool("by", description = "option to filter the index by", choices = ["letter", "content", "category", "tag"], required = True), target = pool("with", description = "the value to filter with", required = True)):
  index = sorted(ancest)

  if sort == "letter":
    target = target[0].upper()
    index = [ls(i) for i in index if lx(i) and i.startswith(target)]
    sort = f"Index – {target}"
  elif sort == "content":
    index = [ls(i) for i in index if lx(i) and (target.upper() in lt(i).title.upper() or target.upper() in lt(i).caption.upper())]
    sort = f"Search – ‘{target}’"
  elif sort == "category":
    index = [ls(i) for i in index if lx(i)]
    sort = f"Category – {target}"
  elif sort == "tag":
    index = [ls(i) for i in index if lx(i) and (target.upper() in lt(i).tags.upper() if hasattr(lt(i), "tags") else False)]
    sort = f"Tagged – ‘{target}’"

  class visual(View):
    def __init__(self):
      super().__init__(timeout = None)
      self.state = False

    expand = expand("stxp.dxft")

  if interaction is None: return visual()
  
  idx = len(index)
  await interaction.send(embed = embed(title = sort, description = "\n".join(index), colour = uti.grey
    ).set_footer(text = f"{idx} item{'s' * (idx != 1)} {'found' * (idx == 0)}"), view = visual())


# games index
@ index.subcommand(description = adept.index.games.desc.full)
@ accumulate(call = "/index games")
async def games(interaction):
  class visual(View):
    def __init__(self):
      super().__init__(timeout = None)
      self.state = False

    expand = expand("stxp.dxpl")

  if interaction is None: return visual()
  await interaction.send(embed = uti.embed(avail.games), view = visual())



# info (root)
@ penguin.slash_command()
async def info(interaction):
  pass


# fun fact
@ info.subcommand(description = adept.info.fact.desc.full)
@ accumulate(act = "/info fact")
async def fact(interaction):
  await interaction.send(random.choice(aspect))


# about
@ info.subcommand(description = adept.info.about.desc.full)
@ accumulate(init = 25, call = "/info about")
async def about(interaction, item = pool(description = "pick an item to lookup, or find out about a random item", required = False)):
  if item:
    target = " ".join([i.capitalize() for i in item.split()])
    if not target in ancest:
      if target.upper() in ancest:
        target = target.upper()
      else:
        await interaction.send(random.choice(attest.index).format(item), ephemeral = True)
        return
  else:
    target = random.choice(list(ancest.keys()))
  item = ancest[target].value

  try:
    content = uti.embed(item)
    if hasattr(item, "url"):
      content.set_thumbnail(url = item.url)

    class visual(View):
      def __init__(self):
        super().__init__(timeout = None)
        self.state = False
        self.content = content
      
      expand = expand("stxp.info")

    if interaction is None: return visual()
    await interaction.send(embed = content, view = visual())
  
  except:
    await arti.avert(interaction, "with the embed.")
    raise

# autofill
@ about.on_autocomplete("item")
async def fill_about(interaction, query):
  if query:
    await interaction.response.send_autocomplete([
      ls(i) for i in sorted(ancest.keys()) if lx(i)
      and (lt(i).alias if hasattr(lt(i), "alias") else lt(i).title)
      .upper().startswith(query.upper())
    ][:12])
  else:
    await interaction.response.send_autocomplete(random.sample([
      ls(i) for i in ancest.keys() if lx(i)], 12))


# acronym
@ info.subcommand(description = adept.info.acro.desc.full)
@ accumulate(call = "/info acro")
async def acro(interaction, acronym = pool(description = "pick an acronym to lookup, or find out what a random acronym stands for", required = False)):
  if not acronym:
    acronym = random.choice([i for i in ancest if lx(i) and i.isupper()])

  if acronym.upper() in ancest:
    acro = lt(acronym.upper())
    acro = acro.acro if hasattr(acro, "acro") else acro.title
  else:
    await arti.avert(interaction, attest.index)
    raise

  await interaction.send(f"{acronym.upper()}: {acro}.")

# autofill
@ acro.on_autocomplete("acronym")
async def fill_acro(interaction, acronym):
  if acronym:
    acro = acronym.upper()
    fill = [i for i in ancest if lx(i) and i.isupper() and i.startswith(acro)]
    if len(fill) < 5 and len(acro) >= 3:
      fill += [i for i in ancest if lx(i) and acro in i and i not in fill]
    await interaction.response.send_autocomplete(fill[:12])
  else:
    await interaction.response.send_autocomplete(random.sample([
      ls(i) for i in ancest.keys() if lx(i) and i.isupper()], 12))


# role info
@ info.subcommand(description = adept.info.role.desc.full)
@ accumulate(call = "/info role")
async def role(interaction, role: discord.Role = pool(description = "pick a role, or find out about a random role")):
  if role.name in ascept:
    content = uti.embed(ascept[role.name], colour = home.get_role(role.id).colour)

    class visual(View):
      def __init__(self):
        super().__init__(timeout = None)
        self.state = False
        self.content = content
        
    if interaction is None: return visual()
    wait interaction.send(embed = content, view = visual())
  
  else: await arti.avert(interaction, attest.index)


# game info
@ info.subcommand(description = adept.info.game.desc.full)
@ accumulate(init = 25, call = "/info game")
async def game(interaction, game = pool(description = "pick a game, or find out about a random game", choices = {absorb[i].title: i for i in absorb}, required = False)):
  if not game:
    game = random.choice(list(absorb.keys()))
  content = uti.embed(absorb[game])
  await interaction.send(embed = content)



# play (root)
@ penguin.slash_command()
async def play(interation):
  pass

async def wait(interaction, type, thread, dur):
  try:
    out = await penguin.wait_for(type, timeout = dur, check = (
      lambda check: check.author == interaction.user and check.channel == thread))
  except asyncio.TimeoutError:
    return
  return out


# guessing games
@ play.subcommand()
async def guess(interaction):
  pass

# guess the number
@ guess.subcommand(description = adept.play.guess.num.desc.full)
@ accumulate(0, 0, "/play guess num")
async def num(interaction, top: int = pool("range", description = "the secret number will be between 1 and this number – the higher, the more points available", min_value = 4, required = True)):
  class visual(View):
    def __init__(self):
      super().__init__(timeout = None)
      self.start()

    @ button(label = "End", style = style.red, custom_id = "acplgn")
    async def end(self, button, interaction):
      self.label = "Ended"
      self.style = style.grey
      await interaction.edit(view = self)
      self.stop()

  if interaction is None:
    return visual()

  if isinstance(interaction.channel, discord.Thread):
    await arti.avert(interaction, aspire.thread)
  elif isinstance(interaction.channel, discord.DMChannel):
    await arti.avert(interaction, aspire.direct)
  
  global current
  if "num" in current:
    await arti.avert(interaction, aspire.play)
    return
  current.append("num")
  
  arti.advance(interaction.user, "play")
  if not "num" in arti.asseverate(interaction.user.id, "played"):
    arti.asseverate(interaction.user.id, "played", "+['num']")

  class game:
    state = None
    answer = str(random.randint(1, top))
    tries = round(math.log(top / 2, 10) * math.pi ** 2)
    left = tries
    points = math.log(top - math.e, 2) * 69 - random.randint(20, 42)
    log = []
  ###
  content = (embed(title = "Guess the Number", description = uti.avast(f"""
    Random number between 1 and {top}
    {round(game.points)} points available
    {game.left} guesses remaining
  """, line = 0), colour = uti.pink)
  .set_footer(text = "Initialyzing")
  .set_author(name = f"Game with {interaction.user.display_name}", icon_url = interaction.user.avatar.url)
  )

  await interaction.send(embed = content)
  root = await interaction.original_message()
  rise = await root.create_thread(name = "Guess the Number", auto_archive_duration = 60)

  join = await rise.send(interaction.user.mention)
  await join.delete()
  content.set_footer(text = "Ongoing")

  for i in range(game.tries):
    if not (guess := await wait(interaction, "message", rise, 20)):
      await rise.send(random.choice(aspire.wait))
      if not (guess := await wait(interaction, "message", rise, 120)):
        await rise.send(random.choice(aspire.time))
        game.state = False
        break

    guess = guess.content
    if guess.lower() in ["exit", "end"]:
      game.state = False
      break

    if "." in guess:
      await rise.send(random.choice(aspire.number[1]))
    elif not guess.isdigit():
      await rise.send(random.choice(aspire.number[0]))
    elif guess in game.log:
      await rise.send(random.choice(aspire.done))

    else:
      game.left -= 1
      game.log.append(guess)
      
      if guess == game.answer:
        await rise.send(random.choice(aspire.right))

        content.description = uti.avast(f"""
          Random number between 1 and {top}
          {round(game.points)} points rewarded
          {f'{game.tries - game.left} guesses used' if {game.tries - game.left} != 1 else 'First try'}
          
          Guessed: {", ".join([f"`{i}`" for i in game.log])}
          Answer: {game.answer}
        """, line = 0)

        await rise.send(f"You won {round(game.points)} points!")
        arti.asseverate(interaction.user.id, "points", f"+{round(game.points)}", f"Won Guess the Number in {game.tries - game.left} tries")
        arti.advance(interaction.user, "win")
        game.state = True
        break

      else:
        await rise.send(astrix.accuryze(guess, game.answer, top = top))
        game.points *= 0.92

        content.description = uti.avast(f"""
          Random number between 1 and {top}
          {round(game.points)} points available
          {game.left} guesses remaining

          Guesses: {", ".join([f"`{i}`" for i in game.log])}
        """, line = 0)
        await root.edit(embed = content)
  
  else:
    content.description = uti.avast(f"""
      Random number between 1 and {top}
      {round(game.points)} points available
      Ran out of guesses
  
      Guessed: {", ".join([f"`{i}`" for i in game.log])}
          Answer: {game.answer}
    """, line = 0)
    await root.edit(embed = content)

  if game.state == False:
    content.set_footer(text = "Timed Out")
    await root.add_reaction(uti.icons.clock)
  elif game.state:
    content.set_footer(text = "Finished")
    await root.add_reaction(uti.icons.tick)
    arti.advance(interaction.user, "lose")
  else:
    content.set_footer(text = "Ended")
    await root.add_reaction(uti.icons.cross)
    arti.advance(interaction.user, "out")

  await root.edit(embed = content)
  await rise.edit(archived = True, locked = True)
  current.remove("num")


# guess the reaction
@ guess.subcommand(description = adept.play.guess.emoji.desc.full)
@ accumulate(0, 0, "/play guess emoji")
async def emoji(interaction, difficulty = pool(description = "determines how hard the emoji may be to find – the higher, the more points available!", choices = ["easy", "normal", "medium", "hard", "extreme", "pro", "impossible"], required = True)):
  if isinstance(interaction.channel, discord.Thread):
    await arti.avert(interaction, aspire.thread)
  elif isinstance(interaction.channel, discord.DMChannel):
    await arti.avert(interaction, aspire.direct)
  
  global current
  if "emoji" in current:
    await arti.avert(interaction, aspire.play)
    return
  current.append("emoji")
  
  arti.advance(interaction.user, "play")
  if not "emoji" in arti.asseverate(interaction.user.id, "played"):
    arti.asseverate(interaction.user.id, "played", "+['emoji']")

  class game:
    state = None
    answer = random.choice([i.id for i in home.emojis])
    tries = 10
    left = tries
    points = 100
    log = []
  ###
  content = (embed(title = "Guess the Emoji", description = uti.avast(f"""
    {difficulty.capitalize()} difficulty
    {round(game.points)} points available
    {game.left} guesses remaining
  """, line = 0), colour = uti.pink)
  .set_footer(text = "Initialyzing")
  .set_author(name = f"Game with {interaction.user.display_name}", icon_url = interaction.user.avatar.url)
  )
  
  await interaction.send(embed = content)
  root = await interaction.original_message()
  rise = await root.create_thread(name = "Guess the Emoji", auto_archive_duration = 60)

  join = await rise.send(interaction.user.mention)
  await join.delete()
  content.set_footer(text = "Ongoing")

  for i in range(game.tries):
    if not (guess := await wait(interaction, "message", rise, 20)):
      await rise.send(random.choice(aspire.wait))
      if not (guess := await wait(interaction, "message", rise, 120)):
        await rise.send(random.choice(aspire.time))
        game.state = False
        break

    if guess.content.lower() in ["exit", "end"]:
      game.state = False
      break

    try:
      guess = await commands.PartialEmojiConverter().convert(await penguin.get_context(guess), guess.content)
    except commands.PartialEmojiConversionFailure:
      await rise.send(random.choice(aspire.emoji[0]))
      continue
    
    if guess.id in [i.id for i in game.log]:
      await rise.send(random.choice(aspire.done))

    else:
      game.left -= 1
      game.log.append(guess)
      
      if guess.id == game.answer:
        await rise.send(random.choice(aspire.right))

        content.description = uti.avast(f"""
          {difficulty.capitalize()} difficulty
          {round(game.points)} points rewarded
          {f'{game.tries - game.left} guesses used' if {game.tries - game.left} != 1 else 'First try'}
          
          Guessed: {" ".join(str(i) for i in game.log)}
          Answer: {game.answer}
        """, line = 0)

        await rise.send(f"You won {round(game.points)} points!")
        arti.asseverate(interaction.user.id, "points", f"+{round(game.points)}", f"Won Guess the Emoji in {game.tries - game.left} tries")
        arti.advance(interaction.user, "win")
        game.state = True
        break

      else:
        await rise.send(random.choice(aspire.wrong))
        game.points *= 0.92

        content.description = uti.avast(f"""
          {difficulty.capitalize()} difficulty
          {round(game.points)} points available
          {game.left} guesses remaining

          Guesses: {" ".join(str(i) for i in game.log)}
        """, line = 0)
        await root.edit(embed = content)
  
  else:
    content.description = uti.avast(f"""
      {round(game.points)} points available
      Ran out of guesses
  
      Guessed: {", ".join(str(i) for i in game.log)}
      Answer: {game.answer}
    """, line = 0)
    await root.edit(embed = content)
  
  if game.state == False:
    content.set_footer(text = "Timed Out")
    await root.add_reaction(uti.icons.clock)
  elif game.state:
    content.set_footer(text = "Finished")
    await root.add_reaction(uti.icons.tick)
    arti.advance(interaction.user, "lose")
  else:
    content.set_footer(text = "Ended")
    await root.add_reaction(uti.icons.cross)
    arti.advance(interaction.user, "out")

  await root.edit(embed = content)
  await rise.edit(archived = True, locked = True)
  current.remove("emoji")


# # react
# @ play.subcommand(description = adept.play.react.desc.full)
# async def react(interaction, difficulty = pool(description = "difficulty", choices = ["easy", "normal", "medium", "hard", "extreme", "pro", "impossible"], required = True), reactions: int = pool(description = "the number of reactions you’ll need to react with – the higher, the more points up for grabs!", min_value = 2, max_value = 20, required = True)):
#   raise NotImplementedError


# # flick
# @ play.subcommand(description = adept.play.flick.desc.full)
# async def flick(interaction, difficulty = pool(description = "determines how obscure the twist may be – the higher, the more points up for grabs!", choices = ["1", "2", "3"], required = True)):
#   raise NotImplementedError


# # rush
# @ play.subcommand(description = adept.play.rush.desc.full)
# async def rush(interaction, layers: int = pool(description = "the number of layers of spoilered emojis – the higher, the more points up for grabs!", min_value = 2, max_value = 20, required = True)):
#   raise NotImplementedError


# # spam
# @ play.subcommand(description = adept.play.spam.desc.full)
# async def spam(interaction):
#   raise NotImplementedError


# quack
@ play.subcommand(description = adept.play.quack.desc.full)
@ accumulate(0, 0, "/play quack")
async def quack(interaction, letters: int = pool(description = "the number of letters the word will contain – if you pick too high, you’ll win fewer points!", min_value = 3, max_value = 12, required = True)):
  raise NotImplementedError
  
  global current
  if "quack" in current:
    await arti.avert(interaction, attest.play)
    return
  current.append("quack")

  class game:
    state = None
    answer = random.choice(arti.assort(letters))
    tries = None
    left = tries
    points = None
    log = []


# # knowledge
# @ play.subcommand(description = adept.play.know.desc.full)
# async def know(interaction):
#   raise NotImplementedError


# # count
# @ play.subcommand(description = adept.play.count.desc.full)
# async def count(interaction, quirk: bool = pool(description = "a random quirk to make counting harder – granting a point multiplier!", required = False)):
#   raise NotImplementedError


# # shardhunter
# @ play.subcommand(description = adept.play.hunt.desc.full)
# async def hunt(interaction, depth = pool(description = "how in-depth the game will develop – the greater, the more points rewarded upon completion!", choices = ["1", "2", "3"], required = True)):
#   raise NotImplementedError


# # cryptcracker
# @ play.subcommand(description = adept.play.crypt.desc.full)
# async def crypt(interaction, depth = pool(description = "how in-depth the game will develop – the greater, the more points rewarded upon completion!", choices = ["1", "2", "3"], required = True)):
#   raise NotImplementedError


# # quest
# @ play.subcommand(description = adept.play.quest.desc.full)
# async def quest(interaction, depth = pool(description = "coming soon", choices = ["1", "2", "3"], required = True)):
#   raise NotImplementedError


# # excursion
# @ play.subcommand(description = adept.play.excursion.desc.full)
# async def excursion(interaction, depth = pool(description = "coming soon", choices = ["1", "2", "3"], required = True)):
#   raise NotImplementedError



# account (root)
@ penguin.slash_command(guild_ids = [uti.home])
async def vita(interation):
  pass

def aliate(identity):
  try:
    if identity == "self":
      self = arti.asseverate("self")
      update = uti.antect(datetime.datetime.fromtimestamp(arti.acquire(self, "up")))

      content = embed(
        title = "PENGUIN",
        description = uti.avast(f"""
          Version {version}
          {uti.line}
          Last updated {update[0]} {update[1]}
          {uti.icons.clock} {uti.display(time.time() - arti.acquire(self, "up"))} ago
        """),
      colour = uti.pink)

      content.add_field(name = "Stats", value = uti.avast(f"""
        {arti.acquire(self, "sent")} messages
        {arti.acquire(self, "react")} reactions
        {arti.acquire(self, "res")} restarts
        {arti.acquire(self, "ping")} pings
        {arti.acquire(self, "stas")} status switches
        {uti.display(arti.acquire(self, "live"))} uptime
        """, line = 1),
      inline = False)

      content.add_field(name = "Global", value = uti.avast(f"""
        {arti.acquire(self, "mes")} messages received
        {arti.acquire(self, "dir")} direct messages received
        {arti.acquire(self, "rec")} command invocations received
        {arti.acquire(self, "act")} commands succesfully activated
        {arti.acquire(self, "ctx")} context commands activated
        {arti.acquire(self, "err")} errors raised
        {arti.acquire(self, "acc")} restricted attempts
        {sum([arti.asseverate(user, "rise") for user in arti.asseverate("users")])} lifetime vita points
        {uti.display(sum([arti.asseverate(user, "live") for user in arti.asseverate("users")]))} lifetime presence
        """, line = 1),
      inline = False)

      content.add_field(name = "Commands", value = uti.avast(f"""
        {arti.acquire(self, "help")} `/help` commands used
        {arti.acquire(self, "util")} `/util` command used
        {arti.acquire(self, "index")} `/index` commands used
        {arti.acquire(self, "info")} `/info` commands used
        {arti.acquire(self, "play")} `/play` command used
        {arti.acquire(self, "vita")} `/vita` commands used

        {sum(arti.asseverate(user, "play") for user in arti.asseverate("users"))} games played
        {sum(arti.asseverate(user, "win") for user in arti.asseverate("users"))} games won
        {sum(arti.asseverate(user, "lose") for user in arti.asseverate("users"))} games lost
        {arti.acquire(self, "jokes")} jokes told
        """, line = 1),
      inline = False)

      content.add_field(name = "Discovies", value = uti.avast(f"""
        {sum(len(arti.asseverate(user, "shards")) for user in arti.asseverate("users"))} shards discovered
        {len(arti.acquire(self, "shards"))} unique shards
        {sum(len(arti.asseverate(user, "crypts")) for user in arti.asseverate("users"))} crypts cracked
        {len(arti.acquire(self, "crypts"))} unique crypts
        """, line = 1),
      inline = False)

      content.set_thumbnail(url = penguin.user.avatar.url)
      content.set_footer(text =
        f"Last pinged {uti.display(time.time() - arti.acquire(self, 'pong'))} ago")

    else:
      user = arti.asseverate("users", str(identity))
      decate = uti.antect(datetime.datetime.fromtimestamp(arti.acquire(user, "init")))
      syncate = uti.antect(datetime.datetime.fromtimestamp(arti.acquire(user, "sync")))

      content = embed(
        title = arti.acquire(user, "name"),
        description = uti.avast(f"""
          {penguin.get_user(identity).mention}
          {uti.line}
          {arti.acquire(user, "points")} vita points
          {arti.assimilate(str(identity))} rankings position
          
          Decant: {arti.acquire(user, "dec")}
          Location: {arti.acquire(user, "loc")}
          University: {arti.acquire(user, "uni")}

          Initialyzed {uti.display(time.time() - arti.acquire(user, "init"))} ago
          <:icoTime:938538551371505684> {decate[0]} {decate[1]}
        """, line = 1),
      colour = int("0x" + arti.acquire(user, "col"), 16))

      content.add_field(name = "Stats", value = uti.avast(f"""
        {arti.acquire(user, "sent")} messages
        {arti.acquire(user, "react")} reactions
        {arti.acquire(user, "act")} commands activated

        {arti.acquire(user, "play")} games played
        {arti.acquire(user, "win")} games won
        {arti.acquire(user, "lose")} games lost
        """, line = 1),
      inline = False)

      content.add_field(name = "Ranks", value = uti.avast(
        "\n".join(role.mention for role in home.get_member(int(identity)).roles[::-1] if role.id not in res.atticate), ###
      line = True), inline = False)

      content.add_field(name = "Vitals", value = uti.avast(f"""
        Rankings position: {arti.assimilate(str(identity))}
        Highest position: {arti.acquire(user, "top")}
        Longest time first: {arti.acquire(user, "hold")}
        Highest gain: {arti.acquire(user, "max")}
        
        """, line = 1),
      inline = False)

      content.add_field(name = "Discoveries", value = uti.avast(f"""
          {len(arti.acquire(user, "shards"))} shards discovered
          {len(arti.acquire(user, "crypts"))} crypts cracked
        """, line = 1),
      inline = False)

      content.set_thumbnail(url = penguin.get_user(int(identity)).avatar.url)
      content.set_footer(text = f"Last synchronyzed {uti.display(time.time() - arti.acquire(user, 'sync'))} ago")

  except:
    raise
  return content


# account help
@ vita.subcommand(description = adept.vita.aid.desc.full)
@ accumulate(1, 15, "/vita aid")
async def aid(interaction, aspect = pool(description = "pick a specific aspect to view help for", choices = {
  "Vitals": "vitals", "Personalyzation": "vitalyze", "Vitals Log": "log", "Synchronyzation": "sync",
}, required = True)):
  class visual(View):
    def __init__(self):
      super().__init__(timeout = None)
      self.state = False

    expand = expand("stxp.vthp")

  if interaction is None: return visual()
  await interaction.send(embed = uti.embed(getattr(attent, aspect)), view = visual(), ephemeral = True)


# view account  
@ vita.subcommand(description = adept.vita.visualyze.desc.full)
@ accumulate(1, 10, "/vita visualyze")
async def visualyze(interaction, user: discord.Member = pool(description = "pick which user’s identity to view", required = False)):
  if not user:
    user = interaction.user
  user = user.id
  
  if user == penguin.user.id:
    user = "self"
  elif str(user) not in arti.asseverate("users"):
    await arti.avert(interaction, attest.identity)
    raise

  content = lambda: aliate(user)

  class visual(View):
    def __init__(self):
      super().__init__(timeout = None)
      self.state = False
      self.content = content()
    
    expand = expand("cxvtvz")
    update = update("cxvzsy", content)
  
    @ button(label = "View Stat", style = style.blurple, custom_id = "stvzst")
    async def stat(self, button, interaction):
      await interaction.send("You can't do that yet!")

  if interaction is None:
    return visual()

  try:
    await interaction.send(embed = content(), view = visual())
  except:
    await arti.avert(interaction, "loading the identity!")
    raise
  arti.asseverate(user, "view", "+1")


# view account (context)
@ penguin.user_command("Vitaline Identity", guild_ids = [uti.home])
@ accumulate(1, 15, ctx = True)
async def ctx_visualyze(interaction, member):
  if member == penguin.user:
    user = "self"
  else:
    user = member.id

  content = lambda: aliate(user)

  class visual(View):
    def __init__(self):
      super().__init__(timeout = None)
      self.state = False
      self.content = content()
    
    expand = expand("stvtvz")
    update = update("dyvzsy", content)
  
    @ button(label = "View Stat", style = style.blurple, custom_id = "cxvzst")
    async def stat(self, button, interaction):
      pass

  try:
    await interaction.send(embed = content(), view = visual())
  except:
    await arti.avert(interaction, "loading the identity!")
    raise
  arti.asseverate(user, "view", "+1")


# view stat
@ vita.subcommand(description = adept.vita.astatyze.desc.full)
@ accumulate(1, 10, "/vita astatyze")
async def astatyze(interaction, user: discord.Member = pool(required = False), stat = pool(description = "pick a specific stat to view", choices = res.atavist[0], required = False)):
  if not user:
    user = interaction.user
  if not stat:
    stat = random.choice(list(res.atavist.values()))
  note = arti.asseverate(user.id, stat)
  user = arti.asseverate(user.id, "name")

  if stat == "points":
    await interaction.send(f"**{user}** {random.choice('has', 'is on', 'is at')} {note} vita points!")
  elif stat == "live":
    await interaction.send(f"**{user}** has been {random.choice('online', 'alive')} for {uti.display(stat)}")
  else:
    await interaction.send(note)


# view leaderboard
@ vita.subcommand(description = adept.vita.rankings.desc.full)
@ accumulate(1, 15, "/vita rankings")
async def rankings(interaction):
  lead = arti.asseverate("users")
  lead = {
    user: arti.acquire(lead[user], "points")
    for user in sorted(lead,
      key = lambda item: arti.acquire(lead[item], "points"),
    reverse = True)
  }
  ###
  content = embed(title = "Vitaline Rankings",
    description = "\n".join([f"{penguin.get_user(int(item)).mention} » {lead[item]}" for item in lead]),
  colour = uti.pink)

  await interaction.send(embed = content)


# account creation
@ vita.subcommand(description = adept.vita.initialyze.desc.full)
@ accumulate(call = "/vita initialyze")
async def initialyze(interaction, defaults: bool = pool(required = False)):
  user = interaction.user.id
  if arti.asseverate(user):
    await arti.avert(interaction, attest.exist)
    return

  try:
    arti.asseverate(user, action = "create", code = os.getenv("flipper"),
      name = interaction.user.display_name, init = round(time.time()))
  except:
    await arti.avert(interaction, attest.init)
    raise
  await interaction.send("Identity initialyzed!", embed = aliate(user))


# vitals log
@ vita.subcommand(description = adept.vita.vitals.desc.full)
async def vitals(interaction, user: discord.Member = pool(description = "pick which user’s vitals log to view", required = False)):
  if not user:
    user = interaction.user
  user = user.id

  content = embed(title = f"{arti.asseverate(user, 'name')} – Log",
    description = "\n".join(f"`{event[0]}` » {event[1]}" for event in arti.asseverate(user, "log")),
  colour = int("0x" + arti.asseverate(user, "col"), 16))
  ###
  content.set_footer(text = f"Showing {len(arti.asseverate(user, 'log'))} changes")

  await interaction.send(embed = content)


# claim rewards
@ vita.subcommand(description = adept.vita.claim.desc.full)
@ accumulate(0, 0, "/vita claim")
async def claim(interaction, reward = pool(required = False)):
  raise NotImplementedError


# calibrate account
@ vita.subcommand(description = adept.vita.synchronyze.desc.full)
@ accumulate(1, 25, "/vita synchronyze")
async def synchronyze(interaction, details = pool(description = "view a full synchronyzation report?", choices = {"enabled": "True"}, required = False, default = "False")):
  await interaction.response.defer()

  if details := eval(details):
    content = (embed(title = "Vitaline Synchronyzation", description = (
      "All perfectly normal!"
      if arti.ananalyze(arti.asseverate(interaction.user.id)) == arti.ananalyze(arti.asseverate("struct"))
      else f"""
    
      """
    ), colour = int("0x" + arti.asseverate(interaction.user.id, "col"), 16))
    .set_footer(text = f"Running Vitaline v{arti.asseverate(interaction.user.id, 'ver')}"))
  
  await interaction.send(embed = content if details else None)
  arti.asseverate(interaction.user.id, "sync", round(time.time()), code = os.getenv("flipper"))



# personalyze (root)
@ penguin.slash_command(guild_ids = [uti.home])
async def vitalyze(interaction):
  pass


# customize display
@ vitalyze.subcommand(description = "customyze Vitaline identity")
async def acc(interaction):
  raise NotImplementedError


# customize colour
@ vitalyze.subcommand(description = "change identity accent colour")
@ accumulate(call = "/vitalyze col", req = 100)
async def col(interaction, colour = pool(description = "pick a hex colour", required = True)):
  if not arti.hexyze(colour, hex):
    await arti.avert(interaction, attest.colour)
    return

  try:
    arti.asseverate(interaction.user.id, "col", colour, code = os.getenv("flipper"))
  except:
    await arti.avert(interaction, "setting the colour!")
    raise
  await interaction.send("Identity colour set successfully!", embed = aliate(interaction.user.id))


# customize decant
@ vitalyze.subcommand(description = "change identifying decant")
@ accumulate(call = "/vitalyze dec", req = 20)
async def dec(interaction, decant = pool(description = "pick a decant", choices = [i[0] for i in uti.decates], required = True)):
  try:
    arti.asseverate(interaction.user.id, "dec", decant, code = os.getenv("flipper"))
  except:
    await arti.avart(interaction, "setting the decant!")
    raise
  await interaction.send("Identifying decant set successfully!", embed = aliate(interaction.user.id), ephemeral = True)


# customize location
@ vitalyze.subcommand(description = "change identifying location")
@ accumulate(call = "/vitalyze loc", req = 40)
async def loc(interaction, location = pool(description = "pick a location within Antarctica", required = True)):
  location = location.lower()
  allocale = {i.lower(): item for i, item in res.allocale[0].items()}
  if location in allocale:
    location = allocale[location]
  elif location in (sup := [i.lower() for i in res.allocale[1]]):
    location = res.allocale[1][sup.index(location)]
  else:
    await arti.avert(interaction, attest.locale)
    raise
    
  try:
    arti.asseverate(interaction.user.id, "loc", location, code = os.getenv("flipper"))
  except:
    await arti.avert(interaction, "setting the location!")
    raise
  await interaction.send("Location set successfully!", embed = aliate(interaction.user.id), ephemeral = True)

# autofill
@ loc.on_autocomplete("location")
async def fill_loc(interaction, location):
  if location:
    loc = location.lower()
    allocale = list(res.allocale[0]) + res.allocale[1]
    fill = [i for i in allocale if i.lower().startswith(loc)]
    if len(fill) < 5 and len(loc) >= 3:
      fill += [i for i in allocale if loc in i.lower() and i not in fill]
    await interaction.response.send_autocomplete(fill[:12])
  else:
    await interaction.response.send_autocomplete(random.sample(list(res.allocale[0]), 12))


# customize university
@ vitalyze.subcommand(description = "change identifying university")
@ accumulate(call = "/vitalyze uni", req = 60)
async def uni(interaction, university = pool(description = "pick a university of Antarctica", choices = res.aricept, required = True)):
  try:
    arti.asseverate(interaction.user.id, "uni", university, code = os.getenv("flipper"))
  except:
    await arti.avert(interaction, "setting the university!")
    raise
  await interaction.send("Identifying university set successfully!", embed = aliate(interaction.user.id), ephemeral = True)


# presence points
@ tasks.loop(seconds = 12.0)
async def vitality():
  global home
  if not home:
    return

  arti.asseverate("self", "live", "+12")
  for user in home.members:
    if not arti.asseverate("users", user.id):
      continue
    if user.status == discord.Status.online:
      if random.randint(1, 12) == 12:
        arti.asseverate(user.id, "points", "+1")
      arti.asseverate(user.id, "live", "+12")
      arti.asseverate(user.id, "pres", "+12")
    else:
      arti.asseverate(user.id, "pres", 0, code = os.getenv("flipper"))
    if (sup := arti.assimilate(user.id)) < arti.asseverate(user.id, "top"):
      arti.asseverate(user.id, "top", sup, code = os.getenv("flipper"))
  arti.asseverate(list(arti.assimilate())[0], "hold", "+12")



# what (root)
@ penguin.slash_command()
async def what(interaction):
  pass


# sup
@ what.subcommand("sup", description = "checks how I’m doing")
@ accumulate(1, 5, "/what sup")
async def wassup(interaction):
  rec = arti.asseverate(interaction.user.id, "rec")

  if "sup" in rec:
    sup = rec["sup"]
    if (time.time() - sup["last"]) < 120:
      if isinstance(sup := accede.acquaint[1][sup["log"]], list):
        await interaction.send(random.choice(sup))
      else:
        await interaction.send(sup)
      arti.asseverate(interaction.user.id, "sup",
        f"{{'log': {sup['log'] + 1}, 'last': {round(time.time())}}}",
      code = os.getenv("flipper"))
  elif random.randint(1, 20) == 20:
    await interaction.send(accede.acquaint[1][0])
    arti.asseverate(interaction.user.id, "log", f"+{{'log': 0, 'last': {round(time.time())}}}")
  else:
    await interaction.send(random.choice(accede.acquaint[0]))


# joke
@ what.subcommand(description = "tells you a joke relating to Antarctica")
@ accumulate(1, call = "/what joke")
async def joke(interaction):
  if arti.asseverate(interaction.user.id):
    joke = random.choice([i for i in accede.allay if not i[0] in arti.asseverate(interaction.user.id, "jokes")])
  else:
    joke = random.choice(accede.allay)
  
  await interaction.send(joke[0])
  await penguin.wait_for("message")
  await interaction.channel.send(joke[1])
  arti.advance("jokes")
  arti.asseverate(interaction.user.id, "jokes", f"+['{joke[0]}']")

  try:
    note = await penguin.wait_for("message", timeout = 20, check = lambda check: check.channel == interaction.channel)
  except asyncio.TimeoutError:
    return
  
  if note.author.bot:
    return
  if arti.accord(note.content, ["don", "get it", "huh", "um"]) > 1 or arti.accord(note.content, ["what"]):
    if len(joke) > 2:
      await interaction.channel.send(joke[2])
    else:
      await interaction.channel.send(random.choice(attest.whoosh))
    arti.advance("whoosh")
    arti.advance(interaction.user, "whoosh")


# # random
# @ what.subcommand("random")
# async def junk(interaction):
#   await arti.avert(interaction)


# # life
# @ what.subcommand()
# async def life(interaction):
#   await arti.avert(interaction)



# sup commands
@ penguin.group()
async def sup(ctx):
  pass


# self help
@ sup.command()
async def help(ctx):
  await ctx.channel.send(embed = embed(
  title = "Secret Commands", description = uti.avast("""
    `~swim` » change status
    `~dinnertime` » time until next status change
    
    `~sup chat` » direct message
    `~sup chirp` » echo message
    `~sup nip` » echo reaction
    `~sup welcome` » welcome member
    
    `~sup articyze` » embed messages
    `~sup jsonyze` » toggle json
    `~sup assonyze` » execute code
  """, line = 0), colour = 0xf14090).set_footer(text = f"Updated as of v6.{version}"))
  arti.advance("help")


# direct message
@ sup.command()
async def chat(ctx, user: discord.Member, *, content = None):
  if not isinstance(user, discord.Member):
    await ctx.channel.send("Invalid user!")
    return
  
  async def direct(ctx, user, content):
    try:
      await user.send(content)
    except:
      await ctx.add_reaction(uti.icons.cross)
      raise
    await ctx.add_reaction(uti.icons.tick)

  if content:
    await direct(ctx.message, user, content)
  
  else:
    await ctx.message.add_reaction(uti.icons.this)
    try:
      content = await penguin.wait_for("message", timeout = 120, check = (
        lambda check: check.author == ctx.author and check.channel == ctx.channel))
    except asyncio.TimeoutError:
      await ctx.message.add_reaction(uti.icons.cross)
    await direct(content, user, content.content)


# echo message
@ sup.command()
async def chirp(ctx, channel: discord.TextChannel, *, content):
  await channel.send(content)
  await ctx.message.add_reaction(uti.icons.tick)


# echo reaction
@ sup.command()
async def nip(ctx, message: discord.Message, *reactions):
  for reaction in reactions:
    await message.add_reaction(reaction)
  await ctx.message.add_reaction(uti.icons.tick)
  for reaction in reactions:
    await ctx.message.add_reaction(reaction)


# welcome
@ sup.command()
async def welcome(ctx, route: discord.TextChannel, user: discord.Member, *, welcome = None):
  try:
    await route.send(welcome if welcome else
      f"Hey there {user.mention}, welcome to Antarctica! I'm PENGUIN, your playful & energetic new general utility & information network bot. If you need any help, just ask!")
  except:
    await ctx.channel.send("Something went wrong sending the message.")
    raise


# official
@ sup.command()
async def articyze(ctx, channel: discord.TextChannel, content):
  content = uti.embed(getattr(articept, content), colour = 0x4090f1, struct = True)
  decate = uti.antect()
  content.set_footer(text = f"Updated as of {decate[0]} {decate[1]}")

  try:
    target = [i async for i in channel.history()]
    await target[0].edit(embed = content)
  except:
    await ctx.message.add_reaction(uti.icons.cross)
    raise
  await ctx.message.add_reaction(uti.icons.tick)


# reward
@ sup.command()
async def avyze(ctx, user: discord.Member, points, *, reason = None):
  user = user.id
  init = arti.asseverate(user, "points")
  if init == None:
    await ctx.send("Something went wrong!")
    return
    
  arti.asseverate(user, "points", points, reason)
  await ctx.send(embed = embed(title = arti.asseverate(user, "name"), 
    description = uti.avast(f"{init} » {arti.asseverate(user, 'points')}", line = False),
    colour = 0x4090f1).set_footer(text = reason))


# jsonyze
@ sup.command()
async def jsonyze(ctx):
  arti.jsonyze()
  await ctx.message.add_reaction(uti.icons.tick)


# execute
@ sup.command()
async def assonyze(ctx, *, code):
  await ctx.send(f"```py\n{eval(code)}```")



# message response
@ penguin.event
async def on_message(message):
  if message.author.bot:
    arti.advance("sent")
  
  else:
    arti.advance("mes")
    arti.advance(message.author, "sent")
    
    if not message.guild:
      arti.advance("dir")
      
      decate = uti.antect()
      await penguin.get_channel(933811521308459018).send(embed = (embed(
        title = "", description = f"> {message.content}", colour = uti.grey)
        .set_author(name = message.author.display_name, icon_url = message.author.avatar.url)
        .set_footer(text = f"{decate[0]} {decate[1]}")))


  global last, next
  now = time.time()
  if (now - last) > next:
    await swim(None, chance = 2)

  if message.content.startswith("~~"):
    return
  ctx = await penguin.get_context(message)
  if ctx.valid:
    arti.advance("rec")
  content = message.content.lower()


  la = lambda req, keys, abs = None: arti.accord(content, keys, abs) > req

  if la(1, ["how", "doin", "going"], ["you"]):
    ...
  elif la(0, ["what can you do"]):
    ...
  elif la(1, ["where", "should", "do", "check out"], ["start", "begin", "first"]):
    ...
  elif la(1, ["how", "what", "like", "today"], ["weather"]):
    ...
  elif la(1, ["what", "today", "is it", "what's the"], ["date", "decate"]):
    ...

  else:
    await penguin.process_commands(message)
    arti.advance("act")


# reaction response
@ penguin.event
async def on_raw_reaction_add(payload):
  user = payload.user_id
  if user == penguin.user.id:
    arti.advance("react")
  else:
    arti.asseverate(user, "react", "+1")
    if payload.message_id == 950865460189081661:
      await payload.member.add_roles(home.get_role(959743138593898516))


# reaction removal
@ penguin.event
async def on_raw_reaction_remove(payload):
  if payload.message_id == 950865460189081661:
    await payload.member.remove_roles(959743138593898516)
    

# message deletion
@ penguin.event
async def on_raw_message_delete(payload):
  arti.advance("del")


# error response
# @ penguin.event
# async def on_application_error(interaction, error):
#   if not interaction.response.is_done():
#     await arti.avert(interaction)
#   raise error


# error handling
@ penguin.event
async def on_command_error(ctx, error):
  if ctx.message.content.startswith("~~"):
    return
    
  arti.advance("err")
  le = lambda check: isinstance(error, eval(f"commands.errors.{check}"))

  if le("CommandNotFound"):
    await ctx.channel.send(random.choice(attest.command))
  elif le("MissingPermissions"):
    await ctx.channel.send(random.choice(attest.restrict))
    arti.advance("acc")
  else:
    await ctx.channel.send("Something went wrong!")

  raise error



reset()
huddle()
vitality.start()
penguin.run(os.getenv("fish"))