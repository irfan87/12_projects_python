# string concatenation (aka how to put strings together)
# suppose we want to create a string that says "subscribe to _____"

adjective = input('Adjective: ')
verb1 = input("Verb: ")
verb2 = input("Second Verb: ")
famous_person = input("Famous Person: ")

madlibs = f"Computer programming is so {adjective}!\nIt makes me so exiceted all the times because I love to {verb1}.\nStay hydrated and {verb2} like you are {famous_person}!"

print(madlibs)