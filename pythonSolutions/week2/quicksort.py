
# first 157946
# last 162330
# median 131563

def quicksort(array):
    if len(array) <= 1:
        return (array, 0)  ## an array of zero or one elements is already sorted

    counter = len(array) - 1
    # choose pivot
    # select and remove a pivot value 'pivot' from array
    ifirst = 0
    ilast = len(array) - 1
    imid = (len(array)-1)/2

    medianArray = [array[ifirst],array[imid],array[ilast]]

    medianArray.sort()
    x = array.index(medianArray[1])
    
    # x = ifirst
    # x = ilast
    
    pivot = array.pop(x)
    
    less = list()
    greater = list()

    for item in array:
        #print "comparison ===="
        #print "    pivot", pivot
        #print "    item:", item
        if item <= pivot:
            less.append(item)
        else:
            greater.append(item)
    (first, temp) = quicksort(less)
    counter += temp
    temp = 0
    (second, temp) = quicksort(greater)
    counter += temp
    return (first + [pivot] + second, counter)
        #concatenate(quicksort('less'), 'pivot', quicksort('greater'))


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
