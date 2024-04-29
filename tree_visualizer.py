from random_tree import *

import networkx as nx
import matplotlib.pyplot as plt

from time import sleep

def get_adj_list(G):
    adj = [[] for node in G.nodes()]
    for (u, v) in G.edges():
        adj[u].append(v)
        adj[v].append(u)

    return adj

def gen_graph(adj):
    G = nx.Graph()
    for i in range(len(adj)):
        G.add_node(i)
        
    for i in range(len(adj)):
        for node in adj[i]:
            G.add_edge(i, node)
            
    return G
            
#Generates a random spanning tree of a connected graph G, taken in as an adjacency list
def visualize_tree(G, filename='fig'):
    nx.draw(gen_graph(gen_tree(G)), node_color="blue", edge_color="green", node_size=10)
    
    plt.savefig(filename)
    plt.clf()