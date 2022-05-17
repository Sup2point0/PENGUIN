from copy import deepcopy
import util


class item:
  def __init__(self, **features):
    self.index = False
    for feature in features:
      self.__setattr__(
        feature,
        features[feature] if feature != "content" else util.avast(features[feature], line = 0)
      )
  
  def show(self, alias = None):
    self = deepcopy(self)
    self.index = True
    if alias:
      self.alias = alias
    return self
  
  class field:
    def __init__(self, title, content, *, line = False):
      self.title = title
      self.content = util.avast(content, line = 0)
      self.line = line


class main:

  Antarctica = item(
    title = "United Nation of Antarctica",
    caption = "Country",
    content = f"""
      {util.icons.sound} /ænt'ɑːktɪkə/

      *Not to be confused with the __Continent of Antarctica__.*

      The Nation of Antarctica, officially the *United Nation of Antarctica*, otherwise simply known as ‘Antarctica‘, is a country spanning the entirety of the Antarctic continent of the same name, at the very south of the Earth. It has a moderate population of ~0.2 billion people. Due to its technological capabilities and extraordinarily harmonious society, it has risen to become a major global superpower.

      Antarctica is governed by the Foundation of Antarctica. Its capital city and centre of operations is Ross City, in the Aventurina district.

      Antarctica has its own calendar, festivals, and education system.

      Citizens of Antarctica are known as ‘Antarcticans’.
    """,
    other = "Continent of Antarctica, Colonies of Antarctica, Republic of Antarctica",
    tags = "main, antarctica, country, countries, home, start",
    url = "https://cdn.discordapp.com/attachments/925419481205968916/926779087073194014/Flag_of_Antarctica.jpg",
    more = "https://en.wikipedia.org/wiki/Antarctica",
  )

  Continent = item(
    title = "Continent of Antarctica",
    caption = "Geographical Continent",
    content = """
      *Not to be confused with the __Nation of Antarctica__.*

      The Continent of Antarctica, classification *Terra Antarcticus*, generally referred to as simply ‘Antarctica’, is a massive polar landmass located at the very south of the Earth. The natural continent consists of extremely thick and ancient ice. It is one of the coldest, driest and most barren places on Earth, although the inhabitance of humans has changed this.

      The natural climate is incredibly harsh, with temperatures remaining well below freezing throughout almost the entire year. For the most part, the natural continent is a polar desert. Snowfall is common, while rainfall is rare. Native wildlife includes phytoplankton, krill, seals, and of course Penguins. There are no naturally growing plants in Antarctica.
    """,
    other = "Nation of Antarctica",
    tags = "main, antarctica, continent, continents, natural, nato, home, start",
    url = "https://cdn.discordapp.com/attachments/925419481205968916/925419503322546216/Antarctica.png",
    more = "https://en.wikipedia.org/wiki/Antarctica",
  )

  Foundation = item(
    title = "Foundation of Antarctica",
    caption = "Governmental Body",
    content = """
      The Foundation of Antarctica, officially the *National Foundation of Antarctica*, also known as the Antarctic or Antarctican Foundation, is the main governmental body of the Nation Antarctica. Its current chairman is Alonzo Altan Ark.
    """,
    other = "Antarctica, Antarctican Trust",
    url = "https://cdn.discordapp.com/attachments/925419481205968916/928393382122909736/Foundation_of_Antarctica.jpg",
  )

  Trust = item(
    title = "Antarctican Trust",
    caption = "Governmental Organyzation",
    content = """
      The National Antarctican Trust is a special multi-purpose organyzation, whose activities involve funding projects, charitable ventures, healthcare and development, among many others.
    """,
    other = "Foundation of Antarctica",
  )

  SAME = item(
    title = "Sino-Antarctican Modern English",
    caption = "Language",
    content = """
      The official language of the Nation of Antarctica. A fusion of British, American and Antarctican English, as well as some Chinese influence, emphasyzing intuitivity and consistency.
    """,
    other = "Antarctican English, Old Antarctican English",
  )

  Marvels = item(
    title = "Marvels of Antarctica",
    caption = "",
    content = """
      The Marvels of Antarctica, officially the *Seven Natural And Technological Marvels of Antarctica*, is an official list of incredible, awe-inspiring, and generally marvellous things, which includes phenomena, structures, and items.

      The 7 Marvels are, in official order:

      Cyptoplankton
      CORE
      Esperanza Citadel
      The Geosphere + Geomatrix
      Icicle Fortress
      Vitaline Core + Vitaline Shard
      Inga Cavern of the Ancients
    """,
    other = "Each of the Marvels",
  )


class time:

  Calendar = item(
    title = "Modern Antarctican Calendar",
    caption = "Calendar System",
    content = """
      The Modern Antarctican Calendar, sometimes abbreviated as *MAC*, generally referred to as the ‘Antarctican calendar’, is the official calendar system of the Nation of Antarctica. It functions similarly to the Gregorian calendar, but with entirely unique times and names.

      The Modern Antarctican Calendar begins from 1 NE, which stands for ‘New Era’. Each year spans 365 days, with 366 on leap years. The year is split into 10 ‘decants’ (months), which alternate between 37 and 36 days long, respectively. Each year begins on Arteria Prime (April 2), the Antarctican New Year. ‘Septans’ (weeks) are 7 days long, so each decant has just over 5 septans. The ‘decate’ is the current day of the decant; the ‘septate’ is the current day of the septan. To ‘antect’ is to convert a date from the Gregorian calendar to the Antarctican calendar.

      The manner in which dates are written in does not vary. In their full form, dates are written in the format `‹septate› ‹decate› ‹decant› ‹year› ‹era›`, i.e. ‘Kynate 2 Arteria 200 NE’. The septate and era can both be omitted with the order shifting. However, when only including the decate and decant, the order is `‹decant› ‹decate›`, i.e. ‘Arteva 16’. The compact date, with only numbers, follows the format `‹decant› ‹decate› ‹year›`, i.e. ‘02|07|200’ (which would represent 7 Vitida 200 NE). The leading zeros can be omitted, but are often left for clarity.
    """,
    other = "Decant, Septan, Old Antarctican Calendar",
  )

  Decant = item(
    title = "Decant",
    caption = "Unit of Time",
    content = f"""
      {util.icons.sound} /'dɛkənt/

      The equivalent of a month in the Antarctican calendar. In a year, there are 10 decants that alternate between 37 and 36 days long. Each decant has its own name, as follows:

      Arteria
      Vitida
      Arrikta
      Valia
      Aliquanda
      Verita
      Arteva
      Vepida
      Aeva
      Verena

      Decants whose names begin with ‘a’ are 37 days long, and are known as *adecants*, while decants that start with ‘v’ are 36 days long, and are known as *vedecants*.

      2 decants (a pair consisting of an adecant and a vedecant) form a 73-day long ‘didecant’, which is a commonly used logistical measure of time. Functionally, it is useful in terms of length, and due to all didecants being equal in length.
    """,
    other = "Antarctican Calendar, Septan",
  )

  Decate = item(
    title = "Decate",
    caption = "Concept of Time",
    content = f"""
      {util.icons.sound} /'dɛkeɪt/

      The day of the decant in the Antarctican calendar. Usually, it is expressed as an integer ranging from 1 to 37; however, there are a few exceptions for special days:

      » The first day of a decant is called ‘prime’, i.e. ‘Verena Prime’.
      » The last day of a decant is called ‘fine’, i.e. ‘Aeva Fine’.
    """,
    other = "Antarctican Calendar, Septate",
  )

  Septan = item(
    title = "Septan",
    caption = "Unit of Time",
    content = f"""
      {util.icons.sound} /'sɛptən/

      The equivalent of a week in the Antarctican calendar. For the most part, it remains exactly the same as a week, being 7 days long; however, there is no such concept as weekdays and weekends – every day is a regular day.
    """,
    other = "Antarctican Calendar, Decant",
  )

  Septate = item(
    title = "Septate",
    caption = "Concept of Time",
    content = f"""
      {util.icons.sound} /'sɛpteɪt/

      The day of the septan in the Antarctican calendar. Each septate has its own name, unique from the Gregorian calendar:

        ...
    """,
    other = "Antarctican Calendar, Decate",
  )


  class decants:

    Arteria = item(
      title = "Arteria",
      caption = "Decant",
      content = f"""
        {util.icons.sound} /ɑː'tɛrɪə/
        {util.icons.value} Integrity

        The first decant of the year in the Antarctican calendar. It is named after the ancient warrior, Arterion.
      """,
      other = "Decant, Antarctican Calendar",
    )

    Vitida = item(
      title = "Vitida",
      caption = "Decant",
      content = f"""
        {util.icons.sound} /vɪ'tʌɪdə, vɪ'tiːdə, vʌɪ'tʌɪdə/
        {util.icons.value} Love
      """,
      other = "Decant, Antarctican Calendar",
    )

    Arrikta = item(
      title = "Arrikta",
      caption = "Decant",
      content = f"""
        {util.icons.sound} /'arɪktə/
        {util.icons.value} Resilience
      """,
      other = "Decant, Antarctican Calendar",
    )

    Valia = item(
      title = "Valia",
      caption = "Decant",
      content = f"""
        {util.icons.sound} /'veɪlɪə, ‘valɪə/
        {util.icons.value} Worth
      """,
      other = "Decant, Antarctican Calendar",
    )

    Aliquanda = item(
      title = "Aliquanda",
      caption = "Decant",
      content = f"""
        {util.icons.sound} /alɪ'kwandə/
        {util.icons.value} Hope
      """,
      other = "Decant, Antarctican Calendar",
    )

    Verita = item(
      title = "Verita",
      caption = "Decant",
      content = f"""
        {util.icons.sound} /'vɛrɪtə/
        {util.icons.value} Truth
      """,
      other = "Decant, Antarctican Calendar",
    )

    Arteva = item(
      title = "Arteva",
      caption = "Decant",
      content = f"""
        {util.icons.sound} /ɑː'teɪvə, ɑː'tɛvə/
        {util.icons.value} Light
      """,
      other = "Decant, Antarctican Calendar",
    )

    Vepida = item(
      title = "Vepida",
      caption = "Decant",
      content = f"""
        {util.icons.sound} /'vɛpɪdə/
        {util.icons.value} Warmth

        The eighth decant of the Antarctican calendar. It is the warmest decant of the year, being right at the peak of the Antarctican summer.
      """,
      other = "Decant, Antarctican Calendar",
    )

    Aeva = item(
      title = "Aeva",
      caption = "Decant",
      content = f"""
        {util.icons.sound} /'iːvə, ‘eɪvə/
        {util.icons.value} Time
      """,
      other = "Decant, Antarctican Calendar",
    )

    Verena = item(
      title = "Verena",
      caption = "Decant",
      content = f"""
        {util.icons.sound} /və'riːnə, ‘vɛrɪnə/
        {util.icons.value} Destiny

        The final decant of the year in the Antarctican calendar.
      """,
      other = "Decant, Antarctican Calendar",
    )


  class fest:
    
    Discovery = item(
      title = "Discovery Day",
      caption = "National Holiday",
      content = """
        An annual national holiday celebrated on Aeva 8, commemorating the day the Antarctica was first discovered continent, on 27 January 1820 by Fabian Bellingshausen and Mikhail Lakarev.
      """,
      other = "Antarctican Holidays, Tersolle",
    )

    Tersolle = item(
      title = "Tersolle",
      caption = "National Holiday",
      content = """
        An annual national holiday celebrated on Aeva 19, commemorating the day of the first successful landing on the Antarctica continent, on 7 February 1821 by John Davis.
      """,
      other = "Antarctican Holidays, Discovery Day",
    )

    Invict = item(
      title = "Invict Day",
      caption = "National Holiday",
      content = """
        An annual national holiday celebrated on Vepida Prime, commemorating the day Roald Amundsen reached the True South Pole, 14 December 1911.
      """,
      other = "Antarctican Holidays, Falcon’s Noon, Roald Amundsen",
    )

    Falcon = item(
      title = "Falcon’s Noon",
      caption = "National Holiday",
      content = """
        An annual national holiday, originally celebrated informally but now officially recognyzed, taking place on Verena 33. It is held in remembrance of the day Sir Robert Falcon Scott died when returning from reaching the South Pole, 29 March 1912.
      """,
      other = "Antarctican Holidays, Invict Day, Robert Scott",
    )


class geo:

  class dist:

    District = item(
      title = "District",
      caption = "Administrative Division",
      content = """
        Districts are major administrative regions the Nation of Antarctica is divided into. They do not have a local ruler or government, but do have a council that can report to the Foundation of Antarctica.

        There are a total of 12 districts, each with their own unique name:

        Aventurina
        Atalla
        Ascerta
        ...
        Titeria
        Tyrestra
        Divelda
        Dessica
        Dicenda

        Districts from different eras have names that start with a certain letter. In descending ancestral order:

        A » New Antarctica
        T » Republic of Antarctica
        D » Ancient Anarchy

        Districts should generally referred be to as ‘the District’, i.e. *the Aventurina district*. When used in conjunction with a city name, the format should be ‘<city>, <district>’, i.e. *Alta, Atalla*.
      """,
      other = None,
    )

    Aventurina = item(
      title = "Aventurina District",
      caption = "District of Antarctica",
      content = f"""
        {util.icons.sound} /ə'vɛntʃə'riːnə/

        The prime district of Antarctica, comprised of 5 cities, including the capital, Ross City. It is located in Central Antarctica. It is named after aventurine, the national gemstone of Antarctica.
      """,
      fields = [
        item.field("Cities",
          content = """
            Ross City
            Archadia
          """,
        ),
        item.field("Notable Landmarks",
          content = """
            Geomatrix Core
            Ross Academy
            Antarctic Arcade
          """,
        ),
      ],
      other = "District, Ross City",
    )

    Atalla = item(
      title = "Atalla District",
      caption = "District of Antarctica",
      content = f"""
        {util.icons.sound} /ə'tʰɑlə, ə'talə/

        *Not to be confused with the city, Atla.*

        A modern district of Antarctica, comprised of 12 cities. It is named after Atalon, a mythical place told of in Antarctican legends.
      """,
      fields = [
        item.field("Cities",
          content = """
            Atla
          """,
        ),
        item.field("Notable Landmarks",
          content = """
            NioTech
          """,
        ),
      ],
      other = "District, Atla, Atalon",
    )

    Ascerta = item(
      title = "Ascerta District",
      caption = "District of Antarctica",
      content = f"""
        {util.icons.sound} /ə'səːtə, a'skəːtə/

        A district of Antarctica, comprised of 7 cities.
      """,
      fields = [
        item.field("Notable Landmarks",
          content = """
            Lakara
          """,
        ),
      ],
      other = "District, Aleta",
    )

    Titeria = item(
      title = "Titeria District",
      caption = "District of Antarctica",
      content = f"""
        {util.icons.sound} /tʌɪ'tɛrɪə/
      """,
      other = "District",
    )

    Tyrestra = item(
      title = "Tyrestra District",
      caption = "District of Antarctica",
      content = f"""
        {util.icons.sound} /tɪ'rɛstrə/
      """,
      other = "District",
    )

    Divelda = item(
      title = "Divelda District",
      caption = "District of Antarctica",
      content = f"""
        {util.icons.sound} /dɪ'vɛldə/
      """,
      other = "District",
    )

    Dessica = item(
      title = "Dessica District",
      caption = "District of Antarctica",
      content = f"""
        {util.icons.sound} /'dɛsɪkə/
      """,
      other = "District",
    )

    Discenda = item(
      title = "Discenda District",
      caption = "District of Antarctica",
      content = f"""
        {util.icons.sound} /dɪ'sɛndə, ‘dʌɪsɛndə/
      """,
      other = "District",
    )


  class city:

    # Aventurina District
    Ross = item(
      title = "Ross City",
      caption = "Capital City",
      content = """
        *For the historical figure, see __James Ross__.*

        The capital city of Antarctica. Located in the central Aventurina district, it is a colossal metropolis and one of the most economically, technologically and socially developed cities in the world. It is named after Sir James Clark Ross.
      """,
      other = "Aventurina District, James Ross",
    )

    Archadia = item(
      title = "Archadia",
      caption = "City of Antarctica",
      content = f"""
        {util.icons.sound} /ɑː'keɪdɪə/

        A city in the Aventurina district.
      """,
      other = "Aventurina District",
    )

    # Atalla District
    Atla = item(
      title = "Atla",
      caption = "City of Antarctica",
      content = f"""
        {util.icons.sound} /ɑtlə/

        *For the District, see __Atalla District__.*

        The prime city of the Atalla district.
      """,
      other = "Atalla District",
      fields = [
        item.field("Landmarks",
          content = """
            NioTech
          """,
        ),
      ],
    )

    # Ascerta District
    Aleta = item(
      title = "Aleta",
      caption = "City of Antarctica",
      content = f"""
        {util.icons.sound} /ə'lɛtə/

        *Not to be confused with __Atla__, a city in the Atalla District.*
      """,
      other = "Ascerta District",
    )

    Axona = item(
      title = "Axona",
      caption = "City of Antarctica",
      content = f"""
        {util.icons.sound} /aksəʊnə/
      """,
      other = "Ascerta District",
    )

    # Divelda District
    Novada = item(
      title = "Novada",
      caption = "City of Antarctica",
      content = f"""
        {util.icons.sound} /nə'vɑːdə/
      """,
      other = "Divelda District",
    )

    Teneca = item(
      title = "Teneca",
      caption = "City of Antarctica",
      content = f"""
        {util.icons.sound} /'tɛnəkə, ‘tɛnɪkə/
      """,
      other = "Divelda District",
    )

    Yena = item(
      title = "Yena",
      caption = "City of Antarctica",
      content = f"""
        {util.icons.sound} /'yɛnə/
      """,
      other = "Divelda District",
    )

    # Dessica District
    Escharcha = item(
      title = "Escharcha",
      caption = "City of Antarctica",
      content = """
      """,
      other = "Dessica District",
    )

    Panaxa = item(
      title = "Panaxa",
      caption = "City of Antarctica",
      content = f"""
        {util.icons.sound} /pə'naxə/
      """,
      other = "Dessica District"
    )

    # Discenda District
    Vanqua = item(
      title = "Vanqua",
      caption = "City of Antarctica",
      content = f"""
        {util.icons.sound} /'vaŋkwə/
      """,
      other = "Discenda District",
    )

    Anarcha = item(
      title = "Anarcha",
      caption = "City of Antarctica",
      content = f"""
        {util.icons.sound} /a'nɑːkə, ə'nɑːkə/
      """,
      other = "Discenda District",
    )

    Helada = item(
      title = "Helada",
      caption = "City of Antarctica",
      content = """
      """,
      other = "Discenda District",
    )


class loc:

  Carrot = item(
    title = "CARROT",
    acro = "the Central Amundsen-Ross Reconnaissance and Operations Tower",
    caption = "Structure",
    content = """
      The Central Amundsen-Ross Reconnaissance and Operations Tower is a tall structure that acts as a central control tower for all of Antarctica, involving broadcasts, communications, etc. It is located in the centre of Ross City.
    """,
    other = "Ross City",
  )

  Rubicon = item(
    title = "Rubicon Valley",
    caption = "Geographical Location",
    content = """
    """,
    other = None,
  )

  Atalon = item(
    title = "Atalon",
    caption = "Legendary Location",
    content = """
    """,
    other = "Atalos, Atalla",
  )


class edu:

  System = item(
    title = "Education System of Antarctica",
    caption = "Logistical System",
    content = """
      The Education System of Antarctica, officially the *Formal Education System of Antarctica*, sometimes abbreviated as ‘FESA’, is the official education system of education in Antarctica, that all children are legally required to undergo.

      Formal education begins at the age of 4. Informal, or ‘casual’ education can be optionally received earlier at the parents’ discretion. It is compulsory for all children to go through at least 12 years of formal education (to age 16), and almost all will complete 16 years (age 20). In its entirety, it can span up to 21 years.

      There are 4 stages of education:

      Foundational (4-8)
      Lower (8-13)
      Prime (13-20)
      Higher (20-25)

      Unlike most other countries, Antarctica’s education system is not based on one’s year of birth, but rather one’s didecant of birth; so children are sorted into classes with others born in the same didecant. This ensures no one has an unfair advantage or disadvantage due to starting education earlier or later.
    """,
    other = "Each of the stages of education",
  )

  Foundational = item(
    title = "Foundational Education",
    caption = "Stage of Education",
    content = f"""
      {util.icons.clock} Age 4-8

      Also known as ‘basic’ education, foundational education is the first stage of education in Antarctica, spanning 4 years. It is equivalent to ‘kindergarten’ or ‘infant’ education in other countries.
    """,
    other = "Education System of Antarctica",
  )

  Lower = item(
    title = "Lower Education",
    caption = "Stage of Education",
    content = f"""
      {util.icons.clock} Age 8-13

      The second stage of education in Antarctica, spanning 5 years. It is equivalent to ‘elementary’ or ‘junior education’ in other countries.
    """,
    other = "Education System of Antarctica",
  )

  Prime = item(
    title = "Prime Education",
    caption = "Stage of Education",
    content = f"""
      {util.icons.clock} Age 13-20

      The third and main stage of education in Antarctica. It is the longest of all, spanning up to 7 years. Since it is only required for children to complete 16 years of formal education, some will choose to leave early at age 18 or even 16, for reasons such as special careers, content creation, personal pursuits, etc.

      It is equivalent to ‘secondary’ education in other countries.
    """,
    other = "Education System of Antarctica",
  )

  Higher = item(
    title = "Higher Education",
    caption = "Stage of Education",
    content = f"""
      {util.icons.clock} Age 20-25

      Also known as ‘further’ or ‘specialyzed’ education, higher education is an additional fourth stage of education in Antarctica. It is only required for highly specialyzed professions where further training is necessary. The duration varies depending on the particular profession, but will not exceed 5 years (as always, there are rare exceptions).
    """,
    other = "Education System of Antarctica",
  )


  class uni:

    Universities = item(
      title = "Universities of Antarctica",
      caption = "Categoryzer",
      content = """
        Scott University
        Amundsen College
        Ross Academy

        NioTech
        Royal Academy Of Geoengineering
        Lakara
        Evelyn Institute of Exploration
        Ingra-Shackleton Academy of Bioengineering
      """,
      other = "Education System of Antarctica",
    )

    Scott = item(
      title = "Scott University",
      caption = "University of Antarctica",
      content = """
      """,
      other = "Amundsen College, Ross Academy",
    )

    Amundsen = item(
      title = "Amundsen College",
      caption = "University of Antarctica",
      content = """
      """,
      other = "Scott University, Ross Academy",
    )

    Ross = item(
      title = "Ross Academy",
      caption = "University of Antarctica",
      content = """
        A school located in the capital, Ross City. It offers primary through secondary education.
      """,
      other = "Scott University, Amundsen College",
    )

    Nio = item(
      title = "NioTech",
      caption = "University of Antarctica",
      content = """
        The National Institute Of Technology, generally known as ‘NioTech’, is a university of Antarctica located in Atla, Atalla.
      """,
      other = "ROAG",
    )

    ROAG = item(
      title = "ROAG",
      acro = "the Royal Academy Of Geoengineering",
      caption = "University of Antarctica",
      content = """
        The Royal Academy Of Geoengineering, commonly known as ‘ROAG’, is a university of Antarctica located in Teneca, Divelda.

        It has been noted that the actual acronym for the university is ‘RAOG’, however for pronunciation and readability purposes ‘ROAG’ is used instead. A long-running joke among the students is that this will forever be ‘a geo’-engineering (the letters A, G and O, referencing the mixed up letters in the acronym) problem that can never be fixed.
      """,
      other = "NioTech",
    )

    Lakara = item(
      title = "Lakara",
      acro = "the Lazarev & Klenova Academy of Research & Advancement",
      caption = "University of Antarctica",
      content = """
        The Lazarev & Klenova Academy of Research & Advancement, generally known as ‘Lakara’, is a university of Antarctica located in Aleta, Ascerta.
      """,
      other = None,
    )

    Evelyn = item(
      title = "Evelyn Institute of Exploration",
      caption = "University of Antarctica",
      content = """
        A school specialyzing in exploration and survival skills.
      """,
      other = None,
    )

    ISAB = item(
      title = "Ingra-Shackleton Academy of Bioengineering",
      caption = "University of Antarctica",
      content = """
        The Ingra-Shackleton Academy of Bioengineering (ISAB) is a university of Antarctica.
      """,
      other = None,
    )


class tech:

  Geosphere = item(
    title = "The Geosphere",
    caption = "Technological Device",
    content = """
      *For the device that generates and maintains the Geosphere, see __Geomatrix__.*

      A massive spherical dome that permanently covers the entirety of the Antarctic mainland, controlling the climate within and maintaining suitable temperatures. For energy conservation reasons, the Geosphere only raises temperatures slightly above freezing; citizens rely on their much more efficient COREs to keep comfortable body temperatures.

      The Geosphere also acts as an impenetrable shield, protecting Antarctica from both natural hazards and external threats. Most projectiles or entities cannot pass through; but if exceptionally fast, can briefly enter, before being deflected. Human contact will result first in an unpleasant sensation, then severe discomfort, and if further pushed, loss of neural control (but never death).

      The Geosphere is one of the __Seven Marvels of Antarctica__.
    """,
    other = "The Geomatrix, CORE",
  )

  Geomatrix = item(
    title = "The Geomatrix",
    caption = "Technological Device",
    content = """
      *Not to be confused with __the Geosphere__.*

      The source of the Geosphere. A highly advanced technological device...
    """,
    other = "The Geosphere",
  )


  class core:

    CORE = item(
      title = "Core Of Residence",
      caption = "Technological Device",
      content = """
        A special metabioelectric-powered device installed above the chest, that enhances a multitude of essential life processes; most notably maintaining body temperature, allowing humans to reside comfortably in the geosphere, and survive in natural conditions in rare situations.

        There are many variants, each serving different purposes, that can be permanent or temporary. The most common types are the A-CORE and V-CORE. Other specialyzed types include the:

        E-CORE
        S-CORE
        W-CORE
        I-CORE

        The CORE is one of Antarctica’s proudest technological innovations, and has been paramount in its rapid development for such a barren landscape. As such, it is one of the Seven Marvels of Antarctica.
      """,
      other = "ADE"
    )

    A = item(
      title = "Antarctican Core Of Residence",
      caption = "CORE Variant",
      content = """
        A standard CORE installed on all long-term residents of Antarctica. Enhances a multitude of essential life processes, most notably maintaining body temperature. Also monitors health, constantly checking for diseases and infections, while also being able to administer medication itself. Does not provide any meaningful effects in battle.

        An A-CORE is not required to be a citizen of Antarctica, but is generally recommended. Installation is painless, although can take up to 12 hours. Most native Antarcticans have theirs installed by the age of 12. It is designed to be permanent, but can be perfectly safely removed, should the need arise.
      """,
      other = "ARC, CORE, V-CORE",
    )

    V = item(
      title = "Visitor’s Core Of Residence",
      caption = "CORE Variant",
      content = """
        A temporary CORE attached to all visitors, providing some of the benefits of an A-CORE. Visitors must have theirs attached to enter Antarctica. Also has tracking capabilities to monitor visitors.
      """,
      other = "AVA, CORE, A-CORE",
    )

    E = item(
      title = "Electrical Core Of Residence",
      caption = "CORE Variant",
      content = """
      """,
      other = "CORE",
    )

    S = item(
      title = "Specialyzed Core Of Residence",
      caption = "CORE Variant",
      content = """
      """,
      other = "CORE",
    )

    W = item(
      title = "Weaponyzed Core Of Residence",
      caption = "CORE Variant",
      content = """
        A special CORE installed on some high-ranking or important Military personnel. As well as boosting physical strength and stamina, it enhances other elekine-based weapons and has both destructive and defensive capabilities itself.
      """,
      other = "CORE",
    )

    I = item(
      title = "Invulnerable Core Of Residence",
      caption = "CORE Variant",
      content = """
        A highly exclusive CORE, reserved for only people of the utmost importance. Renders the user totally impervious to all forms of physical damage, essentially granting them invulnerability.
      """,
      other = "CORE",
    )


class medi:

  Niccolu = item(
    title = "Niccolu",
    caption = "Infectious Disease",
    content = """
    """,
    other = "CLOMS, EDAICS",
  )

  CLOMS = item(
    title = "CLOMS",
    acro = "Concerningly Low Metabolism Syndrome",
    caption = "Degenerative Disease",
    content = """
      Concerningly Low Metabolism Syndrome (CLOMS), commonly referred to as ‘Drain’, is a degenerative disease where the body’s vital metabolism is significantly lower than normal. It can usually be solved with simply an A-CORE, which enhances metabolism. In especially severe cases, it can lead to EDAICS.

      The cause for CLOMS remains unknown.
    """,
    other = "EDAICS",
  )

  EDAICS = item(
    title = "EDAICS",
    acro = "Energy Deficient AutoImmune Collapse Syndrome",
    caption = "Hypergenerative Disease",
    content = """
      Energy Deficient AutoImmune Collapse Syndrome (EDAICS) is a hypergenerative disease caused by severe CLOMS.
    """,
    other = "CLOMS",
  )


class mili:

  class div:

    Terra = item(
      title = "Terra Forza",
      caption = "",
      content = """
        The ground force of the Antarctican Military, officially classified and referred to as *Terra Forza*, also known as the ‘Antarctican Ground Force’.
      """,
      other = "Nava Corza, Aera Norza, Ginga Ranza",
    )

    Nava = item(
      title = "Nava Corza",
      caption = "",
      content = """
        The naval force of the Antarctican Military, officially classified and referred to as *Nava Corza*, also known as the ‘Antarctican Naval Corps’.
      """,
      other = "Terra Forza, Aera Norza, Ginga Ranza",
    )

    Aera = item(
      title = "Aera Norza",
      caption = "",
      content = """
        The air force of the Antarctican Military, officially classified and referred to as *Aera Norza*, also known as the ‘Antarctican Aeronauts’.
      """,
      other = "Terra Forza, Nava Corza, Ginga Ranza",
    )

    Ginga = item(
      title = "Ginga Ranza",
      caption = "",
      content = """
        The space force of the Antarctican Military, officially classified and referred to as *Ginga Ranza*, also known as the ‘Antarctigalactic Front’.
      """,
      other = "Terra Forza, Nava Corza, Aera Norza",
    )

    ASDF = item(
      title = "Antarctican Special Defence Force",
      caption = "",
      content = """
        The Antarctic Special Defence Force (ASDF), sometimes referred to as the ‘Antarctican Specialyzed Defence Forces’, is the special forces of Antarctican Military.
      """,
      other = None,
    )


  class awards:

    ASMR = item(
      title = "Antarctican Seal of Military Recognition",
      caption = "Award",
      content = """
        A special award given to soldiers who demonstrate remarkable military achievement or devotion.
      """,
      other = "RESOUND",
    )

    RESOUND = item(
      title = "RESOUND",
      acro = "Royal Elite Seal Of Undying Dedication",
      caption = "Award",
      content = """
        The Royal Elite Seal Of Undying Dedication (RESOUND), colloquially referred to as ‘RES’, is a highly prestigious and honourable Antarctican award, given to individuals who have demonstrated outstanding dedication and/or made significant contributions to Antarctica.

        The awardee does not have to be, and indeed is frequently not, alive; the award is often awarded to people who have given their lives. Examples of awardees and reasons include #.
      """,
      other = "ASMR",
    )


class hist:

  class fig:

    Amundsen = item(
      title = "Roald Amundsen",
      caption = "Historical Explorer",
      content = f"""
        {util.icons.clock} 16 July 1872 ~ 18 June 1928

        Roald Amundsen, full name *Roald Engelbregt Gravning Amundsen*, was a Norwegian explorer, and the first person to reach the geographic South Pole, in the legendary Race to the South Pole between him and Robert Scott.
      """,
      other = "Robert Scott",
    )

    Scott = item(
      title = "Robert Scott",
      caption = "Historical Explorer",
      content = f"""
        {util.icons.clock} 6 June 1868 ~ 29 March 1912

        Robert Scott, full name *Robert Falcon Scott*, officially *Captain Robert Falcon Scott CVO*, was a British explorer and captain in the Royal Navy. He is known for his valiant and honourable efforts in the legendary Race to the South Pole between him and Roald Amundsen, narrowly losing to Amundsen by just over a month.
      """,
      other = "Roald Amundsen",
    )

    Ross = item(
      title = "James Ross",
      caption = "Historical Explorer",
      content = f"""
        {util.icons.clock} 15 April 1800 ~ 3 April 1862

        James Ross, full name *James Clark Ross*, officially *Sir James Clark Ross FRS FLS FRAS*, was a British explorer and officer in the Royal Navy. He is known for his contributions to the discovery and exploration of Antarctica, through various pioneering expeditions.
      """,
      other = "",
    )

    Lynuca = item(
      title = "Lynuca Veritori",
      caption = "Ascendant of Antarctica",
      content = """
        Lynuca Veritori, full name *Lynucanes Istra Veritorious*, colloquially referred to as ‘Lyn Veri’, was the final Ascendant of the Ancient Anarchy era, and the founder of the Republic of Antarctica.
      """,
      other = "Ancient Anarchy, Republic of Antarctica",
    )

    Detrin = item(
      title = "Detrin Viruna",
      caption = "Ascendant of Antarctica",
      content = """
        Detrin Viruna, true name unknown, generally known as ‘The Dark Emperor’, was an Ascendant of Antarctica during the Ancient Anarchy era.
      """,
      other = "Ancient Anarchy, Anatrin Anaconda",
    )

    Anatrin = item(
      title = "Anatrin Anaconda",
      caption = "Ascendant of Antarctica",
      content = """
        Anatrin Anaconda, true name unknown, generally known as ‘The Dark Sovereign’, was an Ascendant of Antarctica during the Ancient Anarchy era.
      """,
      other = "Ancient Anarchy, Detrin Viruna",
    )

    Alonzo = item(
      title = "Alonzo Altan Ark",
      caption = "Figure",
      content = """
        Alonzo Ark, full name *Alonzo Altan Ark*, is the chairman of the Foundation of Antarctica.

        He has been given many nicknames, including ‘Alo’, ‘Zo’, and ‘Lark’.
      """,
      other = "Foundation of Antarctica, Adelina Altan Ark",
    )

    Adelina = item(
      title = "Adelina Altan Ark",
      caption = "Figure",
      content = """
        Adelina Ark, full name Adelina Altan Ark, is the wife of Alonzo Altan Ark, and chairman of the National Antarctican Trust.
      """,
      other = "National Antarctican Trust, Alonzo Altan Ark",
    )


  class stat:

    Timeline = item(
      title = "Timeline of Antarctican History",
      caption = "Categoryzer",
      content = """
        This page lists all the eras and notable events in the history of Antarctica.
      """,
      fields = [
        item.field("Ancient Antarctica",
          content = """
          """,
        ),
        item.field("The South Lands",
          content = """
            *Terra Australis Incognita*
          """,
        ),
        item.field("The South Pole",
          content = """
            *Terra Australis*

            Heroic Age of Antarctic Exploration
          """,
        ),
        item.field("Colonies of Antarctica",
          content = """
            Wilkes War
            Native Uprising
            » Battle of Amundsen Peak
            » Antarctic Peninsula Catastrophe
            The First Fall
          """,
        ),
        item.field("Ancient Anarchy",
          content = """
            Dark Era
            Tyranny of Tiberius
          """,
        ),
        item.field("Republic of Antarctica",
          content = """
            Iron Era
            Golden Era
            Silver Era
            Ruby Era
            Platinum Era
            Ross Rebellion
            Downfall
            Second Reformation
          """,
        ),
        item.field("New Antarctica",
          content = """
            Revitalyzation
          """,
        ),
        item.field("United Nation of Antarctica",
          content = """
          """,
        ),
      ],
      other = "Historical Figures of Antarctica",
    )

    Figures = item(
      title = "Historical Figures of Antarctica",
      caption = "Categoryzer",
      content = """
        This page lists all notable figures in the history of Antarctica.
      """,
      fields = [
        item.field("Ancient Antarctica",
          content = """
            Dessica Dew
          """,
        ),
        item.field("The South Pole",
          content = """
            Roald Amundsen
            Robert Scott
            James Ross
          """,
        ),
        item.field("Ancient Anarchy",
          content = """
            Detrin Viruna
            Anatrin Anaconda
          """,
        ),
        item.field("Republic of Antarctica",
          content = """
            Lynuca Veritori
          """,
        ),
        item.field("New Antarctica",
          content = """
          """,
        ),
      ],
      other = "Timeline of Antarctican History",
    )

    Ascendant = item(
      title = "Ascendant",
      caption = "Ruling Position",
      content = """
        An ancient term used to refer the emperors, sovereigns and other rulers who took power during the eras of Ancient Anarchy and the Republic of Antarctica.

        e.g.
        *The new Ascendant was feared by all.*

        ‘Ascendant’ should be capitalyzed in general use.
      """,
      fields = [
        item.field("Notable Ascendants",
          content = """
            Lynuca Veritori
            Detrin Viruna
            Anatrin Anaconda
          """,
        ),
      ],
      other = "Ancient Anarchy, Republic of Antarctica",
    )


  class era:

    Ancient = item(
      title = "Ancient Antarctica",
      caption = "Historical Era",
      content = f"""
        {util.icons.clock} Unclassified
        
        Ancient Antarctica, classified *Antarctica Anteactus*, refers to the era before any humans set foot on or even knew about Antarctica.
      """,
      other = None,
    )

    Colonies = item(
      title = "Colonies of Antarctica",
      caption = "Historical Era",
      content = f"""
        *Not to be confused with the __Antarctic Colonies__.*

        {util.icons.clock} 21st Century ~ Cotalivita 1 SE

        The Colonies of Antarctica refers to the era where the continent of Antarctica was colonyzed by multiple different countries. It is succeeded by Ancient Anarchy; and loosely preceded by ‘The South Pole’ era.
      """,
      other = None,
    )

    Anarchy = item(
      title = "Ancient Anarchy",
      caption = "Historical Era",
      content = f"""
        {util.icons.clock} Cotalivita 1 SE ~ 376 SE

        Ancient Anarchy refers to the era where the continent of Antarctica was in a continuous state of anarchy, with numerous Ascendants seizing supreme power. It is preceded by the Colonies of Antarctica, and succeeded by the Republic of Antarctica.
      """,
      other = None,
    )

    Republic = item(
      title = "Republic of Antarctica",
      caption = "Historical Country",
      content = f"""
        {util.icons.clock} 1 Investra 1 RE ~ 25 Sevestra 651 RE

        The Republic of Antarctica, officially *The Primal Republic of Antarctica*, was a republic. It is preceded by Ancient Anarchy, and succeeded by New Antarctica.
      """,
      other = None,
    )

    New = item(
      title = "New Antarctica",
      caption = "Historical Country",
      content = f"""
        {util.icons.clock} Arteria Prime 1 NE ~ Verena 201 NE

        New Antarctica refers to the era ~. It is preceded by Republic of Antarctica, and succeeded by the United Nation of Antarctica.
      """,
      other = "Antarctica",
    )


class nato:

  Aurora = item(
    title = "Aurora Australis",
    caption = "Natural Marvel",
    content = """
      The Antarctic Lights, officially classified *Aurora Australis*, also known as ‘The Southern Lights’, are a series of naturally occurring light displays, in the form of supercolourful wavy lines. They are also colloquially referred to as ‘The Lights’, jokingly referred to as ‘Aurora Australis Antarcticus’, or otherwise simply known as ‘[the] Aurora’.
    """,
    other = "Continent of Antarctica",
  )

  Plankton = item(
    title = "Photoplankton",
    caption = "Micro-Organism",
    content = """
      A special type of phytoplankton found in the deeper waters of Antarctica.
    """,
    other = None,
  )

  Coli = item(
    title = "Ni. Coli",
    caption = "Species of Bacterica",
    content = """
      A special type of bacteria that thrives in the natural conditions of Antarctica. It is the natural cause of Niccolu.
    """,
    other = "Niccolu"
  )

  
  class cryst:

    Opal = item(
      title = "Simmering Opal",
      caption = "Crystalline Gemstone",
      content = """
        Nato-Operium Intrisite Cryo-Variat, commonly known as ‘Simmering Opal’, also known as ‘Trekker’s Treasure’, is a special type of rare gemstone found naturally in Antarctica.
      """,
      other = None,
    )

    Essence = item(
      title = "Antarctic Essence",
      caption = "Supercompound",
      content = """
        Vericium Ultri, commonly known as ‘Antarctic Essence’, also known as ‘Celestial Essence’, is a special type of supercompound existing in Antarctica.
      """,
      other = None,
    )


class misc:

  Atalos = item(
    title = "Atalos",
    caption = "Legendary Protector",
    content = f"""
      {util.icons.sound} /a'tʰɑlɒs, ə'talə/
    """,
    other = "Atalon, Atalla",
  )

  ARCANE = item(
    title = "ARCANE",
    acro = "Antarctican Royal Consortium for the Authentication/Application of New Elements",
    caption = "Organyzation",
    content = """
      The Antarctican Royal Consortium for the Authentication/Application of New Elements (ARCANE), is an organyzation.
    """,
    other = "ASCENSE",
  )

  ASCENSE = item(
    title = "ASCENSE",
    acro = "Antarctican Scientific Complete Enumeration of Natural and Synthesyzed Elements",
    caption = "Concept",
    content = """
      The Antarctican Scientific Complete Enumeration of Natural and Synthesyzed Elements (ASCENSE) is the Antarctican extended version of the complete Periodic Table of the Elements.
    """,
    other = "ARCANE",
  )

  Nuclear = item(
    title = "Nuclear Armaments of Antarctica",
    caption = "Concept",
    content = """
    """,
    other = "RETINA",
  )

  RETINA = item(
    title = "RETINA",
    acro = "Regularly Enforced Treaty for the Inhibition of Nuclear Armaments",
    caption = "Diplomatic Agreement",
    content = """
      The Regularly Enforced Treaty for the Inhibition of Nuclear Armaments (RETINA), generally referred to as ‘Retina’ (capitalyzed), is a diplomatic treaty by the Foundation of Antarctica, the Antarctican Trust, and various other organyzations, to restrict the development, creation, and use of nuclear armaments and other destructive devices.

      The treaty comprises of 9 parts, each covering a particular aspect or field of nuclear weaponry. In summary, the treaty has 4 aims:

      » Inhibit the activation and use of nuclear armaments, except as a last-resort measure of self-defence
      » Restrict the development of nuclear weaponry, except for authouryzed research purposes
      » Limit the deadliness of all nuclear weapons created, so as to avoid a global nuclear catastrophe
      » Limit how many nuclear armaments are kept in storage by the Antarctican Military

      Retina is reviewed every 2 years, and formally revised every 20 years. However, it has been said that it is “highly unlikely” that the aims and views it expresses will change.
    """,
    other = "Foundation of Antarctica, Nuclear Armaments of Antarctica",
  )

  supcode = item(
    title = "supcode",
    caption = "Programming Language",
    content = """
      Supcode, officially *supcode* (uncapitalyzed), is a high-level general-purpose interpreted programming language. It is extremely widespread in Antarctica, used to program everything from automated devices to ADEs.
    """,
    other = "Sup#2.0",
  )


class disc:

  class ade:

    ADE = item(
      title = "ADE",
      caption = "Technological Class",
      content = f"""
        {util.icons.sound} /eɪd/

        An Artificial/Automated/Assisstive Digital(yzed) Entity (ADE) is a programmed bot, that can have artificial intelligence or just simply respond to commands, and may or may not have a solid, corporeal form.
      """,
      other = "CORE, Adeline",
    )

    Adeline = item(
      title = "Adeline",
      caption = "Concept",
      content = f"""
        {util.icons.sound} /'eɪdlʌɪn/
        
        *Not to be confused with __Adelina Altan Ark__.*

        A particular line of ADEs, wherein each generation replaces the last.

        ‘Adeline’ should be capitalyzed in general use.
      """,
      other = "ADE",
    )

    Sup = item(
      title = "Sup#0.2",
      caption = "ADE",
      content = """
        The personal ADE of Sup#2.0.
      """,
      other = "ADE, Sup#2.0",
    )

    Shard = item(
      title = "SHARD",
      acro = "SuperHuman Administrative and Regulative Discord Bot",
      caption = "ADE",
      content = """
        SuperHuman Administrative and Regulative Discord Bot, officially *SHARD-bot*, generally known as ‘SHARD’ or ‘Shard’, is the main administrative ADE of the Foundation of Antarctica. It governs and administrates everything to do with the Discord server, such as role distribution and behavioural moderation.

        SHARD is the 3rd generation of its Adeline, preceded by SPARK and SHIVER.
      """,
      other = "ADE, PENGUIN",
    )

    Penguin = item(
      title = "PENGUIN",
      acro = "Playful & Energetic New General Utility & Information Network Bot",
      caption = "ADE",
      content = """
        Playful & Energetic New General Utility & Information Network Bot, officially *PENGUIN-bot*, generally known as ‘PENGUIN’ or simply ‘Penguin’, is the masbot ADE of Antarctica. It is known for being upbeat and positive. Its main advanced feature is a humongous database of Antarctica-related knowledge and information, which you are using right now. It is also the only ADE that currently has AI (augmented intelligence).

        PENGUIN is the 2nd generation of its Adeline, preceded by EDEN, as well as the failed early prototype ATLAS.
      """,
      other = "ADE, SHARD",
    )

    Absolute = item(
      title = "ABSOLUTE",
      acro = "Antarctican Bot for Special Operations & Legendary Undercover Technological Excursions",
      caption = "ADE",
      content = """
      """,
      other = "ADE",
    )


class egg:

  Egg = item(
    title = "Easter Egg",
    acro = "???",
    caption = "Easter Egg",
    content = "A hidden secret in my database.",
    surplus = "+20,000 points",
    points = 20000,
  )

  Rare = item(
    title = "Easter Egg",
    acro = "???",
    caption = "*Rare*",
    content = "Nice.",
    surplus = "+35,000 points",
    points = 35000,
  )

  Epic = item(
    title = "Easter Egg",
    acro = "???",
    caption = "*Epic*",
    content = "Awesome.",
    surplus = "+55,000 points",
    points = 55000,
  )

  Legendary = item(
    title = "Easter Egg",
    acro = "???",
    caption = "*Legendary*",
    content = "Impressive.",
    surplus = "+90,000 points",
    points = 90000,
  )

  Mythical = item(
    title = "Easter Egg",
    acro = "???",
    caption = "*Mythical*",
    content = "What?",
    surplus = "+125,000 points",
    points = 125000,
  )

  Heavenly = item(
    title = "Easter Egg",
    acro = "???",
    caption = "*Heavenly*",
    content = "\*bathes in sunlight* YES, REVERE ME, YOUR MIGHTY PENGUIN!",
    surplus = "+210,000 points",
    points = 210000,
  )

  Celestial = item(
    title = "Easter Egg",
    acro = "???",
    caption = "*Celestial*",
    content = "How did you even find this?",
    surplus = "+420,000 points",
    points = 420000,
  )

  Diamond = item(
    title = "Easter Egg",
    caption = "Diamond",
    content = "Oddly specific, but here you go.",
    surplus = "+270,000 points",
    points = 270000,
  )


class word:

  antect = item(
    title = "antect",
    caption = "Antarctican Verb",
    content = "",
    fields = [
      item.field("Verb", """
        /an'tɛkt/

        1. *prototransitive*
        To convert a date from another calendar to the Antarctican calendar.
        *All devices have an inbuilt feature to antect a given decate.*
      """),
      item.field("Conjugation", """
        I antect
        you antect
        one antects
        we antect
        they antect
      """),
      item.field("Participles", """
        I antected
        have antected
        be antecting
      """),
      item.field("Derivatives", """
        antectics
        antectical
      """, line = True),
      item.field("Synonyms", """
        convert
      """, line = True),
      item.field("See Also", """
        Antarctican Calendar
      """),
      item.field("Etymologics", """
        *Spontaneous emergence*
      May have derived from ‘Antarctica’
      """),
    ],
  )

  concyze = item(
    title = "concyze",
    caption = "Antarctican Verb",
    content = "",
    fields = [
      item.field("Verb", """
        /kənˈsʌɪz/
        1. *prototransitive*
        To make something concise.
        *Can you concyze it down?*
      """),
      item.field("Conjugation", """
        I concyze
        you concyze
        one concyzes
        we concyze
        they concyze
      """),
      item.field("Participles", """
        I concyzed
        have concyzed
        am concyzing
      """),
      item.field("Derivatives", """
        concyzation
      """, line = True),
      item.field("Synonyms", """
        concise
        compact
      """, line = True),
      item.field("Antonyms", """
        complicyze
      """),
      item.field("Etymologics", """
        *Republic of Antarctica* » English *concise* + *-yze*
      """),
    ],
  )

  decant = item(
    title = "decant",
    caption = "Antarctican Concept",
    content = "",
    fields = [
      item.field("Noun", """
        /'dɛkənt/

        1. *abstract*
        A unit of time in the Antarctican calendar, corresponding to a month in the Gregorian calendar. Each year consists of 10 decants, alternating between 37 and 36 days long.
      """),
      item.field("Derivatives", """
        didecant
        decate
      """, line = True),
      item.field("Synonyms", """
        month
      """, line = True),
      item.field("See Also", """
        Decant
        Antarctican Calendar
      """),
      item.field("Etymologics", """
        *New Antarctica* » Greek *deka* ‘ten’ + *Antarctica*
      """),
    ],
  )

  decate = item(
    title = "decate",
    caption = "Antarctican Concept",
    content = "",
    fields = [
      item.field("Noun", """
        /'dɛkeɪt/

        1. *abstract*
        The date.
        *What’s the decate?*

        2. *abstract*
        The specific day of the decant.
        *The decate is 20*.
      """),
      item.field("Synonyms", """
        date
      """),
      item.field("See Also", """
        Decate
        Antarctican Calendar
      """),
      item.field("Etymologics", """
        *New Antarctica* » Greek *deka* ‘ten’ + *-ate*
        Also from Antarctican *decant*
      """),
    ],
  )

  septan = item(
    title = "septan",
    caption = "Antarctican Concept",
    content = "",
    fields = [
      item.field("Noun", """
        /'sɛptən/

        1. *abstract*
        A unit of time in the Antarctican calendar, equivalent to a week.
      """),
      item.field("Derivatives", """
        septate
      """, line = True),
      item.field("Synonyms", """
        week
      """, line = True),
      item.field("See Also", """
        Septan
        Antarctican Calendar
      """),
      item.field("Etymologics", """
        *New Antarctica* » Latin *septem* ‘seven’ + *Antarctica*
      """),
    ],
  )

  septate = item(
    title = "septate",
    caption = "Antarctican Concept",
    content = "",
    fields = [
      item.field("Noun", """
        /'sɛpteɪt/

        1. *abstract*
        The day of the week in the Antarctican calendar.
      """),
      item.field("Synonyms", """
        weekday
        weekend
      """),
      item.field("See Also", """
        Septate
        Antarcictan Calendar
      """),
      item.field("Etymologics", """
        *New Antarctica* » Latin *septem* ‘seven’ + *-ate*
      """),
    ],
  )


some = item(
  title = "",
  caption = "",
  content = """
  """,
  other = "",
)
