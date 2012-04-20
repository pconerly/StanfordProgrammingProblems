## test inversions.py

import inversions
import brute
import time

def test_mergsort():
    print "testing inversions.py"
    (c, temp) = inversions.mergesort_splitcount([3,4], [1,2])
    print c
    print temp

def compare_solutions(maxentries, filename):
    ptime = 0
    print "====================="
    ptime -= time.clock()
    mergeResult = inversions.testrun(maxentries, filename)
    ptime += time.clock()
    print mergeResult, "mergesort"
    print "took:", ptime ,"seconds"

    ptime -= time.clock()
    bruteResult = brute.count_inversions(maxentries, filename)
    ptime += time.clock()
    print bruteResult, "brute"
    print "took:", ptime ,"seconds"

    if mergeResult != bruteResult:
        print "ANSWERS NOT EQUAL"
    else:
        print "ANSWERS == equal"

if __name__ == "__main__":
    #compare_solutions(1000000, 'IntegerArray.txt')
    compare_solutions(3, 'IntegerArray.txt')
    compare_solutions(255, 'IntegerArray.txt')
    compare_solutions(3336, 'IntegerArray.txt')
    compare_solutions(10000, 'IntegerArray.txt')
