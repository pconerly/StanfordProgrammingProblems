
# first 163145
# last 162483
# median 133842
"""
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
    
    #x = ifirst
    #x = ilast
    
    less = list()
    greater = list()



    #// left is the index of the leftmost element of the array
    #// right is the index of the rightmost element of the array (inclusive)
    #//   number of elements in subarray = right-left+1
    #function partition(array, 'left', 'right', 'pivotIndex')
    pivotValue = array[x]
    temp = array[0]
    array[0] = array[x]
    array[x] = temp
    i = 1
    
    for j in range(i, len(array)):  ## left =< i < right
        if array[j] < pivotValue:
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
            #swap array[j] and array['storeIndex']

    less = array[1:i]
    greater = array[i:]
    (first, temp) = quicksort(less)
    counter += temp
    temp = 0
    (second, temp) = quicksort(greater)
    counter += temp
    return (first + [pivotValue] + second, counter)
        #concatenate(quicksort('less'), 'pivot', quicksort('greater'))
"""
def quicksort(array):
    if len(array) <= 1:
        return (array, 0)  ## an array of zero or one elements is already sorted

    medianArray = [array[0],array[(len(array)-1)/2],array[-1]]
    medianArray.sort()
    x = array.index(medianArray[1])
    #x = ifirst
    #x = ilast
    
    pivotValue = array[x]
    (array[0], array[x]) = (array[x], array[0])
    i = 1
    for j in range(i, len(array)):  ## left =< i < right
        if array[j] < pivotValue:
            (array[i], array[j]) = (array[j], array[i]);
            i += 1

    counter = len(array) - 1
    (first, temp) = quicksort(array[1:i])
    counter += temp
    (second, temp) = quicksort(array[i:])
    counter += temp
    return (first + [pivotValue] + second, counter)


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


    
    """
    temp = array[j]
    array[j] = array[i]
    array[i] = temp
    """
    #swap array['storeIndex'] and array['right']  ## Move pivot to its final place
    #return 'storeIndex'
"""
    for item in array:
        #print "comparison ===="
        #print "    pivot", pivot
        #print "    item:", item
        if item <= pivot:
            less.append(item)
        else:
            greater.append(item)
            """
