from recog import item
from recom import adept
from util import icons


absorb = dict(
  num = item(
    title = "Guess the Number",
    caption = "`/play guess num`",
    desc = "A classic beginner game of trying to guess the secret number!",
    content = """
      Player: single
      Type: guessing game
      Difficulty: simple
      Depth: basic
    """,
    fields = [
      item.field("Points", "TBA"),
      item.field("Tries", "TBA"),
      item.field("Fields", "TBA"),
    ],
    other = "Guess the Emoji",
  ),

  emoji = item(
    title = "Guess the Emoji",
    caption = "`/play guess emoji`",
    desc = "Guess the Number, but instead of a number, it’s a secret emoji.",
    content = """
      Player: single
      Type: guessing game
      Difficulty: simple
      Depth: basic
    """,
    fields = [],
    other = "Guess the Number"
  ),

  react = item(
    title = "React",
    caption = "`/play react`",
    desc = "A challenging speedrun of reacting with a series of specific emojis (not like *React* or *REact* at all, btw)",
    content = "",
    fields = [],
    other = "",
  ),

  flick = item(
    title = "Flick",
    caption = "`/play flick`",
    desc = "No description provided",
    content = "",
    fields = [],
    other = "",
  ),

  rush = item(
    title = "Rush",
    caption = "`/play rush`",
    desc = "No description provided",
    content = "",
    fields = [],
    other = "",
  ),

  spam = item(
    title = "Spam",
    caption = "`/play spam`",
    desc = "No description provided",
    content = "",
    fields = [],
    other = "",
  ),

  quack = item(
    title = "Quack",
    caption = "`/play quack`",
    desc = "The Antarctican version of Hangman – try guess the letters of a hidden word before the drawing is complete!",
    content = "",
    fields = [],
    other = "",
  ),

  know = item(
    title = "Antarctican Knowledge Quiz",
    caption = "`/play know`",
    desc = "No description provided",
    content = "",
    fields = [],
    other = "",
  ),

  count = item(
    title = "Count",
    caption = "`/play count`",
    desc = "No description provided",
    content = "",
    fields = [],
    other = "",
  ),

  hunt = item(
    title = "Shardhunter",
    caption = "`/play hunt`",
    desc = "An exciting delve into a hunt for secret shards.",
    content = "",
    fields = [],
    other = "",
  ),

  crypt = item(
    title = "Cryptcracker",
    caption = "`/play crypt`",
    desc = "Attempt to crack confuzzling crypts, with epic rewards.",
    content = "",
    fields = [],
    other = "",
  ),

  quest = item(
    title = "Quest",
    caption = "`/play quest`",
    desc = "No description provided",
    content = "",
    fields = [],
    other = "",
  ),

  excursion = item(
    title = "Excursion",
    caption = "`/play excursion`",
    desc = "No description provided",
    content = "",
    fields = [],
    other = "",
  ),
)


class avail:

  help = item(
    title = "What I Can Do",
    caption = "Command Help",
    content = "`~ping` » checks if I’m awake",
    fields = [
      item.field("Help", f"""
        `/help info` » all about me
        `/help all` » see what I can do (this command)
        `/help start` » help getting started
        `/help command` » help with specific command
        `/help tip` » helpful tip
      """),
      item.field("Utility", f"""
        `/util cast` » {adept.util.cast.desc.curt}
        `/util decate` » {adept.util.decate.desc.curt}
        `/util antect` » {adept.util.antect.desc.curt}
        `/util cal` » {adept.util.cal.desc.curt}
        `/util idea` » {adept.util.idea.desc.curt}
        `/util define` » {adept.util.dict.desc.curt}
      """),
      item.field("Index", f"""
        `/index view` » {adept.index.view.desc.curt}
        `/index filter` » {adept.index.filter.desc.curt}
        `/index games` » {adept.index.games.desc.curt}
      """),
      item.field("Information", f"""
        `/info fact` » {adept.info.fact.desc.curt}
        `/info about` » {adept.info.about.desc.curt}
        `/info acro` » {adept.info.acro.desc.curt}
        `/info role` » {adept.info.role.desc.curt}
        `/info game` » {adept.info.game.desc.curt}
      """),
      item.field("Play", f"""
        `/play guess num` » {adept.play.guess.num.desc.curt}
        `/play guess emoji` » [WIP] {adept.play.guess.emoji.desc.curt}
        `/play react` » [TBA] {adept.play.react.desc.curt}
        `/play flick` » [TBA] {adept.play.flick.desc.curt}
        `/play rush` » [TBA] {adept.play.rush.desc.curt}
        `/play spam` » [TBA] {adept.play.spam.desc.curt}
        `/play quack` » [TBA] {adept.play.quack.desc.curt}
        `/play know` » [TBA] {adept.play.know.desc.curt}
        `/play count` » [TBA] {adept.play.count.desc.curt}
        `/play hunt` » [TBA] {adept.play.hunt.desc.curt}
        `/play crypt` » [TBA] {adept.play.crypt.desc.curt}
        `/play quest` » [TBA] {adept.play.quest.desc.curt}
        `/play excursion` » [TBA] {adept.play.excursion.desc.curt}
      """),
      item.field("Vitaline", f"""
        `/vita aid` » {adept.vita.aid.desc.curt}
        `/vita visualyze` » {adept.vita.visualyze.desc.curt}
        `/vita astatyze` » {adept.vita.astatyze.desc.curt}
        `/vita rankings` » {adept.vita.rankings.desc.curt}
        `/vita initialyze` » {adept.vita.initialyze.desc.curt}
        `/vita vitals` » {adept.vita.vitals.desc.curt}
        `/vita claim` » [TBA] {adept.vita.claim.desc.curt}
        `/vita synchronyze` » {adept.vita.synchronyze.desc.curt}
      """),
      item.field("Personalyzation", f"""
        `/vitalyze acc` » [TBA] personalyze Vitaline identity
        `/vitalyze col` » change identity colour
        `/vitalyze dec` » change identifying decant
        `/vitalyze loc` » change identifying location
        `/vitalyze uni` » change identifying university
      """),
    ],
  )

  start = item(
    title = "Where to Start",
    content = "Try using `/help info` to find out all about me, or `/help all` to see all the things I can do!",
    fields = [
      item.field("Commands to Try Out", """
        If you’re unsure which commands to use, here are some cool and fun ones to start with:

        `/help tip` » tells you a useful tip
        `/info fact` » tells you a fun fact relating to Antarctica
        `/index view` » views the info index of all the things I can tell you about
        `/what joke` » tells you a joke relating to Antarctica
        `/util cast` » views the natural weather forecast for Antarctica
      """),
      item.field("Topics to Read About", """
        Use `/info about` to view info about items in the index. These are some nice places to start:

        Antarctica
        Antarctican Calendar
        District
        CORE
        Marvels of Antarctica
        Education System of Antarctica
        Overview of Antarctican History
      """),
      item.field("Games to Check Out", """
        You can use `/index games` to see a list of all the games I can play – here are some simple ones to play first:

        `/play guess num` » Guess the Number
        `/play guess emoji` » Guess the Emoji
        
        More coming soon!
      """),
    ],
  )

  games = item(
    title = "Games I Can Play",
    content = "",
    fields = [
      item.field(adept.play.guess.num.caption, absorb["num"].desc),
      item.field(adept.play.guess.emoji.caption, absorb["emoji"].desc),
      item.field(adept.play.react.caption, absorb["react"].desc),
      item.field(adept.play.flick.caption, absorb["flick"].desc),
      item.field(adept.play.rush.caption, absorb["rush"].desc),
      item.field(adept.play.spam.caption, absorb["spam"].desc),
      item.field(adept.play.quack.caption, absorb["quack"].desc),
      item.field(adept.play.know.caption, absorb["know"].desc),
      item.field(adept.play.count.caption, absorb["count"].desc),
      item.field(adept.play.hunt.caption, absorb["hunt"].desc),
      item.field(adept.play.crypt.caption, absorb["crypt"].desc),
      item.field(adept.play.quest.caption, absorb["quest"].desc),
      item.field(adept.play.excursion.caption, absorb["excursion"].desc),
    ],
  )

  lang = item(
    title = "Antarctican English",
    content = """""",
    fields = [],
  )


class attent:

  vitals = item(
    title = "Vitals",
    content = "Vita points are earned from almost everything you do. This help page won’t cover completely all of them – some of them you can discover for yourself!",
    fields = [
      item.field("Constant", """
        Remaining online (not idle, undisturbed, or invisible) will periodically accumulate Vita points. Sending messages will also accumulate points, although only to a limited extent (spamming messages will not work).

        Activating commands for the first time will reward some Vita points – after that, only certain commands (which shouldn’t be spammed) will continue rewarding points.
      """),
      item.field("Games", """
        The most rewarding, satisfying and fun way to earn Vita points, is playing games with @!Penguin! As with commands, just trying out a game for the first time rewards Vita points.

        The number of points rewarded is determined by the difficulty and how well you play, and varies between different games. Some more in-depth games, such as *Cryptcracker*, will reward much more, although taking more time and thought.
      """),
    ],
  )

  vitalyze = item(
    title = "Personalyzation",
    content = "You can personalyze lots of aspects of your Vitaline identity.",
    fields = [
      item.field("Colour", """
        The accent colour of your identity (the coloured line along the left edge of the embed). Can be any hex colour you like, bar a few reserved. Set using `/vitalyze col`.
      """),
      # item.field("Guild", """
      # """),
      item.field("Decant", """
        Your identifying decant, displayed on your identity. Could be your birth decant, or a decant you really like – the choice is completely up to you. Set using `/vitalyze dec`.
      """),
      item.field("Location", """
        Your location within Antarctica, displayed on your identity. Can be any city within Antarctica, or a general district, or even other places (which you’ll have to discover yourself). Set using `/vitalyze loc`.
      """),
      item.field("University", """
        Your identifying university of Antarctica, displayed on your identity. You can choose whichever one you like. Set using `/vitalyze uni`.
      """),
    ],
  )

  log = item(
    title = "Vitals Log",
    content = "You can view a log of all your vitals fluctuations using `/vita vitals`. It lists the number of points gained (or lost) along with the reason (if available). The log (for now) will only trace back as far as 20 changes.",
  )

  sync = item(
    title = "Synchronyzation",
    content = """
      Occasionally, new features or stats may be added to the Vitaline identity. These will only take effect for new identities initialyzed after the update, so for existing identities, you’ll have to synchronyze your identity to receive the new changes. For some additions, they cannot be automatically added to your identity – instead, <@752972078579449888> will have to manually add them. Synchronyzing your identity also rewards a few Vita points!
    """,
  )


class articept:

  ranks = item(
    title = "Roles & Ranks",
    content = "Note: Not all roles are listed in hierarchy order – many are flat-hierarchical.",
    fields = [
      item.field("Special", f"""
        {icons.cross} <@&922540938390306826> » ...
        {icons.cross} <@&922819785073508363> » ...
        {icons.cross} <@&927510754788257822> » ...
      """),
      item.field("Military", f"""
        {icons.cross} <@&924703588939362334> » ...
        {icons.cross} <@&924703629313712218> » ...
        {icons.cross} <@&924703795915677746> » ...
        {icons.cross} <@&924703868602941482> » ...

        {icons.cross} <@&924703649148592179> » ...
        {icons.cross} <@&924703857962025011> » ...
        {icons.cross} <@&924703890606260294> » ...
        {icons.cross} <@&924703902895595540> » ...
        {icons.cross} <@&924703918720712714> » ...
      """),
      item.field("Field", f"""
        {icons.cross} <@&924034646214316073> » advanced technical development
        {icons.cross} <@&924034579843678239> » high-level scientific research
        {icons.tick} <@&924034957402333214> » technical development
        {icons.tick} <@&924034927429832744> » scientific research
        {icons.tick} <@&924035016785268756> » venture into unknown spaces
        {icons.tick} <@&924035056215920661> » explore novel lands
      """),
      item.field("Prestige", f"""
        Not just for show, these may grant exclusive access to secret content!

        {icons.cross} <@&922922759783321640> » exclusive title for original members
        {icons.tick} <@&946838226662994012> » rank first on the Vitaline rankings for over one continuous decant
        {icons.tick} <@&946838387933986826> » score maximum marks on an Antarctican knowledge examination

        {icons.tick} <@&946838417403166800> » uncover 20 secret shards
        {icons.tick} <@&946838450257162270> » break 20 crypts
        {icons.tick} <@&950498550826008627> » uncover 7 secret shards
        {icons.tick} <@&950498570358911036> » break 7 crypts
        {icons.tick} <@&950498593675018240> » discover a secret shard (Easter egg)
        {icons.tick} <@&950498605683318794> » crack a crypt (cypher)
      """),
      item.field("Residence", f"""
        {icons.tick} <@&922540648601640960> » apply in <#935264654677139486>
        {icons.tick} <@&946843928752173137> » initialyzed Vitaline identity
        {icons.tick} <@&922540717023326228> » temporary visitor
        {icons.tick} <@&959743138593898516> » react with <:icoSup:925411693524316191>
      """),
      item.field("Acquisition", "All ranks must be granted. Most are automatically granted upon fulfilling their criteria; others you can request for."),
    ],
  )
  
  vitaline = item(
    title = "Vitaline Info",
    content = "Welcome to *Vitaline* – the life account system of Antarctica.",
    fields = [
      item.field("Induction", """
        Anyone in Antarctica can create a Vitaline ‘identity’ for themselves. Essentially, it’s a personalyzed life account for residence in Antarctica, which tracks your stats and activity. It also acts as a national profile for others to see who you are, and can be customyzed in a multitude of ways!

        There are no requirements to initialyze an identity; although, visitors’ identities will be deactivated upon leaving. You can use `/vita visualyze` to view your own or anyone else’s.
      """),
      item.field("Vitals", """
        The main facet of the Vitaline system is ‘vita’ points, which you can earn from doing pretty much everything. The goal is, of course, to accumulate as many as possible. The number of points you have is called your ‘vitals’.

        The higher your vitals, the higher your position in the server, and the more respect and glory you gain – unlocking new ranks, opportunities and privileges. Naturally, there’s a Vitaline leaderboard to see who has the highest vitals. Of course, no one wants to be at the bottom of that, right?

        Who am I kidding, it’s just for a bit of fun, with a competitive edge =)
      """),
      item.field("Accumulation", """
        Almost any actions you make in the server will reward vita points. The main constant sources are:

        » remaining online (yup!)
        » sending messages
        » activating commands

        The most rewarding method, by far, is playing games with Penguin! Some games reward more vita points than others, and the difficulty along with how well you play also affect the vita points rewarded.

        Another way is through discovering ‘secret shards’ (Easter eggs) – but that’s all that’ll be revealed. As to how you find them, that’s for you to figure out!
      """),
      item.field("Initialyzation", """
        Once you’re ready, use `/vita initialyze` to create your Vitaline identity. <@923508907014492180> will guide you through the whole procedure, which takes less than a second. Then, you’ll be all set to start earning vita points!
      """),
    ],
  )

  core = item(
    title = "Core Application",
    content = "Here is where you can apply for an A-CORE installation. Once you meet the requirements, the process can be started whenever you choose to do so.",
    fields = [
      item.field("Privileges", """
        A-CORE installation is not compulsory; the choice is completely up to you. All it does is make life more comfortable, grant a few quality of life permissions, and – most importantly – turns your name Electric Blue, which is far more visible in dark mode.
      """),
      item.field("Installation Requirements", """
        » Antarctican citizenship
        » 1 decant of residence
        » 2000 vita points

        You can find out more about the A-CORE and installation process through `/info about`.
      """),
    ],
  )

  update = item(
    title = "What’s New in PENGUIN v6.0",
    content = """
      Update 6.0 – without a doubt, the biggest update yet – brings a massive overhaul to Penguin!
      
      The migration from the libraries of discord.py to the lands of Nextcord was certainly not easy, with a major diversion to Pycord along the way, but in the end it was finally successful. Penguin’s source code is now powered by Nextcord 2.0, opening up new opportunities for cool features and integrations!
    """,
    fields = [
      item.field("Slash Commands", """
        Certainly, the most impressive new development is the integration of slash commands. Now, all the commands will be available right at your fingertips, with all the options and parameters laid out intuitively by Discord. No more forgetting to pass the command argument, skimming through paragraphs of command help, or trying to figure out how the blasted index filters work!

        All of Penguin’s various commands have been converted to slash commands (bar a few, such as `~ping`), and organized into major categories. Out of sheer luck (or genius pre-planning, perchance?), `/help` just so happens to be first alphabetically – so it’ll be right at the top of the list when you need it (and even if it weren’t, `/aid` would be a perfect rename). Some commands will still be available as prefix commands, for quick and easy access should you need it.
      """),
      item.field("Autocomplete", """
        Along with slash commands comes autocomplete – try it in action now, with `/info acro` or `/info about`! As you type, suggestions will appear in real time to show items that match what you’re typing – so you know if the item you’re trying to find exists. Additionally, when you haven’t typed anything yet there’ll be a list of randomized suggestions, for you to choose from if you’re feeling curious.

        Right now, the slash commands menu may seem a bit cluttered with all the different subcommands, but sometime in the future Discord might (hopefully) combine subcommands into a single root command with the subcommands as options – then, it’ll be far less cluttered, but for now, just have fun checking out the plethora of things Penguin can do! || ~~and don’t forget about the awesome `util` commands that are at the very bottom~~ ||
      """),
      item.field("Vitaline System", """
        Oh yeah, it’s finally here. Introducing: *Vitaline* – the official account system of Antarctica. Each citizen can create their own Vitaline ‘identity’, to track their stats and, more importantly, accumulate ‘vita’ points. And what do these do exactly, you ask? Well, mostly bragging rights, of course; and also unlocking cool stuff. Oh, and there’s leaderboard that’ll shame you for being last.

        From a technical standpoint, it was a great challenge, involving the use of recursion indexing and json modelling, but also highly educational. From a personal standpoint, this was something that was planned from conception day, that’s finally become a reality. Either way, it’s an epic accomplishment, and it’s ready for you to use now! All the info and logistics about how it works can be found in #vitaline. Once you’re ready, just use `/vita initialyze` to create your account!
      """),
      item.field("Fun & Games", """
        Completing the trifecta of game-changing changes, you can now play games with Penguin! This has also been a long time coming. Use `/index games` to view a list of games you can play; there’s only one to play right now – that being Guess the Number – since it’s still very much so a work in progress. Watch out for more games to come!
      """),
      item.field("Utility & Tips", """
        2 new utility commands have been introduced: `/util calendar` and `/util idea`. They’re all pretty self-explanatory; the calendar command views a calendar of upcoming events and holidays in Antarctica, and the idea command can be used to submit ideas. These will be sent in #brainwave, where everyone can vote on them, and if they gain overwhelming approval and are possible, then they’ll be implemented!
      """),
    ],
    surplus = "Verena 11",
  )