import sys
import datetime
import time 

try: 
    from recipe import Recipe
    class Book:
        def __init__(self, name):
            try:
                if isinstance(name, str):
                        self.name = name
                else:
                    raise AttributeError('AttributeError: [name] is of type string')
                self.recipes_list = dict([('lunch', []), ('starter', []), ('dessert', [])])
                self.creation_date = self.last_update = datetime.datetime.now()
            except AttributeError as a:
                print(a)
                sys.exit()

        def get_recipe_by_name(self, name):
            """Prints a recipe with the name \texttt{name} and returns the instance"""
            for rt, recipes in self.recipes_list.items():
                for r in recipes:
                    if r.name == name:
                        print(r)
                        return r
            print("Recipe not found")
            return None


        def get_recipes_by_types(self, recipe_type):
            try:
                return [recipe_name.name for recipe_name in self.recipes_list[recipe_type]]
            except KeyError as k:
                print('Error:', k, 'is no type')
                return None



        def add_recipe(self, recipe):
            self.last_update = datetime.datetime.now()
            if isinstance(recipe, Recipe):
                self.recipes_list[recipe.recipe_type].append(recipe)
            else:
                print('Error: wrong argument: Recipe instance required')
except:
    print('Recipe class is not accessible !')