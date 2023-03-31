"""
Program: my_definitions.py
Author: Lily Ellison
Last date modified: 03/31/2023

The purpose of this program is to create a module with functions to be used in another file.

"""


def friendly_greeting():
    print("Salutations!")

def code_author():
    print("Code written by Lily Ellison.")


def print_dict(d: dict):
    for x, y in d.items():
        print(x,y)


def print_set(s: set):
    for item in s:
        print(item)
