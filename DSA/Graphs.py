from collections import deque
class Graph:

    def bfs(self, adj):
        n = len(adj)
        visited = [False]*n
        distance = [0]*n
        queue = deque()
        
        visited[0]=True
        queue.append(0)

        while queue:
            node = queue.popleft()
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor]=True
                    distance[neighbor]=distance[node]+1
                    queue.append(neighbor)
        return distance
    def dfs(self, adj):
        n = len(adj)
        visited = [False]*n
        ds = []
        
        def helper(node):
            visited[node]=True
            ds.append(node)
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    helper(neighbor)
        helper(0)
        return ds

def main():
    adj = [
        [1, 2],     # Node 0 is connected to 1 and 2
        [0, 3, 4],  # Node 1 is connected to 0, 3, and 4
        [0],        # Node 2 is connected to 0
        [1],        # Node 3 is connected to 1
        [1]         # Node 4 is connected to 1
    ]

    graph = Graph()
    bfsResult = graph.bfs(adj)
    print("BFS Distances from node 0:", bfsResult)
    dfsResult = graph.dfs(adj)
    print("DFS REsult: ", dfsResult)

if __name__ == "__main__":
    main()
