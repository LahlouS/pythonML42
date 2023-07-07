import sys

class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description = None):
        try:
            if isinstance(name, str):
                self.name = name
            else:
                raise AttributeError('AttributeError: [name] is of type string')
            if isinstance(cooking_lvl, int):
                self.cooking_lvl = cooking_lvl
            else:
                raise AttributeError('AttributeError: [cooking_lvl] is of type integer')
            if isinstance(cooking_time, int):
                self.cooking_time = cooking_time
            else:
                raise AttributeError('AttributeError: [cooking_time] is of type integer')
            if isinstance(ingredients, list):
                self.ingredients = ingredients
            else:
                raise AttributeError('AttributeError: [ingredients] is of type list')
            if description == None or isinstance(description, str):
                self.description = description
            else:
                raise AttributeError('AttributeError: [desciption] is of type string or None')
            if isinstance(recipe_type, str) and recipe_type in ('starter', 'lunch', 'dessert'):
                self.recipe_type = recipe_type
            else:
                raise AttributeError("AttributeError: [recipe_type] is of type ('starter', 'lunch', 'dessert')")
        except AttributeError as a:
            print(a)
            sys.exit()

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = f"""Recipe: {self.name}
        Cooking level: {self.cooking_lvl}
        Cooking time: {self.cooking_time}
        Ingredients: {', '.join(self.ingredients)}
        recipe type: {self.recipe_type}
        description: {self.description}
        """
        return txt

