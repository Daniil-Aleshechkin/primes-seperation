#Daniil Alesheckin
#CS 20
#Primes
#11/22/17

import time
import math

primes = [2]
sexyPrimes = []
primeAmount = 0
highestN = 0

pAmount = (int(input("What is the prime range?")))
seperationAmount = int(input("How much do you want the seperation amount?(Note that all primes are seperated by an even amount (appart from 2 and 3))"))
pLength = int(input("How long do you want the minimal lenght to be"))

print("Finding primes...")

print(2)

for n in range(3,pAmount+1):
  #Check for divisible in each prime
  for p in primes:
    if math.sqrt(n) > p:
     if n%p==0:
      break
    else:
      primes.append(n)
      print(n)
      break

primeAmount = len(primes)

print("Finding the primes seperated by {}".format(seperationAmount))

for p in primes:
  worthContinue = True
  n = 0
  print()
  sexyPrime = []
  
  print("Checking {}".format(p))
  
  sexyPrime.append(p)
  isSexyPrime = False
  pPos = primes.index(p)
  
  while worthContinue == True:
    n += 1
    #print("round {}".format(n))
    for pos in range (1,seperationAmount//2+1):
      if pPos+pos < primeAmount:
        prime = primes[pPos+pos]
        #print("are {} and {} {} primes".format(p,prime,seperationAmount))
        if p+seperationAmount*n == prime:
          sexyPrime.append(prime)
          del primes[pPos+pos]
          primeAmount -= 1
          worthContinue = True
          #print("Found one {}".format(prime))
          #print(
          pPos += pos-1
          break
        else:
          #print("no prime found")
          worthContinue = False
      else:
        #print("out of primes")
        worthContinue = False
        break
  
  if n>pLength-1:
    sexyPrimes.append(sexyPrime)
  if n>highestN-1:
    highestN = n
    highestList = sexyPrime
  
print("Look at them...")
for prime in sexyPrimes:
  time.sleep(0.1)
  print(prime)
print("The highest pair was a {} pair".format(highestN))
print("The smallest {} pair was : {}".format(highestN,highestList))
input()