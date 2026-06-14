import pygame
import time

def drumRoll():
    t = 1
    s = 2
    while s > 0.35:
        print(".")
        time.sleep(s)
        t+=0.5
        s = 2/t

name = input("How would you like to name your character? ")
print("The story of " + name + " starts here.\nIn the grey lands of the Southern Marshes, where the big beat sounds.\nWhere the Crawling King Snake rules, though he is old and his skin is cold.\nIn these marshes, the peace frogs dance jollily to the big beat.\nThis is where the story starts.")
time.sleep(2) #change to longer later
print("\nSubterraneans")
time.sleep(2)

drumRoll()
print("Chapter 1: The King")
time.sleep(3)
print("Here you are, in the marshes, you look around and see shallow brown water, plants in the water, plants on the water. There are mosquitoes everywhere.\nYou've got a mere three options: ")
 
choice1 = "1"
while choice1 != "2":
    choice1 = input("[1] Turn back to where you came from\n[2] Wade on through the dirty waters\n[3] Drown\n")
    if choice1 == "1" or choice1 == "2" or choice1 == "3":
        if choice1 == "1":
            print("You turn 180 degrees, but see a big dirt wall behind you. You can't turn back.")
        if choice1 == "3":
            print("You drowned in the dirty waters. May you rest in peace.")
            quit()
            break 
    else:
        print("Choose an available option")
        continue
else:
    print("You keep on wading through the water, your feet sinking in the mud, your head and shoulders getting repeatedly stung by the many mosquitoes. A light drizzle starts.")

time.sleep(5)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print("After a few hours of plowing through the swamps, the chirping of the crickets and the big beat is interrupted by an initially soft hissing, become increasingly louder.")
time.sleep(8)
print("The hissing forms a song that is haunting but at the same time groovy and that takes you away to higher dimentions.")
time.sleep(8)
print("Before you, a face emerges out of the rain. [insert description of Crawling King Snake]. He asks you: 'Where did you come from and how dare you enter my Southern Marshes?'\n")
time.sleep(10)
print("You conjure up a reply:\n")

def crystalShipDialogue():
    print("The Crawling King Snake takes you to a small wooden dock.\nOn the very end of the dock, a rusty old car with no wheels is parked in the shallow water.\nAs you come closer, you see three muddy, brown frogs. The driver-frog is wearing glasses.\n")
    time.sleep(20)
    print("The one frog sitting a back seat says: 'Hey man... get in.'\n")
    time.sleep(5)
    print("You open the rusty door and step inside as a nauseating smell enters your nose.\nThe driver-frog, with the glasses, turns to you and says: 'Hi.. We're the Riders... on the storm, welcome to our Crystal Ship. We heard we gotta take you outta here.'\nThe shotgun-frog hands you a small, green fruit and says: 'Here take this, eat it. It's the only way outta here man...'\n")
    time.sleep(20)
    print("You hesitantly take the fruit.\nJust as you open your mouth to start chewing, the Crawling King Snake speaks and says: 'Alright now take it easy. Fare you well Stranger, soil-marcher.'\n")
    time.sleep(10)
    print("You put the fruit in your mouth and chew.\nAn orange glow slowly forms around the edges of your view.\nThe driver-frog, with the glasses, yells: 'Alright! Let's go on a moonlight drive!'\n")

answer1 = "0"
while answer1 != "1" or answer1 != "2" or answer1 != "3" or answer1 != "4":
    answer1 = input("[1] You say: 'I tripped and fell into a dark pit, falling for what felt like hours, landing in your marshes in front of a dirt wall.' (philosophical truth)\n[2] You say: 'I'm not sure where I came from, I didn't know these were your marshes, sorry.' (truth)\n[3] You say: 'May peace be upon you and your lands, I am a traveller from the country of sunken mountains and fallen trees, greetings.' (made up philosophical reply with some truth in it)\n[4] You say: 'I walked in here, in search of King Crimson's treasure, do you know where it might be?' (lie)\n")
    if answer1 == "1":
        print("The Crawling King Snake says: 'Ah, you are one of those, a stranger from the top of the soil.\nWell, as long as you don't disturb our peace, we won't bother you.'")
    elif answer1 == "2":
        print("The Crawling King Snake says: 'Hmm... You must be one of those Soil-Marchers from the top.\nCan you remember anything at all from before you got here?\n")
        time.sleep(8)
        answer1sub1 = "0"
        while answer1sub1 != "1" or answer1sub1 != "2":
            answer1sub1 = input("[1] You say: 'I can only remember a vague white light surrounded by blue.' (truth)\n[2] You say: 'No, nothing.' (lie)\n")
            if answer1sub1 == "1":
                print("The Crawling King Snake says:\n'A Soil-Marcher indeed.\nIn that case, I'll try to help your poor soul.\nI'll get you out of these godforsaken lands, my Riders will take you over my highway to the west.\nThe west is the best.'\n")
                time.sleep(15)
                crystalShipDialogue()
                time.sleep(8)
                drumRoll()
                print("Chapter 2: In the Court of the Crimson King")
                break
            elif answer1sub1 == "2":
                print("b")
            else:
                print("Choose an available option.")
                continue
        break
    elif answer1 == "3":
        print("The Crawling King Snake says: 'From the Quiet Country huh?\nWe don't see your kind much around here, what brings you here, Stranger?'")
    elif answer1 == "4":
        print("The Crawling King Snake says: 'You're bold to just walk in my lands like that.\nKing Crimson's treasure you said huh? \nWell since our families have been in a rivalry for aeons, I might just help you with your search. \nYou got a trace yet?'")
    else:
        print("Choose an available option")
        continue
