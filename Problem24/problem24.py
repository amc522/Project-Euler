# To find the nth lexicographic permutation, I looked
# at one digit at a time. Each digit is based on the number
# of permutations that the following digits can make.
# For example lets look at the permutations for 0, 1, 2:
#
# To find the first digit in the permutation for the nth
# term we have to look at how it compares as a multiple of
# the number of permutations the last two digits can be in.
# 2! is the number of permutations for the last two digits.
# So for permutation 1 & 2, the first digit is 0. For 2 &3
# the first digit is 1, etc. Then when looking at the next
# digit, you find the remainder of the first digit times the
# number of permutations that can follow it. Do this for
# every digit of the permutation.

import math
import sys

def findNthLexTerm(term, digitList):
  if term > math.factorial(len(digitList)):
    return []

  numDigits = len(digitList)
  permutation = []
  availableList = list(digitList)

  term -= 1

  for i in range(numDigits - 1):
    fact = math.factorial(numDigits - i - 1)
    index = term / fact

    term -= fact * index

    num = availableList.pop(index)
    permutation.append(num)

  permutation.append(availableList.pop())

  return permutation

term = 1000000

if len(sys.argv) > 1:
  term = int(sys.argv[1])

print "The lexicographic permutation", term, "is", findNthLexTerm(term, range(10))
