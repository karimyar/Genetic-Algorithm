import random
from random import randint, choice 

MaxWeight = 10
ObjectList = [[3,5],[4,4],[4,7],[2,5], [10,5], [3,9], [1,3], [2,7], [7,2],[3,2],[6,7],[3,5]]
fitness_list = [] 
size = len(ObjectList)
spawn = size*4
chromo_list = []
start = True

def fitness(chromo):
   weight = 0
   value = 0
   for i in range(size):
      if(chromo[i] == 1):
         weight += ObjectList[i][0]
         value += ObjectList[i][1]
   if weight > MaxWeight:
      value = 0
   return value 
            
def mate(chromo):
   chromo1 = random.choice(chromo_list[0:spawn])
   chromo2 = random.choice(chromo_list[0:spawn])
   while(chromo1 == chromo2):
      chromo2 = random.choice(chromo_list)
   new_chromo = []
   new_chromo1 = []
   random_cross = randint(1,size-1)
   random_choice = randint(1,2)
   r = randint(0,size-1) 
   new_chromo = chromo1[0 : random_cross] + chromo2[random_cross : size]
   new_chromo1 = chromo2[0 : random_cross] + chromo1[random_cross : size]
   if(random_choice == 1):
      if(new_chromo[r] == 1):
         new_chromo[r] = 0
      else:
         new_chromo[r] = 1
   else:
      if(new_chromo1[r] == 1):
         new_chromo1[r] == 0
      else:
         new_chromo[r] = 1
   fitness_list.append(fitness(new_chromo))
   fitness_list.append(fitness(new_chromo1)) 
   chromo_list.append(new_chromo)
   chromo_list.append(new_chromo1)
            
def create_chromosomes():
   global start 
   if(start == True):
      for i in range(spawn):
         random_chromo = [randint(0,1) for i in range(size)]
         fitness_list.append(fitness(random_chromo))
         chromo_list.append(random_chromo)
      start = False 
   mate(chromo_list)
   return chromo_list


   
def main():
   print("Executing....\n")
   create = create_chromosomes();
   max_value = [] 


   for i in range(100000):
      new = [create for fitness_list, create in sorted(zip(fitness_list, create), key = lambda pair: pair[0])]
      fitness_list.sort()
      del fitness_list[0:2]
      del new[0:2]
      max_value.append(fitness_list[spawn-1])
      mate(new)

   print("Final optimal value: " ,fitness_list[spawn-1])
   print("Average optimal value through" , i+1 , " iterations: ", sum(max_value)/len(max_value))
   

   
if __name__ == '__main__':
   main()
     
