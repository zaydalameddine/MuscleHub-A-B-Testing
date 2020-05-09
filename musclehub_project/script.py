# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 11:24:03 2020

@author: Zayd Alameddine
"""

from codecademySQL import sql_query

df = sql_query(''' 
               SELECT *
               FROM visits
               LIMIT 5''')

print(df.head())