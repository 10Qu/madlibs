# string concatenation (aka how to put strings together)
# suppose we want to create a string that says "subscribe to _____"
# youtuber = "Tenku" # some string variable

# a few ways to do this

## 1
# print("subscribe to " + youtuber)

## 2
# print("subscribe to {}".format(youtuber))

## 3 F-String
# print(f"subscribe to {youtuber}")

# Inputs
adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}"

print(madlib)