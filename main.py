# -*- coding: utf-8 -*-
#''''
#    game: hunt the wumpus
#    '''

from random import choice
#from cave import print_t

class Caves(object):
    def __init__(self,number_of_caves):
        self.number_of_caves = number_of_caves
        self.cave_list=range(number_of_caves)
        self.unvisited = range(number_of_caves)[1:]
        self.visited = [0]
        self.caves = []
        self.setup_caves(number_of_caves)
        self.link_caves()
    
    def setup_caves(self,cave_numbers):
        for cave in range(cave_numbers):
            self.caves.append([])
    
    def link_caves(self):
        while self.unvisited != []:
            this_cave = self.choose_cave(self.visited)
            next_cave = self.choose_cave(self.unvisited)
            self.create_tunnel(this_cave,next_cave)
            self.visit_cave(next_cave)
    def create_tunnel(self,cave_from,cave_to):
        self.caves[cave_from].append(cave_to)
        self.caves[cave_to].append(cave_from)
    
    def visit_cave(self,cave_number):
        self.visited.append(cave_number)
        self.unvisited.remove(cave_number)
    
    def choose_cave(self,cave_list):
        cave_number = choice(cave_list)
        while len(self.caves[cave_number]) >= 3:
            cave_number = choice(cave_list)
        return cave_number
    
    def print_caves(self):
        for number in self.cave_list:
            print number,':',self.caves[number]

if __name__ == '__main__':
    ccaves=Caves(20)
    ccaves.print_caves()













