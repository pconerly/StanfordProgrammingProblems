import time

# first problem for stanford class

# find the number of inversions in the file.

def mergesort_count(array):
    # main recusive function
    length = len(array)
    invcount = 0
    if length == 1:
        return array, 0
    else:
        (a, temp) = mergesort_count(array[0:length/2])
        invcount += temp
        (b, temp) = mergesort_count(array[length/2:length])
        invcount += temp
        (c, temp) = mergesort_splitcount(a, b)
        invcount += temp
        return c, invcount

def mergesort_splitcount(a, b):
    #given two arrays, mergesort them to find # of split inversions
    counter = 0
    c = list()
    i = 0
    j = 0
    while (len(a) - i) > 0 or (len(b) - j) > 0:
        #print "i", i, "j", j, "counter", counter
        if (len(a) - i) >= 1 and (len(b) - j) >= 1:
            # compare
            #print "compare!"
            if a[i] < b[j]:
                c.append(a[i])
                i += 1
            else:
                c.append(b[j])
                j += 1
                counter += (len(a) - i)                
        elif (len(a) - i) >= 1:
            #take the last one from a.
            c.append(a[i])
            i += 1
        elif (len(b) - j) >= 1:
            c.append(b[j])
            j += 1
            
    return c, counter

def run(filename):
    f = open(filename, 'r')

    array = list()

    counter = 0
    for e in f:
        array.append(int(e))
        #counter += 1
        if counter > 1000:
            break

    print "number of entries:", len(array)

    ptime = 0
    ptime -= time.clock()
    (sortedarrayed, result) = mergesort_count(array)
    ptime += time.clock()
    print result, "inversions"
    print "took:", ptime ,"seconds"
    return result

def testrun(maxentries, filename):
    f = open(filename, 'r')
    array = list()
    counter = 1
    
    for e in f:
        array.append(int(e))
        counter += 1
        if counter > maxentries:
            break
    print "inversion mergesort"
    print "number of entries:", len(array)

    (sortedarrayed, result) = mergesort_count(array)
    return result

if __name__ == "__main__":
    run('IntegerArray.txt')
