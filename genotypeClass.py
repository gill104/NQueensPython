from random import shuffle
import random

class Genotype:
    def __init__(self,gene = None):#--------------------------------------a constructor that can take 2 types (with and without GENE passed)
        self.map_row = 8
        self.map_col = 8
        self.fitness = 0.0
        self.map = [['[_]' for x in range(8)] for y in range(8)]#--creates a board for the queens
        
        if gene is None:
            self.gene = []
            for i in range(8):#--------------------------------------------------------makes a random string for the gene
                self.gene.append(i)
            shuffle(self.gene)#-----------------------------------------------------Shuffles the gene
        else:
            self.gene = gene
        self.checkFitness(self.gene)#--------------------------------------Checks the fitness by the # of collisions and sets the [fitness] value
            
            
    def __lt__(self, other):#---------------------------------------------------Helps use the [SORT] function to be able to sort the objects in main by fitness
        return self.fitness > other.fitness
    
    def checkFitness(self,gene):#------------------------------------------Checks the fitness the gene 
        self.resetMap()#----------------------------------------------------------Precaution map reset to blank state [not sure if i need]
        for x in range(len(self.gene)):#----------------------------puts the values from [GENE] onto the [MAP]
            y = self.gene[x]
            self.putInMap(x,y)
        for x in range(len(self.gene)):#-----------------------------------Checking for the number of [COLLISIONS] that are on the map
            for y in range(len(self.gene)):
                if(self.map[x][y] == '[&]'):
                    self.fitness += self.checkNE(x-1, y+1)
                    self.fitness += self.checkSE(x+1, y+1)
                    self.fitness += self.checkNW(x-1, y-1)
                    self.fitness += self.checkSW(x+1, y-1)
                    
        self.fitness = (1/self.fitness + 0.001)#------------------------Fitness function [FITNESS VALUE]
        
        return (1/(self.fitness + 0.001))
    
    def mutate(self):#---------------------------------------------------------Checks whether there is a chance to mutate the gene [SWAPS] two values
        mutateVal = random.randint(0,100)
        ind1 = random.randint(0,7)
        ind2 = random.randint(0,7)
        if(mutateVal < 10):
            temp = self.gene[ind1]
            
            self.gene[ind1] = self.gene[ind2]
            self.gene[ind2] = temp
            
            self.checkFitness(self.gene)#-----------------------------If mutated it [SWAPS] values and checks fitness again
    #   (+,-)   N   (+ +)
    #       W           E
    #   (-,-)     S    (-,+)
    #
    #--------------------------------------------------------------------------------These are straight forward they check the [DIAGONALS] for each queen
    def checkNE(self,xPassed, yPassed):#-1 +1
        x = xPassed
        y = yPassed
        while(x < 8 and y < 8):
            if(self.map[x][y] == '[&]'):
                return 1
            x -= 1
            y += 1
        return 0
    def checkSE(self,xPassed, yPassed):#+1+1
        x = xPassed
        y = yPassed
        while(x < 8 and y < 8):
            if(self.map[x][y] == '[&]'):
                return 1
            x += 1
            y += 1
        return 0
    def checkSW(self,xPassed, yPassed):# +1 -1
        x = xPassed
        y = yPassed
        while(x < 8 and y > -1):
            if(self.map[x][y] == '[&]'):
                return 1
            x += 1
            y -= 1
        return 0
    def checkNW(self,xPassed, yPassed):#-1 -1
        x = xPassed
        y = yPassed
        while(x >= 0 and y >= 0):
            if(self.map[x][y] == '[&]'):
                return 1
            x -= 1
            y -= 1
        return 0
    
    def putInMap(self,x,y):#------------------------------------------Places the [QUEEN] in its proper spot in the [MAP]
        self.map[x][y] = '[&]'
        
    def resetMap(self):#-----------------------------------------------Fresh map [RESET]
        self.map = [['[_]'for x in range(self.map_row)] for y in range(self.map_col)]
                
    def getSize(self):#---------------------------------------------------Returns the length of the gene
        return len(self.gene)
    
    def getGene(self):#-----------------------------------------------Returns the [GENE] list
        return self.gene
        
    def getFitness(self):#---------------------------------------------returns the [GENE] [FITNESS]
        return self.fitness
    
    def display(self):#-------------------------------------------------Allows for easy [DEBUGGING] displays [MAP]
        for x in range(len(self.gene)):
            for y in range(len(self.gene)):
                print(self.map[x][y], end='')
            print()
        
