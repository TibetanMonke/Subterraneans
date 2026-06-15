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

def snakeMeeting():
    time.sleep(5)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("After a few hours of plowing through the swamps, the chirping of the crickets and the big beat is interrupted by an initially soft hissing, become increasingly louder.")
    time.sleep(8)
    print("The hissing forms a song that is haunting but at the same time groovy and that takes you away to higher dimentions.\n")
    time.sleep(8)
    print("Before you, a face emerges out of the rain. It's a giant king cobra. \nThe snake wears a royal crown on his head, from underneath which long brown curled strands of thick hair fall over the cobra's hood. \nThe cobra asks you: 'Where did you come from and how dare you enter my Southern Marshes?'\n")
    time.sleep(20)
    print("You conjure up a reply:\n")

def crystalShipDialogue():
    print("The Crawling King Snake takes you to a small wooden dock.\nOn the very end of the dock, a rusty old car with no wheels is parked in the shallow water.\nAs you come closer, you see three muddy, brown frogs sitting inside the car2. The driver-frog is wearing glasses.\n")
    time.sleep(20)
    print("The one frog sitting a back seat says: 'Hey man... get in.'\n")
    time.sleep(5)
    print("You open the rusty door and step inside as a nauseating smell enters your nose.\nThe driver-frog, with the glasses, turns to you and says: 'Hi.. We're the Riders... on the storm, welcome to our Crystal Ship. We heard we gotta take you outta here.'\nThe shotgun-frog hands you a small, green fruit and says: 'Here take this, eat it. It's the only way outta here man...'\n")
    time.sleep(20)
    print("You hesitantly take the fruit.\nJust as you open your mouth to start chewing, the Crawling King Snake speaks and says: 'Alright now, take it easy. Fare you well Stranger, soil-marcher.'\n")
    time.sleep(10)
    print("You put the fruit in your mouth and chew.\nAn orange glow slowly forms around the edges of your view.\nThe driver-frog, with the glasses, yells: 'Alright! Let's go on a moonlight drive!'\n")
    time.sleep(10)

def journeyToKingdom():
    print("You," + name + ", fly over the clouds, inside the Crystal Ship, to lands unknown.")
    time.sleep(5)
    print("The clouds below you are in every colour and in shapes like in a kaleidoscope.")
    time.sleep(5)
    print("The faces of the frogs around you change proportions constantly.")
    time.sleep(4)
    print("As you seem to slowly turn back to normal, the Crystal Ship starts descending into the now bright white clouds.")
    time.sleep(8)
    print("Looking below you, you see a landscape of seemingly everlasting green hills in all directions.")
    time.sleep(8)
    print("The Crystal Ship touches down softly in the grass of one of those hills and the doors fly open automatically.")
    time.sleep(8)
    print("The driver-frog, with the glasses, says: 'Here you are, had a nice flight? Good luck with whatever you Strangers are trying to do...'")
    time.sleep(8)
    print("The moment both of your feet are on the grass, the Crystal Ship flies away with an incredible speed.")
    time.sleep(8)
    print("What will you do now?\n")

def moonchildMeeting():
    print("After a short walk, you close in on the Willow.\nYou realise there is someone there, a child it seems.\nThe child is dancing in the lake and then suddenly runs to sit behind the Willow.\nYou walk up to her and ask her what she's doing.\n")
    time.sleep(20)
    print("The child, not at all fazed by your arrival, replies, whispering:\n 'Shh! I'm playing hide and seek with the Ghosts of Dawn!\nAlthough just then I was dancing in the shallows of a river and in a moment I will be dreaming in the shadows of a Willow.'\n")
    time.sleep(20)
    print("She seems to have forgotten about the game she's playing, for she continues:\n'You must be one of those Strangers that pass by here occasionaly, I'm the Moonchild, still waiting for a smile of a Sunchild.\nI'll give you some advice: be careful with the King's Gaurds, you mustn't lie to them!'\n")
    time.sleep(20)
    print("Suddenly the Moonchild runs away into the hills and dissapears behind one soon after...\nSo, now what? You ask yourself.\n")
    time.sleep(8)

def redNightmare():
    print("Well... there you are, in a desert of grassy hills. \nThe night divides the day, and now you gaze at the night sky, which you notice is starless and thus bible black.")
    time.sleep(15)
    print("Your eyelids slowly close as you realise you haven't slept for a day and a half.")
    time.sleep(5)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(2)
    print("You open your eyes and vaguely remember a Red Nightmare about an aeroplane, you sweating, and a greyhound...")
    time.sleep(10)
    print("You look around and remember where you are")


print("DISCLAIMER: You might have a better experience with the use of imagination and read carefully!")
time.sleep(8)

name = input("How would you like to name your character? ")
print("The story of " + name + " starts here.\nIn the grey lands of the Southern Marshes, where the big beat sounds.\nWhere the Crawling King Snake rules, though he is old and his skin is cold.\nIn these marshes, the peace frogs dance jollily to the big beat.\nThis is where the story starts.")
time.sleep(12) #change to longer later
print("\n===============\n\nSubterraneans\n\n===============")
time.sleep(2)

drumRoll()
print("\n----------------\nChapter 1: Break on Through (To the Other Side)\n----------------")
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

snakeMeeting()

answer1 = "0"
while answer1 != "1" or answer1 != "2" or answer1 != "3" or answer1 != "4":
    answer1 = input("[1] You say: 'I tripped and fell into a dark pit, falling for what felt like hours, landing in your marshes in front of a dirt wall.' (philosophical truth)\n[2] You say: 'I'm not sure where I came from, I didn't know these were your marshes, sorry.' (truth)\n[3] You say: 'May peace be upon you and your lands, I am a traveller from the country of sunken mountains and fallen trees, greetings.' (made up philosophical reply with some truth in it)\n[4] You say: 'I walked in here, in search of King Crimson's treasure, do you know where it might be?' (lie based on ancient folklore)\n")
    if answer1 == "1":
        print("The Crawling King Snake says: \n'Ah, you are one of those Soil-Marchers, a Stranger from the top, aren't you?'\n")
        time.sleep(5)
        answer1sub1 = "0"
        while answer1sub1 != "1" or answer1sub1 != "2":
            answer1sub1 = input("[1] You say: 'I'm sorry, but I have no idea what a Soul-Marcher is or what you mean by 'the top' (truth).\n[2] You say: That's right... I think...' (obvious lie in order to get an explanation)")
            if answer1sub1 == "1":
                print("The Crawling King Snake says: \n'Right... Well neither do any of the Strangers down here. \nAll I can say that you are now in the realm of the Subterraneans and people from the top are what we call Soil-Marchers.\nI'll help your poor soul out of these godforsaken lands.\nMy Riders will take you over my highway to the west.\nThe west is the best.'\n")
                time.sleep(20)
                break
            if answer1sub1 == "2":
                print("The Crawling King Snake says: \n'Yeah that's what I thought.\nWell in that case, I'll try to help your poor soul.\nI'll get you out of these godforsaken lands, my Riders will take you over my highway to the west.\nThe west is the best.'\n")
                time.sleep(15)
                break
        break
    elif answer1 == "2":
        print("The Crawling King Snake says: \n'Hmm... You must be one of those Soil-Marchers from the top.\nCan you remember anything at all from before you got here?\n")
        time.sleep(8)
        answer1sub2 = "0"
        while answer1sub2 != "1" or answer1sub2 != "2":
            answer1sub2 = input("[1] You say: 'I can only remember a vague white light on a clear blue background.' (truth)\n[2] You say: 'No, nothing.' (lie)\n")
            if answer1sub2 == "1":
                print("The Crawling King Snake says:\n'A Soil-Marcher indeed.\nIn that case, I'll try to help your poor soul.\nI'll get you out of these godforsaken lands, my Riders will take you over my highway to the west.\nThe west is the best.'\n")
                time.sleep(15)
                break
            elif answer1sub2 == "2":
                print("The Crawling King Snake says:\n'Though I see straight through your lie, I respect your suspicion of strangers.\nYou should be suspicious in these, to you, unknown lands.\nThere are creatures out here who are not afraid to rob or kill, so be cautious like were just then, play it smart.'\n")
                time.sleep(20)
                print("He continues: \n'Well, like I said, I presume you are a Soil-Marcher, one from the top.\nIf that is indeed the case, I'm gonna try to help you as best as I can.\nYou can't stay here, it's too dangerous and besides, you probably won't get out of here on you own.\nI'll get you out of these godforsaken lands, my Riders will take you over my highway to the west.\nThe west is the best.'\n")
                time.sleep(25)
                break
            else:
                print("Choose an available option.")
                continue
        break
    elif answer1 == "3":
        print("The Crawling King Snake says: \n'From the Quiet Country huh?\nWe don't see your kind much around here, what brings you here, Stranger?'")
        time.sleep(8)
        answer1sub3 = "0"
        while answer1sub3 != "1" or answer1sub3 != "2":
            answer1sub3 = input("[1] You say: 'An almost infinite amount of causes that are retracable to before the creation of the universe bring me to the place and position I'm currently in.' [technically the truth] \n[2] You say: 'To be honest, I don't know. (lie, but close to the truth)'\n")
            if answer1sub3 == "1":
                print("The Crawling King Snake says: \n'You're that kind of person huh?\nWell, be cautious: a lot of creatures in these lands wouldn't have even let you finish that sentence.\nYou don't look like you belong or want to be here.\nFor your own sake, I'll have you taken west over my highway.\nThe west is the best, you'll travel with my Riders.'\n")
                time.sleep(20)
                break
            elif answer1sub3 == "2":
                print("The Crawling King Snake says: \n'Neither did any of the Strangers that have passed through these lands.\nI'm guessing you're a Soil-Marcher, from the top.\nIf that is indeed the case, I'm gonna try to help you as best as I can.\nYou can't stay here, it's too dangerous and besides, you probably won't get out of here on you own.\nI'll get you out of these godforsaken lands, my Riders will take you over my highway to the west.\nThe west is the best.'\n")
                time.sleep(20)
                break    
        break
    elif answer1 == "4":
        print("The Crawling King Snake says: \n'You're bold to just walk in my lands like that.\nKing Crimson's treasure you said huh? \nWell since our families have been in a rivalry for aeons, I might just help you with your search. \nYou got a trace yet?'")
        time.sleep(10)
        answer1sub4 = "0"
        while answer1sub4 != "1" or answer1sub4 != "2":
            answer1sub4 = input("[1] You say: 'Yes, I found out that the treasure is somewhere in his kingdom, under The Willow.' (lie based on the same folklore)\n[2] You say: 'Uhm no... I'm not actually looking for a treasure, I don't know how I ended up here.' (painful truth)")
            if answer1sub4 == "1":
                print("The Crawling King Snake says:\n'Alright great! I can help you with getting to the King's kingdom.\nMy Riders can take you there in the blink of an eye, let me take you to them.'\n")
                time.sleep(15)
                break
            elif answer1sub4 == "2":
                print("The Crawling King Snake says:\n 'Of course... Just like every other Stranger that passes through these marshes.\nYou must be a Soil-Marcher, from the top.\nIf that is indeed the case, I'm gonna try to help you as best as I can.\nYou can't stay here, it's too dangerous and besides, you probably won't get out of here on you own.\nI'll get you out of these godforsaken lands, my Riders will take you over my highway to the west.\nThe west is the best.'\n")
                time.sleep(20)
                break
    else:
        print("Choose an available option")
        continue

crystalShipDialogue()
drumRoll()
print("\n----------------\nChapter 2: Red\n----------------")
 
journeyToKingdom()

choice2 = "0"
willow = False
walking = False
waiting = False
while choice2 != "1" or choice2 != "2" or choice2 != "3":
    choice2 = input("[1] Start walking in a random direction \n[2] Walk to the lonely Willow standing on the shore of a small river \n[3] Wait\n")
    if choice2 == "1":
        print("You start walking... \nFor hours upon hours you walk, uphill, downhill, uphill, downhill, but the hills won't budge.\nThe sun sinks and the sky turns a soft peach pink.\n")
        time.sleep(15)
        walking = True
        break
    elif choice2 == "2" and willow == False:
        moonchildMeeting()
        willow = True
        continue
    elif choice2 == "2" and willow == True:
        print("Surely you remember what happened at the Willow, go do something else.")
        continue
    elif choice2 == "3":
        print("You wait... for hours...\nYou wait some more...\nWhile you're waiting, the sun starts to sink behind the hills and the sky turns a soft peach pink.\n")
        time.sleep(15)
        waiting = True
        break
    else:
        print("Choose an available option")
        continue

redNightmare()

if walking == True and waiting == False:
    print("Should you keep on walking?")
    choice3Text1 = "You keep on walking"
    choice3Text2 = "You wait"
elif walking == False and waiting == True:
    print("Should you start moving?")
    choice3Text1 = "You start walking"
    choice3Text2 = "You keep waiting"

choice3 = "0"
while choice3 != "1" or choice3 != "2":
    choice3 = input("[1] " + choice3Text1 + "\n[2] " + choice3Text2 + "\n")
    if choice3 == "1":
        print("You walk.\nYou walk for a long time.\nThen... From behind the endless green hills, three towers rise up.\nA mighty palace made entirely out of red bricks appears before you.\nYou approach the gates...\n")
        time.sleep(20)
        print("On each side of the gate stands a tall guard in medieval knight armour, both armed with a halberd.\nAs you approach the gate they cross there halberds and speak in unison:\n'Who are you and why do you wish to enter King Crimson's palace?\n")
        time.sleep(20)
        print("You reply with: ")
        time.sleep(2)
        choice3sub1 = "0"
        liar = False
        while choice3sub1 != "1" or choice3sub1 != "2":
            choice3sub1 = input("[1] 'I come from the Southern Swamps, I'm " + name +  " and I'm looking for a way back home...' (truth)\n[2] 'I'm a free traveller and wish to speak to the King about the treasure in these lands.' (lie)\n")
            if choice3sub1 == "1":
                print("The guards reply in unison: 'From the Southern Swamps you say... Hmpf, well the King can always use new reports from those dirty lands, come on in.'\n")
                time.sleep(15)
                break
            elif choice3sub1 == "2" and liar == False:
                print("The guards reply in unison: 'A liar and deluded treasure-seekers, the King does not want you in his palace, begone!\n")
                time.sleep(15)
                print("Being sent back into the green hills will mean certain death for you, are you sure you don't want to correct yourself?")

                choice3sub1sub1 = "0"
                while choice3sub1sub1 != "1" or choice3sub1sub1 != "2":
                    choice3sub1sub1 = input("[1] Change your answer\n[2] Don't change your answer\n")
                    if choice3sub1sub1 == "1":
                        print("Good choice")
                        time.sleep(2)
                        break
                    if choice3sub1sub1 == "2":
                        print("So you have chosen... death")
                        time.sleep(5)
                        quit()
                        break
                continue
            elif choice3sub1 == "2" and liar == True:
                print("The guards yell (still in unison): 'Playing the jester, are we?!'\nThey raise their halberds and the last thing you see are the shiny clean blades falling...\nRest in peace, brave liar.")
                time.sleep(10)
                quit()
                break
            else:
                print("Choose an available option.")
                continue
        break
    elif choice3 == "2":
        print("You wait.\nYou wait for hours and hours.\nThen... from behind the endless green hills two knights on horseback appear.\nThey ride towards you...\n")
        time.sleep(15)
        print("The two riders halt besides you.\nThey look identical, wearing medieval armour and both armed with a halberd.\nThey speak in unison:\n'Who are you and why are you in King Crimson's land?\n")
        time.sleep(20)
        print("You reply with: ")
        time.sleep(2)
        choice3sub2 = "0"
        liar = False
        while choice3sub2 != "1" or choice3sub2 != "2":
            choice3sub2 = input("[1] 'I come from the Southern Swamps, I'm " + name +  " and I'm looking for a way back home...' (truth)\n[2] 'I'm a free traveller and wish to find treasure in these lands.' (lie)\n")
            if choice3sub2 == "1":
                print("The guards reply in unison: 'From the Southern Swamps you say... Hmpf, well the King can always use new reports from those dirty lands, we'll take you to him.'\n")
                time.sleep(15)
                print("After a long ride on horseback, a palace, fully made out of red bricks, rises up from behind the green hills.\nThe guards take you to the gates and let you in...\n")
                time.sleep(15)
                break
            elif choice3sub2 == "2" and liar == False:
                print("The guards reply in unison: 'A liar and deluded treasure-seekers, the King does not want you in his lands, begone!\n")
                time.sleep(15)
                print("Being sent away from these lands means certain death for you, you've got no idea where to go, are you sure you don't want to correct yourself?")

                choice3sub2sub1 = "0"
                while choice3sub2sub1 != "1" or choice3sub2sub1 != "2":
                    choice3sub2sub1 = input("[1] Change your answer\n[2] Don't change your answer\n")
                    if choice3sub2sub1 == "1":
                        print("Good choice")
                        time.sleep(2)
                        break
                    if choice3sub2sub1 == "2":
                        print("So you have chosen... death")
                        time.sleep(5)
                        quit()
                        break
                continue
            elif choice3sub2 == "2" and liar == True:
                print("The guards yell (still in unison): 'Playing the jester, are we?!'\nThey raise their halberds and the last thing you see are the shiny clean blades falling...\nRest in peace, brave liar.")
                time.sleep(10)
                quit()
                break
            else:
                print("Choose an available option.")
                continue
        break
    else:
        print("Choose an available option.")
        continue

drumRoll()
print("\n----------------\nChapter 3: In the Court of the Crimson King\n----------------")

print("Inside the palace, it doesn't look mutch different: red bricks.\nYou walk through halls of red bricks, not knowing where to go.\nThe palace seems to be totally empty of people, but full of red bricks...")
time.sleep(15)
print("\nEventually, might be a coincidence, it might be not, you end up in big hall (of red bricks) with one singular chair in the centre of the huge hall.\nThis chair is surrounded by about ten of the same kind of guards that questioned you earlier.")
time.sleep(15)
print("\nAs soon as they hear you, all of the guards turn around.\nA group of guards starts marching towards you, while the ones left behind akwardly try to turn the chair around.\nThe guards approach menacingly, while slowly but surely the chair is turned around...")
time.sleep(18)
print("\nJust as the guards want to take you away, the chair is finally fully turned and a small naked lizard appears sitting in that very chair.\nIn a very high voice he yells: 'Stop that! Let me see the Stranger!'")
time.sleep(15)
print("\nThe guards now hastily make way for the lizard to see you.\nThe lizard's jaw drops and he says: 'Ohhh... It's you..., " + name + "...\nI'm the Crimson King, or King Crimson, if you will, but you won't know me... Nor do you know why you're here...'")
time.sleep(15)
print("A silence falls...")
time.sleep(5)
print("You stay silent, in hope of getting an answer to your question.")
time.sleep(5)
print("Finally, the King Crimson continues: 'Well... It's simple. You're not here... You're dreaming... Wake up " + name + ".'")
time.sleep(10)

drumRoll()
print("===============\n\nThis is The End: beautiful friend...\n\n===============")