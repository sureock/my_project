import requests
import matplotlib.pyplot as plt

base_url = 'https://pokeapi.co/api/v2/'
limit = 10
a = limit
url = f'{base_url}pokemon?limit={limit}'
r = requests.get(url)
# s = json.load(r.json()['results'])

data = []

while limit > 0:
    s = requests.get(r.json()['results'][a-limit]['url'])
    # print(s.json()['height'])

    poke_dict = dict(
        id=a-limit+1,
        name=r.json()['results'][a-limit]['name'],
        height=s.json()['height'],
        weight=s.json()['weight'],
        speed=s.json()['stats'][0]['base_stat'],
        defense=s.json()['stats'][3]['base_stat'],
        attack=s.json()['stats'][4]['base_stat'],
        hp=s.json()['stats'][5]['base_stat'])

    # print(poke_dict)
    # break

    data.append(poke_dict)
    limit = limit - 1

plt.plot([x['hp'] for x in data])
plt.xlabel('pokemon hp')
plt.show()

plt.scatter([x['attack'] for x in data], [x['name'] for x in data])
plt.xlabel('pokemon attack/name')
plt.show()

plt.bar([x['weight'] for x in data],
        [10*int(x['weight']) for x in data],
        width=10)
plt.xlabel('pokemon weight')
plt.show()

plt.barh([x['name'] for x in data],
         [5*int(x['height']) for x in data],
         height=0.8)
plt.xlabel('pokemon name/height')
plt.show()

plt.hist([x['speed'] for x in data])
plt.xlabel('pokemon speed')
plt.show()

plt.pie([x['defense'] for x in data])
plt.xlabel('pokemon defense')
plt.show()

plt.stairs([x['defense'] for x in data])
plt.xlabel('pokemon defense')
plt.show()
# print(data)
