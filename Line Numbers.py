import os
from string import punctuation

with open("text_to_put_num_lines_in.txt", "r+") as file:
    with open("new_text.txt", "w+") as new_file:
        line = file.readline()
        num = 1
        letters = 0
        punct = 0

        while line != "":
            for el in line:
                if el.isalpha():
                    letters += 1
                elif el in punctuation:
                    punct += 1
            new_file.write(f"Line {num}: {line[:-1]} ({letters})({punct})\n")
            line = file.readline()
            num += 1
            letters = 0
            punct = 0
