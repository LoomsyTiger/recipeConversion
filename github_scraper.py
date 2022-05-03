from recipe_scrapers import scrape_me

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


for ingredient in allIngredients:
    print(ingredient)

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
    "”": "cm"
}

print(unitMapping.get("cup"))
