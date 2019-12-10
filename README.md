# Oblivion Alchemy Ingredients Sorter

Just a few scripts to help view alchemy ingredients and find combinations.



## Files

- `alchemy_ingredient.py`: class definition to hold info about individual ingredients
- `ingredients.pkl`: data file including all the ingredients scraped from
- `oblivion_alchemy.py`: script scrapes UESP.net for alchemy ingredients in Oblivion and creates a pickle file of all the ingredients.
- `potions.py`: search for potion ingredients by effect, or sort ingredients by value, weight, and harvest probability

## Usage

If you clone this repo, you don't need to run oblivion_alchemy.py, as the ingredients.pkl file is already created for you from previous runs.  Just use potions.py:


Sort all ingredients by value:
```
$> python potions.py sort value
```

Sort all ingredients by harvest probability:
```
$> python potions.py sort harvest
```

Sort all ingredients by weight:
```
$> python potions.py sort weight
```

Find all rare ingredients:
```
$> python potions.py rare
```

Find all potions with a particular effect:
```
$> python potions.py effect [which effect]
```
