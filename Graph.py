from collections import defaultdict

class Graph(object):
    def __init__(self, directed=True):
        self.graph = defaultdict(set) # Adjacency list with node as key and set of
                        # incident nodes as value
        self.directed = directed

    def add_edge(self, v1, v2):
        self.graph[v1].add(v2)

        if not self.directed:
            self.graph[v2].add(v1)

    def find_path(self, start, goal, dfs=True):
        paths = [[start]]
        while paths:
            if dfs:
                path = paths.pop()
            else:
                path = paths.pop(0)
            for next in self.graph[path[-1]] - set(path):
                if next == goal:
                    return path + [next]
                else:
                    paths.append(path + [next])

    def find_path_recursive(self, start, goal, path=None):
        if path is None:
            path = [start]
            
        if start == goal:
            return path

        for next in self.graph[start] - set(path):
            return self.find_path_recursive(next, goal, path + [next])

    def search(self, start, goal, dfs=True):
        nodes = [start]
        visited = []
        while nodes:
            if dfs:
                node = nodes.pop()
            else:
                node = nodes.pop(0)
                
            if node == goal:
                return True
            elif node not in visited:
                for next in self.graph[node]:
                    nodes.append(next)
                visited.append(node)
        return False

    def dfs(self, start, goal, visited=None):
        if visited is None:
            visited = set()

        visited.add(start)
        if start == goal:
            return True
        else:
            for next in self.graph[start] - visited:
                return self.dfs(next, goal, visited)
        return False
        

if __name__ == "__main__":
    graph = Graph()
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('B', 'E')
    graph.add_edge('C', 'F')
    graph.add_edge('E', 'F')

    print graph.graph

    print 'A --> F path'
    print graph.find_path('A', 'F')
    print graph.find_path('A', 'F', False)
    print graph.find_path_recursive('A', 'F')

    print 'F --> A path'
    print graph.find_path('F', 'A')
    print graph.find_path('F', 'A', False)
    print graph.find_path_recursive('F', 'A')

    print 'A --> F exists'
    print graph.search('A', 'F')
    print graph.search('A', 'F', False)
    print graph.dfs('A', 'F')

    print 'F --> A exists'
    print graph.search('F', 'A')
    print graph.search('F', 'A', False)
    print graph.dfs('F', 'A')

    undirected_graph = Graph(False)
    undirected_graph.add_edge('A', 'B')
    undirected_graph.add_edge('A', 'C')
    undirected_graph.add_edge('B', 'D')
    undirected_graph.add_edge('B', 'E')
    undirected_graph.add_edge('C', 'F')
    undirected_graph.add_edge('E', 'F')

    print undirected_graph.graph

    print 'A --> F path'
    print undirected_graph.find_path('A', 'F')
    print undirected_graph.find_path('A', 'F', False)
    print undirected_graph.find_path_recursive('A', 'F')

    print 'F --> A path'
    print undirected_graph.find_path('F', 'A')
    print undirected_graph.find_path('F', 'A', False)
    print undirected_graph.find_path_recursive('F', 'A')

    print 'A --> F exists'
    print undirected_graph.search('A', 'F')
    print undirected_graph.search('A', 'F', False)
    print undirected_graph.dfs('A', 'F')

    print 'F --> A exists'
    print undirected_graph.search('F', 'A')
    print undirected_graph.search('F', 'A', False)
    print undirected_graph.dfs('F', 'A')
    
