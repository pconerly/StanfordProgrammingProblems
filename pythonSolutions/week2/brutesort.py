
array = []

def brutesort(filename, maxentries = 1000000000):
    f = open(filename, 'r')
    array = list()
    counter = 1
    for e in f:
        array.append(int(e))
        counter += 1
        if counter > maxentries:
            print "brute broke, len:", len(array)
            break

    array.sort()

    return array


if __name__ == "__main__":
    filename = ""
    brutesort(filename)
    print "success"
