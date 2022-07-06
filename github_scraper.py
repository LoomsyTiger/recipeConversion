from enum import EnumMeta
import enum
from operator import index
from recipe_scrapers import scrape_me
from itertools import cycle

scraper = scrape_me('https://www.bonappetit.com/recipe/spicy-braised-eggplant-noodles')
title = scraper.title()
scraper.total_time()
scraper.yields()
allIngredients = scraper.ingredients()
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

# key values
unitMapping = {  
    "oz.": "gram",
    "cup": "ml",
    "lb.": "gram",
    "”": " cm"
}

# nog niet gebruikt
# key_list = list(unitMapping.keys())
# val_list = list(unitMapping.values())

# dict voor alle conversie-ratios
conversionMapping = {
    "gram": 28.34952  # oz naar gram
}


conversionOldNew = {}

# return een lijst van alle keys uit een dict
def getList(dict):
    return list(dict.keys())

oldNewList = getList(conversionOldNew)

# haal van alle keys in de dict het volgende woord op en werk de dict bij
i = 0
# split zin op spatie
for sentence in allIngredients:
    allWords = sentence.split(" ")
    print(sentence.split(" "))
    for word in allWords:
        for key in oldNewList:
            if key == word:
                if (i+1 < len(allWords) and i -1 >= 0):
                    currWord = str(key)
                    nextWord = allWords[i+1]
                    conversionOldNew[currWord] = nextWord
        i+=1
    
# zet alle digits en fractions in conversionOldNew dict
for word in allWords:
    if word.isdigit():
        int_word = int(word)
        conversionOldNew.update({int_word:0})
        # hoe zorg ik er voor dat deze vervolgens netjes de index +1 pakt?
        conversionOldNew.update({int(word):0})
    elif word == "¼":
        conversionOldNew.update({0.25:0})
    elif word == "½":
        conversionOldNew.update({0.5:0})
    elif word == "¾":
        conversionOldNew.update({0.75:0})
        
            
print(conversionOldNew)
              
                
# vervangt de amerikaanse unit/keys in allIngredients met value uit de mapping

def imperial_metric(allIngredients):
    ingredientsMetricList = []
    for ingredient in allIngredients:
        ingredientM = ingredient
        
        for unit in unitMapping.keys():
            if unit in ingredient:
                ingredientM = ingredientM.replace(unit, unitMapping.get(unit))
                ingredientsMetricList.append(ingredientM)
    return ingredientsMetricList

ingredientsMetric = imperial_metric(allIngredients)
print(ingredientsMetric)

print(conversionOldNew)