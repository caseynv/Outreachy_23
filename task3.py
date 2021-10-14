# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 16:44:22 2021

@author: NWANDU KELECHUKWU
"""

import pywikibot
from pywikibot.data import api


site = pywikibot.Site('wikidata', 'wikidata')



def search(site, title):
    
    params = {'action' : 'wbsearchentities', 'format' : 'json', 'language' : 'en', 'type' : 'item', 'search' : title}
    
    request = api.Request(site=site, parameters=params)
    result = request.submit()
    
    need = list(result.values())[1]
    i = 0
    for i in range(0, len(need)):
        qid = need[i]['id']
        labels = need[i]['label']
        keyword = "fetus"
        if keyword in labels:
            print(qid + " - " + labels)
        
        
search(site, "Neuromat")
    