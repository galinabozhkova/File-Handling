import os
num_of_line = 0
with open("text.txt") as file:
    line = file.readline()
    while line!="":

        if num_of_line%2 ==0:
            for el in ["-", ",", ".", "!", "?"]:
                if el in line:
                    line = line.replace(el, "@")
            line = line.split()
            print(f'{" ".join(line[::-1])}')

        line = file.readline()
        num_of_line += 1
