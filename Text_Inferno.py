# Start up
import chance
import random

yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]
 
# The game
name = input("What is the name of the person silly enough to play?\n")
print(", " + name + ". Let us start a journey through the levels of...!")
print("You find yourself on the edge of a firey inferno.")
print("Can you find your way through the 7 levels and back to reality?\n")

response = ""
while response not in yes_no:
    response = input("Will you want to jump over the fire?\nyes/no\n")
    if response == "yes":
        print("You head into a cavernous area. You hear shieks and screams in the distance.\n")
    elif response == "no":
        print("You must heat because this is where you'll stay. Goodbye, " + name + ".")
        quit()
    else: 
        print("Would you like to change your mind?\n")
 
response = ""
while response not in directions:
    print("To your left, you see a dwarf with a pitchfork.")
    print("To your right, there are more caves with twists are turns.")
    print("There is something sitting on a thrown holding a pitchfork infront of you.")
    print("Behind you is the exit to the next level of the firey inferno.\n")
    response = input("What direction do you move?\nleft/right/forward/backward\n")
    if response == "left":
        print("The dwarf starts jabbing you with their pitchfork. Farewell, " + name + ".")
        quit()
    elif response == "right":
        print("You head deeper into the caves.\n")
    elif response == "forward":
        print("Are you magical? I don't think you are, so don't try to walk through rock.\n")
        response = "" 
    elif response == "backward":
        print("You leave this level and only a few more levels to get back to land dwellers like you. Goodbye, " + name + ".")
        quit()
    else:
        print("Would you like to change your mind and try again?\n")