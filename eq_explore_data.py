import json
import matplotlib.pyplot as plt
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

with open('data/eq_data_30_day_m1.json', encoding="utf8") as f:
    all_eq_data = json.load(f)

# filename = 'data/readable_eq_data.json'
# with open(filename, 'w') as f:
#     json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data['features']

mags, lons, lats, texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    text = eq_dict['properties']['title']

    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    texts.append(text)

# Map the earthquake
data = [Scattergeo(lon=lons, lat=lats)]
# other way to define the data
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'text': texts,
    'lat': lats,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'}
    }
}]
my_layout = Layout(title='Global Recorded EarthQuakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')

# fig, ax = plt.subplots()
# plt.style.use('seaborn')
# ax.plot(mags, c='blue', linewidth=2)
#
# ax.set_title('Earthquake Magnitudes')
# ax.set_xlabel('', fontsize=10)
# ax.set_ylabel('Magnitude', fontsize=10)
# ax.tick_params(axis='both', which='major', labelsize=10)
#
# plt.show()

print(mags[:10])
print(lons[:10])
print(lons[:10])
