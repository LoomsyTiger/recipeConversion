from operator import index
from recipe_scrapers import scrape_me
from itertools import cycle

# give the url as a string, it can be url from any site listed below
scraper = scrape_me('https://www.bonappetit.com/recipe/spicy-braised-eggplant-noodles')

# Q: What if the recipe site I want to extract information from is not listed below?
# A: You can give it a try with the wild_mode option! If there is Schema/Recipe available it will work just fine.
# scraper = scrape_me('', wild_mode=True)

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
    # oz. = ml of gram
    # cup = ml of gram
    # lb. = gram
    # ” = cm

# key values
unitMapping = {  
    "oz.": "gram",
    "cup": "ml",
    "lb.": "gram",
    "”": " cm"
}

key_list = list(unitMapping.keys())
val_list = list(unitMapping.values())

print(key_list, val_list)

# vervang alle units uit de mapping
for ingredient in allIngredients:
    ingredientM = ingredient
    
    for unit in unitMapping.keys():
        if unit in ingredient:
            ingredientM = ingredientM.replace(unit, unitMapping.get(unit))
    # print(ingredientM) 
    
# volgende functions nodig:
    # gebruik unit als delimiter
    # pak de laatste karakters uit de linker snippet
    # vorm om naar integer
    # reken de waarden om naar metric
    
conversionMapping = {
    "oz.": 28.34952
}

# split zin op spatie
# loop tot integer
# pak integer en index+1

allWords = []
allWordsCycle = cycle(allWords)
conversionOldNew = {
    
}


for sentence in allIngredients:
    allWords = sentence.split(" ")
    print(sentence.split(" "))
    
    for word in allWords:
        if word.isdigit():
            enumerate(word)
            conversionOldNew.update({word:next(allWordsCycle)})
               
print(conversionOldNew)
    


    
    
# tests
