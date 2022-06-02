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

key_list = list(unitMapping.keys())
val_list = list(unitMapping.values())

# vervang alle units uit de mapping
class unit_replace:
    for ingredient in allIngredients:
        ingredientM = ingredient
        
        for unit in unitMapping.keys():
            if unit in ingredient:
                ingredientM = ingredientM.replace(unit, unitMapping.get(unit))
        # print(ingredientM) 
       
# dict voor alle conversie-ratios
conversionMapping = {
    "oz.": 28.34952
}


conversionOldNew = {}

# split zin op spatie
for sentence in allIngredients:
    allWords = sentence.split(" ")
    print(sentence.split(" "))
    
    # zet alle digits in conversionOldNew dict
    for word in allWords:
        if word.isdigit():
            enumerate(word)
            conversionOldNew.update({int(word):0})
        elif word == "¼":
            conversionOldNew.update({0.25:0})
        elif word == "½":
            conversionOldNew.update({0.5:0})
        elif word == "¾":
            conversionOldNew.update({0.75:0})

# return een lijst van alle keys uit een dict
def getList(dict):
    return list(dict.keys())

oldNewList = getList(conversionOldNew)

# haal van alle keys in de dict het volgende woord op en werk de dict bij
for word in allWords:
    for key in oldNewList:
        if key == word:
            if (index+1 < len(allWords) and index -1 >= 0):

                currWord = str(key)
                nextWord = allWords[index+1]
                conversionOldNew[currWord] = nextWord
                
                
print(conversionOldNew)