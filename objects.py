#! /usr/bin/env python3


class Category:
    def __init__(self, category):
        self.__category = category

    def get_Name(self):
        return self.__category

    def set_Name(self, category):
        self.__category = category


# Create meal class with name, instructions, ingredients, and amount informations
class Meal:
    def __init__(self, meal_name, strInstructions, ingredients, amounts):
        self.__meal_name = meal_name
        self.__strInstructions = strInstructions
        self.__amounts = amounts
        self.__ingredients = ingredients

    def get_Name(self):
        return self.__meal_name

    def get_instructions(self):
        return self.__strInstructions

    def get_ingredients(self):
        return self.__ingredients

    def get_amount(self):
        return self.__amounts


# Creates an area class
class Area:
    def __init__(self, area):
        self.__area = area

    def get_Name(self):
        return self.__area
