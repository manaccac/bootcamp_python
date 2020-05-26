import sys
from datetime import date
from recipe import Recipe


class Book:
    def __init__(self, name, last_update, creation_data, recipes_list):
        self.name = name
        self.last_update = last_update
        self.creation_data = creation_data
        self.recipes_list = recipes_list


    def get_recipe_by_name(self, name):
        recipe = Recipe(name, self.recipes_list[name]['cooking_lvl'],
                        self.recipes_list[name]['cooking_time'],
                        self.recipes_list[name]['ingredients'],
                        self.recipes_list[name]['recipe_type'],
                        self.recipes_list[name]['description'])
        print(str(recipe))


    def get_recipes_by_types(self, recipe_type):
        print("Recipes for this type: %s" % recipe_type)
        for name in self.recipes_list:
            if (self.recipes_list[name]['recipe_type']):
                print(name)


    def add_recipe(self, recipe):
        if (recipe.__class__.__name__ != "Recipe"):
            print("Not a Recipe")
            exit()
        self.recipes_list[recipe.name] = {'cooking_lvl': recipe.cooking_lvl,
                                          'cooking_time': recipe.cooking_time,
                                          'ingredients': recipe.ingredients,
                                          'description': recipe.description,
                                          'recipe_type': recipe.recipe_type}
        self.last_update = date.today()
        print("new recipe %s " % recipe.name)
        print("last update: %s" % self.last_update)