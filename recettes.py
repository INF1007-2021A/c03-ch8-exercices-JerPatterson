def add_recipes(dictionnaire):
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    name = input("Entrez le nom de votre recette?\n")
    ingredients = input("Entrez la liste d'ingrédients de la recette, svp séparer les ingrédients par une ,\n").split(",")
    dictionnaire[name] = ingredients

    return dictionnaire


def print_recipe(ingredients: dict) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    name = input("Entrez le nom d'une recette?\n")

    if name in ingredients:
        print(ingredients[name])
    else:
        print("La recette demandée n'existe pas!")
        print(f"Les recettes existantes sont: {list(ingredients.keys())}")