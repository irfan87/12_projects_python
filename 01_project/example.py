# string concatenation (aka how to put strings together)
# suppose we want to create a string that says "subscribe to _____"

favorite_youtuber = "Kyle Ying" # some string variables

# a few ways to do this
# using the '+' sign as concatenation
print("subscribe to " + favorite_youtuber)

# or using f string
print(f"subscribe to {favorite_youtuber}")

# or the old school concat using double curly braces with format function
print("subscribe to {}".format(favorite_youtuber))

# we can use concate() to concat the strings
print("subscribe to ".concat(favorite_youtuber))