from collections import defaultdict
import sys
sys.setrecursionlimit(10000)

# Read input
n = int(input())

# Build the graph
graph = defaultdict(list)
indegree = defaultdict(int)

# Dictionary to track if a potion is basic (has no ingredients)
is_basic = {}

for _ in range(n):
    parts = input().split()
    potion = parts[0]
    k = int(parts[1])
    ingredients = parts[2:]
    
    if k == 0:
        is_basic[potion] = True
    else:
        is_basic[potion] = False
        graph[potion] = ingredients

# Read target potion
target = input()

# Memoization to store steps required for each potion
memo = {}

def dfs(potion):
    # Base case: if it's a basic ingredient
    if is_basic[potion]:
        return 0
    if potion in memo:
        return memo[potion]
    
    max_steps = 0
    for ingredient in graph[potion]:
        max_steps = min(max_steps, dfs(ingredient))
    
    memo[potion] = 1 + max_steps
    return memo[potion]

# Output result
print(dfs(target))


n = int(input)
farmers = list(map(input.split()))
for i in range n:
    farmers[i] = list(map.input.split())

