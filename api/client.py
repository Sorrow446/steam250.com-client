import requests
from bs4 import BeautifulSoup


class Client():

	def __init__(self):
		self.base = 'https://steam250.com/'
		self.paths = {
			'$10-$15': "price/10-15",
			'$5-$10': "price/5-10",
			'2006': "2006",
			'2007': "2007",
			'2008': "2008",
			'2009': "2009",
			'2010': "2010",
			'2011': "2011",
			'2012': "2012",
			'2013': "2013",
			'2014': "2014",
			'2015': "2015",
			'2016': "2016",
			'2017': "2017",
			'2018': "2018",
			'2019': "2019",
			'2020': "2020",
			'2d': "tag/2d",
			'3d platformer': "tag/3d_platformer",
			'4 player local': "tag/4_player_local",
			'action rpg': "tag/action_rpg",
			'action': "tag/action",
			'action-adventure': "tag/action-adventure",
			'addictive': "tag/addictive",
			'adventure': "tag/adventure",
			'anime': "tag/anime",
			'arcade': "tag/arcade",
			'atmospheric': "tag/atmospheric",
			'base building': "tag/base_building",
			'bottom 100': "bottom100",
			'building': "tag/building",
			'bullet hell': "tag/bullet_hell",
			'card game': "tag/card_game",
			'cartoony': "tag/cartoony",
			'casual': "tag/casual",
			'character customization': "tag/character_customization",
			'choices matter': "tag/choices_matter",
			'classic': "tag/classic",
			'co-op': "tag/co-op",
			'colorful': "tag/colorful",
			'colourful': "tag/colorful",
			'comedy': "tag/comedy",
			'competitive': "tag/competitive",
			'controller': "tag/controller",
			'crafting': "tag/crafting",
			'cute': "tag/cute",
			'dark fantasy': "tag/dark_fantasy",
			'dark': "tag/dark",
			'developers': "developer",
			'difficult': "tag/difficult",
			'discounts': "discounts",
			'dlc': "dlc",
			'dungeon crawler': "tag/dungeon_crawler",
			'early access': "tag/early_access",
			'education': "tag/education",
			'exploration': "tag/exploration",
			'family friendly': "tag/family_friendly",
			'fantasy': "tag/fantasy",
			'fast-paced': "tag/fast-paced",
			'female protagonist': "tag/female_protagonist",
			'fighting': "tag/fighting",
			'first person': "tag/first-person",
			'fps': "tag/fps",
			'free games': "tag/free_to_play",
			'free to play': "tag/free_to_play",
			'free': "tag/free_to_play",
			'funny': "tag/funny",
			'games $10-$15': "price/10-15",
			'games $5-$10': "price/5-10",
			'games over $15': "price/over15",
			'games under $5': "price/under5",
			'gore': "tag/gore",
			'great soundtrack': "tag/great_soundtrack",
			'hack and slash': "tag/hack_and_slash",
			'hidden gems': "hidden_gems",
			'hidden novels': "hidden_novels",
			'hidden object': "tag/hidden_object",
			'historical': "tag/historical",
			'horror': "tag/horror",
			'indie': "tag/indie",
			'isometric': "tag/isometric",
			'jrpg': "tag/jrpg",
			'linux': "linux250",
			'local co-op': "tag/local_co-op",
			'local multiplayer': "tag/local_multiplayer",
			'mac': "mac250",
			'management': "tag/management",
			'massively multiplayer': "tag/massively_multiplayer",
			'masterpiece': "tag/masterpiece",
			'mature': "tag/mature",
			'medieval': "tag/medieval",
			'memes': "tag/memes",
			'minimalist': "tag/minimalist",
			'month': "30day",
			'most played': "most_played",
			'multiplayer': "tag/multiplayer",
			'multiple endings': "tag/multiple_endings",
			'music': "tag/music",
			'mystery': "tag/mystery",
			'nudity': "tag/nudity",
			'old school': "tag/old_school",
			'old': "old",
			'online co-op': "tag/online_co-op",
			'open world': "tag/open_world",
			'over $15': "price/over15",
			'physics': "tag/physics",
			'platformer': "tag/platformer",
			'point & click': "tag/point_&_click",
			'point and click': "tag/point_&_click",
			'post-apocalyptic': "tag/post-apocalyptic",
			'pre 2006': "old",
			'psychological horror': "tag/psychological_horror",
			'publishers': "publisher",
			'puzzle platformer': "tag/puzzle_platformer",
			'puzzle': "tag/puzzle",
			'pvp': "tag/pvp",
			'quarter': "90day",
			'racing': "tag/racing",
			'realistic': "tag/realistic",
			'relaxing': "tag/relaxing",
			'replay value': "tag/replay_value",
			'resource management': "tag/resource_management",
			'retro': "tag/retro",
			'roguelike': "tag/roguelike",
			'roguelite': "tag/roguelite",
			'romance': "tag/romance",
			'rpg': "tag/rpg",
			'rpgmaker': "tag/rpgmaker",
			'rts': "tag/rts",
			'sandbox': "tag/sandbox",
			'sci-fi': "tag/sci-fi",
			'sexual content': "tag/sexual_content",
			'shoot \'em up': "tag/shoot_em_up",
			'shooter': "tag/shooter",
			'short': "tag/short",
			'side scroller': "tag/side_scroller",
			'simulation': "tag/simulation",
			'singleplayer': "tag/singleplayer",
			'space': "tag/space",
			'sports': "tag/sports",
			'stealth': "tag/stealth",
			'story rich': "tag/story_rich",
			'strategy': "tag/strategy",
			'stylized': "tag/stylized",
			'surreal': "tag/surreal",
			'survival horror': "tag/survival_horror",
			'survival': "tag/survival",
			'tactical': "tag/tactical",
			'third person': "tag/third_person",
			'third-person shooter': "tag/third-person_shooter",
			'this month': "30day",
			'this quarter': "90day",
			'this week': "7day",
			'this year': "90day",
			'top 250 developers': "developer",
			'top 250 discounts': "discounts",
			'top 250 dlc': "dlc",
			'top 250 games': "",
			'top 250 publishers': "publisher",
			'top-down shooter': "tag/top-down_shooter",
			'top-down': "tag/top-down",
			'tower_defense': "tag/tower_defense",
			'trending games': "trending",
			'trending': "trending",
			'turn-based combat': "tag/turn-based_combat",
			'turn-based strategy': "tag/turn-based_strategy",
			'turn-based tactics': "tag/turn-based_tactics",
			'turn-based tactics': "tag/turn-based_tactics",
			'turn-based': "tag/turn-based",
			'under $5': "price/under5",
			'violent': "tag/violent",
			'virtual reality': "vr250",
			'visual novel': "tag/visual_novel",
			'vr exclusives': "vr_exclusives",
			'vr': "vr250",
			'walking simulator': "tag/walking_simulator",
			'war': "tag/war",
			'week': "7day",
			'year': "90day",
			'zombies': "tag/zombies"
		}
		self.s = requests.Session()
		self.s.headers.update({
			"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
						  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
						  "81.0.4044.138 Safari/537.36"
		})

	def get_html(self, path):
		r = self.s.get(self.base + path)
		r.raise_for_status()
		return r.text
	
	def ranking(self, path, limit):
		parsed = {'description': None, 'ranking': []}
		html = self.get_html(path)
		soup = BeautifulSoup(html, 'html.parser')
		ranking = soup.find('div', {'class': 'main ranking'})
		columns = ranking.find_all('div', id=True)
		desc = soup.find('div', {'class': 'content'}).find('p').text.strip().replace('   ', ' ')
		parsed['description'] = desc
		for c in columns:
			pos = int(c['id'])
			if c.find('span', {'title': 'No change'}):
				movement = "-"
			elif c.find('span', {'title': 'New entry'}):
				movement = "New entry"
			else:
				_movement = c.find('span', {'class': 'movement pos'})
				if _movement:
					mov_pos = "▲"
				else:
					_movement = c.find('span', {'class': 'movement neg'})
					mov_pos = "▼"
				movement = mov_pos + _movement.text
			title = c.find('span', {'class': 'title'}).contents[1]
			try:
				price = c.find('span', {'class': 'price'}).text
			except AttributeError:
				price = "Free"
			game = {
				'movement': movement,
				'platforms': [
					p['title'] for p in c.find('span', {'class': 'platforms'})
				],
				'pos': pos,
				'price': price,
				'rating': c.find('span', {'class': 'rating'}).text[-3:],
				'tag': c.find('a', {'class': 'genre'}).text,
				'thumbnail': c.find('img', {'alt': 'Logo'})['src'],
				'title': title.text,
				'url': title['href'].strip()
			}
			try:
				game['date'] = c.find('span', {'class': 'date'})['title']
			except TypeError:
				game['date'] = None
			if path == "most_played":
				game['players'] = int(c.find('span', {'class': 'players'}).text.replace(',', ''))
			elif path == "trending":
				game['velocity'] = int(c.find('span', {'class': 'velocity'}).contents[1][1:].replace(',', ''))
			else:
				game['score'] = float(c.find('span', {'class': 'score'}).text)
				game['votes'] = int(c.find('span', {'class': 'votes'}).text[:-6].replace(',', ''))
				if path in ["developer", "publisher"]:
					game['known_for'] = c.find('span', {'class': 'knownfor'}).text
			parsed['ranking'].append(game)
			if pos == limit:
				break
		return parsed

	def get_top(self, ranking='top 250 games', limit=250):
		if not isinstance(ranking, str):
			raise ValueError('Ranking must be a string.')
		if not isinstance(limit, int):
			raise ValueError('Limit must be an int.')
		if not 1 <= limit <= 250:
			raise ValueError('Limit must be between 1 and 250.')
		try:
			path = self.paths[ranking.lower()]
		except KeyError:
			raise ValueError('Received an invalid rank type: ' + str(ranking))
		return self.ranking(path, limit)
