#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

import recettes 


def first_difference_finder(file1, file2) -> tuple:
    with open(file1, "r", encoding = "utf-8") as file1, open(file2, "r", encoding = "utf-8") as file2:
            character_file1 = file1.read(1)
            character_file2 = file2.read(1)
            position = 1
            while character_file1 == character_file2:
                character_file1 = file1.read(1)
                character_file2 = file2.read(1)
                position += 1

    return character_file1, position


def triple_spaces_file(file_given, file_to_write) -> __file__:
    with open(file_given, "r", encoding = "utf-8") as file_r, open(file_to_write, "w", encoding = "utf-8") as file_w:
        for line in file_r:
            words = line.split()
            for word in words:
                file_w.write(word + " " * 3)
            file_w.write("\n")


def grades_equivalent_letter(file_grades, equivalence: dict) -> __file__:
    mentions_equivalent = equivalence.items()
    with open(file_grades, "r", encoding = "utf-8") as grades, open("notes+mentions.txt", "w", encoding = "utf-8") as mentions:
        for line in grades:
            line = line.split()[0]
            for mention in mentions_equivalent:
                if int(line) >= mention[1][0] and int(line) < mention[1][1]:
                    mention_given = mention[0]
                    break
            mentions.write(line + " : " + mention_given + "\n")


def recipes_book(file_recipes):
    choice = input("Voulez-vous entrer une recette (Tapez: 1) ou accéder à une recette (Tapez: 2): ")
    if choice == "1":
        new_recipe = recettes.add_recipes({})
        for name in new_recipe.keys():
            ingredients = new_recipe[name]
            with open(file_recipes, "a", encoding = "utf-8") as recipes:
                recipes.write(str(name) + " : " + str(ingredients) + "\n")

    elif choice == "2":
        dictionary = {}
        with open(file_recipes, "r", encoding = "utf-8") as recipes_list:
            for line in recipes_list:
                recipe = line.split(" : ")[0]
                ingredients = line.split(" : ")[1].split("\n")[0]
                dictionary[recipe] = ingredients
        recettes.print_recipe(dictionary)


def sorted_number_in_file(file) -> list:
    numbers_in_file = []
    with open(file, "r", encoding = "utf-8") as content:
        for line in content:
            number = ""
            for character in line:
                if character.isdigit():
                    number += character
                elif number != "":
                    numbers_in_file.append(int(number))
                    number = ""

    return sorted(numbers_in_file)


def every_other_line(file) -> __file__:
    with open(file, "r", encoding="utf-8") as content:
        lines = content.readlines()
    with open("EOL.txt", "w", encoding="utf-8") as new_content:
        for line_number in range(0, len(lines), 2):
            new_content.write(lines[line_number])


if __name__ == '__main__':
    first_difference, position = first_difference_finder("exemple.txt", "exemplecopy.txt")
    print(f"La première différence rencontrée est {first_difference} et elle se retrouve après {position} caractères")
    triple_spaces_file("exemple.txt", "exemplewrite.txt")
    grades_equivalent_letter("notes.txt", PERCENTAGE_TO_LETTER)
    recipes_book("recettes.txt")
    print("Les nombres présents dans le document sont: " + str(sorted_number_in_file("exemple.txt")))
    every_other_line("notes.txt")