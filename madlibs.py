# prompt user for a series of inputs
# take inputs and plug them in to a story template
# print out story at the end

print("Let's play madlibs!")
plural_noun =  raw_input("Plural noun:  ")
occupation =  raw_input("Occupation:  ")
plural_animal =  raw_input("Animal, plural:  ")
place =  raw_input("Place:  ")
verb =  raw_input("Verb:  ")
noun =  raw_input("Noun:  ")

story = "In the book War of the {}, the main character is an anonymous {} who records the arrival of {} in {}. Needless to say, havoc reigns as the {} continue to {} everything in sight, until they are killed by the common {}.".format(plural_noun, occupation, plural_animal, place, plural_animal, verb, noun)

print(story)
