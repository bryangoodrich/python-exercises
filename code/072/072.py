import sys
import pandas as pd
from collections import deque

def make_adjacency_list(source):
    names = ["source", "target"]
    edges = pd.read_csv(source, sep=" ", header=None, names=names)
    
    adj = {}
    for source, target in edges.itertuples(index=False):
        if source not in adj:
            adj[source] = []  
        
        adj[source].append(target)
    
    return adj

def bfs(start_node, adj):
    visited = set()
    queue = deque()
    queue.append(start_node)
    friend_count = 0
    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        
        visited.add(node)
        friends = adj[node]
        friend_count += len(friends)
        print(f"{node} has {len(friends)} friends") 
        for friend in friends:
            if friend in adj:
                queue.append(friend)
    
    return visited, friend_count


if __name__ == "__main__":
    args = len(sys.argv)
    start = sys.argv[1] if args >= 2 else 0
    
    dataset = "data/facebook.txt"
    adj = make_adjacency_list(dataset)
    visited, friends = bfs(int(start), adj)
    
    print(f"Total visited nodes: {len(visited)}")
    print(f"Total number of friends: {friends}")
    # Total visited nodes: 3_217
    # Total number of friends: 82_086
