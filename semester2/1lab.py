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
        id=s.json()['id'],
        name=r.json()['results'][a-limit]['name'],
        height=s.json()['height'],
        weight=s.json()['weight'])

    for i in s.json()['stats']:
        name = i['stat']['name']
        if i['stat']['name'] in ['speed', 'defense', 'attack', 'hp']:
            poke_dict[name] = i['base_stat']

    # print(poke_dict)
    # break
    data.append(poke_dict)
    limit = limit - 1

plt.plot([x['name'] for x in data], [x['hp'] for x in data])
plt.title('pokemon hp')
plt.xlabel('names')
plt.ylabel('hp')
plt.xticks(rotation=45, size=7)
plt.show()

plt.scatter([x['attack'] for x in data], [x['name'] for x in data])
plt.title('pokemon attack & name')
plt.ylabel('names')
plt.xlabel('attack')
plt.show()

plt.bar([x['name'] for x in data],
        [int(x['weight']) for x in data])
plt.title('pokemon weight')
plt.xlabel('names')
plt.ylabel('weight')
plt.xticks(rotation=45, size=7)
plt.show()

plt.barh([x['name'] for x in data],
         [int(x['height']) for x in data],
         height=0.8)
plt.title('pokemon name & height')
plt.xlabel('height')
plt.ylabel('names')
plt.show()

plt.hist([x['speed'] for x in data], width=0.1)
plt.title('pokemon speed')
plt.xlabel('speed')
plt.show()

plt.pie([x['defense'] for x in data],
        labels=[(x['name'], x['defense']) for x in data],
        autopct='%1.1f%%')
plt.title('pokemon defense pie')
plt.show()

# plt.stairs([x['defense'] for x in data])
# plt.title('pokemon defense stairs')
# plt.xlabel('names')
# plt.ylabel('defense')
# plt.show()

print(data)
