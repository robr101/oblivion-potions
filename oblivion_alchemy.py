"""
Scrape uesp.net for alchemy ingredients in Oblivion and create a pickle file of all the ingredients

uses Ingredient class definition from alchemy_ingredient.py
"""

import bs4, requests, os, pickle
from alchemy_ingredient import Ingredient
from potions import print_all
url = 'https://en.uesp.net/wiki/Oblivion:Ingredients'

# get the page and parse it with beautifulsoup
whole_page = requests.get(url)
soup = bs4.BeautifulSoup(whole_page.text)

# get the tables of ingredients: 1) regular 2) rare 3) unavailable
ingredient_tables = soup.select('table')
ingredients_table_regular = ingredient_tables[0]
ingredients_table_rare = ingredient_tables[1]
ingredients_table_unavailable = ingredient_tables[2]

# declare master list of all ingredients, to be written to pickle file
ingredients = []


first_row = True

# get all the <tr> tags from the table
rows = ingredients_table_regular.findAll('tr')
new_ingredient = None
print('starting standard table...')
# loop through each row in the ingredients tables, saving the appropriate cells
for row in rows:
    col = row.findAll('td')
    # this is a weird table where every other row has a merged line, so we need to get both
    if first_row and len(col) > 2:
        new_ingredient = Ingredient()
        name = col[1].text.split('\n')[0]
        new_ingredient.name = name
        new_ingredient.classification = 'standard'
        new_ingredient.description = col[2].text
        first_row = False
    elif not first_row and len(col) > 6:
        new_ingredient.effects.extend([col[0].text.replace('\xa0', ''), col[1].text.replace('\xa0', ''), col[2].text.replace('\xa0', ''), col[3].text.replace('\xa0', '')])
        new_ingredient.value = col[4].text
        new_ingredient.weight = col[5].text
        new_ingredient.harvest_probability = col[6].text
        ingredients.append(new_ingredient)
        first_row = True

# loop through each row in the ingredients tables, saving the appropriate cells
first_row = True
rows = ingredients_table_rare.findAll('tr')
new_ingredient = None
print('starting rare table...')
for row in rows:
    col = row.findAll('td')
    if first_row and len(col) > 2:
        new_ingredient = Ingredient()
        name = col[1].text.split('\n')[0]
        new_ingredient.name = name
        new_ingredient.classification = 'rare'
        new_ingredient.description = col[2].text
        first_row = False
        print('Adding rare potion...')
    elif not first_row and len(col) > 6:
        new_ingredient.effects.extend([col[0].text.replace('\xa0', ''), col[1].text.replace('\xa0', ''), col[2].text.replace('\xa0', ''), col[3].text.replace('\xa0', '')])
        new_ingredient.value = col[4].text
        new_ingredient.weight = col[5].text
        new_ingredient.harvest_probability = col[6].text
        # debug
        
        print_all([new_ingredient])
        ingredients.append(new_ingredient)
        first_row = True

with open('ingredients.pkl', 'wb') as f:
    pickle.dump(ingredients, f)
