# inversions_brute
def count_inversions(maxentries, filename):
    f = open(filename, 'r')
    array = list()
    counter = 1
    
    for e in f:
        array.append(int(e))
        counter += 1
        if counter > maxentries:
            break

    counter = 0
    print "BRUTE"
    print "number of entries:", len(array)
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            #print i, j, array[i], array[j]
            if array[i] > array[j]:
                #print "counted"
                counter += 1
    return counter
