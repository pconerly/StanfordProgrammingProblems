"""UnionFind.py

Union-find data structure. Based on Josiah Carlson's code,
http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/215912
with significant additional changes by D. Eppstein.
"""

class UnionFind:
    """Union-find data structure.

    Each unionFind instance X maintains a family of disjoint sets of
    hashable objects, supporting the following two methods:

    - X[item] returns a name for the set containing the given item.
      Each set is named by an arbitrarily-chosen one of its members; as
      long as the set remains unchanged it will keep the same name. If
      the item is not yet part of a set in X, a new singleton set is
      created for it.

    - X.union(item1, item2, ...) merges the sets containing each item
      into a single larger set.  If any item is not yet part of a set
      in X, it is added to X as one of the members of the merged set.
    """

    def __init__(self):
        """Create a new empty union-find structure."""
        self.weights = {}
        self.parents = {}

    def __getitem__(self, object):
        """Find and return the name of the set containing the object."""

        # check for previously unknown object
        if object not in self.parents:
            self.parents[object] = object
            self.weights[object] = 1
            return object

        # find path of objects leading to the root
        path = [object]
        root = self.parents[object]
        # print "======="
        # print "path:", path
        # print "root:", root

        while root != path[-1]:
            path.append(root)
            root = self.parents[root]
            # print "--------"
            # print "path:", path
            # print "root:", root

        # compress the path and return
        for ancestor in path:
            self.parents[ancestor] = root
        return root
        
    def __iter__(self):
        """Iterate through all items ever found or unioned by this structure."""
        return iter(self.parents)

    def __len__(self):
        ends = []
        for item in self:
            ends.append(self[item])
        return len(set(ends))

    def identifyUnions(self):
        ends = []
        for item in self:
            ends.append(self[item])
        return set(ends)


    def produceUnions(self):
        # assumes you have an edge/vertix graph set up.
        # produces a dictionary with the leader as a key and list of items as a value.
        unions = {}
        for item in self:
            if not unions.has_key(self[item]):
                unions[self[item]] = [item]
            else:
                unions[self[item]].append(item)
            # ends.append(self[item])
        return unions

    def union(self, *objects):
        """Find the sets containing the objects and merge them all."""
        roots = [self[x] for x in objects]
        heaviest = max([(self.weights[r],r) for r in roots])[1]
        for r in roots:
            if r != heaviest:
                self.weights[heaviest] += self.weights[r]
                self.parents[r] = heaviest


if __name__ == "__main__":
    uf = UnionFind()
    for i in range(1, 6):
        uf[i]
    print "before stuff:"
    print uf.parents
    print uf.weights
    print len(uf)

    uf.union(1, 3)
    uf.union(2,5)
    uf.union(3, 5)

    print "after stuff:"
    print uf.parents
    print uf.weights
    print "len", len(uf)

    for i in range(1, 6):
        print uf[i]













