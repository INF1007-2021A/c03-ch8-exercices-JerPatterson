#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici
def first_difference_finder(file1, file2) -> bool:
    with open(file1, "r", encoding = "utf-8") as file1, open(file2, "r", encoding = "utf-8") as file2:
            content_file1 = file1.read(1)
            content_file2 = file2.read(1)
            position = 1
            while content_file1 == content_file2:
                content_file1 = file1.read(1)
                content_file2 = file2.read(1)
                position += 1
            first_difference = content_file1

    return first_difference, position


def triple_spaces_file(file_given, file_to_write):
    with open(file_given, "r", encoding = "utf-8") as file_r, open(file_to_write, "w", encoding = "utf-8") as file_w:
        for line in file_r:
            words = line.split()
            for word in words:
                file_w.write(word + " " * 3)
            file_w.write("\n")


def grades_equivalent_letter(file_grades, equivalence):
    mentions_equivalent = equivalence.items()
    with open(file_grades, "r", encoding = "utf-8") as grades, open("notes+mentions.txt", "w", encoding = "utf-8") as mentions:
        for line in grades:
            line = line.split()[0]
            for mention in mentions_equivalent:
                if int(line) >= mention[1][0] and int(line) < mention[1][1]:
                    mention_given = mention[0]
                    break
            mentions.write(line + " : " + mention_given + "\n")


def recipes():
    pass

# TODO: Définissez vos fonction ici


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    first_difference, position = first_difference_finder("exemple.txt", "exemplecopy.txt")
    print(f"La première différence rencontrée est {first_difference} et elle se retrouve après {position} caractères")
    triple_spaces_file("exemple.txt", "exemplewrite.txt")
    grades_equivalent_letter("notes.txt", PERCENTAGE_TO_LETTER)

