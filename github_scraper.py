from recipe_scrapers import scrape_me

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

dict_imperial_ingredients = {} # dictionary met de integer-waarden van ieder ingrediënt als KEY + de string van de eenheid als VALUE
list_imperial_amounts = [] # list voor alle KEYS uit de dict
list_all_ingredients = []

# split zin op spatie

for sentence in all_ingredients:
    list_all_ingredients.append(sentence.split(" "))

# print(list_all_ingredients)

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
def dict_to_list(dict):
    return list(dict.keys())

list_imperial_amounts = dict_to_list(dict_imperial_ingredients)
print("list_imperial_ingrediets:")
print(list_imperial_amounts)

# haal van alle keys in de dict het volgende woord op en werk de dict bij
i = 0
for sentence in list_all_ingredients:
    for word in sentence:
        for key in list_imperial_amounts:
            if str(key) == word:
                if (i+1 < len(sentence)):
                    current_word = key
                    next_word = sentence[i+1]
                    rest = sentence[i+2]
                    dict_imperial_ingredients[current_word] = next_word
        i+=1
    i = 0
    
# Todo: er gaat iets mis in deze FOR loop, waardoor o.a. de CUPS niet worden meegenomen


print("dict_imperial_ingredients:")                
print(dict_imperial_ingredients)
print("list_all_ingredients:")    
print(list_all_ingredients)



# vertaalt de amerikaanse unitnamen in all_ingredients

def imperial_metric(all_ingredients):
    metric_ingredient_list = []
    for ingredient in all_ingredients:
        ingredient_metric = ingredient
        
        for unit in dict_unit_mapping.keys():
            if unit in ingredient:
                ingredient_metric = ingredient_metric.replace(unit, dict_unit_mapping.get(unit))
                metric_ingredient_list.append(ingredient_metric)
    return metric_ingredient_list

translated_ingredient_list = imperial_metric(all_ingredients)

print("translated_ingredient_list: ")   
print(translated_ingredient_list)

# poging 1 omrekenen van hoeveelheden
# for number in list_imperial_amounts:
#     imperial_value = dict_imperial_ingredients[key]
    
#     for imperial_value in 
    
#     if key in dict_imperial_ingredients:
#         if imperial_value in dict_conversion_rates:
#             rate = dict_conversion_rates[imperial_value]
#             converted_amount = key * rate
#             print(converted_amount)
            
# poging 2 omrekenen van hoeveelheden


list_metric_amounts = []
        
for key in dict_imperial_ingredients:
    unit = dict_imperial_ingredients[key]
    if unit in dict_conversion_rates:
        conversion_rate = dict_conversion_rates[unit]
        metric_amount = key * conversion_rate
        metric_unit = dict_unit_mapping[unit]
        list_metric_amounts.append(str(round(metric_amount)) + " " + metric_unit + " ") 


# Todo: de laatste regel van deze FOR loop mist alleen nog het ingredient in kwestie.
     
print(list_metric_amounts)