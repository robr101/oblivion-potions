"""
Usage:
    potions.py effect 'Restore Health' returns all alchemy ingredients with a Restore Health effect
    potions.py sort value sorts all the potions by value (or weight, harvest_probability)

uses ingredients.pkl and Ingredient class def from alchemy_ingredient.py
"""

import pickle, sys
from alchemy_ingredient import Ingredient


with open('ingredients.pkl', 'rb') as f:
    ingredients = pickle.load(f)

if not ingredients:
    print("Error loading ingredients file, try running oblivion_alchemy.py")
    quit()

mode = None
criteria = None
if len(sys.argv) > 1:
    mode = sys.argv[1]
    criteria = sys.argv[2]

def get_all_with_effect(effect):
    return [ing for ing in ingredients if effect in ing.effects]

def get_all_rare():
    return [ing for ing in ingredients if ing.classification == 'rare']

def print_all(ingreds):
    for ing in ingreds:
        print("\n")
        if ing.classification == 'rare':
            print('*** RARE ***')
        print("\nName: {}\n Desc: {}\n Class: {}".format(ing.name, ing.description, ing.classification))
        print(" Effects:")
        for effect in ing.effects:
            print("  {}".format(effect))
        print(" Value: {}\n Weight: {}\n HarvestProb: {}".format(ing.value, ing.weight, ing.harvest_probability))

def sort_by_value(ingreds):
    return sorted(ingreds, key=lambda x: x.value, reverse=True)

def sort_by_weight(ingreds):
    return sorted(ingreds, key=lambda x: x.weight, reverse=True)

def sort_by_harvest_prob(ingreds):
    return sorted(ingreds, key=lambda x: x.harvest_probability, reverse=False)

if mode and criteria:
    mode = mode.lower()
    if mode == 'effect':
        ings = get_all_with_effect(criteria)
        if ings:
            print('All ingredients with {} as an effect:'.format(criteria))
            print_all(ings)
    if mode == 'rare':
        print('All rare ingredients:')
        print_all(get_all_rare())
    if mode == 'sort':
        if criteria == 'value':
            print('All ingredients sorted by value (high to low)')
            print_all(sort_by_value(ingredients))
        if criteria == 'weight':
            print('All ingredients sorted by weight (high to low)')
            print_all(sort_by_weight(ingredients))
        if criteria == 'harvest':
            print('All ingredients sorted by harvest probability (low to high)')
            print_all(sort_by_harvest_prob(ingredients))
        else:
            print('dunno how to sort by that yet')



    
