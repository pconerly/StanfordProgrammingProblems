from UnionFind import UnionFind
def importGraph(filename = 'clustering2.txt'):
    """Imports pairs of endpoints into an adjancey list graph representation.
    Keep track of both edges and vertices."""
    f = open(filename)
    (totalnodes, bits) = [int(x) for x in f.readline().split()]
    nodecount = 0
    nodes = {}
    for line in f:
        nodes[nodecount] = [int(x) for x in line.split()]
        nodecount += 1
    f.close()

    count = 0
    buckets = {}
    # prep buckets
    for i in range(0, bits - 1):
        for j in range(i + 1, bits):
            buckets[(i, j)] = {}
            # print i, j
            count += 1
    print count

    count = 0
    for nkey, nval in nodes.items():
        count += 1
        if count % 1000 == 0:
            print count
        for i in range(0, bits - 1):
            for j in range(i + 1, bits):
                nvalminustwo = tuple(nval[0:i] + nval[i+ 1:j] + nval[j+1: bits])

                if not buckets[(i, j)].has_key(nvalminustwo):
                    buckets[(i, j)][nvalminustwo] = [nkey]
                else:
                    buckets[(i, j)][nvalminustwo].append(nkey)

    uf = UnionFind()

    for n in xrange(len(nodes)):
        uf[n]

    count = 0
    for key in buckets.keys():
        for valkey in buckets[key]:

            count += 1
            if count % 1000000 == 0:
                print count
            uf.union(*buckets[key][valkey])

    return uf


def hammering(node1, node2):
    # returns the hammering distance.
    assert len(node1) == len(node2)
    diffcount = 0
    for i in range(len(node1)):
        if node1[i] != node2[i]:
            diffcount += 1

    return diffcount


if __name__ == '__main__':
    uf = importGraph() #filename = 'clustering2_test.txt')
    print len(uf)
    # 16508


