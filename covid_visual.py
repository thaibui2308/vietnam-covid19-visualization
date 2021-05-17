import json

from plotly import offline
from plotly.graph_objs import Scattergeo, Layout

filename = 'data/vietnam_covid_data.json'
with open(filename, encoding='utf-8') as f:
    covid_info = json.load(f)

# readable_json = 'data/edited_covid_data.json'
# with open(readable_json, 'w') as f:
#     json.dump(covid_info, f, indent=4)

all_eq_dicts = covid_info['features']
infects, lons, lats, titles = [], [], [], []

for eq_dic in all_eq_dicts:
    infected = eq_dic['properties']['infected']
    title = eq_dic['properties']['Name_VN']
    lon = eq_dic['geometry']['coordinates'][0]
    lat = eq_dic['geometry']['coordinates'][1]

    infects.append(infected)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': titles,
    'marker': {
        'size': [.1*infected for infected in infects],
        'color': infects,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'}
    }
}]
layout = Layout(title='Số ca Covid ở 64 tỉnh thành')
fig = {
    'data': data,
    'layout': layout
}

offline.plot(fig, filename='covid_visualiztion.html')

