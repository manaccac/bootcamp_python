import sys


class Recipe:
    type = "RECIPE"


    def __init__(self, name, cooking_lvl,cooking_time,
                 ingredients, recipe_type, description=""):
            if (name == "" or cooking_lvl == "" or cooking_time == ""
                or ingredients == "" or description == "" or recipe_type == ""):
                print ("Only description can be empty")
                exit()
            if (type(name) != str):
                print("Name are not str")
                exit()
            if (type(cooking_lvl) != int or cooking_lvl < 1 or cooking_lvl > 5):
                print("Cooking lvl need to be int and in range of 1 and 5")
                exit()
            if (type(cooking_time) != int or cooking_time < 0):
                print("cooking time need to be int and not negative number")
                exit()
            if (type(ingredients) != list):
                print("ingredients must be a list")
                exit()
            for ingredient in ingredients:
                if (type(ingredient) != str or ingredient == ""):
                    print("each ingredient need to be str and ingredient cant be empty")
                    exit()
            if (type(description) != str):
                print("description need to be str")
                exit()
            if (recipe_type not in ["starter", "lunch", "dessert"]):
                print("recipe type need to be starter or lunch or dessert")
                exit()
            self.name = name
            self.cooking_lvl = cooking_lvl
            self.cooking_time = cooking_time
            self.ingredients = ingredients
            self.description = description
            self.recipe_type = recipe_type


    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = ("Recipe {}\ncooking level need {}\ncooking time {} min\n"
               "ingredients for cook {}\neat like a {}\nDescription:\n{}"
               ).format(self.name, self.cooking_lvl, self.cooking_time,
                        self.ingredients, self.recipe_type, self.description)
        return (txt)