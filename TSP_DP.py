# Dynamic programming solution for the Traveling Salesman Problem
# O((n^2)*(2^n)) runtime 
#
# Input: Graph g as a two dimensional matrix with g[i][j] having the
# weight of the link between vertices i and j. i and j are 0-indexed
#
#Output: Cost of minimum tour

from collections import defaultdict

class TSP_DP(object):
    def __init__(self, graph=None):
        if graph is not None:
            self.graph = graph

    def _get_subsets_r(self, nodes, s):
        if s == 1:
            return [[node] for node in nodes]
        else:
            sets = []
            for i, cur in enumerate(nodes):
                if i + s <= len(nodes):
                    rest = self._get_subsets_r(nodes[i + 1:], s - 1)
                    sets.extend([[cur] + i for i in rest])
            return sets

    def _get_subsets(self, s):
        num_nodes = len(self.graph)
        if s > 0 and s <= num_nodes:
            nodes = range(1, num_nodes)
            if s == 1:
                return [0]
            else:
                subsets = self._get_subsets_r(nodes, s - 1)
                return [[0] + i for i in subsets]

    def solve(self):
        C = defaultdict(list)
        C[tuple((0,))].insert(0, 0) # C[{0}, 0] := 0

        n = len(self.graph)

        # For subsets of size s
        for s in range(2, n + 1):
            subsets = self._get_subsets(s)
            for S in subsets:
                for j in S:
                    if j != 0:
                        for dest in range(len(C[tuple(S)]), j + 1):
                            C[tuple(S)].insert(dest, float("inf"))
                        for i in S:
                            if i != j:
                                cost = C[tuple(set(S) - set((j,)))][i] + self.graph[i][j]
                                if cost < C[tuple(S)][j]:
                                    C[tuple(S)][j] = cost

        opt = float("inf")
        for k in range(1, n):
            cost = C[tuple(range(0, n))][k] + self.graph[0][k]
            if cost < opt:
                opt = cost

        return opt


if __name__ == "__main__":
    g1 = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
    g2 = [[0, 2, 2, 1, 4], [2, 0, 3, 2, 3], [2, 3, 0, 2, 2], [1, 2, 2, 0, 4], [4, 3, 2, 4, 0]]

    t1 = TSP_DP(g1)
    t2 = TSP_DP(g2)

    print(t1.solve())
    assert t2.solve() == 10
