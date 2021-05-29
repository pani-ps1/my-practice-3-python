# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 04:31:05 2020

@author: utob
"""

import json

adad = [100, 200, 3, 25, 81, 123, 20]

esme_file = 'adad.json'
with open(esme_file, 'w') as f:
    json.dump(adad,f)