#! /usr/bin/env python3
#  Created by Sia Khorsand on May 23rd, 2022 for CIMP8A
#  This program shows lists of categories, areas, meals by category, meals by area,
#  and ingredients based on the user input

import urllib.request
import urllib.parse
import json

from objects import Category, Meal, Area


#  Retrieves the full list of categories from the API

def get_Categories():
    # import url
    url = "https://www.themealdb.com/api/json/v1/1/list.php?c=list"
    f = urllib.request.urlopen(url)
    categories = []

    # get each category from API
    try:
        data = json.loads(f.read().decode('utf-8'))
        for categoryData in data['meals']:
            category = Category(categoryData['strCategory'])
            categories.append(category)

    except(ValueError, KeyError, TypeError):
        return None

    return categories


#  Returns the meals in the respective categories
def get_Meal(mealName):
    url = "https://www.themealdb.com/api/json/v1/1/search.php?s=" + urllib.parse.quote(mealName)
    f = urllib.request.urlopen(url)

    # find meals from API
    try:
        data = json.loads(f.read().decode('utf-8'))
        for mealData in data['meals']:
            ingredients = add_Ingredients(mealData)
            amounts = add_Measurements(mealData)
            meal = Meal(mealData['strMeal'], mealData['strInstructions'], ingredients, amounts)
    except(ValueError, KeyError, TypeError):
        return None
    return meal


#  Returns all meals
def get_Meal_By_Category(category):
    # import URL
    url = "https://www.themealdb.com/api/json/v1/1/filter.php?c=" + category
    f = urllib.request.urlopen(url)
    meals = []

    # Get each category fro API
    try:
        data = json.loads(f.read().decode('utf-8'))
        for mealData in data['meals']:
            meal = Meal(mealData['strMeal'], "", "", "")
            meals.append(meal)
    except(ValueError, KeyError, TypeError):
        return None
    return meals


#  Creates a list of ingredients
def add_Ingredients(mealData):
    ingredients = []
    num = 1
    while num != 21:
        ingredient_Name = "strIngredient" + str(num)
        # gets the ingredient
        ingredient = mealData[ingredient_Name]
        # stops adding entries if empty
        if ingredient == "":
            break
        else:
            ingredients.append(mealData[ingredient_Name])
            num += 1
    return ingredients


#  List of amounts
def add_Measurements(mealData):
    amounts = []
    num = 1
    while num != 21:
        # gets the amounts:
        amount_Name = "strMeasure" + str(num)
        amount = mealData[amount_Name]
        if amount == "":
            break
        else:
            amounts.append(mealData[amount_Name])
            num += 1
    return amounts


# finds areas on the API
def get_Areas():
    # imports URL
    url = "https://www.themealdb.com/api/json/v1/1/list.php?a=list"
    f = urllib.request.urlopen(url)
    areas = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for areaData in data['meals']:
            area = Area(areaData['strArea'])
            areas.append(area)

    except(ValueError, KeyError, TypeError):
        return None

    return areas


# Gets meals by areas from API
def get_Meal_By_Area(area):
    url = "https://www.themealdb.com/api/json/v1/1/filter.php?a=" + area
    f = urllib.request.urlopen(url)
    meals = []
    try:
        data = json.loads(f.read().decode('utf-8'))
        for mealData in data['meals']:
            meal = Meal(mealData['strMeal'], "", "", "")
            meals.append(meal)
    except(ValueError, KeyError, TypeError):
        return None
    return meals


#  Gets random meal from url
def get_Random_Meal():
    # Get random meal from url
    url = "https://www.themealdb.com/api/json/v1/1/random.php"
    f = urllib.request.urlopen(url)
    try:
        data = json.loads(f.read().decode('utf-8'))
        for mealData in data['meals']:
            ingredients = add_Ingredients(mealData)
            amounts = add_Measurements(mealData)
            meal = Meal(mealData['strMeal'], mealData['strInstructions'], ingredients, amounts)
    except(ValueError, KeyError, TypeError):
        return None
    return meal
