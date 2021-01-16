#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов
from pprint import pprint
sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}
mos = sites['Moscow']
lon = sites["London"]
par = sites["Paris"]

mos_lon = ((mos[0]-lon[0]) ** 2 + (mos[1] - lon[1]) ** 2) ** .5
mos_par = ((mos[0]-par[0]) ** 2 + (mos[1] - par[1]) ** 2) ** .5
par_lon = ((par[0]-lon[0]) ** 2 + (par[1] - lon[1]) ** 2) ** .5

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = dict()
distances["from Moscow"] = {}
distances["from Moscow"]["to London"] = mos_lon
distances["from Moscow"]["to Paris"] = mos_par
distances["London"] = {}
distances["London"]["Moscow"] = mos_lon
distances["London"]["Paris"] = par_lon
distances["Paris"] = {}
distances["Paris"]["London"] = par_lon
distances["Paris"]["Moscow"] = mos_par


pprint(distances)




