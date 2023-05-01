import json
slov = {
'window_size':  {'width': 1400, 'height': 1080}, # Заполняется вручную
'url':  {'HomePage': 'https://store.steampowered.com/', 'AboutPage': 'https://store.steampowered.com/about/', 'TopSellersPage': 'https://store.steampowered.com/search/?filter=topsellers', 'MakretPage': 'https://steamcommunity.com/market/'}, # Заполняется вручную
'attributes': {'Linux': "value", 'LinuxAttribute': 'linux', 'NumberOfPlayers': 'class', 'NumberOfPlayersAttribute': 'checked',}, # Заполняется вручную
'listforcompare': {'GameName': '', 'GameDate': '', 'GamePrice': ''}, # Заполняется кодом
'listforcomparefrompage': {'GameNamePage': '', 'GameDatePage': '', 'GamePricePage': ''}, # Заполняется кодом
'listofvalues': {'GameName': '', 'HeroName': '', 'Rarity': '', 'WordInName': ''}, # Заполняется кодом
'testvalues': {'GameName': 'Dota2', 'HeroName': 'Lifestealer', 'Rarity': 'Immortal', 'WordInName': 'golden'}, # Заполняется вручную
'gamepagevalues': {'GameName': '', 'HeroName': '', 'Rarity': '', 'WordInName': ''}, # Заполняется кодом
'itemforcompare': 'Golden',
}


with open('test.json', 'w') as f:
    f.write(json.dumps(slov))

with open('test.json') as f:
    l = json.load(f)








