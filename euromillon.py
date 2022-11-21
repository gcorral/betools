#!/usr/bin/env python3

import sys, getopt
import random

def main(argv):
    
    bets = 1
    try:
      opts, args = getopt.getopt(argv,"hb:",["bets="])
    except getopt.GetoptError:
      print ('euromillon.py -b <NumberOfBets>')
      sys.exit(2)
      
    for opt, arg in opts:
      if opt == '-h':
         print ('euromillon.py -b <NumberOfBets>')
         sys.exit()
      elif opt in ("-b", "--bets"):
         bets = int(arg)  
    
    random.seed()
    
    for bet in range(bets):
    
        print("Apuesta {}:".format(  str(bet+1) )) 
    
        numbers = []
        for n in range(5):
            new = random.randrange(1, 51)
            while new in numbers:
              new = random.randrange(1, 51)
            numbers.append( new )
        
        numbers.sort()
        
        print("Números: {}".format( numbers ) )
    
        stars = []
        for s in range(2):
            new = random.randrange(1, 13)
            while new in stars:
              new = random.randrange(1, 13)
            stars.append( new )
    
        stars.sort()
        print("Estrellas: {}".format( stars ) )
        print("")        


if __name__ == "__main__":
   main(sys.argv[1:])