# Start up
import random
import time

def print_pause(message):
    print(message)
    time.sleep(1)
def end():
    done = False
    while not done:
        quit = input("Do you want to quit? ")
    if quit == "y":
        done = True
def wtd():
    print("I'm thinking of a number between 1 and 10")
    guess = 0 # give guess a starting value
    randNum = random.randint(1,10)
    guess = int(input("You want another try, guess the number:"))
    print (randNum)
    while guess != randNum:
        guess = int(input("Try to guess the number:"))
        if (guess == randNum):
            print ("You got it!")
        if (guess > randNum):
            print ("Wrong! You guessed too high")
        if (guess < randNum):
            print ("Wrong! You guessed too low")
        (end)

yes_no = ["yes", "no", "y", "n"]
directions = ["left", "right", "forward", "backward"]

# The game
name = input("What is the name of the person silly enough to play?\n")
print_pause(", " + name + ". Let us start a journey through the levels of...!")
response = input("Are you silly enough to play?\nyes/no\n")
print_pause("You find yourself on the edge of a firey inferno.")
print_pause("Can you find your way through the 7 levels and back to reality?\n")

response = ""
while response not in yes_no:
    response = input("Will you want to jump over the fire?\nyes/no\n")
    if response == "yes":
        print_pause("You head into a cavernous area. You hear shreiks and screams in the distance.\n")
    elif response == "no":
        print_pause("You must like heat because this is where you'll stay. Goodbye, " + name + ". Hahaha")
        wtd()
    else:
        print_pause("Would you like to change your mind?\n")
        if response == "yes":
            wtd()

response = ""
while response not in directions:
    print_pause("To your left, you see a dwarf with a pitchfork.\n"
                "To your right, there are more caves with twists are turns.")
    print_pause("There is something sitting on a thrown holding a pitchfork in front of you.")
    print_pause("Behind you is the exit to the next level of the firey inferno.\n")
    response = input("What direction do you move?\nleft/right/forward/backward\n")
    if response == "left":
        print_pause("The dwarf starts jabbing you with their pitchfork. Farewell, " + name + ".")
        wtd()
    elif response == "right":
        print_pause("You head deeper into the caves.\n")
    elif response == "forward":
        print_pause("Are you magical? I don't think you are, so don't try to walk through rock.\n")
        response = ""
    elif response == "backward":
        print_pause("You leave this level and only a few more levels to get back to land dwellers like you. Goodbye, " + name + ".")

response = ""
while response not in directions:
    print_pause("You look left, what do you see?\n"
                "To your right, there are more caves with twists are turns.")
    print_pause("There is something sitting on a thrown holding a pitchfork in front of you.")
    response = input("What direction do you move?\nleft/right/forward/backward\n")
    if response == "left":
        print_pause = input("You see Snow White, should you go toward her?\nyes/no\n")
        wtd()
    elif response == "no":
        print_pause("You must like heat because this is where you'll stay. Goodbye, " + name + ". Hahaha")
        end()
    elif response == "right":
        print_pause("You head deeper into the caves.\n")
        print_pause("Wait... little creatures with horns are chasing after you. They'/re throwing flaming spears at you!\n")
        print_pause = input("Do you want to run back?\nyes/no\n")
    if response == "yes":
        print_pause("Behind you is the exit to the next level of the firey inferno.\n")
        print_pause = input("Do you want to jump over a canyon filled with fire and screams coming from the bottom?\nyes/no\n")
    if response == "yes":
        print_pause("You didn't make it and now your screams can be heard from the canyon as well, hahaha!\n")
        wtd()
    elif response == "no":
        wtd()
    elif response == "no":
        wtd()
    elif response == "forward":
        print_pause("Are you magical? I don't think you are, so don't try to walk through rock.\n")
        response = ""
        print_pause("Now the rocks fell and crushed you. Well... I guess your game is over.")
        wtd()
    elif response == "backward":
        print("Are you trying to go back to your first level, " + name +"?\n")
        wtd()
