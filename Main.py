# Course: CS2301 - Data Structures
# Author: Victor Huicochea
# Assignment: Project 1 - Option A
# Instructor: Diego Aguirre
# T.A.: Manoj Saha
# Last date of modification: 09/12/2018
# Purpose: Practice recursion in a real-life situation.


import os
import random


# Method provided by instructor. It returns two lists, one holding the names of all the folders in the current folder
#                                and the other one holding the names of all files inside the current folder.
def get_dirs_and_files(path):
    dir_list = [directory for directory in os.listdir(path) if os.path.isdir(path + '/' + directory)]
    file_list = [directory for directory in os.listdir(path) if not os.path.isdir(path + '/' + directory)]

    return dir_list, file_list


# Method provided by instructor. It returns a number between 0 and 1. The closer it is to 1, the more likely the file
#                                located in the given path is a dog picture. The closer it is to 0, the more likely it
#                                is a cat picture.
def classify_pic(path):
    # To be implemented by Diego: Replace with ML model
    if "dog" in path:
        return 0.5 + random.random() / 2

    return random.random() / 2


# Method defined by student. Method uses recursion to explore until the last directory and then starts saving the paths
#                            to each file in its respective list.
def process_dir(path):
    dir_list, file_list = get_dirs_and_files(path)

    cat_list = []
    dog_list = []

    # Your code goes here
    # Checks if there is any other directory in current directory.
    if len(dir_list) > 0:
        for i in range(len(dir_list)):
            new_cats, new_dogs = process_dir(path + '/' + dir_list[i])  # recursive call with updated path
            for j in range(len(new_cats)):  # Assignment of new list from current directory to the master list
                cat_list.append(new_cats[j])
            for k in range(len(new_dogs)):  # Assignment of new list from current directory to the master list
                dog_list.append(new_dogs[k])

    for i in range(len(file_list)):
        if classify_pic(path + '/' + file_list[i]) >= .5:  # Creation of new list in current directory
            dog_list.append(path + '/' + file_list[i])
        else:
            cat_list.append(path + '/' + file_list[i])

    return cat_list, dog_list


def main():
    start_path = './'  # current directory

    cats, dogs = process_dir(start_path)

# Loops created to print values inside each list
    if len(cats) > 1:
        for m in range(len(cats)):
            print(cats[m])
    else:
        print('There are no available cats to adopt!')
    if len(dogs) > 1:
        for n in range(len(dogs)):
            print(dogs[n])
    else:
        print('There are no available dogs to adopt!')


main()

