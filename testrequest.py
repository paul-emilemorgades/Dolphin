# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 09:02:55 2020

@author: Pio
"""

import requests
 
r = requests.get('https://hostname:port/api/v1/ratio/')
print(type(r))
print(r.status_code)
print(r.headers)
