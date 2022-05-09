from weightedlist import WeightedList


class attest:
  generic = WeightedList(
    "Something went wrong",
    "An error occured",
    "Encountered an error",
  )

  index = WeightedList(
    "Nothing found",
    "No items found",
    "No item ‘{}’ found",
    "Didn’t find anything",
    "Didn’t find anything...",
    "Didn’t find anything?",
    "Did you make a typo?",
  )

  command = WeightedList(
    "No command found",
    "Didn’t find that command...",
    "Don’t think that command exists!",
    "Don’t think that command exists...",
    "Are you sure I can do that?",
    "Uh, I don’t think I can do that...",
    "Wait, I can do that?",
  )

  restrict = WeightedList(
    "Access denied",
    "Unauthouryzed access",
    "You can’t use that command",
    "Hold up, you aren’t allowed to use that command!",
  )

  future = WeightedList(
    "Working on it",
    "You can’t used that command yet",
    "You can’t used that command yet, but you will be able to soon",
  )

  require = WeightedList(
    "You need more vita points",
    "You need more vita points to use that command",
    "That command requires {} vita points to use",
  )


  init = WeightedList(
    "Initialyzation failed",
    "Identity initialyzation failed",
  )
  
  exist = WeightedList(
    "You already have an identity!",
    "Hey, you already have an identity!",
    "Hold up, you already have an identity!",
    "Your identity already exists!",
    "You’ve already got an identity",
  )

  identity = WeightedList(
    "Identity not found",
    "Didn’t find an identity",
    "Couldn’t find anyone",
    "Couldn’t find an identity",
    "Couldn’t find that user’s identity. Maybe they don’t have one?",
    "That identity doesn’t exist!",
  )


  colour = WeightedList(
    "Invalid colour",
    "Invalid colour provided",
    "Not a valid colour",
    "Just provide the raw colour code, no need to add `#` or `0x`",
  )

  date = WeightedList(
    "Invalid date",
    "Day out of range of month",
  )

  locale = WeightedList(
    "Invalid location",
    "I can’t set your location to that",
    "Can’t find that location",
    "Never heard of that place",
  )


  whoosh = WeightedList(
    "Really?",
    "Come on.",
    "Are you joking?",
    "You can’t be serious.",
    "What.",
    "How do you not get that!?",
    "Whoosh.",
  )


class aspire:
  play = WeightedList(
    "Game ongoing!",
    "Game already ongoing!",
    "There’s already a game ongoing!",
    "There’s already a game going on!",
  )

  thread = WeightedList(
    "You can't play a game within a thread",
    "I can’t initialyze a game within a thread",
  )

  direct = WeightedList(
    "I can’t initialyze a game in direct messages",
    "You can’t play a game in direct messages",
    "As cool as it would be, unfortunately I can’t initialyze a game in direct messages",
    "As cool as it would be, unfortunately you can’t play a game in direct messages",
  )

  wrong = WeightedList(
    "Incorrect",
    "Nope",
    "Don't think so",
    "That’s not it",
  )

  right = WeightedList(
    "Correct!",
    "Yeah!",
    "Yep!",
    "Nice!",
    "Alright!",
    "That’s it!",
    "You got it!",
    "Nice!",
    "Awesome!",
    "Congratulations!",
    "That’s correct!",
    "There we go!",
  )

  wait = WeightedList(
    "Waiting...",
    "Waiting for a guess...",
    "Waiting for an answer...",
  )

  time = WeightedList(
    "Timed out",
    "Game timed out",
    "Ran out of time",
    "Game expired!",
  )

  done = WeightedList(
    "Already guessed",
    "Already guessed before",
    "You’ve guessed that number before",
    "You’ve already guessed that number before",
  )

  number = [WeightedList(
    "Invalid number",
    "That’s not a number",
  ), WeightedList(
    "Needs to be an integer",
    "Guess must be an integer",
    "Guess has to be an integer",
    "We’re only playing with integers here!",
  )]

  emoji = [WeightedList(
    "Invalid emoji",
    "That’s not an emoji",
  ), WeightedList(
    "Emoji not in pool",
    "That emoji’s not in the pool",
  )]


class accede:
  affirm = [WeightedList(
    "I’m awake!",
    "Hey there!",
    "I’m ready to play!",
    "Hey, thanks for pinging me! I fall asleep sometimes.",
    "Is it dinnertime soon?",
  ), WeightedList(
    "Hey, no one’s pinged me in a while. Here, take some points!",
    "Wow, no one’s pinged me in a while. Here, take some points!",
  )]
  
  acquaint = [WeightedList(
    "I’m doing great!",
    "Yeah, I’m doing alright!",
    "Life’s good!",
  ), WeightedList(
    "Hey, thanks for asking! Take some points for being nice :adePenguin:",
    "Oh, now you’re trying to exploit the system? Well, I’ll take those points right back.",
    "Still more? The audacity, unbelievable. Fine, take your points.",
    (1, ["Stop asking me.", "Stop pestering me."]),
    "Now you’re just being pesky.",
    "Let me play in peace.",
  )]

  attrite = WeightedList(
    "You do realize I don’t have artificial intelligence, right?",
    "I don’t understand any of what you’re saying right now.",
    "Perhaps you could add ~ in front of your message :P",
    "I can search indexes, play complex games with lore, and operate an interconnected account system. Unfortunately, I don’t have artificial intelligence quite yet.",
  )

  allay = [
    ("Why do people find it so lonely in Antarctica?",
      "Cuz it’s so ice-o-lated!"),
    ("Why is it difficult to make friends in Antarctica?",
      "You can’t break the ice!"),
    ("What did the explorer say when he spotted Antarctica?",
      "I see land!",
      "‘Icy land’, geddit?"),
    ("Have you heard of the latest expedition to Antarctica?",
      "Yeah, things went south very quickly."),
    ("Why is Antarctica the least corrupt nation in the world?",
      "Cuz we have justice!",
      "We have ‘just ice’, geddit?"),
    ("What do you call a bear who’s been to both Antarctica and the Arctic?",
      "A bipolar bear!",
      "The bear’s been to both poles of the Earth, so it’s ‘bipolar’."),
    ("What do Antarcticans say when someone does something great?",
      "Freeze a jolly good fellow!",
      "‘He’s’ a jolly good fellow, geddit?"),
    ("Where do penguins go to dance?",
      "At the snow ball!"),
    ("What is a penguin’s favourite meal?",
      "An ice-berg-er!"),
    ("What do penguins drink out of?",
      "Beak-ers!"),
    ("How do penguins make pancakes?",
      "With their flippers!",
      "Their ‘flippers’ flip the pancakes, geddit?"),
    ("A group of flat-Earthers decided to come around to Antarctica.",
      "They were disappointed, but it wasn’t the end of the world."),
    ("What do you call kids in Antarctica?",
      "Chilldren!"),
    ("Why are arguments rare in Antarctica?",
      "Cuz everyone’s really chill!",
      "Chilly place, innit?"),
    ("What’s the drunkest animal in Antarctica?",
      "A pengwine!"),
    ("Why is Antarctican English spelling so controversial?",
      "It’s a polaryzing topic.",
      "It’s a ‘polarising’ topic. ‘Polarizing’ indeed."),
    ("Global warming seems really funny...",
      "Even the ice sheets are cracking up."),
    ("Who are the best at exploring Antarctica?",
      "The Polish!",
      "The ‘pole-ish’ people, geddit? Also, Polish people are actually known as ‘poles’. Isn’t that ironic~"),
    ("What did the Antarctican Technician say when programming?",
      "This is really code!",
      "This is ‘really cold’, geddit?"),
    ("Who’s married to Antarctica?",
      "Uncle Arctica!",
      "‘Aunt-arctica’, what a beautiful name."),
    ("What do you call a frozen dad in Antarctica?",
      "A pops-icle.",
      "\*sniff* pops \*sniff*"),
    ("What did the terrorists say when they invaded Antarctica?",
      "The ISIS everywhere.",
      "The ‘ice is’ everywhere! Except of course it’s not ice..."),
  ]


class ascent:
  action = WeightedList(
    "accelerating",
    "activating",
    "actuating",
    "adding",
    "adjust",
    "applying",
    "assembling",
    "asseverating",
    "assigning",
    "assimilating",
    "attaching",
    "attuning",
    "calibrating",
    "capacitating",
    "capturing",
    "catalyzing",
    "charging",
    "connecting",
    "constructing",
    "converging",
    "deploying",
    "developing",
    "equipping",
    "finalyzing",
    "fine-tuning",
    "firing",
    "fragmenting",
    "fusing",
    "gearing up",
    "harmonizing",
    "inducing",
    "inducting",
    "initializing",
    "initiating",
    "inserting",
    "installing",
    "integrating",
    "ionizing",
    "loading",
    "mechanizing",
    "modulating",
    "operating",
    "organizing",
    "preparing",
    "priming",
    "readying",
    "setting up",
    "striking",
    "transmitting",
    "tuning",
    "verging",
    "vertistrating",
  )

  arratus = WeightedList(
    "components", "gears", "parts",
    "central systems",
    "supercircuits", "anticircuits", "cryocircuits",
    "microquantum drivers",
    "metacells", "protocells",
    "petacells", "hexacells",
    "solar cells", "hydro cells",
    "shard cells", "mechanisis cells",
    "vita cells", "vita nodes",
    "Vitaline connection node",
    "modules", "micromodules", "macromodules",
    "regulators", "modulators", "pulsators",
    "seculators", "nodules",
    "fission pods", "fission nodes",
    "solar shards", "electro shards", "hydro shards", "control shards",
    "icicles", "krill remains", "fish bones",
  )

  attune = WeightedList(
    "ananalyzing",
    "balancing",
    "checking",
    "evolving",
    "examining",
    "fixing",
    "rectifying",
    "rejuvenating",
    "repairing",
    "synchronyzing",
    "terminating",
  )