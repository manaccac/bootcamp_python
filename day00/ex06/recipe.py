cookbook = {
    'sandwich': {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': '10'},
    'cake':{
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': '60'},
    'salade':{
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': '15'}
}


def print_cook():
    i = 0
    if (cookbook == {}):
        print("Empty CookBook")
    else:
        for recipe in cookbook:
            print(recipe)


def print_recipe(name):
    if (name not in cookbook):
        print ("Recipe does not exist.")
    else:
        recipe = cookbook[name]
        print("\nRecipe for {}:\nIngredients list: {}\nTo be eaten for {}.\n"
        "Takes {} minutes of cooking.".format(name,
                                            recipe['ingredients'],
                                            recipe['meal'],
                                            recipe['prep_time']))


def del_recipe(name):
    if (name not in cookbook):
        print ("Recipe does not exist.")
    else:
        del cookbook[name]
        print("Recipe of %s deleted" % name)        


def add_recipe(name, ls, meal, time):
    cookbook[name] = {'ingredients': ls,
                      'meal': meal,
                      'prep_time': time}
    print("Recipe add %s" % name)


print("Please select an option by typing the corresponding number:")
print("1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n"
        "4: Print the cookbook\n5: Quit")

option = input()

while(option != '5'):
    while (option not in ['1', '2', '3', '4', '5']):
        print("\nThis option does not exist, please type the corresponding number.")
        print("To exit, enter 5.")
        option = input()
    if (option == '1'):
        print("Please enter the recipe's name to creat:")
        name = input()
        print("Enter the first ingredient")
        new = input()
        ls = [new]
        while True:
            print("New ingredient?\nYes or No?")
            request = input()
            if (request == "Yes"):
                print("Name of new ingredient?")
                new = input()
                ls.append(new)
            elif (request == 'No'):
                break
        print("Enter type of meal")
        meal = input()
        print("Enter time for cook in minutes")
        time = input()
        add_recipe(name, ls, meal, time)
    elif (option == '2'):
        print("Please enter the recipe's name to get delete:")
        name = input()
        del_recipe(name)
    elif (option == '3'):
        print("\nPlease enter the recipe's name to get its details:")
        name = input()
        print_recipe(name)
    elif (option == '4'):
        print_cook()
    option = input()
print("\nCookbook closed.")
exit()