# randomContractions.py
import random
import time

def importGraph(filename = 'kargerAdj.txt'):
    f = open(filename)
    adjEdges = []
    adjVertix = []
    
    for line in f:
        points = line.split()
        v = Vertix(points.pop(0))
        for item in points:
            e = Edge(v.n, item)
            adjEdges.append(e)
            v.addEdge(e)
        adjVertix.append(v)
            
    # redundancy processing:
    n = len(adjEdges)
    adjEdges.sort(key=lambda x: x.ends[1])
    adjEdges.sort(key=lambda x: x.ends[0])
    
    i = 0
    while i < n - 1:
        if adjEdges[i].ends == adjEdges[i+1].ends:
            adjEdges.pop(i+1)
            n = len(adjEdges)
        else:
            i += 1
    
    return (adjEdges, adjVertix)

class Vertix:
    def __init__(self, n):
        self.n = int(n)
        self.edges = []
        
    def addEdge(self, v):
        self.edges.append(v)

class Edge:
    def __init__(self, end1, end2):
        end1 = int(end1)
        end2 = int(end2)
        if end1 < end2:
            self.ends = [end1, end2]
        else:  # end1 > end2:
            self.ends = [end2, end1]
    
    def hasEndPoint(self, endTest):
        if endTest in self.ends:
            return True
        else:
            return False

    def isSelfLoop(self):
        if self.ends[0] == self.ends[1]:
            return True
        else:
            return False

    def replaceEndPoint(self, find, replace):
        for i in range(len(self.ends)):
            if self.ends[i] == find:
                self.ends[i] = replace


def findmincut(adj):
    adje = adj[0]
    adjv = adj[1]
    
    # random.seed(time.time())
    while len(adjv) > 2:
        # pick a remaining edge randomly
        r = random.randint(0, len(adje) - 1)

        # contract u and v to a single vertex
        contractEdge = adje[r]
        
        for i in range(len(adjv)):
            if adjv[i].n == contractEdge.ends[0]:
                vh_idx = i
            if adjv[i].n == contractEdge.ends[1]:
                vt_idx = i
        
        find = adjv[vh_idx].n
        replace = adjv[vt_idx].n
        adjv[vt_idx].edges = adjv[vt_idx].edges + adjv[vh_idx].edges
        adjv.pop(vh_idx)
        
        # replace vertix values in edge list
        for i in range(len(adje)):
            adje[i].replaceEndPoint(find, replace)
        
        
        # remove self-loops
        new_adje = []
        for e in adje:
            if not e.isSelfLoop():
                new_adje.append(e)
        adje = new_adje
    
    # return cut
    return len(adje)
    
    
if __name__ == '__main__':
    adj = importGraph()
    print findmincut(adj)
    
    
    
    
    