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
$10-$15
$5-$10
2006
2007
2008
2009
2010
2011
2012
2013
2014
2015
2016
2017
2018
2019
2020
2d
3d platformer
4 player local
action rpg
action
action-adventure
addictive
adventure
anime
arcade
atmospheric
base building
bottom 100
building
bullet hell
card game
cartoony
casual
character customization
choices matter
classic
co-op
colorful
colourful
comedy
competitive
controller
crafting
cute
dark fantasy
dark
developers
difficult
discounts
dlc
dungeon crawler
early access
education
exploration
family friendly
fantasy
fast-paced
female protagonist
fighting
first person
fps
free games
free to play
free
funny
games $10-$15
games $5-$10
games over $15
games under $5
gore
great soundtrack
hack and slash
hidden gems
hidden novels
hidden object
historical
horror
indie
isometric
jrpg
linux
local co-op
local multiplayer
mac
management
massively multiplayer
masterpiece
mature
medieval
memes
minimalist
month
most played
multiplayer
multiple endings
music
mystery
nudity
old school
old
online co-op
open world
over $15
physics
platformer
point & click
point and click
post-apocalyptic
pre 2006
psychological horror
publishers
puzzle platformer
puzzle
pvp
quarter
racing
realistic
relaxing
replay value
resource management
retro
roguelike
roguelite
romance
rpg
rpgmaker
rts
sandbox
sci-fi
sexual content
shoot 'em up
shooter
short
side scroller
simulation
singleplayer
space
sports
stealth
story rich
strategy
stylized
surreal
survival horror
survival
tactical
third person
third-person shooter
this month
this quarter
this week
this year
top 250 developers
top 250 discounts
top 250 dlc
top 250 games
top 250 publishers
top-down shooter
top-down
tower_defense
trending games
trending
turn-based combat
turn-based strategy
turn-based tactics
turn-based
under $5
violent
virtual reality
visual novel
vr exclusives
vr
walking simulator
war
week
year
zombies
```
