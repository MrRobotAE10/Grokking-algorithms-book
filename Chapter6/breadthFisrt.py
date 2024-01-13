# Breadth first search algorithm
# Answers two type of questions
# 1. Is there a path from Node A to Node B
# 2. What's the shortest path from node A to node B
from collections import deque

def is_person_seller(name):
    return name[-1] == "m" # If person names end with m
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["tom", "jonny"]
graph["anuj"] = []  
graph["peggy"] = []
graph["tom"] = []
graph["jonny"] = []

search_queue = deque() # Creates a queue
search_queue += graph["you"] # Add all my neighbors to the queue

while search_queue:
    person = search_queue.popleft()
    if is_person_seller(person):
        print(f"{person} is a mango seller!")
        break 
    else:
        search_queue += graph[person]
else:
    print("No mango seller was found")
