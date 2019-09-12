#!/usr/bin/env python

# -*- coding: utf-8 -*-
#''''
#game: hunt the wumpus
#'''

from random import choice

def create_channel(cave_from,cave_to):
    cave[cave_from].append(cave_to)
    cave[cave_to].append(cave_from)
    
def visit_cave(cave_numbers):
    visited_caves.append(cave_numbers)
    unvisited_caves.remove(cave_numbers)
def choose_cave(cave_list):
    cave_numbers = choice(cave_list)
    if len(cave[cave_numbers])>=3:     #每个洞穴有三个通道
        cave_numbers = choice(cave_list)
    return cave_numbers
    
def setup_caves(cave_numbers):    
    cave = []
    for i in cave_numbers:
        cave.append([])
    return cave

def link_caves():
    while unvisited_caves !=[] :
        this_cave = choose_cave(visited_caves)
        next_cave = choose_cave(unvisited_caves)
        create_channel(this_cave, next_cave)
        visit_cave(next_cave)
    
def finish_caves():
    for i in cave_numbers:
        while len(cave[i]) < 3:
            passage_to = choose_cave(cave_numbers)
            cave[i].append(passage_to)
        
def print_caves():
    for i in cave_numbers:
        print(i,":",cave[i])
        
def print_location(player_location):
    '''tell the player about where his is'''
    print()
    print(cave_names[player_location])
    print("From here, you can see caves: ")
    neighbors = cave[player_location]
    for tunnel in range(0,3):
        next_cave = neighbors[tunnel]
        print(" ",tunnel+1,"-",cave_names[next_cave])
    if wumpus_location in neighbors:
        print("I smell a wmpus!")

        
def ask_for_cave():
    ''''
    Ask the player to chose a cave from their current_location
    '''
    player_input = raw_input("which cave ?")
    if (player_input in ["1","2","3"]):
        index = int(player_input)-1
        neighbors = cave[player_location]
        cave_number = neighbors[index]
        return cave_number
    else:
        print(player_input+"?")
        print("That's not a direction that I can see!")
        return False
# def update_player_location():
#     """ Change the player's location based on their input """
#     print ("Which cave next?")
#     player_input = input(">")
#     if (not player_input.isdigit() or 
#         int(player_input) not in cave[player_location]):
#         print (player_input + "? That's not a direction that I can see!")
#         return False
#     else:
#         return int(player_input)
def get_action():
    #'''Find out what the player wants to do next'''
    print('What do you do next?\nmove(m) or fire an arrow(a)?')
    action = raw_input(">")
    if action =="m" or action =="a":
        return action
    else:
        print(action+"?")
        print("That's not an action that I know about")
        return None
def do_movement():
    print("Moving")
    new_location = ask_for_cave()
    if new_location is None:
        return player_location
    else:
        return new_location
def do_shooting():
    print("Firing...")
    global shooting_count
    shoot_at = ask_for_cave()
    shooting_count -= 1
#     if shoot_at ==None:
#         return False
    while shooting_count != 0:
        if shoot_at == wumpus_location:
            print("Twang...Aargh! You shot the wumpus!\nWell done!, mighty wumpus hunter")
            return True
        else:
    #         print("Twang...clatter,clatter!\nYou wasted your arrow!\nEmpty handed, you begin the \n long trek back to your village...")
            return False
    if shooting_count == 0:
        print("Twang...clatter,clatter!\nYou wasted your arrow!\nEmpty handed, you begin the \n long trek back to your village...")
        return True
def do_move_by_abyss(player_location):
    global cave_numbers, bat_location
    new_location = choice(cave_numbers)
    while new_location == player_location:
        new_location = choice(cave_numbers)
        
    return new_location
#     new_location = cave[player_location]
#     player_location = new_location
#     print("you meet an abyss! And you will be moved to", new_location)
#     return player_location
    
cave_numbers = range(0,20)
cave_names = ["Arched cavern","Twisty passages", "Dripping cave","Dusty crawlspace","Underground lake","Black pit", "Fallen cave", "shallow pool",
                    "Icy underground river", "Sandy hollow", "Old firepit", "Tree root cave", "Narrow ledge", "Winding steps", "Echoing chamber", "Musty cave",
                    "Gloomy cave", "Low ceilinged cave", "Wumpus lair", "Spooky Chasm"]
unvisited_caves = list(range(0,20))
visited_caves=[]
cave = setup_caves(cave_numbers)
visit_cave(0)
print_caves()
link_caves()
print_caves()
finish_caves()
wumpus_location = choice(cave_numbers)
#print("wumpus_location is ",wumpus_location)
bat_location = choice(cave_numbers) #遇到蝙蝠会将玩家拖到另一个洞穴
#print("bat_location is  ",bat_location)
abyss_location = choice(cave_numbers) #遇到深渊则和遇到Wumpus类似-丧命，但射箭的效果无效
player_location = choice(cave_numbers)
shooting_count = 3


while player_location == wumpus_location or player_location == abyss_location:   
    player_location = choice(cave_numbers)
 
while 1:
    print_location(player_location)
    print("Remainging arrows = ", shooting_count)
    action = get_action()
    if action == None:
        continue
    if action == "m":
        player_location=do_movement()
        if player_location ==bat_location:
            player_location = do_move_by_abyss(bat_location)
            print("you meet an abyss! And you will be moved to", player_location)
            continue
        elif player_location == wumpus_location :
            print("Aargh! You got eaten by a wumpus!")
            break
        elif player_location == abyss_location:
            print("You fell in the dark abyss!")
            break
    elif action == "a":
        game_over = do_shooting()
        if game_over:
            break
        else:
            next_location = choice(cave_numbers)
            while player_location ==next_location:
                next_location =choice(cave_numbers)
            player_location =next_location
            print("You wasted your arrow!! And you will be moved to", player_location)
            continue

        
        


    