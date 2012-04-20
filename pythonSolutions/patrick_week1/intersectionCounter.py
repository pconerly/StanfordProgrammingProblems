def loadarray():
    arrayFile = open("Integerarray.txt", "r")
    array = []
    for i in arrayFile:
        array.append(int(i[:-1]))
    return array

	
def sortCount(array):
    #Divide
    n = len(array)
    if n == 1:
        return array
    else:
        array1 = array[:n/2]
        array2 = array[n/2:]

    #Recursive Call
    array1 = sortCount(array1)
    array2 = sortCount(array2)

    #Merge
    global counter
    j = 0
    k = 0
    i = 0
    Output = []    
    while i < (len(array1) + len(array2)):
        if j==len(array1):
            Output.append(array2[k])
            k += 1                 
        elif k==len(array2):
            Output.append(array1[j])
            j += 1            
        elif array1[j] <= array2[k]:
            Output.append(array1[j])
            j += 1
        elif array1[j] > array2[k]:
            Output.append(array2[k])
            counter += (len(array1) - j)
            k += 1
        i += 1
    return Output
	
	
array = loadarray()
counter = 0
sortCount(array)
print counter
