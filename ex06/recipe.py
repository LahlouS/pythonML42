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
    try:
        recipe['prep_time'] = int(input('Enter preparation time: '))
    except:
        recipe['prep_time'] = int(input('Enter an integer value '))

    cook_book[recipe_name] = recipe

def delete_recipe(recipe_name):
    if cook_book.get(recipe_name):
        del cook_book[recipe_name]
        print(recipe_name, 'has been deleted')
    else:
        print(recipe_name, 'not found')

if __name__ == "__main__":
    print('Welcome to the cookBook program')
    while 1:
        print('''
        1) show all recipes
        2) show recipe detail
        3) add a recipe
        4) delete a recipe
        5) Quit
        ''')
        feature = int(input('Enter a feature code: '))
        if feature == 1:
            all_recipes()
        elif feature == 2:
            print_recipe(input('recipe name: '))
        elif feature == 3:
            add_recipe()
        elif feature == 4:
            delete_recipe(input('recipe name: '))
        elif feature == 5:
            print('exiting...')
            exit()
            


