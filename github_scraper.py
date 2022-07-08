from enum import EnumMeta
import enum
from operator import index
from recipe_scrapers import scrape_me
from itertools import cycle

scraper = scrape_me('https://www.bonappetit.com/recipe/spicy-braised-eggplant-noodles')
title = scraper.title()
scraper.total_time()
scraper.yields()
all_ingredients = scraper.ingredients()
scraper.instructions()
scraper.image()
scraper.host()
scraper.links()
scraper.nutrients()  # if available

# voor alle 'oz.', 'cup', 'inch (”)' en 'lb.'
# vertaal het getal links hiervan naar de bijbehorende metric eenheid
#     oz. = ml of gram
#     cup = ml of gram>>
#     lb. = gram
#     ” = cm

dict_unit_mapping = {  
    "oz.": "gram",
    "cup": "ml",
    "lb.": "gram",
    "”": " cm"
}

dict_conversion_rates = {
    "oz.": 28.34952,  # oz naar gram
    "cup": 235.6, # cups naar ml
    "lb.": 453.59237, # lb. naar gram
    "”": 2.54 # inch naar cm
}

imperial_ingredient_list = {} # dictionary met de integer-waarden van ieder ingrediënt als KEY + de string van de eenheid als VALUE
oldNewList = [] # 

# split zin op spatie
i = 0
for sentence in all_ingredients:
    allWords = sentence.split(" ")

# zet alle digits en fractions in conversionOldNew dict
for word in allWords:
    if word.isdigit():
        int_word = int(word)
        imperial_ingredient_list.update({int_word:0})
        # hoe zorg ik er voor dat deze vervolgens netjes de index +1 pakt?
        imperial_ingredient_list.update({int(word):0})
    elif word == "¼":
        imperial_ingredient_list.update({0.25:0})
    elif word == "½":
        imperial_ingredient_list.update({0.5:0})
    elif word == "¾":
        imperial_ingredient_list.update({0.75:0})

# return een lijst van alle keys uit een dict
def getList(dict):
    return list(dict.keys())

oldNewList = getList(imperial_ingredient_list)

# haal van alle keys in de dict het volgende woord op en werk de dict bij
for word in allWords:
    for key in oldNewList:
        if key == word:
            if (i+1 < len(allWords) and i -1 >= 0):
                currWord = str(key)
                nextWord = allWords[i+1]
                imperial_ingredient_list[currWord] = nextWord
    i+=1
                
print(imperial_ingredient_list)


# vervangt de amerikaanse unitnamen in all_ingredients met value uit de mapping

def imperial_metric(all_ingredients):
    metric_ingredient_list = []
    for ingredient in all_ingredients:
        ingredientM = ingredient
        
        for unit in unitMapping.keys():
            if unit in ingredient:
                ingredientM = ingredientM.replace(unit, unitMapping.get(unit))
                metric_ingredient_list.append(ingredientM)
    return metric_ingredient_list

ingredientsMetric = imperial_metric(all_ingredients)
