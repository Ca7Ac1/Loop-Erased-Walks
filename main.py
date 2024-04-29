from random_tree import *
from tree_visualizer import *

def sample_square():
    G = [[1, 2], [0, 3], [0, 3], [1, 2]]

    a = 0
    b = 0
    c = 0
    d = 0

    for i in range(100000):
        T = gen_tree(G)
        
        if 1 not in T[0]:
            a += 1
        elif 2 not in T[0]:
            b += 1
        elif 1 not in T[3]:
            c += 1
        elif 2 not in T[3]:
            d += 1
            
    print(f"{a}, {b}, {c}, {d}")
    
def sample_complete(n):
    G = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                G[i].append(j)    
      
    for i in range(1000):
        visualize_tree(G, f'figs/fig{i}')
            
def sample_petereson():
    for i in range(10):
        visualize_tree(get_adj_list(nx.petersen_graph()), f'figs3/fig{i}')

sample_complete(10000)
# sample_petereson()