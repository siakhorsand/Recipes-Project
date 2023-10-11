#! /usr/bin/env python3

import requests
import textwrap


#  Returns all meals
def display_item_list(title, items):
    if items is None:
        print("There was a problem, please try again later")
    else:
        # print the list
        print(title.upper())
        for i in range(len(items)):
            item = items[i]
            print(" " + item.get_Name())
        print()


#  Returns all categories
def list_Categories(categories):
    # Get categories:
    if categories is None:
        print("There was a problem, please try again later")
    else:
        # If it was able to get the list, print it:
        print()
        print(" CATEGORIES\n")

        for i in range(len(categories)):
            category = categories[i]
            print(" " + category.get_Name())
        print()


#  Returns all meals by categories
def list_Meals_By_Category():
    # Ask user for category
    lookupCategory = input("Enter a category: ")
    print()
    categories = requests.get_Categories()
    found = False

    if categories is None:
        print("There was a problem, please try again later")
    else:
        # find item in each category
        for i in range(len(categories)):
            category = categories[i]
            if category.get_Name().lower() == lookupCategory.lower():
                found = True
                break
        if found:
            # returns meals by categories
            meals = requests.get_Meal_By_Category(lookupCategory)
            display_item_list(lookupCategory + "MEALS", meals)
        else:
            print("Category not found, please try again")


#  Returns meal name input by user
def search_Meals():
    # Ask for meal name
    mealName = input("Enter Meal Name: ")
    meal = requests.get_Meal(mealName)

    if meal is None:
        print("there was a problem, please try again later")
    else:
        Display_Meal(meal)


#  Meal Randomizer
def random_Meal():
    # get a random meal:
    meal = requests.get_Random_Meal()

    if meal is None:
        print("There was a problem, please try again later")
    else:
        Display_Meal(meal)


#  Prints meal info
def Display_Meal(meal):
    # Meal recipe
    print()
    print("Recipe:  " + meal.get_Name())
    print()

    # Meal instructions
    print("Instructions:")
    #  Uses text wrapper to format instructions
    wrap = textwrap.TextWrapper(width=80)
    wrap_list = wrap.wrap(meal.get_instructions())
    for line in wrap_list:
        print(line)
    print()

    # Meal ingredients
    print("Ingredients:\n")
    print("Measure\t\t\t\t\t Ingredients")
    print('_' * 40)

    ingredients = meal.get_ingredients()
    amounts = meal.get_amount()

    for index in range(len(ingredients)):
        amount = amounts[index]
        ingredient = ingredients[index]
        print('{:25s}{:<25}'.format(amount, ingredient))
    print('_' * 40)
    print()


# Returns a list of areas
def list_Areas(areas):
    # gets a list of areas
    areas = requests.get_Areas()
    if areas is None:
        print("There was a problem, please try again later")
    else:
        print()
        print(" AREAS\n")

        for i in range(len(areas)):
            area = areas[i]
            print("" + area.get_Name())
        print()


#  Returns list of meal based on area
def list_Meals_By_Area(areas):
    # Ask user for the area
    lookupArea = input("Enter an area: ")
    print()
    areas = requests.get_Areas()
    found = False

    if areas is None:
        print("There was a problem, please try again later")
    else:

        for i in range(len(areas)):
            area = areas[i]
            if area.get_Name().lower() == lookupArea.lower():
                found = True
                break
        if found:
            meals = requests.get_Meal_By_Area(lookupArea)
            display_item_list(lookupArea, meals)
        else:
            print("Invalid area, please try again")


#  Title display
def Show_Title():
    print("My Recipe Program")
    print()


# Menu, listing all options:
def show_menu():
    print("COMMAND MENU")
    print("1 - List All Categories")
    print("2 - List All Meals For Categories")
    print("3 - Search Meal by Name")
    print("4 - Get a Random Meal")
    print("5 - List All Areas")
    print("6 - Search Meals by Area")
    print("7 - Display Menu")
    print("0 - Exit The Application")
    print()


def main():
    Show_Title()
    show_menu()

    categories = requests.get_Categories()
    areas = requests.get_Areas()

    while True:
        command = input("Please enter a command: (0-7) ")
        if command == "1":
            list_Categories(categories)
        elif command == "2":
            list_Meals_By_Category()
        elif command == "3":
            search_Meals()
        elif command == "4":
            random_Meal()
        elif command == "5":
            list_Areas(areas)
        elif command == "6":
            list_Meals_By_Area(areas)
        elif command == "7":
            show_menu()
        elif command == "0":
            print("Thank you for dining with us!")
            break
        else:
            print("Invalid Command, try again.")


if __name__ == "__main__":
    main()
