with open('recipes.txt', encoding='utf-8') as f:
    cook_book = {}
    for line in f:
        name_dish = line.strip()
        ingredients_amount = int(f.readline())
        ingredients = []
        for i in range(ingredients_amount):
            ingredient = f.readline().strip().split(' | ')
            ingredient_name, quantity, measure = ingredient
            ingredients.append(
                {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        f.readline()
        cook_book[name_dish] = ingredients

print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    necessary_ingredients = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] in necessary_ingredients.keys():
                necessary_ingredients[ingredient['ingredient_name']]['quantity'] += int(ingredient['quantity']) * person_count
            else:
                necessary_ingredients[ingredient['ingredient_name']] = {'measure': ingredient['measure'],
                                                                        'quantity': int(ingredient['quantity']) * person_count}
    return necessary_ingredients

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

import os

files = {}
merged_file = os.getcwd() + r'\sorted'

for name_file in os.listdir(merged_file):
    with open(os.path.join(merged_file, name_file), 'r', encoding='utf-8') as f:
        files[name_file] = len(f.readlines())

for name_file in sorted(files, key=files.get):
    with open(os.path.join(merged_file, name_file), 'r', encoding='utf-8') as f:
        with open(os.path.join(os.getcwd(), 'result.txt'), 'a', encoding='utf-8') as f1:
            f1.writelines(['\n'.join([name_file, str(files[name_file])]) + '\n'] + f.readlines() + ['\n'])