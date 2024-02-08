# Finds the path with the smallest weight, doesn't work on negative-weight (use Bellman-Ford algorithm instead)

# Steps:
# 1. Find the cheapest node
# 2. Update the costs of the neighbors of this node
# 3. Repeat until you've done this for every node
# 4. Calculate the final path

# One hash table, Four nested hash tables
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

# Costs hash table
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# Parents hash table
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# Array to keep track of the nodes already processed
processed = []

# Implementation
node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)