
# introduce the game
print("WHAT KIND OF DOG ARE YOU?")
print("we have: Dog Dog")
print("There's: Big Dog (cow)")
print("who's that? oh it's a Road DawwwG (motorbike)")
print("Knock Knock baby! It's Sea Dog ARF ARF")

# initialise variables
dogdog = 0
bigdog = 0
roaddog = 0
seadog = 0

# get input for questions
answer1 = input("Do you have four legs? (Y/N) ")
answer2 = input("Do you have a wet nose? (Y/N) ")
answer3 = input("Are you made of metal? (Y/N) ")
answer4 = input("Are you found on a farm? (Y/N) ")
answer5 = input("do you have a tail? (Y/N) ")

# points logic
if answer1.capitalize() == "Y":
    dogdog = dogdog + 1
    bigdog = bigdog + 1
    roaddog = roaddog + 0
    seadog = seadog + 0
elif answer1.capitalize() == "N":
    dogdog = dogdog + 0
    bigdog = bigdog + 0
    roaddog = roaddog + 1
    seadog = seadog + 1
else:
    print("INVALID ANSWER! THIS IS SERIOUS DAMMIT!")

if answer2.capitalize() == "Y":
    dogdog = dogdog + 1
    bigdog = bigdog + 1
    roaddog = roaddog + 0
    seadog = seadog + 1
elif answer2.capitalize() == "N":
    dogdog = dogdog + 0
    bigdog = bigdog + 0
    roaddog = roaddog + 1
    seadog = seadog + 0
else:
    print("INVALID ANSWER! THIS IS SERIOUS DAMMIT!")

if answer3.capitalize() == "Y":
    dogdog = dogdog + 0
    bigdog = bigdog + 0
    roaddog = roaddog + 1
    seadog = seadog + 0
elif answer3.capitalize() == "N":
    dogdog = dogdog + 1
    bigdog = bigdog + 1
    roaddog = roaddog + 0
    seadog = seadog + 1
else:
    print("INVALID ANSWER! THIS IS SERIOUS DAMMIT!")

if answer4.capitalize() == "Y":
    dogdog = dogdog + 1
    bigdog = bigdog + 1
    roaddog = roaddog + 0
    seadog = seadog + 0
elif answer4.capitalize() == "N":
    dogdog = dogdog + 0
    bigdog = bigdog + 0
    roaddog = roaddog + 1
    seadog = seadog + 1
else:
    print("INVALID ANSWER! THIS IS SERIOUS DAMMIT!")

if answer5.capitalize() == "Y":
    dogdog = dogdog + 1
    bigdog = bigdog + 1
    roaddog = roaddog + 0
    seadog = seadog + 1
elif answer5.capitalize() == "N":
    dogdog = dogdog + 0
    bigdog = bigdog + 0
    roaddog = roaddog + 1
    seadog = seadog + 0
else:
    print("INVALID ANSWER! THIS IS SERIOUS DAMMIT!")

# find the highest score.
dogs = [dogdog, bigdog, roaddog, seadog]
# print results
if max(dogs) == dogdog:
  print("Congratulations! you are a nice normal dog. wet nose, waggy tail, all that good stuff.")
elif max(dogs) == bigdog:
    print("Neat! You're a Big Dog AKA a cow. You eat grass and have lots of stomachs, which must be well bad if you get the flu. Anyway, good job")
elif max(dogs) == roaddog:
    print("Okay so something went wrong here because you're actually a motorbike AKA ROADDAWGG")
elif max(dogs) == seadog:
    print("You're a salty ol' sea dog AKA a sealion. Hope you like balls on your nose.")
else:
    print("okay so something has gone wrong here, probably the two highest variables have the same value and I couldn't work out how to fix that sooo here we are. Let's just say you're a cat instead.")