from UnionFind import UnionFind



def importGraph(filename = 'clustering1.txt'):
    """Imports pairs of endpoints into an adjancey list graph representation.
    Keep track of both edges and vertices."""
    f = open(filename)

    edges = []
    vees = {}
    
    print f.readline()

    for line in f:
        edgeinfo = line.split()
        ends = edgeinfo[0:2]
        weight = edgeinfo[2]
        e = Edge(ends[0], ends[1], weight)
        edges.append(e)
        for end in ends:
            if not vees.has_key(end):
                vees[end] = Vertix(end)
            vees[end].addEdge(e)

    # sort edges by weight
    return (edges, vees)

class Vertix:
    def __init__(self, n):
        self.n = int(n)
        self.edges = []
        
    def addEdge(self, v):
        self.edges.append(v)

class Edge:
    def __init__(self, end1, end2, weight):
        self.ends = [end1, end2]
        self.weight = int(weight)



def cluster(edges, vees, goal = 4):
    edges.sort(key=lambda x: x.weight)

    print [e.weight for e in edges[0:20]]

    uf = UnionFind()
    for key, value in vees.items():
        uf[key]

    count = len(vees.keys())
    eindex = 0
    # end = len(edges)
    # while eindex < end:
    while count > goal:
        if eindex % 1000 == 0:
            print eindex
        # find an edge that doesn't have endpoints in the same cluster
        while uf[edges[eindex].ends[0]] == uf[edges[eindex].ends[1]]:
            eindex += 1
        # cluster them together
        uf.union(edges[eindex].ends[0], edges[eindex].ends[1])
        eindex += 1
        count -= 1

    print "count", count
    print len(uf)
    for key, value in uf.parents.items():
        print "%s: %s" % (key, value)


    return uf

    
    
if __name__ == '__main__':
    (edges, vees) = importGraph() #'clustering1_test.txt')
    uf = cluster(edges, vees) #, goal = 2)

    edgeweightDict = {}
    for e in edges:
        edgeweightDict[(e.ends[0], e.ends[1])] = e.weight
        edgeweightDict[(e.ends[1], e.ends[0])] = e.weight
    
    indexes = uf.produceUnions().keys()
    values = uf.produceUnions().values()
    spanningdistances = {}
    for i in range(0, len(indexes) -1):
        for j in range(i + 1, len(indexes)):
            print "%s vs %s" % (indexes[i], indexes[j])
            spanningdistances[(i, j)] = []
            for vi in values[i]:
                for vj in values[j]:
                    spanningdistances[(i, j)].append(edgeweightDict[(vi, vj)])

    for key in spanningdistances.keys():
        print "the min of %s is %s" % (spanningdistances[key], min(spanningdistances[key])) 
        spanningdistances[key] = min(spanningdistances[key])

    for v in spanningdistances.values():
        print "value:", v
    answer = min(spanningdistances.values())

    print answer
    # 8457







    
    