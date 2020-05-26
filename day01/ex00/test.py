from recipe import Recipe
from book import Book
from datetime import date

cookbook = {'sandwich': {'cooking level': 1, 'cooking_time': 5,
                         'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
                         'description': 'Perfect to go',
                         'recipe_type': 'lunch'}}

painperdu = Recipe('pain perdu', 1, 10,
                   ['brioche', 'oeuf', 'lait'], 'dessert',
                   'Pain perdu is a french dish.')
burger = Recipe('burger', 1, 10, ['viande', 'bun', 'cheddar'],
                'lunch', 'Best dish when you are sad.')

to_print = str(painperdu)
print(to_print)

book = Book('Cookbook', date.today(),
            date.today(), cookbook)
book.add_recipe(painperdu)
book.add_recipe(burger)

book.get_recipes_by_types('lunch')

print("\n")
book.get_recipe_by_name('pain perdu')
print("\n")

book.add_recipe(book)
