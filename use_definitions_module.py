"""
Program: use_definitions_module.py
Author: Lily Ellison
Last date modified: 03/31/2023

The purpose of this program is to use the module and functions "my_definitions".

"""
import my_definitions as md

myDictionary = {
    "Puppy": "Ash",
    "Boy Kitten": "Hercules",
    "Girl Kitten": "Pegasus",
    "Girl Cat": "Hazel"
}

mySet = {1, 2, 3, 4, 5, 6}

if __name__ == '__main__':
    md.friendly_greeting()
    md.code_author()
    md.print_dict(myDictionary)
    md.print_set(mySet)
