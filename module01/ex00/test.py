from book import Book
from recipe import Recipe
import random
import time
from loading import ft_progress

i = 0
recipe_type = ("lunch", "dessert", "starter")


pastaBook = Book('pasTAbook')
print('pastaBook has been created')
print(f"pastaBook.creation_date = {str(pastaBook.creation_date)}\npastaBook.last_update {str(pastaBook.last_update)}\n")

print('Adding 50 pasta recipe. . .')
for i in ft_progress(range(50)):
    random_type = random.randint(0, 2)
    recipe_temp = Recipe(f"pasta{i + 1}", i + 1, i + 15, ["salmon", "cream", "caper"], recipe_type[random_type])    
    pastaBook.add_recipe(recipe_temp)
    time.sleep(0.2)

print('\n\n----------- getting all recipe name by type ----------')
print('ALL STARTER', (pastaBook.get_recipes_by_types("starter")))
print('ALL LUNCH', (pastaBook.get_recipes_by_types("lunch")))
print('ALL DESSERT', (pastaBook.get_recipes_by_types("dessert")))

print('\n\n----------- Now trying a wrong key -------------------')
print('ALL DESERT', (pastaBook.get_recipes_by_types("desert")))


print('\n\n----------- checking that time has been updated ----------')
print(f"pastaBook.creation_date = {str(pastaBook.creation_date)}\npastaBook.last_update {str(pastaBook.last_update)}")

print('\n\n----------- finding a recipe by name ----------', end='\n\n')
pasta12 = pastaBook.get_recipe_by_name('pasta12')
print('----------- printing the return value ---------')
print(pasta12)

print('----------- searching a recipe that doesnt exist ----------', end='\n\n')
pasta00 = pastaBook.get_recipe_by_name('pasta00')
print('----------- printing the return value ---------')
print(pasta00)


