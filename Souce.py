#[MAIN comments are with '--------------' others were for debugging purposes ]
import genotypeClass
import parentClass
import random
import operator
import tkinter

def main():
    gen = 0#-----------------------------------------------------------------------------------------------[GENERATION] counter
    population = []#-----------------------------------------------------------------------------------genotypes which together they make a [POPULATION]
    
    
    #setting up the popultion of 100 randomly made genomes
    for x in range(100):#----------------------------------------------------------------------------creates 100 [GENES] with the [GENOTYPE CONSTRUCTOR]
        population.append(genotypeClass.Genotype())
    
    while(gen < 1000):#-----------------------------------------------------------------------------loops 1000 [GENERATIONS] should be enough to get a result
        print('\n\nGEN: ', gen)
########################################################
    #we need to make a mating pool and select the parents
        matingPool = []#--------------------------------------------------------------------------------list to store the [CHOSEN] parents for [MATING]
        population, matingPool = parentSelection(population, matingPool)#---[SELECT] parents from [POPULATION]
        
#########################################################
    #make the children from the matingPool, use ParentClass
        allParents = pairParents(matingPool)#------------------------------------------------get all [PARENTS] and [PAIR] them together to make [CHILDREN]
        for x in range(len(allParents)):
            population = allParents[x].makeChildren(population)#--------------------make [CHILDREN] and add to the population
        population.sort()#--------------------------------------------------------------------------------[SORT] the [POPULATION] based on the[FITNESS]
        
#########################################################
    #survivorSelection
        survivorSelection(gen,population)#-------------------------------------------------checks to see if the [MOST FIT] gene the correct setup -> [FITNESS == 1.000]
        gen += 1
    print(population[0].getFitness())
#########################################################

def parentSelection(population, matingPool):#-------------------------------------[PARENT] selection, gets 10% of the population at random to be the parents
    tenPercent = len(population) * .10
    chosenParents = 0#-----------------------------------------------------------------------------keeps track of the total amount of [PARENTS]
    k = 0#---------------------------------------------------------------------------------------------------[FORGOT] what this is for, maybe [DONT USE]
    while(chosenParents < tenPercent):#--------------------------------------------------loop till [10%] is met
        best = 0#------------------------------------------------------------------------------------------holds the [BEST] fitness of the three chosen from the [GENES]
        threeChosen = []#----------------------------------------------------------------------------holds the three [RANDOM] [GENES]
        for x in range(3):#-----------------------------------------------------------------------------picks 3 [GENES] at [RANDOM] and adds the threeChosen[]
            randValue = random.randint(0,len(population)-1)
            threeChosen.append(population[randValue])

            if(best < threeChosen[x].getFitness()):#-------------------------------------finds the [BEST] of the threechosen[]
                best = threeChosen[x].getFitness()
            
        for x in range(3):#----------------------------------------------------------------------------looks at threeChosen for [BEST] fitness to [DELETE] from [POPULATION]
            if(threeChosen[x].getFitness() == best):#------------------------------------looks at threeChosen for [BEST] fitness to [DELETE] from [POPULATION]
                matingPool.append(threeChosen[x])#--------------------------------------adds the the [MATINGPOOL]
                if(threeChosen[x] in population):#--------------------------------------------checks to [DELETE] from [POPULATION], the [GENE] that was added to [MATINGPOOL]
                    for i in range(len(population)):
                        if(threeChosen[x] == population[i]):
                            del population[i]
                            break
                break
        temp = len(matingPool)-1#------------------------------------------------------------[FORGOT] what it is for maybe [DONT USE]
        k += 1#--------------------------------------------------------------------------------------------[SAME]
        chosenParents += 1
    return (population, matingPool)
############################################################
def pairParents(matingPool):#-------------------------------------------------------------pairing [PARENTS] to prep. to make [CHILDREN]
    parent = []
    for x in range(0, len(matingPool)-1, 2):
        parent.append(parentClass.Parent(matingPool[x], matingPool[x+1]))
        
    return parent
############################################################
def survivorSelection(gen,population):#-------------------------------------------------checks to see if [SOLUTION] was [FOUND]
    if(population[0].getFitness() >= 1.000):
        print(gen)
        print('We found a generation!!!!')
        print(population[0].getGene())
        print(population[0].getFitness())
        population[0].display()
        
        guiDisplay(population[0].getGene())#-----------------------------------------------[GUI] representation
############################################################
def guiDisplay(gene):
    top = tkinter.Tk()#---------------------------------------------------------------------------------makes window [DONT REMEMBER]
    photo = tkinter.PhotoImage(file="queen.png")#----------------------------------get the image
    queen_position = gene#------------------------------------------------------------------------[SOLUTION] [GENE]
    for r in range(8):#-----------------------------------------------------------------------------------regular nested loop to place the [BUTTONS] [LOOKS NICE]
        for c in range(8):
            if(c==  queen_position[r]):#------------------------------------------------------------places [QUEEN] image on [BUTTON]
                b = tkinter.Button(top,image=photo, text  = ('(' + str(r) +',' + str(c)+ ')'))
                b.grid(row = r, column=c)
            else:#------------------------------------------------------------------------------------------------otherwise uses [COORDINATES]
                b = tkinter.Label(top,text  = ('(' + str(r) +',' +str(c)+ ')'),padx=10,pady=18, relief="ridge")
                b.grid(row = r, column=c)
    top.mainloop()#-------------------------------------------------------------------------------------loops the window to show [GOOGLE IT]
    exit()

    
main()
