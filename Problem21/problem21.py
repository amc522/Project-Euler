# Theory:
# Every divisor of a number can be represented by
# its prime factors. Each divisor of n has its own
# set of prime factors, and that set of prime
# factors is a subset of n's prime factors. By multiplying
# every combination of primes factors and adding them,
# you can find the sum of the divisors
#
# Ex:
# Lets use 12 as an example. Its divisors are:
# 	1, 2, 3, 4, 6
# The sum of those divisors is 16.
# Now if we break those divisors into their primes
# we get the following (excluding 1):
# 2 = 2^1
# 3 = 3^1
# 4 = 2^2
# 6 = 2^1 * 3^1
#
# If you find all the prime factors of 12 you get
# three 2's and two 3's, the same number of prime
# factors of all the divisors.
# Instead of multiplying all combinations of prime
# factors to get the divisors and summing them, you
# can use the form:
# 	(2^0 + 2^1 + 2^2)(3^0 + 3^1) - 12 = 16 
# To get that form lets look at the divisors like this:
# 1  = 2^0 * 2^0 * 3^0
# 2  = 2^1 * 2^0 * 3^0
# 3  = 2^0 * 2^0 * 3^1
# 4  = 2^1 * 2^1 * 3^0
# 6  = 2^0 * 2^1 * 3^1
# 12 = 2^1 * 2^1 * 3^1
#
# (2^0 * 2^0 * 3^0) + (2^1 * 2^0 * 3^0) + (2^0 * 2^0 * 3^1) + (2^1 * 2^1 * 3^0) + (2^0 * 2^1 * 3^1) + (2^1 * 2^1 * 3^1) - 12 = 
# 2^0(3^0) + 2^1(3^0) + 2^0(3^1) + 2^2(3^0) + 2^2(3^1) + 2^1(3^1) + 2^2(3^1) - 12 = 
# (2^0 + 2^1 + 2^2)(3^0 * 3^1) - 12 =
# (2^3 - 1)((3^2 - 1) / 2) - 12 = 16
#
# Which can be expressed in the general form as:
# pf = a list of prime factors
# p = the current prime
# n = the number of times the current prime is a factor of the number
# product for each pf ( (p^(n + 1) - 1) / (n - 1) )

import math
import timeit
import sys

# reduces 'num' by 'factor' until 'num'
# is no longer divisible by 'factor'
# returns the result of 'num' being divided
# and the amount of times 'num' was divisible
# by 'factor'
def reduceFactor(num, factor):
	if not num % factor == 0:
		return (num, 0)

	currentBound = num
	count = 0

	while currentBound % factor == 0:
		currentBound /= factor
		count += 1

	return (currentBound, count)

# This find divisor sum function is based
# on the and optimized prime factorization
# function. The optimization is based on 
# finding primes greater than five that arent
# already divisible by 2 or 3
def findDivisorSum(num):
	divisorSum = 1
	currentBound = num;

	result = reduceFactor(currentBound, 2)
	currentBound = result[0]
	divisorSum *= (2 ** (result[1] + 1) - 1)

	result = reduceFactor(currentBound, 3)
	currentBound = result[0]
	divisorSum *= (3 ** (result[1] + 1) - 1) / 2

	i = 5

	currentBoundSqrt = math.sqrt(currentBound)

	while currentBoundSqrt >= i:
		result = reduceFactor(currentBound, i)
		currentBound = result[0]
		if result[1] > 0:
			currentBoundSqrt = math.sqrt(currentBound)
		divisorSum *= (i ** (result[1] + 1) - 1) / (i - 1)

		i += 2
		result = reduceFactor(currentBound, i)
		currentBound = result[0]
		if result[1] > 0:
			currentBoundSqrt = math.sqrt(currentBound)
		divisorSum *= (i ** (result[1] + 1) - 1) / (i - 1)

		i += 4

	if divisorSum < num:
		# if we got here, the final divisor is a prime and needs
		# to be accounted for
		divisorSum *= (currentBound ** 2 - 1) / (currentBound - 1)
	
	return divisorSum - num

def amicableSum(upperBound):
	# keep a dictionary of already found sums so we arent
	# recomputing the same sum over and over
	sumDict = {}
	amicableList = []
	counter = 0

	i = 3

	while i < upperBound:
		counter += 1
		divisorSum = None

		if i in sumDict:
			divisorSum = sumDict[i]
		else:
			divisorSum = findDivisorSum(i)
			sumDict[i] = divisorSum

		if divisorSum <= i:
			# if the sum of the divisors is less than i
			# we know we can continue on because if it was
			# an amicable pair, we would already have
			# checked it
			i += 1
			continue

		amicableSum = None
		if divisorSum in sumDict:
			amicableSum = sumDict[divisorSum]
		else:
			amicableSum = findDivisorSum(divisorSum)
			sumDict[divisorSum] = amicableSum

		if amicableSum == i:
			amicableList.append(i)
			amicableList.append(divisorSum)
			i = divisorSum

			# can skip all numbers inbetween this amicable
			# pair. I dont have actual proof for why, but
			# it was an observation i made

		i += 1

	return sum(amicableList)

def findDivisorSumNaive(num):
	numSqrt = int(math.ceil(math.sqrt(num)))
	divisors = [1]

	start = numSqrt

	if numSqrt ** 2 == num:
		divisors.append(numSqrt)

	start = numSqrt - 1

	for i in range(start, 1, -1):
		if num % i != 0:
			continue

		divisors.append(i)
		divisors.append(num / i)

	return sum(divisors)

def amicableSumNaive(upperBound):
	sumDict = {}
	amicableList = []

	counter = 0

	i = 3
	while i < upperBound:
		counter += 1
		divisorSum = None

		if i in sumDict:
			divisorSum = sumDict[i]
		else:
			divisorSum = findDivisorSumNaive(i)
			sumDict[i] = divisorSum

		if divisorSum <= i:
			i += 1
			continue

		amicableSum = None
		if divisorSum in sumDict:
			amicableSum = sumDict[divisorSum]
		else:
			amicableSum = findDivisorSumNaive(divisorSum)
			sumDict[divisorSum] = amicableSum

		if amicableSum == i:
			amicableList.append(i)
			amicableList.append(divisorSum)
			i = divisorSum

		i += 1

	return sum(amicableList)

num = 10000

if len(sys.argv) > 1:
	num = int(sys.argv[1])

#feces = 0
#for i in range(3, 10000):
#	primeSum = timeit.Timer(stmt = "findDivisorSum({0})".format(i), setup="from __main__ import findDivisorSum").timeit(10)
#	naiveSum = timeit.Timer(stmt = "findDivisorSumNaive({0})".format(i), setup="from __main__ import findDivisorSumNaive").timeit(10)
#
#	if primeSum < naiveSum:
#		feces += 1
#	else:
#		print "{0}\t{1}\t{2}".format(i, primeSum, naiveSum)
#print "PrimeSum was better", feces, "times"

#runs = 2
#
#runtime = timeit.Timer(stmt = "findDivisorSum({0})".format(num), setup="from __main__ import findDivisorSum").timeit(runs)
#print "Running time is {0} ({1} avg) secs [{2} runs]".format(runtime, (runtime / runs), runs)
#
#runtime = timeit.Timer(stmt = "findDivisorSumNaive({0}, {1})".format(num, {}), setup="from __main__ import findDivisorSumNaive").timeit(runs)
#print "Running time is {0} ({1} avg) secs [{2} runs]".format(runtime, (runtime / runs), runs)


print amicableSum(num)
print amicableSumNaive(num)

runs = 100

runtime = timeit.Timer(stmt = "amicableSum({0})".format(num), setup="from __main__ import amicableSum").timeit(runs)
print "Running time is {0} ({1} avg) secs [{2} runs]".format(runtime, (runtime / runs), runs)

runtime = timeit.Timer(stmt = "amicableSumNaive({0})".format(num), setup="from __main__ import amicableSumNaive").timeit(runs)
print "Running time is {0} ({1} avg) secs [{2} runs]".format(runtime, (runtime / runs), runs)
