# test.py

import quicksort_partition
import brutesort

filename = "QuickSort.txt"

maxnum = 6

brute = brutesort.brutesort(filename, maxnum)
(quick, counter) = quicksort_partition.quicksortprep(filename, maxnum)

print counter

if brute == quick:
    print "the same!"
    print quick
else:
    print "not the same!"
    print "brute"
    print brute
    print "========================="
    print "quick"
    print quick
