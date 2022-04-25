#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
import json
import time

class Rover:
    
    def __init__(self, rover_number):
        self.location = [0, 0] #current location of rover represented by [x,y]
        self.rover_number = rover_number #rover number
        self.direction = 'S' #current direction of rover
        self.rover_moves = self.get_rover_moves() #stores string of rover moves
        self.board_list = self.create_board() #creates base list of lists and populates to represent the board
        self.start_rover()
        
    #retrieve rover instructions from public api    
    def get_rover_moves(self):
        self.response_api = requests.get('https://coe892.reev.dev/lab1/rover/{rover_number}'.format(rover_number = self.rover_number))
        self.data = self.response_api.text
        self.parse_json = json.loads(self.data)
        self.store_moves = self.parse_json["data"]["moves"]
        return self.store_moves

    #create list of lists which will form our "board" or "map" which the rover will traverse
    #the board is preset to 15x15
    def create_board(self):
        self.board_list = []
        for i in range(15):
            self.board_list.append(['0']*15)
        self.board_list[0][0] = '*' #starting point
        return self.board_list

    #writes the final file outputting the results
    def write_file(self):
        with open('path_{}.txt'.format(self.rover_number), 'w') as f:
            for i in self.board_list:
                for j in i:
                    f.write(j)
                f.write('\n')
    
    #facilitates the "M" moving of the rover and updates the board_list 
    #if attempting moving through boundary, nothing will happen
    def set_location(self):
        if (self.direction == 'N' and self.location[1] > 0):
            self.location[1] -= 1
            self.board_list[self.location[1]][self.location[0]] = '*'
        if (self.direction == 'E' and self.location[0] < 15):
            self.location[0] += 1
            self.board_list[self.location[1]][self.location[0]] = '*'
        if (self.direction == 'S' and self.location[1] < 15):
            self.location[1] += 1
            self.board_list[self.location[1]][self.location[0]] = '*'
        if (self.direction == 'W' and self.location[0] > 0):
            self.location[0] -= 1
            self.board_list[self.location[1]][self.location[0]] = '*'
            
    #gets current location of rover       
    def get_location(self):
        return self.location
    
    #sets the direction of the rover depending on the instructions
    #if instruction is "M" or "D", the relavent function will be called
    def set_direction(self, instruction):
        
        #Move
        if(instruction == 'M'):
            self.set_location()
            return
            
        #Dig    
        if(instruction == 'D'):
            return
        
        #The following conditional statements determine current direction the rover is facing, then determines the direction the
        #rover is facing post-rotation left/right
        #Can be coded more efficiently/cleanly but serves its purpose for now*
        
        #North
        if(self.direction == 'N' and instruction == 'R'):
            self.direction = 'E'
            return
        if(self.direction == 'N' and instruction == 'L'):
            self.direction = 'W'
            return
    
        #East
        if(self.direction == 'E' and instruction == 'R'):
            self.direction = 'S'
            return
        if(self.direction == 'E' and instruction == 'L'):
            self.direction = 'N'
            return
            
        #South
        if(self.direction == 'S' and instruction == 'R'):
            self.direction = 'W'
            return
        if(self.direction == 'S' and instruction == 'L'):
            self.direction = 'E'
            return
        
        #West
        if(self.direction == 'W' and instruction == 'R'):
            self.direction = 'N'
            return
        if(self.direction == 'W' and instruction == 'L'):
            self.direction = 'S'
            return
    
    #gets current direction rover is facing
    def get_direction(self):
        return self.direction

    def start_rover(self):
        for i in self.rover_moves:
            self.set_direction(i)
        self.write_file()
        
        
#main function

def main():
    start = time.time()
    for i in range(1,11):
        Rover(i)
    end = time.time()
    print("The computation time was: ", (end-start), "seconds")
    
main()




#*********************************
#INITIAL DEBUG SETUP
#
# rover1.create_board()
# x = rover1.get_rover_moves()

# for i in x:
#     print("Instruction:", i)
#     print("Current Location: ", rover1.get_location())
#     print("Current Direction: ", rover1.get_direction())
#     rover1.set_direction(i)
#     print("New Direction: ", rover1.get_direction())
#     print("New Location: ", rover1.get_location())
#     print("\n")
# rover1.write_file()
#**************************************


# In[ ]:





# In[ ]:




