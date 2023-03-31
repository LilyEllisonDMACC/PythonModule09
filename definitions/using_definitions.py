"""
Program: using_definitions.py
Author: Lily Ellison
Last date modified: 03/31/2023

The purpose of this program is to use the modules and functions from the package "definitions".

"""
from definitions import dictionary_ops, greeting, set_ops

myDictionary = {
    "Puppy": "Ash",
    "Boy Kitten": "Hercules",
    "Girl Kitten": "Pegasus",
    "Girl Cat": "Hazel"
}

mySet = {1, 2, 3, 4, 5, 6}

if __name__ == '__main__':

    greeting.friendly_greeting()
    greeting.code_author()
    dictionary_ops.print_dict(myDictionary)
    set_ops.print_set(mySet)
