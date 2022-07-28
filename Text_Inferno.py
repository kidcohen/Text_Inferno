# Start up
import random
import time

def play_again():
    start().
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
    print_pause("Would you like to change your mind and try again?\n")
    if response == "yes":
        n = random.randint(1, 10)
        guess = int(raw_input("Guess a number from 1 to 10 to keep playing: "))
        while n != "guess":
            guess = input("Tell me a number, any number!\n")
        if guess < n:
            print("guess is low")
            guess = int(raw_input("Is it that hard to guess it from 10 numbers?: "))
        elif guess > n:
            print("guess is high")
            guess = int(raw_input("Guess a number between 1 and 10 one more time: "))
        elif guess == n:
            print ("you guessed it!")
            play_again()
        else:
            print_pause("Too scary, eh, " + name +"?")
            return wtd()

yes_no = ["yes", "no", "y", "n"]
directions = ["left", "right", "forward", "backward"]

# The game
name = input("What is the name of the person silly enough to play?\n")
print_pause(", " + name + ". Let us start a journey through the levels of...!")
response = input("Are you silly enough to play?\nyes/no\n")
if response == "yes":
    wtd()
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
            play_again()
 
response = ""
while response not in directions:
    print_pause("To your left, you see a dwarf with a pitchfork.\n" 
                "To your right, there are more caves with twists are turns.")
    print_pause("There is something sitting on a thrown holding a pitchfork in front of you.")
    print_pause("Behind you is the exit to the next level of the firey inferno.\n")
    response = input("What direction do you move?\nleft/right/forward/backward\n")
    if response == "left":
        print_pause("The dwarf starts jabbing you with their pitchfork. Farewell, " + name + ".")
        quit()
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
    print_pause("Behind you is the exit to the next level of the firey inferno.\n")
    response = input("What direction do you move?\nleft/right/forward/backward\n")
    if response == "left":
        print_pause("You see Snow White, should you go toward her?")
        quit()
    elif response == "right":
        print_pause("You head deeper into the caves.\n")
    elif response == "forward":
        print_pause("Are you magical? I don't think you are, so don't try to walk through rock.\n")
        response = ""
    elif response == "backward":
        print("Are you trying to go back to your first level, " + name +"?\n")
        wtd()
