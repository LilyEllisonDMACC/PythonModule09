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
