import timeit

# classic recursive solution
def fibRecursive(n):
	if n == 1 or n == 2:
		return 1

	return fibRecursive(n - 1) + fibRecursive(n - 2)

# recursive solution that keeps track
# of already calculated solutions
def fibRecursiveMemo_(n, memo):
	if n in memo:
		return memo[n]

	result = 1
	if n > 2:
		result = fibRecursiveMemo_(n - 1, memo) + fibRecursiveMemo_(n - 2, memo)

	memo[n] = result

	return result

# wrapper to call fibRecursiveMemo_
def fibRecursiveMemo(n):
	memo = {}

	return fibRecursiveMemo_(n, memo)

# straight forward iterative solution
def fibIterative(n):
	previous = 1
	current = 1
	
	for i in range(n - 2):
		newPrevious = current
		current += previous
		previous = newPrevious

	return current

runs = 10

for term in range(1, 35, 3):
	print "Term", term
	print "----------"

	print "fibRecursive({0}) = {1}".format(term, fibRecursive(term))
	runtime = timeit.Timer(stmt = "fibRecursive({0})".format(term), setup="from __main__ import fibRecursive").timeit(runs)
	print "Running time is {0} ({1} avg) secs [{2} runs]\n".format(runtime, (runtime / runs), runs)

	print "fibRecursiveMemo({0}) = {1}".format(term, fibRecursiveMemo(term))
	runtime = timeit.Timer(stmt = "fibRecursiveMemo({0})".format(term), setup="from __main__ import fibRecursiveMemo").timeit(runs)
	print "Running time is {0} ({1} avg) secs [{2} runs]\n".format(runtime, (runtime / runs), runs)

	print "fibIterative({0}) = {1}".format(term, fibIterative(term))
	runtime = timeit.Timer(stmt = "fibIterative({0})".format(term), setup="from __main__ import fibIterative").timeit(runs)
	print "Running time is {0} ({1} avg) secs [{2} runs]\n\n".format(runtime, (runtime / runs), runs)