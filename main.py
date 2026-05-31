import pygame
import time

name = input("How would you like to name your character? ")
print("The story of " + name + " starts here.\nIn the grey lands of the Southern Marshes, where the big beat sounds.\nWhere the Crawling King Snake rules, though he is old and his skin is cold.\nIn these marshes, the peace frogs dance jollily to the big beat.\nThis is where the story starts.")
time.sleep(2) #change to longer later
print("\nSubterraneans")
time.sleep(2)

t=1
s = 2
while s > 0.35:
    print(".")
    time.sleep(s)
    t+=0.5
    s = 2/t
print("insert text")