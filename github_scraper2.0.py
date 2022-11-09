from recipe_scrapers import scrape_me

scraper = scrape_me('https://www.bonappetit.com/recipe/spicy-braised-eggplant-noodles')
all_ingredients = scraper.ingredients()

dict_unit_mapping = {  
    "oz.": "grams",
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

test_dict = {
    12: "oz.",
    1: "lb."
}

test_dict_converted = {}

for key in test_dict:
    rate = dict_conversion_rates.get(test_dict.get(key))
    rounded = round(rate)
    metric_unit = dict_unit_mapping.get(test_dict.get(key))
    test_dict_converted.update({rounded:metric_unit})

print("ronde 1 testdict")
print(test_dict)

print("converted dict")
print(test_dict_converted)
