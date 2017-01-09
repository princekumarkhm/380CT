from random import randint, sample
from itertools import chain, combinations
import numpy as np
import time
import warnings
warnings.filterwarnings("ignore")



class SSP():
    """Create subset s= set t= target n= lenght of set
    """
    def __init__(self, S=[], t=0):
        self.S = S
        self.t = t
        self.n = len(S)
        #
        self.decision = False
        self.total = 0
        self.selected = []


    """print subset and target
    """
    def __repr__(self):
        return "SSP instance: S="+str(self.S)+"\tt="+str(self.t)

    """Create random subset
    n is passed in from user
    bitlength is set at 10 to limit size of numbers in subset

    max bit numner is calulated using formula 2**bitlength-1
    S array is created using a random generator between 0 and size of max bit lenth
        they are then sorted by smallest to largest
    T (target) is created by getting the sum from random sample of numbers in array S
    N is the amount of integers in subset S
    """
    def random_yes_instance(self, n, bitlength=5):
        max_n_bit_number = 2**bitlength-1
        self.S = sorted( [ randint(0,max_n_bit_number) for i in range(n) ] , reverse=True)
        self.t = sum( sample(self.S, randint(0,n)) )
        self.n = len( self.S )

    def try_at_random(self):
        candidate = []
        total = 0
        while total != self.t:
            candidate = sample(self.S, randint(0,self.n))
            total     = sum(candidate)
            print( "Trying: ", candidate, ", sum:", total )

   def powerset(self):
        candidate = []
        count = 0
        s = [[]]
        while count != self.n:
            for candidate in combinations(self.S, (count+1)):
                    s.append(candidate)
            count += 1
        return s
            
            
    def bruteforce(self):
        total = 0
        s = self.powerset()

        start = time.time()
        for list in s:
                total = sum(list)
                if total == self.t:
                    self.decision = True
                    end = time.time()
                    num = '{0:.10f}'.format(end-start)
                    return num
           

    def dynamic(self):
        subset = np.full((self.t+1,self.n+1),0)
        results = []
 
        for i in range(0, (self.n+1)):
            subset[0][i] = True

        for i in range(1, (self.t+1)):
            subset[i][0] = False

        start = time.time()
        for i in range(1, (self.t+1)):
            for j in range(1, (self.n + 1)):
                subset[i][j] = subset[i][j-1]
                if (i >= self.S[j-1]):
                    subset[i][j] = subset[i][j] or subset[i - self.S[j-1]][j-1]
        end = time.time()
        num = '{0:.10f}'.format(end-start)

        return num

    def greedy(self):
        total = 0
        subsets = []
        start = time.time()
        for i in range(0, len(self.S)):
            if (sum(subsets) + self.S[i]<= self.t):
                subsets.append(self.S[i])
                total = total + self.S[i]
            else:
                break
        end = time.time()
        num = '{0:.10f}'.format(end-start)
        return num

for i in range(1, 20):
    total = 0.0
    for j in range(0, 10000):
        instance = SSP()
        #print( instance )
        instance.random_yes_instance(i)
        total = total + float(instance.greedy())
    avg = total/100
    print(avg)  
#print("subset found: ", found)
