# Breadth first search algorithm
# Answers two type of questions
# 1. Is there a path from Node A to Node B
# 2. What's the shortest path from node A to node B

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["tom", "jonny"]
graph["anuj"] = []  
graph["peggy"] = []
graph["tom"] = []
graph["jonny"] = []
