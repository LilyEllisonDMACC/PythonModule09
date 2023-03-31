"""
Program: dictionary_ops.py
Author: Lily Ellison
Last date modified: 03/31/2023

The purpose of this program is to create a module with a
dictionary print function to be used in another file as part of a package.

"""


def print_dict(d: dict):
    for x, y in d.items():
        print(x, y)
