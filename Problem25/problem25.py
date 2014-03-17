import timeit
import sys

def fibOfDigits(digits):
	previous = 1
	current = 1
	count = 2

	minLimit = 10 ** (digits - 1)

	while current < minLimit:
		newPrevious = current
		current += previous
		previous = newPrevious
		count += 1

	return (count, current) 

digits = 1000

if len(sys.argv) > 1:
	digits = int(sys.argv[1])

print "Answer is", fibOfDigits(digits)

runs = 10
runtime = timeit.Timer(stmt = "fibOfDigits({0})".format(digits), setup="from __main__ import fibOfDigits").timeit(runs)
print "Running time is {0} ({1} avg) secs [{2} runs]".format(runtime, (runtime / runs), runs)