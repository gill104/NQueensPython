import random
import genotypeClass

class Parent:#---------------------------------------------------------------this class is to [MAKE THE CHILDREN] simple
    def __init__(self,genoA,genoB):#----------------------------constructor that takes in two [GENOTYPES/PARENTS]
        self.parent1 = genoA
        self.parent2 = genoB
    
        
    def makeChildren(self,population):#---------------------------get points in which to [CROSSOVER] the parents and make the [CHILDREN]
        self.crossPointA = random.randint(1,len(self.parent1.getGene()) - 1)#-------------random value between [GENE] length
        self.crossPointB = random.randint(1,len(self.parent2.getGene()) - 1)
        
        #--------------------------------------------------------------------------------[CHILDREN] list to keep the [GENE] in record
        self.child1 = []
        self.child2 = []

        self.p1gene = self.parent1.getGene()#-------------------[PARENT] gene list
        self.p2gene = self.parent2.getGene()#------------------[PARENT] gene list
        
      

        for x in range(len(self.p1gene)):#-----------------------------loopand save till [CROSSPOINT] is reached [CHILD ONE]
            if(self.p1gene[x] == self.crossPointA):
                self.child1.append(self.p1gene[x])
                break;
            else:
                self.child1.append(self.p1gene[x])
        
        
        for x in range(len(self.p2gene)):#--------------------------loop and save till [CROSSPOINT[ is reached [CHILD TWO]
            if(self.p2gene[x] == self.crossPointB):
                self.child2.append(self.p2gene[x])
                break;
            else:
                self.child2.append(self.p2gene[x])

        for x in range(len(self.p2gene)):#---------------------------get [PARENT TWO] gene and place all values that are not in [CHILD ONE]
            if(self.p2gene[x] not in self.child1):
                self.child1.append(self.p2gene[x])

        for x in range(len(self.p1gene)):#---------------------------get [PARENT ONE] gene and place all values that are not in [CHILD TWO]
            if(self.p1gene[x] not in self.child2):
                self.child2.append(self.p1gene[x])

############check for mutation#########################
                
        ch1 = genotypeClass.Genotype(self.child1)#-----------make a [GENOTYPE] for the new [CHILD ONE]
        ch2 = genotypeClass.Genotype(self.child2)#-----------make a [GENOTYPE] for the new [CHILD TWO]
                
        ch1.mutate()#----------------------------------------------------------check if they will [MUTATE]
        ch2.mutate()

##################################################
        population.append(ch1)#----------------------------------------add the the [POPULATION]
        population.append(ch2)
        return population
