import math
import timeit
import sys

def reduceFactor(num, factor):
	if not num % factor == 0:
		return (num, 0)

	currentBound = num
	count = 0

	while currentBound % factor == 0:
		currentBound /= factor
		count += 1

	return (currentBound, count)

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
		divisorSum *= (currentBound ** 2 - 1) / (currentBound - 1)
	
	return divisorSum - num

def amicableSum(upperBound):
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
