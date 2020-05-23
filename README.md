# steam250.com-client
Rough client written in Python for steam250.com for use with Discord bots etc.

## Usage
Get open world ranking and limit to 10 games.
```python
from api import client

client = client.Client()
top = client.get_top(ranking='open world', limit=10)
print(top['description'])
for game in top['ranking']:
  print(game['pos'], game['title'])
```
Out:
```
Top 150 best Steam games of all time tagged with Open World, according to gamer reviews.

1 The Witcher 3: Wild Hunt
2 Terraria
3 Factorio
4 Stardew Valley
5 Euro Truck Simulator 2
6 RimWorld
7 Mount & Blade: Warband
8 A Hat in Time
9 Don't Starve Together
10 Don't Starve
```

## Parsed ranking
```
parsed = {'description': None, 'ranking': []}
Top 250:
{'movement': '▼1', 'platforms': ['Windows', 'Mac'], 'pos': 22, 'price': '$19.99', 'rating': '95%', 'tag': 'Action', 'thumbnail': 'https://steamcdn-a.akamaihd.net/steam/apps/200260/capsule_sm_120.jpg', 'title': 'Batman: Arkham City GOTY', 'url': 'https://store.steampowered.com/app/200260/?curator_clanid=32686107', 'date': '7 Sep 2012', 'score': 8.47, 'votes': 32113}
Most played:
{'movement': '-', 'platforms': ['Windows', 'Mac', 'Linux'], 'pos': 1, 'price': 'Free', 'rating': '88%', 'tag': 'FPS', 'thumbnail': 'https://steamcdn-a.akamaihd.net/steam/apps/730/capsule_184x69.jpg', 'title': 'Counter-Strike: Global Offensive', 'url': 'https://store.steampowered.com/app/730/?curator_clanid=32686107', 'date': '21 Aug 2012', 'players': 736928}
Trending:
{'movement': 'New entry', 'platforms': ['Windows', 'Mac', 'Linux'], 'pos': 1, 'price': '$6.99', 'rating': '92%', 'tag': 'Tanks', 'thumbnail': 'https://steamcdn-a.akamaihd.net/steam/apps/326460/capsule_184x69.jpg', 'title': 'ShellShock Live', 'url': 'https://store.steampowered.com/app/326460/?curator_clanid=32686107', 'date': '22 May 2020', 'velocity': 19140}

```

|Key|Type|
| --- | --- |
|date|str|
|known_for|str
|movement|str
|platforms|list
|players/score/velocity/|int/float/int
|pos|int
|price|str
|rating|str
|tag|str
|thumbnail|str
|title|str
|url|str
|votes|int

Keys vary by ranking type.
- "developers" and "publishers" also return the "known_for" key.
- "most played" returns the "players" key, but no "score" or "votes" key.
- "trending" returns the "velocity" key, but no "score" or "votes" key. 

## Rankings

```
self.paths = {
  "$10-$15": "price/10-15",
  "$5-$10": "price/5-10",
  "2006": "2006",
  "2007": "2007",
  "2008": "2008",
  "2009": "2009",
  "2010": "2010",
  "2011": "2011",
  "2012": "2012",
  "2013": "2013",
  "2014": "2014",
  "2015": "2015",
  "2016": "2016",
  "2017": "2017",
  "2018": "2018",
  "2019": "2019",
  "2020": "2020",
  "2d": "tag/2d",
  "3d platformer": "tag/3d_platformer",
  "4 player local": "tag/4_player_local",
  "action rpg": "tag/action_rpg",
  "action": "tag/action",
  "action-adventure": "tag/action-adventure",
  "addictive": "tag/addictive",
  "adventure": "tag/adventure",
  "anime": "tag/anime",
  "arcade": "tag/arcade",
  "atmospheric": "tag/atmospheric",
  "base building": "tag/base_building",
  "bottom 100": "bottom100",
  "building": "tag/building",
  "bullet hell": "tag/bullet_hell",
  "card game": "tag/card_game",
  "cartoony": "tag/cartoony",
  "casual": "tag/casual",
  "character customization": "tag/character_customization",
  "choices matter": "tag/choices_matter",
  "classic": "tag/classic",
  "co-op": "tag/co-op",
  "colorful": "tag/colorful",
  "colourful": "tag/colorful",
  "comedy": "tag/comedy",
  "competitive": "tag/competitive",
  "controller": "tag/controller",
  "crafting": "tag/crafting",
  "cute": "tag/cute",
  "dark fantasy": "tag/dark_fantasy",
  "dark": "tag/dark",
  "developers": "developer",
  "difficult": "tag/difficult",
  "discounts": "discounts",
  "dlc": "dlc",
  "dungeon crawler": "tag/dungeon_crawler",
  "early access": "tag/early_access",
  "education": "tag/education",
  "exploration": "tag/exploration",
  "family friendly": "tag/family_friendly",
  "fantasy": "tag/fantasy",
  "fast-paced": "tag/fast-paced",
  "female protagonist": "tag/female_protagonist",
  "fighting": "tag/fighting",
  "first person": "tag/first-person",
  "fps": "tag/fps",
  "free games": "tag/free_to_play",
  "free to play": "tag/free_to_play",
  "free": "tag/free_to_play",
  "funny": "tag/funny",
  "games $10-$15": "price/10-15",
  "games $5-$10": "price/5-10",
  "games over $15": "price/over15",
  "games under $5": "price/under5",
  "gore": "tag/gore",
  "great soundtrack": "tag/great_soundtrack",
  "hack and slash": "tag/hack_and_slash",
  "hidden gems": "hidden_gems",
  "hidden novels": "hidden_novels",
  "hidden object": "tag/hidden_object",
  "historical": "tag/historical",
  "horror": "tag/horror",
  "indie": "tag/indie",
  "isometric": "tag/isometric",
  "jrpg": "tag/jrpg",
  "linux": "linux250",
  "local co-op": "tag/local_co-op",
  "local multiplayer": "tag/local_multiplayer",
  "mac": "mac250",
  "management": "tag/management",
  "massively multiplayer": "tag/massively_multiplayer",
  "masterpiece": "tag/masterpiece",
  "mature": "tag/mature",
  "medieval": "tag/medieval",
  "memes": "tag/memes",
  "minimalist": "tag/minimalist",
  "month": "30day",
  "most played": "most_played",
  "multiplayer": "tag/multiplayer",
  "multiple endings": "tag/multiple_endings",
  "music": "tag/music",
  "mystery": "tag/mystery",
  "nudity": "tag/nudity",
  "old school": "tag/old_school",
  "old": "old",
  "online co-op": "tag/online_co-op",
  "open world": "tag/open_world",
  "over $15": "price/over15",
  "physics": "tag/physics",
  "platformer": "tag/platformer",
  "point & click": "tag/point_&_click",
  "point and click": "tag/point_&_click",
  "post-apocalyptic": "tag/post-apocalyptic",
  "pre 2006": "old",
  "psychological horror": "tag/psychological_horror",
  "publishers": "publisher",
  "puzzle platformer": "tag/puzzle_platformer",
  "puzzle": "tag/puzzle",
  "pvp": "tag/pvp",
  "quarter": "90day",
  "racing": "tag/racing",
  "realistic": "tag/realistic",
  "relaxing": "tag/relaxing",
  "replay value": "tag/replay_value",
  "resource management": "tag/resource_management",
  "retro": "tag/retro",
  "roguelike": "tag/roguelike",
  "roguelite": "tag/roguelite",
  "romance": "tag/romance",
  "rpg": "tag/rpg",
  "rpgmaker": "tag/rpgmaker",
  "rts": "tag/rts",
  "sandbox": "tag/sandbox",
  "sci-fi": "tag/sci-fi",
  "sexual content": "tag/sexual_content",
  "shoot 'em up": "tag/shoot_em_up",
  "shooter": "tag/shooter",
  "short": "tag/short",
  "side scroller": "tag/side_scroller",
  "simulation": "tag/simulation",
  "singleplayer": "tag/singleplayer",
  "space": "tag/space",
  "sports": "tag/sports",
  "stealth": "tag/stealth",
  "story rich": "tag/story_rich",
  "strategy": "tag/strategy",
  "stylized": "tag/stylized",
  "surreal": "tag/surreal",
  "survival horror": "tag/survival_horror",
  "survival": "tag/survival",
  "tactical": "tag/tactical",
  "third person": "tag/third_person",
  "third-person shooter": "tag/third-person_shooter",
  "this month": "30day",
  "this quarter": "90day",
  "this week": "7day",
  "this year": "90day",
  "top 250 developers": "developer",
  "top 250 discounts": "discounts",
  "top 250 dlc": "dlc",
  "top 250 games": "",
  "top 250 publishers": "publisher",
  "top-down shooter": "tag/top-down_shooter",
  "top-down": "tag/top-down",
  "tower_defense": "tag/tower_defense",
  "trending games": "trending",
  "trending": "trending",
  "turn-based combat": "tag/turn-based_combat",
  "turn-based strategy": "tag/turn-based_strategy",
  "turn-based tactics": "tag/turn-based_tactics",
  "turn-based tactics": "tag/turn-based_tactics",
  "turn-based": "tag/turn-based",
  "under $5": "price/under5",
  "violent": "tag/violent",
  "virtual reality": "vr250",
  "visual novel": "tag/visual_novel",
  "vr exclusives": "vr_exclusives",
  "vr": "vr250",
  "walking simulator": "tag/walking_simulator",
  "war": "tag/war",
  "week": "7day",
  "year": "90day",
  "zombies": "tag/zombies"
}
```
