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

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if is_person_seller(person):
                print(f"{person} is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

search("you")