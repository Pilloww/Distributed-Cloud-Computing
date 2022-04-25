#!/usr/bin/env python
# coding: utf-8

# In[128]:


import time
import hashlib


#"mines.txt" file is a simple text file contain 5 mines represented in 5 lines
#in each line, the mine number is represented first following by the serial number of the mine
#the mine number is seperated from the serial number by a space " " 
#For Example: 3 452
#where "3" is the mine number and "452" is the corresponding serial number

class Dig():
    
    def __init__(self, mine):
        self.mine = mine
        self.mine_serial = 0
        self.pin = 0
        self.key = ''
        self.hash = ''
        self.disarmed_flag = False
        self.get_mine_serial()
        self.start_disarm()
    #opens the mines.txt file and iterates through each line
    #strips each line into 2 elements (determined by a space) in a list: [mine number, serial number]
    #determines the serial of the target mine as determined by self.mine and stores the serial number to self.mine_serial
    def get_mine_serial(self):
        with open("mines.txt", "r") as reading:
            for line in reading:
                strippedline = line.strip()
                temp = strippedline.split(" ")
                if (int(temp[0]) == self.mine):
                    self.mine_serial = temp[1]
                    return
                
    #generates a pin which is just a increment of the previous pin by 1 to simulate "brute force"
    #this is done so that there is consistency between results when comparing sequential to multithreading
    def get_temporary_mine_key(self):
        self.pin += 1
        self.key = str(self.pin) + str(self.mine_serial)
    #generates the hash 
    def sha256_hash(self):    
        self.hash = hashlib.sha256(self.key.encode()).hexdigest()
    
    #determines if the pin was valid and updates disarm flag if it is valid
    def isValid(self):
        if(self.hash[0] == '0'):
            self.disarmed_flag = True
    
    #starts and runs the methods till a valid key is found and the mine is disarmed
    #loops the 3 steps described in the lab manual until the self.disarmed_flag = True which is only occurs when a key with 
    #a starting value of '0'
    def start_disarm(self):
        while(self.disarmed_flag != True):
            self.get_temporary_mine_key()
            self.sha256_hash()
            self.isValid()

def main():
    start = time.time()
    for i in range(1,6):
        Dig(i)
    end = time.time()
    print("The computation time was: ", end-start, "seconds")

main()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




