from collections import namedtuple
from recog import item

desc = namedtuple("desc", "curt full")


ascept = {
  "Antarctican": item(
    title = "Antarctican",
    caption = "Residence Role",
    content = "A standard role granted to all citizens of Antarctica.",
    fields = [
      item.field("Permissions", "Basic"),
      item.field("Acquisition", "Become authorized as an Antarctican citizen.")
    ],
    other = "A-CORE",
  ),

  "High Command": item(
    title = "High Command",
    caption = "Command Role",
    content = "",
    fields = [
      item.field("Permissions", "Administrator"),
      item.field("Display", "Hoisted"),
    ],
    other = "Central Command",
  ),
}


class adept:

  ping = item(
    title = "~ping",
    caption = "Status Check",
    desc = desc(
      curt = "check if I’m awake.",
      full = None,
    ),
    content = "Checks if I’m awake and functioning.",
    fields = [item.field("Format", "`~ping`")],
    other = None,
  )


  class util:

    cast = item(
      title = "/util cast",
      caption = "Weather Forecast",
      desc = desc(
        curt = "natural weather forecast for Antarctica",
        full = "view natural weather forecast for across Antarctica",
      ),
      content = "Views general forecast for natural weather across Antarctica.",
      fields = [
        item.field("Format", "/util cast ‹detail›"),
        item.field("Fields", """
          __`detail`__ [choice, optional]
          If specified, only displays a specific aspect of the weather forecast.
        """),
      ],
      other = "/util decate, /util cal",
    )

    decate = item(
      title = "/util decate",
      caption = "Antect Decate",
      desc = desc(
        curt = "convert current date to Antarctican calendar",
        full = "convert current date to Antarctican calendar",
      ),
      content = "Converts the current date to the Antarctican calendar.",
      fields = [item.field("Format", "`/util decate`")],
      other = "/util antect, /util cal",
    )

    antect = item(
      title = "/util antect",
      caption = "Antect Date",
      desc = desc(
        curt = "convert specific date to Antarctican calendar",
        full = "convert specific date to Antarctican calendar",
      ),
      content = "Converts a given date in the Gregorian calendar to the Antarctican calendar.",
      fields = [
        item.field("Format", """
        `/util antect ‹month› ‹day›`
        
        Example
        `/util antect April 2`
      """),
        item.field("Fields", """
          __`month`__
          [choice, required]
          The month of the date being converted.

          __`day`__
          [int, required]
          The day of the date being converted. Must be a valid day within the range of the month (i.e. 20 would be invalid input for February).
        """),
      ],
      other = "/util decate, /util cal",
    )

    cal = item(
      title = "/util cal",
      caption = "Events Calendar",
      desc = desc(
        curt = "calendar of upcoming events",
        full = "view calendar of upcoming events and holidays",
      ),
      content = "Views a calendar of all upcoming events and holidays in Antarctica.",
      fields = [item.field("Format", "`/util cal`")],
      other = "/util decate, /util cast",
    )

    idea = item(
      title = "/util idea",
      caption = "Idea Submission",
      desc = desc(
        curt = "suggest idea",
        full = "suggest an idea",
      ),
      content = "",
      fields = [
        item.field("Format", "/util idea ‹title› ‹idea› ‹category›"),
        item.field("Fields", """
          __`title`__

          __`idea`__

          __`category`__
        """),
      ],
      other = "/info fact",
    )


  class index:

    view = item(
      title = "/index view",
      caption = "Information Index",
      desc = desc(
        curt = "view info index",
        full = "view information index",
      ),
      content = "Views a list of items in Penguin’s information index.",
      fields = [item.field("Format", "`/index view`")],
      other = "/index filter",
    )

    filter = item(
      title = "/index filter",
      caption = "Index Search",
      desc = desc(
        curt = "filter info index",
        full = "filter information index",
      ),
      content = "Views a filtered list of items in Penguin’s information index.",
      fields = [
        item.field("Format", "`/index filter ‹by: type› ‹with: value›`"),
        item.field("Fields", """
          __`by`__
          [choice, required]
          The option by which to filter the index. Select from 4 options.

          letter › filters by a specific letter
          content › searches for items with specific text
          category › filters by categories
          tag › searches for items with specified tag

          __`with`__
          [text, required]
          The value to filter the index with. Can take multiple inputs, to filter with many values at once (for example, with 2 different tags)
        """),
      ],
      other = "/index view",
    )

    games = item(
      title = "/index games",
      caption = "Games Index",
      desc = desc(
        curt = "games",
        full = "view list of games I can play",
      ),
      content = "Views a list of all the games I can play with you.",
      fields = [item.field("Format", "`/index games`")],
      other = "/help games, /play",
    )

  
  class info:

    fact = item(
      title = "/info fact",
      caption = "Fun Fact",
      desc = desc(
        curt = "fun fact relating to Antarctica",
        full = "fun fact relating to Antarctica!",
      ),
      content = "Tells you a random fun fact relating to Antarctica.",
      fields = [],
      other = "/index view, /play know",
    )

    about = item(
      title = "/info about",
      caption = "Item Lookup",
      desc = desc(
        curt = "all about an item in the index",
        full = "view info about an item in the index",
      ),
      content = "Views info about a specific item in Penguin’s information index.",
      fields = [],
      other = "/index",
    )

    acro = item(
      title = "/info acro",
      caption = "Acronym Lookup",
      desc = desc(
        curt = "view what an acronym stands for",
        full = "view what an acronym stands for",
      ),
      content = "Views what an acronym(s) relating to Antarctica stands for.",
      fields = [],
      other = "/info about",
    )

    role = item(
      title = "/info role",
      caption = "Role Info",
      desc = desc(
        curt = "all about a role",
        full = "view info about a role",
      ),
      content = "Views info about a role in the Discord server.",
      fields = [],
      other = "/info about",
    )

    game = item(
      title = "/info game",
      caption = "Game Info",
      desc = desc(
        curt = "all about a game",
        full = "view info about a game",
      ),
      content = "Views info about a game I can play.",
      fields = [],
      other = "/info role, /play",
    )


  class play:

    class guess:

      num = item(
        title = "/play guess num",
        caption = "Guess the Number",
        desc = desc(
          curt = "Guess the Number",
          full = "Guess the Number – try guess the secret number!",
        ),
        content = "",
        fields = [],
        other = "/play guess react, /play count",
      )

      emoji = item(
        title = "/play guess emoji",
        caption = "Guess the Emoji",
        desc = desc(
          curt = "Guess the Emoji",
          full = "Guess the Emoji – try guess the secret emoji!",
        ),
        content = "",
        fields = [],
        other = "/play guess num, /play rush",
      )

    react = item(
      title = "/play react",
      caption = "*React*",
      desc = desc(
        curt = "*React*",
        full = "React – react with a series of reactions as fast you can!",
      ),
      content = "",
      fields = [],
      other = "/play flick, /play rush",
    )

    flick = item(
      title = "/play flick",
      caption = "*Flick*",
      desc = desc(
        curt = "*Flick*",
        full = "Flick – react to a sequence with a twist as fast as you can!",
      ),
      content = "",
      fields = [],
      other = "/play react, /play quack",
    )

    rush = item(
      title = "/play rush",
      caption = "*Rush*",
      desc = desc(
        curt = "*Rush*",
        full = "Rush – find the secret emoji as fast as you can!",
      ),
      content = "",
      fields = [],
      other = "/play guess react, /play react",
    )

    spam = item(
      title = "/play spam",
      caption = "Spam",
      desc = desc(
        curt = "Spam",
        full = "Spam – spam click the buttons as fast you can!",
      ),
      content = "",
      fields = [],
      other = "/play count, /play flick",
    )

    quack = item(
      title = "/play quack",
      caption = "*Quack*",
      desc = desc(
        curt = "*Quack*",
        full = "Quack – the Antarctic version of Hangman!",
      ),
      content = "",
      fields = [],
      other = "/play guess num, /play hunt",
    )

    know = item(
      title = "/play know",
      caption = "Antarctican Knowledge Quiz",
      desc = desc(
        curt = "Antarctican Knowledge Quiz",
        full = "A general knowledge quiz on everything relating to Antarctica!",
      ),
      content = "",
      fields = [],
      other = "/info fact"
    )

    count = item(
      title = "/play count",
      caption = "Count",
      desc = desc(
        curt = "Counting Game",
        full = "Count – simple but impossible, see how high you can count between you!",
      ),
      content = "",
      fields = [],
      other = "/play spam, /play guess num",
    )

    hunt = item(
      title = "/play hunt",
      caption = "*Shardhunter*",
      desc = desc(
        curt = "*Shardhunter*",
        full = "Shardhunter – go on the hunt for secret shards!",
      ),
      content = "",
      fields = [],
      other = "/play crypt",
    )

    crypt = item(
      title = "/play crypt",
      caption = "*Cryptcracker*",
      desc = desc(
        curt = "*Cryptcracker*",
        full = "Cryptcracker – try to crack a cryptic cypher for some epic rewards!",
      ),
      content = "",
      fields = [],
      other = "/play hunt"
    )

    quest = item(
      title = "/play quest",
      caption = "Quest",
      desc = desc(
        curt = "...",
        full = "Currently unavailable",
      ),
      content = "",
      fields = [],
      other = "/play hunt, /play crypt",
    )

    excursion = item(
      title = "/play excursion",
      caption = "Excursion",
      desc = desc(
        curt = "...",
        full = "Currently unavailable",
      ),
      content = "",
      fields = [],
      other = "/play hunt, /play crypt",
    )


  class vita:

    aid = item(
      title = "/vita aid",
      caption = "Vitaline Help",
      desc = desc(
        curt = "Vitaline identity help",
        full = "help with Vitaline identity",
      ),
      content = "",
      fields = [],
      other = "/vita visualyze, /vita initialyze",
    )

    visualyze = item(
      title = "/vita visualyze",
      caption = "Vitaline Identity",
      desc = desc(
        curt = "view Vitaline identity",
        full = "view Vitaline identity",
      ),
      content = "Views a Vitaline identity.",
      fields = [],
      other = "/vita astatyze, /vita initialyze",
    )

    astatyze = item(
      title = "/vita astatyze",
      caption = "Vitaline Stat",
      desc = desc(
        curt = "view specific stat",
        full = "view specific stat",
      ),
      content = "Views a specific stat of a particular Vitaline identity.",
      fields = [],
      other = "/vita visualyze, /vita rankings",
    )

    rankings = item(
      title = "/vita rankings",
      caption = "Vitaline Leaderboard",
      desc = desc(
        curt = "view points leaderboard",
        full = "view points leaderboard",
      ),
      content = "Views the Vitaline points leaderboard.",
      fields = [],
      other = "/vita visualyze, /vita astatyze",
    )

    initialyze = item(
      title = "/vita initialyze",
      caption = "Identity Initialyzation",
      desc = desc(
        curt = "create Vitaline identity",
        full = "create a Vitaline identity",
      ),
      content = "Creates a Vitaline identity for the user, if they do not already have one.",
      fields = [],
      other = "/vita visualyze, /vita customyze",
    )

    vitals = item(
      title = "/vita vitals",
      caption = "Vitals Log",
      desc = desc(
        curt = "vitals activity log",
        full = "view log of vitals activity",
      ),
      content = "",
      fields = [],
      other = "/vita rankings, /vita synchronyze"
    )

    claim = item(
      title = "/vita claim",
      caption = "Claim Rewards",
      desc = desc(
        curt = "claim Vitaline rewards",
        full = "claim any Vitaline rewards available to claim",
      ),
      content = "Claims any Vitaline rewards available to claim.",
      fields = [],
      other = "/vita vitals, /vitalyze",
    )

    synchronyze = item(
      title = "/vita synchronyze",
      caption = "Vitaline Synchronyzation",
      desc = desc(
        curt = "synchronyze Vitaline identity",
        full = "synchronyze Vitaline identity",
      ),
      content = "Synchronyzes the user's Vitaline identity.",
      fields = [],
      other = "/vita vitals, /vita initalyze",
    )

    vitalyze = item(
      title = "/vita customyze",
      caption = "Identity Customization",
      content = "Allows the user to customize various identifying aspects of their Vitaline identity.",
      fields = [],
      other = "/vita initialyze, /vita visualyze",
    )