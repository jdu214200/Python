# country = {(5, 6):3}
country = {'code': 'RU', 'name': 'Russian', 'population': 144}
# country = dict(code='RU', name='Russian')
# print(country['name'])
# print(country[(5, 6)])

for key, value in country.items():
    print(key, " - ", value)
