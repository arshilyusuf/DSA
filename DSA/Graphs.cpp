#include <bits/stdc++.h>
using namespace std;
// Depth-First Search (DFS):
// Time Complexity: O(V + E) (where V is the number of vertices and E is the number of edges)
// Space Complexity: O(V) (due to recursion stack or visited array)
// How it works:
//   - DFS starts at a source node and explores as far as possible along each branch before backtracking.
//   - It uses a stack (or recursion) to explore unvisited nodes in the graph.
//   - Marks visited nodes to avoid cycles or revisiting nodes.
// When to Use:
//   - Use when you need to explore all nodes in a graph, detect cycles, or find connected components.
//   - Useful for problems like topological sorting, SCCs, and backtracking problems.

// Breadth-First Search (BFS):
// Time Complexity: O(V + E)
// Space Complexity: O(V) (due to the queue used for BFS traversal)
// How it works:
//   - BFS starts at a source node and explores all its neighbors before moving to their neighbors, level by level.
//   - It uses a queue to manage the nodes to be explored next.
//   - BFS ensures that nodes are visited in increasing order of their distance from the source.
// When to Use:
//   - Use when you need to explore nodes level by level, such as for the shortest path in an unweighted graph.
//   - BFS is also useful for checking graph connectivity or finding the shortest path in a graph without negative weights.

// Dijkstra’s Algorithm (for shortest path in weighted graph):
// Time Complexity: O((V + E) log V) (with a priority queue or binary heap)
// Space Complexity: O(V) (due to the storage of distances and priority queue)
// How it works:
//   - Dijkstra starts from the source node and iteratively selects the node with the minimum distance.
//   - It updates the shortest distances to each neighbor and repeats until all nodes are processed.
//   - It uses a priority queue (min-heap) to efficiently get the node with the smallest tentative distance.
// When to Use:
//   - Use when you need the shortest path from a single source to all other nodes in a graph with non-negative edge weights.
//   - Ideal for scenarios like GPS navigation or network routing when edge weights represent distance or cost.

// Bellman-Ford Algorithm (for shortest path with negative weights):
// Time Complexity: O(V * E)
// Space Complexity: O(V) (due to distance and predecessor storage)
// How it works:
//   - Bellman-Ford works by iterating over all edges repeatedly, relaxing the edges until no further updates are possible.
//   - It can handle negative edge weights and detects negative weight cycles by checking for further relaxation after V-1 iterations.
// When to Use:
//   - Use when the graph contains negative edge weights and you need to find the shortest paths from a source node.
//   - It is also used for detecting negative weight cycles in a graph.

// Floyd-Warshall Algorithm (All-pairs shortest path):
// Time Complexity: O(V^3) (for a graph with V vertices)
// Space Complexity: O(V^2) (for storing the shortest paths between all pairs)
// How it works:
//   - Floyd-Warshall iterates through all pairs of nodes and updates the shortest path between them using an intermediate node.
//   - It performs this update for every node as an intermediate node, resulting in the shortest paths between all pairs.
// When to Use:
//   - Use when you need to compute the shortest paths between all pairs of vertices in a graph.
//   - Particularly useful for small graphs or dense graphs where all pairs need to be considered, such as in network routing tables.

// Kruskal’s Algorithm (Minimum Spanning Tree):
// Time Complexity: O(E log E) (due to sorting edges)
// Space Complexity: O(V) (for storing the parent and rank of each node)
// How it works:
//   - Kruskal’s algorithm sorts the edges in increasing order of their weights and then adds them to the MST if they don’t form a cycle.
//   - It uses a union-find data structure to efficiently track and merge components while checking for cycles.
// When to Use:
//   - Use when you need to find the minimum spanning tree (MST) of an undirected, weighted graph.
//   - Kruskal’s works well with sparse graphs, as it processes edges one by one and uses efficient union-find operations.

// Prim’s Algorithm (Minimum Spanning Tree):
// Time Complexity: O((V + E) log V) (with a priority queue)
// Space Complexity: O(V) (for storing vertex keys and parent nodes)
// How it works:
//   - Prim’s algorithm grows the MST by adding the nearest vertex to the tree from the remaining vertices.
//   - It uses a priority queue (min-heap) to select the edge with the smallest weight that connects the MST to a new vertex.
// When to Use:
//   - Use when you need to find the minimum spanning tree (MST) of a connected, undirected graph.
//   - Prim’s is more efficient for dense graphs compared to Kruskal’s.

// Topological Sort (for Directed Acyclic Graphs - DAG):
// Time Complexity: O(V + E)
// Space Complexity: O(V) (for storing the sorted order)
// How it works:
//   - Topological sort orders the nodes of a DAG such that for every directed edge uv from node u to node v, u comes before v in the ordering.
//   - It can be implemented using DFS or Kahn’s algorithm (BFS-based).
// When to Use:
//   - Use when you need to order tasks or nodes in a directed graph with no cycles (DAG).
//   - Common in scheduling, dependency resolution, and build systems.

// Tarjan’s Algorithm (for Strongly Connected Components - SCC):
// Time Complexity: O(V + E)
// Space Complexity: O(V) (for storing SCCs)
// How it works:
//   - Tarjan’s algorithm uses DFS to identify SCCs by maintaining a low-link value for each node.
//   - It uses a stack to store the nodes in the current DFS path and identifies SCCs when it finds a node whose low-link value matches the current node’s index.
// When to Use:
//   - Use when you need to find strongly connected components (SCCs) in a directed graph.
//   - Useful for detecting cycles and component analysis in directed graphs (like social networks or web crawlers).

// A* Algorithm (for shortest path with heuristic):
// Time Complexity: O((V + E) log V) (similar to Dijkstra but with an additional heuristic)
// Space Complexity: O(V) (for storing distances and nodes in the priority queue)
// How it works:
// - A* uses both the actual cost to reach a node (from the source) and an estimated cost (heuristic) to reach the goal.
//   - It combines Dijkstra’s approach with a heuristic to guide the search toward the goal more efficiently.
// When to Use:
//   - Use when you need to find the shortest path with a heuristic (best-first search) in a weighted graph.
//   - Suitable for AI pathfinding and GPS systems where heuristics (like Euclidean distance) can be used.

// Union-Find (Disjoint Set Union, DSU) - for connected components and MST:
// Time Complexity: O(α(V)) (with union by rank and path compression, where α is the inverse Ackermann function)
// Space Complexity: O(V) (for storing parent and rank arrays)
// How it works:
// - Union-Find efficiently handles dynamic connectivity problems by maintaining a forest of disjoint sets.
// - It supports two operations: find (to find the representative of a set) and union (to merge two sets).
// - Path compression and union by rank optimize these operations for near constant time.
// When to Use:
// - Use when you need to efficiently manage and find connected components in a graph.
// - Essential in Kruskal's algorithm for MST, cycle detection, and in dynamic connectivity problems.

bool dirDetectCycleBFS(int V, vector<vector<int>> adj)
{
    // KAHN'S ALGORITHM
    int n = adj.size();
    vector<int> inDeg(n, 0);

    for (auto it : adj)
    {
        for (auto x : it)
        {
            inDeg[x]++;
        }
    }
    queue<int> q;
    // vector<int> ans;
    int count = 0;
    for (int i = 0; i < n; i++)
    {
        if (inDeg[i] == 0)
        {
            q.push(i);
            // ans.push_back(i);
            count++;
        }
    }

    while (!q.empty())
    {
        int node = q.front();
        q.pop();
        for (auto it : adj[node])
        {
            inDeg[it]--;
            if (inDeg[it] == 0)
            {
                q.push(it);
                // ans.push_back(it);
                count++;
            }
        }
    }
    // if(the topological sort is not of the same size as the number of nodes then theres a cycle)
    return !(count == n);
}
bool dirDetectCycleDFS(int i, vector<vector<int>> adj, vector<int> &vis, vector<int> &pathVis)
{
    vis[i] = 1;
    pathVis[i] = 1;

    for (auto it : adj[i])
    {
        if (!vis[it])
        {
            if (dirDetectCycleDFS(it, adj, vis, pathVis))
                return true;
        }
        else if (pathVis[it])
        {
            return true;
        }
    }
    pathVis[i] = 0;
    return false;
}
bool undirDetectCycleDFS(int start, int parent, vector<vector<int>> &adj, vector<int> &vis)
{
    vis[start] = 1;

    for (auto it : adj[start])
    {
        if (!vis[it])
        {
            if (undirDetectCycleDFS(it, start, adj, vis))
                return true;
        }
        else if (parent != it)
        {
            return true;
        }
    }
    return false;
}
bool undirDetectCycleBFS(int start, vector<vector<int>> &adj, vector<int> &vis) // 0 indexed
{
    vis[start] = 1;
    queue<pair<int, int>> q;
    q.push({start, -1});
    while (!q.empty())
    {
        int node = q.front().first;
        int parentNode = q.front().second;
        q.pop();
        for (auto adjNode : adj[node])
        {
            if (!vis[adjNode])
            {
                vis[adjNode] = 1;
                q.push({adjNode, node});
            }
            else if (parentNode != adjNode)
                return true;
        }
    }
    return false;
}
vector<int> BFS(int start, vector<vector<int>> adjList)
{
    int n = adjList.size();
    vector<int> bfs;
    vector<bool> visited(n, 0);
    queue<int> q;
    visited[start] = 1;
    q.push(start);
    while (!q.empty())
    {
        int node = q.front();
        q.pop();
        bfs.push_back(node);
        for (auto it : adjList[node])
        {
            if (!visited[it])
            {
                visited[it] = 1;
                q.push(it);
            }
        }
    }
    return bfs;
}
void dfsHelper(int node, vector<vector<int>> &adjList, vector<bool> &visited, vector<int> &dfs)
{
    visited[node] = true;
    dfs.push_back(node);

    for (auto neighbor : adjList[node])
    {
        if (!visited[neighbor])
        {
            dfsHelper(neighbor, adjList, visited, dfs);
        }
    }
}
vector<int> DFS(int node, vector<vector<int>> adjList)
{
    int n = adjList.size();
    vector<bool> visited(n, false);
    vector<int> dfs;
    dfsHelper(node, adjList, visited, dfs);
    return dfs;
}
void topoDFS(int node, vector<vector<int>> &adj, vector<int> &vis, stack<int> &st)
{
    vis[node] = 1;
    for (auto it : adj[node])
    {
        if (!vis[it])
        {
            topoDFS(it, adj, vis, st);
        }
    }
    st.push(node);
}
vector<int> TopoSortDFS(vector<vector<int>> adj)
{
    int n = adj.size();
    vector<int> vis(n, 0);
    stack<int> st;

    for (int i = 0; i < n; i++)
    {
        if (vis[i] == 0)
        {
            topoDFS(i, adj, vis, st);
        }
    }
    vector<int> ans;
    while (!st.empty())
    {
        ans.push_back(st.top());
        st.pop();
    }
    return ans;
}
vector<int> TopoSortKahns(int n, vector<vector<int>> &adj) // Kahns Algo
{
    // KAHN"S ALGORITHM
    vector<int> inDeg(n, 0);

    for (auto it : adj)
    {
        for (auto x : it)
        {
            inDeg[x]++;
        }
    }
    queue<int> q;
    vector<int> ans;
    for (int i = 0; i < n; i++)
    {
        if (inDeg[i] == 0)
        {
            q.push(i);
            ans.push_back(i);
        }
    }

    while (!q.empty())
    {
        int node = q.front();
        q.pop();
        for (auto it : adj[node])
        {
            inDeg[it]--;
            if (inDeg[it] == 0)
            {
                q.push(it);
                ans.push_back(it);
            }
        }
    }
    return ans;
}
void topoDFS(int node, vector<vector<pair<int, int>>> adj, vector<int> &vis, stack<int> &st)
{
    vis[node] = 1;
    for (auto it : adj[node])
    {
        int v = it.first;
        if (!vis[v])
            topoDFS(v, adj, vis, st);
    }
    st.push(node);
}
vector<int> shortestPathTopoSort(int V, int E, vector<vector<int>> &edges)
{
    // code here
    vector<vector<pair<int, int>>> adj(V);
    // step 1
    for (int i = 0; i < E; i++)
    {
        for (int j = 0; j < V; j++)
        {
            int u = edges[i][0];
            int v = edges[i][1];
            int wt = edges[i][2];
            adj[u].push_back({v, wt});
        }
    }
    vector<int> vis(V, 0);
    stack<int> st;
    for (int i = 0; i < V; i++)
    {
        if (!vis[i])
        {
            topoDFS(i, adj, vis, st);
        }
    }

    // step 2;
    vector<int> dist(V, 1e9); // set distances to infinity
    int source = 0;
    dist[source] = 0;

    while (!st.empty())
    {
        int node = st.top();
        st.pop();

        for (auto it : adj[node])
        {
            int v = it.first;
            int wt = it.second;

            if (dist[node] + wt < dist[v])
            {
                dist[v] = dist[node] + wt;
            }
        }
    }

    for (auto &it : dist)
    {
        if (it == 1e9)
            it = -1;
    }
    return dist;
}
vector<int> shortestPathUndirUnitEdges(vector<vector<int>> &adj, int src)
{
    // code here
    int n = adj.size();
    vector<int> dist(n, INT_MAX);

    dist[src] = 0;
    queue<int> q;

    q.push(src);

    while (!q.empty())
    {
        int node = q.front();
        q.pop();

        for (auto it : adj[node])
        {
            if (dist[node] + 1 < dist[it])
            {
                dist[it] = dist[node] + 1;
                q.push(it);
            }
        }
    }
    for (int i = 0; i < n; i++)
    {
        if (dist[i] == INT_MAX)
            dist[i] = -1;
    }
    return dist;
}
int wordLadder(string beginWord, string endWord, vector<string> &wordList)
{
    unordered_set<string> set(wordList.begin(), wordList.end());
    if (set.find(endWord) == set.end())
        return 0;

    queue<pair<string, int>> q;
    q.push({beginWord, 1});

    while (!q.empty())
    {
        string word = q.front().first;
        int level = q.front().second;
        q.pop();

        for (int i = 0; i < word.size(); i++)
        {
            string temp = word;
            for (char c = 'a'; c <= 'z'; c++)
            {
                temp[i] = c;

                if (temp == word)
                    continue;
                if (temp == endWord)
                    return level + 1;

                if (set.find(temp) != set.end())
                {
                    q.push({temp, level + 1});
                    set.erase(temp);
                }
            }
        }
    }
    return 0;
}
vector<int> dijkstraPQ(vector<vector<pair<int, int>>> &adj, int src)
{
    // TC: ElogV
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    int n = adj.size();
    vector<int> dist(n, 1e9);

    dist[src] = 0;
    pq.push({0, src});

    while (!pq.empty())
    {
        int node = pq.top().second;
        int dis = pq.top().first;
        pq.pop();
        for (auto it : adj[node])
        {
            int edgeWeight = it.second;
            int adjNode = it.first;
            if (dis + edgeWeight < dist[adjNode])
            {
                dist[adjNode] = dis + edgeWeight;
                pq.push({dist[adjNode], adjNode});
            }
        }
    }

    return dist;
}
vector<int> dijkstraSET(vector<vector<pair<int, int>>> &adj, int src)
{
    // Code here
    set<pair<int, int>> set;
    int n = adj.size();
    vector<int> dist(n, 1e9);

    dist[src] = 0;
    set.insert({0, src});

    while (!set.empty())
    {
        auto it = *(set.begin());
        int node = it.second;
        int dis = it.first;
        set.erase(it);

        for (auto it : adj[node])
        {
            int edgeWeight = it.second;
            int adjNode = it.first;
            if (dis + edgeWeight < dist[adjNode])
            {
                if (dist[adjNode != 1e9])
                {
                    set.erase({dist[adjNode], adjNode});
                }
                dist[adjNode] = dis + edgeWeight;
                set.insert({dist[adjNode], adjNode});
            }
        }
    }

    return dist;
}
vector<int> shortestPathDjisktra(int n, int m, vector<vector<int>> &edges)
{
    // Code here
    vector<vector<pair<int, int>>> adj(n + 1);
    for (auto it : edges)
    {
        int u = it[0];
        int v = it[1];
        int wt = it[2];
        adj[u].push_back({v, wt});
        adj[v].push_back({u, wt});
    }
    priority_queue<pair<int, int>,
                   vector<pair<int, int>>, greater<pair<int, int>>>
        pq;

    vector<int> dist(n + 1, 1e9);
    vector<int> parent(n + 1);
    for (int i = 1; i <= n; i++)
        parent[i] = i;

    dist[1] = 0;
    pq.push({0, 1});

    while (!pq.empty())
    {
        int node = pq.top().second;
        int dis = pq.top().first;
        pq.pop();
        for (auto it : adj[node])
        {
            int edge = it.second;
            int adjNode = it.first;

            if (dis + edge < dist[adjNode])
            {
                dist[adjNode] = dis + edge;
                pq.push({dist[adjNode], adjNode});
                parent[adjNode] = node;
            }
        }
    }

    if (dist[n] == 1e9)
        return {-1};
    
    vector<int> ans;
    int node = n;
    while (parent[node] != node)
    {
        ans.push_back(node);
        node = parent[node];
    }
    ans.push_back(1);
    reverse(ans.begin(), ans.end());
    return ans;
}
int minimumMultiplications(vector<int> &arr, int start, int end)
{
    // code here
    if (start == end)
        return 0;
    queue<pair<int, int>> q;
    q.push({start, 0});
    vector<int> dist(100000, 1e9);
    dist[start] = 0;
    while (!q.empty())
    {
        int node = q.front().first;
        int steps = q.front().second;
        q.pop();

        for (auto it : arr)
        {
            int num = (it * node) % 100000;

            if (steps + 1 < dist[num])
            {
                dist[num] = steps + 1;
                if (num == end)
                    return steps + 1;
                q.push({num, steps + 1});
            }
        }
    }
    return -1;
}
vector<int> BellmanFord(int V, vector<vector<int>> &edges, int src)
{
    // only works on directed graphs, order of [edges] doesnt matter
    // if an undirected graph is given convert it into an directed graph by adding v->u if u->v is given
    //  TC: V x E
    vector<int> dist(V, 1e8);
    dist[src] = 0;
    for (int i = 0; i < V; i++)
    {
        for (auto it : edges)
        {
            int u = it[0];
            int v = it[1];
            int wt = it[2];

            if (dist[u] == 1e8)
                continue;
            else
            {
                if (dist[u] + wt < dist[v])
                {
                    if (i == V - 1) // if dist reduces on the last iteration, then theres a negative cycle in the graph
                    {
                        return {-1};
                    }
                    dist[v] = dist[u] + wt;
                }
            }
        }
    }
    return dist; // return shortest distances
}
vector<vector<int>> FloydWarshall(vector<vector<int>> &mat)
{   // adjacency matrix
    // works on directed graphs
    //  Code here
    int n = mat.size();
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (mat[i][j] == -1) // if we cant reach
            {
                mat[i][j] = 1e9;
            }
            if (i == j)
            {
                mat[i][j] = 0;
            }
        }
    }

    // main algorithm
    for (int k = 0; k < n; k++)
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j]); // reach i to j via k
            }
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (mat[i][j] == 1e9)
            { // if we cant reach
                mat[i][j] = -1;
            }
        }
    }
    return mat; // returns a 2D matrix where mat[i][j] is shortest distance from node i to node j
}
int minSpanningTreeSum(int V, vector<vector<int>> adj[])
{
    priority_queue<pair<int, int>,vector<pair<int, int>>, greater<pair<int, int>>>pq;
    vector<int> vis(V, 0);
    // {wt, node}
    pq.push({0, 0});
    int sum = 0;
    while (!pq.empty())
    {
        auto it = pq.top();
        pq.pop();
        int node = it.second;
        int wt = it.first;

        if (vis[node] == 1)continue;
        // add it to the mst
        vis[node] = 1;
        sum += wt;
        for (auto it : adj[node])
        {
            int adjNode = it[0];
            int edW = it[1];
            if (!vis[adjNode])
            {
                pq.push({edW, adjNode});
            }
        }
    }
    return sum;
}
vector<pair<int, int>> minSpanningTree(int V, vector<vector<int>> adj[]){   
    //PRIMM's ALGORiTHM
    priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>> pq;

    vector<int> vis(V, 0);
    vector<pair<int, int>> mst; // To store the edges of the MST

    // {wt, {node, adjNode}}
    pq.push({0, {0, -1}}); // -1 indicates the starting node

    while (!pq.empty())
    {
        auto it = pq.top();
        pq.pop();
        int node = it.second.first;
        int parent = it.second.second;
        int wt = it.first;

        if (vis[node] == 1)
            continue;

        // Mark the node as visited
        vis[node] = 1;

        // Add edge to MST if it is not the starting node
        if(parent != -1)
        {
            mst.push_back({parent, node});
        }

        for (auto adjIt : adj[node])
        {
            int adjNode = adjIt[0];
            int edW = adjIt[1];
            if (!vis[adjNode])
            {
                pq.push({edW, {adjNode, node}});
            }
        }
    }

    return mst;
}
int findUltimateParent(int u, vector<int>parent){
    if(u==parent[u])
        return u;
    return parent[u] = findUltimateParent(parent[u],parent);
}
void unionByRank(int u, int v, vector<int> parent, vector<int>rank)
{
    int ultpU = findUltimateParent(u, parent);
    int ultpV = findUltimateParent(v, parent);
    if (ultpU == ultpV)
        return;

    if(rank[ultpU]<rank[ultpV]){
        parent[ultpU] = ultpV;
    }else if(rank[ultpU]<rank[ultpV]){
        parent[ultpV] = ultpU;
    }else{
        parent[ultpV] = ultpU;
        rank[ultpU]++;
    }
    
}
void unionBySize(int u, int v, vector<int> parent, vector<int> size)
{
    int ultpU = findUltimateParent(u, parent);
    int ultpV = findUltimateParent(v, parent);
    if (ultpU == ultpV)
        return;

    if(size[ultpU] < size[ultpV]){
        parent[ultpU] = ultpV;
        size[ultpV] += size[ultpU];
    }else{
        parent[ultpV] = ultpU;
        size[ultpU] += size[ultpV];
    }
}
class DisjointSet{
    public:
    vector<int> parent, rank, size;
    DisjointSet(int n){
        parent.resize(n+1);
        rank.resize(n+1,0);
        size.resize(n+1,1);
        for(int i=0;i<=n;i++){
            parent[i] = i;
        }
    }
    int findUltimateParent(int u)
    {
        if (u == parent[u])
            return u;
        return parent[u] = findUltimateParent(parent[u]);
    }
    void unionByRank(int u, int v)
    {
        int ultpU = findUltimateParent(u);
        int ultpV = findUltimateParent(v);
        if (ultpU == ultpV)
            return;

        if (rank[ultpU] < rank[ultpV])
        {
            parent[ultpU] = ultpV;
        }
        else if (rank[ultpU] < rank[ultpV])
        {
            parent[ultpV] = ultpU;
        }
        else
        {
            parent[ultpV] = ultpU;
            rank[ultpU]++;
        }
    }
    void unionBySize(int u, int v)
    {
        int ultpU = findUltimateParent(u);
        int ultpV = findUltimateParent(v);
        if (ultpU == ultpV)
            return;

        if (size[ultpU] < size[ultpV])
        {
            parent[ultpU] = ultpV;
            size[ultpV] += size[ultpU];
        }
        else
        {
            parent[ultpV] = ultpU;
            size[ultpU] += size[ultpV];
        }
    }
};
int KruskalsAlgorithmMstSum(int V, vector<vector<int>> adj[])
{
    // TC: M x 4 x alpha
    // TC: o(M)
    vector<pair<int, pair<int, int>>> edges;
    for (int i = 0; i < V; i++)
    {
        for (auto it : adj[i])
        {
            int node = i;
            int adjNode = it[0];
            int wt = it[1];
            edges.push_back({wt, {node, adjNode}});
        }
    }
    DisjointSet ds(V);
    sort(edges.begin(), edges.end());
    int mstSum = 0;
    for (auto it : edges)
    {
        int wt = it.first;
        int u = it.second.first;
        int v = it.second.second;

        if (ds.findUltimateParent(u) != ds.findUltimateParent(v))
        {
            ds.unionBySize(u, v);
            mstSum += wt;
        }
    }
    return mstSum;
}
void dfs1Kosaraju(int node, vector<vector<int>> &adj, vector<int> &vis, stack<int> &st)
{
    vis[node] = 1;
    for (auto it : adj[node])
    {
        if (!vis[it])
            dfs1Kosaraju(it, adj, vis, st);
    }
    st.push(node);
}
void dfs3Kosaraju(int node, vector<vector<int>> &adj, vector<int> &vis)
{
    vis[node] = 1;
    for (auto it : adj[node])
    {
        if (!vis[it])
            dfs3Kosaraju(it, adj, vis);
    }
}
int Kosaraju(vector<vector<int>> &adj)
{
    // code here
    int n = adj.size();
    // step 1 sort acc to finish time
    stack<int> st;
    vector<int> vis(n, 0);
    for (int i = 0; i < n; i++)
    {
        if (!vis[i])
        {
            dfs1Kosaraju(i, adj, vis, st);
        }
    }

    // step 2 reverse the edges
    vector<vector<int>> adjT(n);
    for (int i = 0; i < n; i++)
    {
        vis[i] = 0; // clear the visited array for step 3
        for (auto it : adj[i])
        {
            adjT[it].push_back(i);
        }
    }

    // step 3
    int ans = 0;
    while (!st.empty())
    {
        int node = st.top();
        st.pop();
        if (!vis[node])
        {
            ans++;
            dfs3Kosaraju(node, adjT, vis);
        }
    }
    return ans;
}

int main()
    {
        // vector<vector<int>> adjList = {
        //     {},
        //     {2, 3},
        //     {1, 5, 6},
        //     {1, 4, 7},
        //     {3, 8},
        //     {2},
        //     {2},
        //     {3, 8},
        //     {4, 7},
        // };

        // vector<vector<int>> adjListCycle = {{5, 5}, {0, 4}, {1, 2}, {1, 4}, {2, 3}, {3, 4}};
        // vector<int> bfs = BFS(1, adjList);
        // vector<int> dfs = DFS(1, adjList);
        // for (int i = 0; i < bfs.size(); i++)
        //     cout << bfs[i] << " ";
        // cout << endl;
        // for (int i = 0; i < dfs.size(); i++)
        //     cout << dfs[i] << " "; // TC:
        // cout << endl;
        // // FOR CYCLE
        // vector<int> vis(adjListCycle.size(), 0);
        // cout << "Is cycle: " << undirDetectCycleBFS(0, adjListCycle, vis);
        // vector<int> Topo = topoSortDFS(adjList);
        // for (int i = 0; i < Topo.size(); i++)
        //     cout << Topo[i] << " ";
        // cout << endl;
        return 0;
    }





