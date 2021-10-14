# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 16:47:03 2021

@author: NWANDU KELECHUKWU
"""

#%%

import pywikibot
 
site = pywikibot.Site('wikidata', 'wikidata')
page = pywikibot.Page(site, 'User:Caseyyy0000/Outreachy_1')


text = page.get()

print(text)

#%%

import pywikibot
 

def edit(page_):
    site = pywikibot.Site('wikidata', 'wikidata')
    
    page = pywikibot.Page(site, page_)

    text = page.get()
    try:
        
        text = text + "\nHello"
        
        page.text = text      
        page.text.save
        
        print(page.text)
        
    except:
        print("oops!")
        
    

edit('User:Caseyyy0000/Outreachy_1')       


       
    


#%%

import pywikibot

site = pywikibot.Site('en', 'wikipedia')
repo = site.data_repository()

def printinfo(testid, propid):
    item = pywikibot.ItemPage(repo, testid)
    
    
    dict_ = item.get()
    
    name = dict_['labels']['en']
    
    desc = dict_["descriptions"]["en"]
   
    try:
        print ('Name of article: ' + name)
        print(name + ' : ' + desc)
    
        for claim in dict_['claims'][propid]:
            qid_val = claim.getTarget()
            qid_item = qid_val.get()
            prop = qid_val.title()
            
            qual = qid_item['labels']['en']
            print('The Property is ' + prop + ' - ' + qual)
    except KeyError:
        print('This Qid is not found in ' + name + '. Create one today!')
    
printinfo('Q4115189', 'P310')

