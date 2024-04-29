from random import randint

#Uniformly choose a vertex adjacent to v on graph G
def rand_vertex(G, v):
    return G[v][randint(0, len(G[v]) - 1)]
    

#Generates a random spanning tree of a connected graph G, taken in as an adjacency list
def gen_tree(G):
    root = 0
    T = [[] for i in range(len(G))]
    
    for v in range(len(G)):
        if T[v] or v == root:
            continue
        
        walk = [v]
        
        while not T[walk[-1]] and walk[-1] != root:
            walk.append(rand_vertex(G, walk[-1]))
            
        rightmost = {}
        for i in range(len(walk) - 1, -1, -1):
            if walk[i] not in rightmost:
                rightmost[walk[i]] = i
            
        prev = 0
        curr = max(1, rightmost[walk[prev]] + 1)      

        while curr < len(walk):
            if curr != rightmost[walk[curr]]:
                curr = rightmost[walk[curr]] + 1
            
            T[walk[prev]].append(walk[curr])
            T[walk[curr]].append(walk[prev])
            
            prev = curr
            curr += 1
            
    return T
        