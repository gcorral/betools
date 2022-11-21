#!/usr/bin/env python3

import sys, getopt
import random

def main(argv):
    
    bets = ["1", "X", "2"]
    
    #bets = 15
    #try:
    #  opts, args = getopt.getopt(argv,"hb:",["bets="])
    #except getopt.GetoptError:
    #  print ('euromillon.py -b <NumberOfBets>')
    #  sys.exit(2)
      
    #for opt, arg in opts:
    #  if opt == '-h':
    #     print ('euromillon.py -b <NumberOfBets>')
    #     sys.exit()
    #  elif opt in ("-b", "--bets"):
    #     bets = int(arg)  
    
    random.seed()
    
    #for bet in range(bets):
    
    print("Apuestas 15:") 
    
    for n in range(1, 16):
       print("{}. {}".format(n,  bets[random.randrange(3)] ) )
    print("")        


if __name__ == "__main__":
   main(sys.argv[1:])