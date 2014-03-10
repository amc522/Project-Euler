import timeit
import math
import sys
import operator

def findPythagTriplet(num):
  a = int(math.floor(math.sqrt(num)))
  b = num
  numDiv2 = num / 2
  
  while a < b:
    # a + b + c = num
    # a^2 + b^2 = c^2
    # a^2 + b^2 = (-a - b + num)^2
    # 2ab - (2*num)a - (2*num)b + num^2 = 0
    # I used wolframalpha to get everything in terms of b because im lazy :)
    # b = (num * (a - num / 2)) / (a - num)
    numerator = num * (a - numDiv2)
    denom = a - num

    if numerator % denom != 0:
      a += 1
      continue

    b = numerator / denom
    c = num - a - b

    if b < c and a < b and (a + b + c) == num and ((a**2) + (b**2)) == c**2:
      return (a,b,c)

    a += 1
  return (0,0,0)

tripletSum = 1000

if len(sys.argv) > 1:
  tripletSum = int(sys.argv[1])

triplet = findPythagTriplet(tripletSum)
print "Answer is", triplet
print "Product is", reduce(operator.mul, triplet)

runs = 1000
runtime = timeit.Timer(stmt = "findPythagTriplet({0})".format(tripletSum), setup="from __main__ import findPythagTriplet").timeit(runs)
print "Running time is {0} ({1} avg) secs".format(runtime, (runtime / runs))
