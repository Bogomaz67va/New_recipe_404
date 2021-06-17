from django.shortcuts import render

MSG_ERROR = False

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def ingredient_views(request, recipe_name):
    item_data = DATA.get(recipe_name, MSG_ERROR)
    servings = request.GET.get('servings')
    if item_data:
        if servings:
            servings_item_data = {key: round(value * float(servings), 1) for key, value in item_data.items()}
            return render(request, 'calculator/index.html', context={'recipe': servings_item_data})
        else:
            return render(request, 'calculator/index.html', context={'recipe': item_data, 'ingredient': recipe_name})
    else:
        return render(request, 'calculator/404.html')
