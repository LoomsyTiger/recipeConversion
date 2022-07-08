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

dict_imperial_ingredients = {} # dictionary met de integer-waarden van ieder ingrediënt als KEY + de string van de eenheid als VALUE
list_imperial_ingredients = [] # list voor alle KEYS uit de dict
list_all_ingredients = []

# split zin op spatie

for sentence in all_ingredients:
    list_all_ingredients.append(sentence.split(" "))
print(list_all_ingredients)

# zet alle digits en fractions in conversionOldNew dict
for ingredient in list_all_ingredients:
    for word in ingredient:
        if word.isdigit():
            int_word = int(word)
            dict_imperial_ingredients.update({int_word:0})
            # hoe zorg ik er voor dat deze vervolgens netjes de index +1 pakt?
            dict_imperial_ingredients.update({int(word):0})
        elif word == "¼":
            dict_imperial_ingredients.update({0.25:0})
        elif word == "½":
            dict_imperial_ingredients.update({0.5:0})
        elif word == "¾":
            dict_imperial_ingredients.update({0.75:0})

# return een lijst van alle keys uit een dict
def getList(dict):
    return list(dict.keys())

list_imperial_ingredients = getList(dict_imperial_ingredients)
print(list_imperial_ingredients)

# haal van alle keys in de dict het volgende woord op en werk de dict bij
i = 0
for word in list_all_ingredients:
    for key in list_imperial_ingredients:
        if key == word:
            if (i+1 < len(list_all_ingredients) and i -1 >= 0):
                currWord = str(key)
                nextWord = list_all_ingredients[i+1]
                dict_imperial_ingredients[currWord] = nextWord
    i+=1
                
print(dict_imperial_ingredients)


# vervangt de amerikaanse unitnamen in all_ingredients met value uit de mapping

def imperial_metric(all_ingredients):
    metric_ingredient_list = []
    for ingredient in all_ingredients:
        ingredientM = ingredient
        
        for unit in dict_unit_mapping.keys():
            if unit in ingredient:
                ingredientM = ingredientM.replace(unit, dict_unit_mapping.get(unit))
                metric_ingredient_list.append(ingredientM)
    return metric_ingredient_list

ingredientsMetric = imperial_metric(all_ingredients)
