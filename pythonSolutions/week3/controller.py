import randomContractions

def run(n):
    adj = randomContractions.importGraph()
    mincut = -1
    print "running..."
    for i in range(n):
        adj = randomContractions.importGraph()
        temp = randomContractions.findmincut(adj)
        if mincut == -1 or temp < mincut:
            mincut = temp
            print mincut
        #print mincut

if __name__ == "__main__":
    run(100)