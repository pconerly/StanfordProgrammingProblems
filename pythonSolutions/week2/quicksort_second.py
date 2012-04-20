# OLDDD
# first 163145
# last 162483
# median 133842

# new 
# first 162085
# last 164123
# median 138382

def ChoosePivot(array, n):
    
    # index = median of 3 rule.    
    medianArray = [array[0],array[(n-1)/2],array[-1]]
    medianArray.sort()
    index = array.index(medianArray[1])

    index = 0
    index = -1
    
    return index

def quicksort(array):
    n = len(array)
    if n == 1:
        return (array, 0)
    
    counter = n - 1
    pindex = ChoosePivot(array, n)

    #pre-processing step to swap pivot to first element
    (array[0], array[pindex]) = (array[pindex], array[0])
    
    (array, i) = Partition(array, n)

    afirst = list()
    asecond = list()

    #recursively sort 1st part
    if i != 0: #first part is zero length
        nfirst = len(array[0:i])
        #counter += len(array[0:i]) - 1
        (afirst, temp) = quicksort(array[0:i])
        counter += temp
    #recursively sort 2nd part
    if i + 1 < n: #second part is zero length
        nsecond = len(array[i+1:])
        #counter += len(array[i+1:]) - 1
        (asecond, temp) = quicksort(array[i+1:])
        counter += temp

    return (afirst + [array[i]] + asecond, counter)
    


def Partition(array, n):
    # assumes first element is pivot
    
    i = 1
    for j in range(1, len(array)):
        #print array, i, j
        if array[j] > array[0]:
            pass # j += 1
        else: # array[j] <= array[0]
            
            try:
                (array[i], array[j]) = (array[j], array[i])
            # also j += 1
            except:
                print n, i, j
            i += 1
            

    (array[0], array[i-1]) = (array[i-1], array[0])
    
    return (array, i-1)    
        

def quicksortprep(filename, maxentries = 1000000000):
    f = open(filename, 'r')
    array = list()    
    counter = 1
    
    for e in f:
        array.append(int(e))
        counter += 1
        if counter > maxentries:
            print "quick broke, len:", len(array)
            print array
            break
    
    return quicksort(array)


if __name__ == "__main__":
    filename = "QuickSort.txt"
    
    (array, counter) = quicksortprep(filename)
    print counter
    print "success"

