import math
import time
import random as rd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from ipywidgets import interact, interactive, fixed, interact_manual 
from IPython.display import Image, display

monty_hall_wins_from_changing = 0
monty_hall_wins_from_staying = 0

# simple function to generate heads and tails flips 
def flip_coins(trials):
    flips = np.random.randint(low=0, high=2, size=trials)
    
    events = {"Heads": 0, "Tails": 0}
        
    for n in range(trials):
        if(flips[n] == 0):
            events["Heads"] = events.get("Heads") + 1
        else:
            events["Tails"] = events.get("Tails") + 1

    keys = events.keys()
    values = events.values()
    plt.bar(keys, values, color = ["cyan","orange"])
    plt.ylabel("# of Flips")
    plt.ylim(0, int(trials))
    
    labels = [events.get("Heads"), events.get("Tails")]
    plt.text(x = -0.05, y = labels[0] + 0.4, s = labels[0], size = 20)
    plt.text(x = 0.90, y = labels[1] + 0.4, s = labels[1], size = 20)

# simple function to generate pairs of heads and tails flips
def flip_coins_pairs(trials):
    trials *= 2
    flips = np.random.randint(low=0, high=2, size=trials)
    
    events = {"HH": 0, "TH": 0, "HT": 0, "TT": 0}
    
    for n in range(0, trials, 2):
        if(flips[n] == 0 and flips[n + 1] == 0):
            events["HH"] = events.get("HH") + 1
        if(flips[n] == 1 and flips[n + 1] == 0):
            events["TH"] = events.get("TH") + 1
        if(flips[n] == 0 and flips[n + 1] == 1):
            events["HT"] = events.get("HT") + 1
        if(flips[n] == 1 and flips[n + 1] == 1):
            events["TT"] = events.get("TT") + 1

    keys = events.keys()
    values = events.values()
    plt.bar(keys, values, color = ["blue","yellow","green","red"])
    plt.ylabel("# of Flips")
    plt.ylim(0, int(trials))
    
    labels = [events.get("HH"), events.get("TH"), events.get("HT"),events.get("TT")]
    plt.text(x = -0.1, y = labels[0] + 0.4, s = labels[0], size = 20)
    plt.text(x = 0.90, y = labels[1] + 0.4, s = labels[1], size = 20)
    plt.text(x = 1.90, y = labels[2] + 0.4, s = labels[2], size = 20)
    plt.text(x = 2.90, y = labels[3] + 0.4, s = labels[3], size = 20)
    
# simple function to generate three heads and tails flips
def flip_coins_triples(trials):
    trials *= 3
    flips = np.random.randint(low=0, high=2, size=trials)
    
    events = {"HHH": 0, "THH": 0, "HTH": 0, "TTH": 0, "HHT": 0, "THT": 0, "HTT": 0, "TTT": 0}
    
    for n in range(0, trials, 3):
        if(flips[n] == 0 and flips[n + 1] == 0 and flips[n + 2] == 0):
            events["HHH"] = events.get("HHH") + 1
        if(flips[n] == 1 and flips[n + 1] == 0 and flips[n + 2] == 0):
            events["THH"] = events.get("THH") + 1
        if(flips[n] == 0 and flips[n + 1] == 1 and flips[n + 2] == 0):
            events["HTH"] = events.get("HTH") + 1
        if(flips[n] == 1 and flips[n + 1] == 1 and flips[n + 2] == 0):
            events["TTH"] = events.get("TTH") + 1
        if(flips[n] == 0 and flips[n + 1] == 0 and flips[n + 2] == 1):
            events["HHT"] = events.get("HHT") + 1
        if(flips[n] == 1 and flips[n + 1] == 0 and flips[n + 2] == 1):
            events["THT"] = events.get("THT") + 1
        if(flips[n] == 0 and flips[n + 1] == 1 and flips[n + 2] == 1):
            events["HTT"] = events.get("HTT") + 1
        if(flips[n] == 1 and flips[n + 1] == 1 and flips[n + 2] == 1):
            events["TTT"] = events.get("TTT") + 1

    keys = events.keys()
    values = events.values()
    plt.bar(keys, values, color = ["blue","yellow","green","red","purple","cyan","orange","violet"])
    plt.ylabel("# of Flips")
    plt.ylim(0, int(trials))
    
    labels = [events.get("HHH"), events.get("THH"), events.get("HTH"),events.get("TTH"),events.get("HHT"), events.get("THT"),events.get("HTT"),events.get("TTT")]
    plt.text(x = -0.1, y = labels[0] + 0.4, s = labels[0], size = 20)
    plt.text(x = 0.90, y = labels[1] + 0.4, s = labels[1], size = 20)
    plt.text(x = 1.90, y = labels[2] + 0.4, s = labels[2], size = 20)
    plt.text(x = 2.90, y = labels[3] + 0.4, s = labels[3], size = 20)
    plt.text(x = 3.9, y = labels[4] + 0.4, s = labels[4], size = 20)
    plt.text(x = 4.9, y = labels[5] + 0.4, s = labels[5], size = 20)
    plt.text(x = 5.9, y = labels[6] + 0.4, s = labels[6], size = 20)
    plt.text(x = 6.9, y = labels[7] + 0.4, s = labels[7], size = 20)
    

# simple function to generate heads and tails flips 
def flip_coins_biased(trials, heads_bias):
    flips = np.random.random(trials)
    events = {"Heads": 0, "Tails": 0}
        
    for n in range(trials):
        if(flips[n] < heads_bias):
            events["Heads"] = events.get("Heads") + 1
        else:
            events["Tails"] = events.get("Tails") + 1

    keys = events.keys()
    values = events.values()
    plt.bar(keys, values, color = ["cyan","orange"])
    plt.ylabel("# of Flips")
    plt.ylim(0, int(trials))
    
    labels = [events.get("Heads"), events.get("Tails")]
    plt.text(x = -0.05, y = labels[0] + 0.4, s = labels[0], size = 20)
    plt.text(x = 0.90, y = labels[1] + 0.4, s = labels[1], size = 20)
    
# A simple simulation of the monty hall problem.
# input:  number_of_doors - the number of doors
#         change_guess    - whether or not a contestant will change their guess
# output: 0 or 1          - if the contestant lost (0) or won (1)
def monty(number_of_doors, change_guess):
    # generate the game
    door_with_car = rd.randint(0,number_of_doors - 1)
    # have contestant guess
    guess = rd.randint(0,number_of_doors -1)
    # have monty reveal the doors by excluding one door and revealing all others
    door_to_keep_shut = door_with_car
    # if the contestant guessed the car, then find a random door to keep shut
    if(guess == door_with_car):
        while(guess == door_to_keep_shut):
            door_to_keep_shut = rd.randint(0,number_of_doors - 1)
    # reveal all of the bad prizes and offer the chance for the contestant to change their guess
    if(change_guess == True):
        guess = door_to_keep_shut
    if(guess == door_with_car):
        # contestant wins so return 1
        return 1
    return 0

# Repeated simulations of the monty hall problem, wins are summed and stored in an array.
# input:  number_of_doors - the number of doors
#         number_of_games - the number of games to play
# output: game_history    - an array containing all of the number of winning games for each game played
def monty_hall_sim(numdoors, numgames):
    game_history_stay = np.zeros(numgames)
    wins = 0
    for i in range(len(game_history_stay)):
        wins = wins + monty(numdoors, False)
        game_history_stay[i] = wins
    game_history_change = np.zeros(numgames)
    wins = 0
    for i in range(len(game_history_change)):
        wins = wins + monty(numdoors, True)
        game_history_change[i] = wins
    # plot the history
    x = np.arange(1,numgames + 1)
    y1 = game_history_stay
    y2 = game_history_change
    fig = plt.figure(figsize=(15,15))
    plt.title("Monty hall problem with " + str(numdoors) + " doors")
    plt.xlabel("Number of Games")
    plt.ylabel("Number of Wins")
    axes = plt.gca()
    axes.set_ylim([0,numgames + 1])
    plt.plot(x,y1,color='blue',label="Stay")
    plt.plot(x,y2,color='red',label="Change")
    plt.legend()
    plt.show()
    
def monty_hall_sim_interactive(guess, change):
    number_of_doors = 3
    guess -= 1
    door_with_car = rd.randint(0,2)
    door_to_keep_shut = door_with_car
    if(guess == door_with_car):
        while(guess == door_to_keep_shut):
            door_to_keep_shut = rd.randint(0,2)
    door_to_reveal = number_of_doors - door_to_keep_shut - guess
    # monty reveals shut door
    time.sleep(1.5)
    print("You tell Monty Hall that you choose door " + str(guess + 1) + "\n")
    time.sleep(1.5)
    print("Monty hall reveals that door " + str(door_to_reveal + 1) + " has a goat behind it!\n")
    guess_statement = "keep"
    if change == "Yes":
        guess_statement = "change"
        guess = door_to_keep_shut
    time.sleep(1.5)
    print("Since you chose to " + guess_statement + " your door, you choose door " + str(guess + 1) +"\n")
    time.sleep(1.5)
    if guess == door_with_car:
        print("Monty hall reveals a car, you win!\n")
    else:
        print("Monty hall reveals a goat", end="")
        time.sleep(1)
        print("...\n")
    time.sleep(1.5)
    print("Try again by changing the values for 'guess' or 'change', or both")

def radar_dectector(detections):
    plane_overhead = 0.05
    plane_not_overhead = 1 - plane_overhead
    # branches for a plane over head
    detect_plane = 0.99
    not_detect_plane = 1 - detect_plane
    # branches for a plane not overhead
    false_alarm = 0.1
    nothing_detected = 1 - false_alarm
        
    randone = np.random.random(detections)
    events = {"Missed": 0, "Detected": 0, "Nothing Detected": 0, "False Alarm": 0}

    for first in randone:
        second = rd.random()
        # plane not overhead
        if first > plane_overhead:
            if second > false_alarm:
                events['Nothing Detected'] = events.get('Nothing Detected') + 1
            else:
                events['False Alarm'] = events.get('False Alarm') + 1
        # plane not overhead
        else:
            if second > not_detect_plane:
                events['Detected'] = events.get('Detected') + 1
            else:
                events['Missed'] = events.get('Missed') + 1

    keys = events.keys()
    values = events.values()
    plt.bar(keys, values, color = ["orange","green","blue","red"])
    plt.ylabel("detections")
    plt.ylim(0, int(detections))
    
    labels = [events.get("Missed"), events.get("Detected"), events.get("Nothing Detected"),events.get("False Alarm")]
    plt.text(x = -0.1, y = labels[0] + 0.4, s = labels[0], size = 20)
    plt.text(x = 0.90, y = labels[1] + 0.4, s = labels[1], size = 20)
    plt.text(x = 1.90, y = labels[2] + 0.4, s = labels[2], size = 20)
    plt.text(x = 2.90, y = labels[3] + 0.4, s = labels[3], size = 20)
