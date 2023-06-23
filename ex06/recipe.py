cook_book = {
    "sandwich": {
        "ingredients": ['ham', 'bread', 'cheese', 'tomatoes'],
        "meal": "lunch",
        "prep_time": 10
    },
    "cake": {
        "ingredients": ['flour', 'sugar', 'eggs'],
        "meal": "dessert",
        "prep_time": 60
    },
    "salad": {
        "ingredients": ['avocado', 'arugula', 'tomatoes', 'spinach'],
        "meal": "lunch",
        "prep_time": 15
    }
}

def all_recipes():
    for recipe_name in list(cook_book):
        print(recipe_name)

def print_recipe(recipe_name):
    print(cook_book.get(recipe_name, 'recipe does not exist !'))

def add_recipe():
    recipe = {
        "ingredients" : [],
        "meal": '',
        "prep_time": 0
        }
    recipe_name = input('enter recipe name: ')
    ingredients_list = '/'
    while 1:
        ingredients_list = input('enter ingredients name: ')
        if len(ingredients_list):
            recipe.get('ingredients').append(ingredients_list)
        else:
            break
    recipe['meal'] = input('enter meal description: ')
    recipe['prep_time'] = int(input('enter preparation time: '))
    cook_book[recipe_name] = recipe

if __name__ == "__main__":
    print('Welcome to the cookBook program')
    while 1:
        print('''
        1) show all register
        2) show recipe detail
        3) add a recipe
        ''')
        feature = int(input('Enter a feature code: '))
        if feature == 1:
            all_recipes()
        if feature == 2:
            print_recipe(input('recipe name: '))
        if feature == 3:
            add_recipe()
            


