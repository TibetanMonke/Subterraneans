import pygame
import time

name = input("How would you like to name your character? ")
print("The story of " + name + " starts here.\nIn the grey lands of the Southern Marshes, where the big beat sounds.\nWhere the Crawling King Snake rules, though he is old and his skin is cold.\nIn these marshes, the peace frogs dance jollily to the big beat.\nThis is where the story starts.")
time.sleep(2) #change to longer later
print("\nSubterraneans")
time.sleep(2)

t = 1
s = 2
while s > 0.35:
    print(".")
    time.sleep(s)
    t+=0.5
    s = 2/t
print("Chapter 1: Stuck")
time.sleep(3)
print("Here you are, in the marshes, you look around and see shallow brown water, plants in the water, plants on the water. There are mosquitoes everywhere.\nYou've got a mere three options: ")
 
choice1 = "1"
while choice1 != "2":
    choice1 = input("[1] Turn back to where you came from\n[2] Wade on through the dirty waters\n[3] Drown\n")
    print(choice1)
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

time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print("After a few hours of plowing through the swamps, the chirping of the crickets and the big beat is interrupted by an initially soft hissing, become increasingly louder.")
time.sleep(1)
print("The hissing forms a song that is haunting but at the same time groovy and that takes you away to higher dimentions.")
time.sleep(1)
print("Before you, a face emerges out of the rain. [insert description of Crawling King Snake]. He asks you: 'Where did you come from and how dare you enter my Southern Marshes?\nYou conjure up a reply:\n")

answer1 = "1"
answer1 = input("[1] You say: 'I tripped and fell into a dark pit, falling for what felt like hours, landing in your marshes in front of a dirt wall.' (Philosophical truth)\n[2] You say: 'I'm not sure where I came from, I didn't know these were your marshes, sorry.' (truth)\n[3] You say: 'May peace be upon you and your lands, I am a traveller from the country of sunken mountains and fallen trees, greetings.' (made up philosophical reply with some kind of truth in it)\n[4] You say: 'I walked in here, in search of King Crimson's treasure, do you know where it might be?' (lie)")
