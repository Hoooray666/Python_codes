import numpy as np
import pandas as pd
import networkx as nx

edges = pd.DataFrame()
edges['sources'] = [1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]
edges['targets'] = [2, 4, 5, 3, 1, 2, 5, 1, 5, 1, 3, 4]
edges['weights'] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

G = nx.from_pandas_edgelist(edges, source='sources', target='targets', edge_attr='weights')
print(nx.degree(G))
#联通分量，最大联通子图
print(list(nx.connected_components(G)))

print(nx.diameter(G))
print(nx.degree_centrality(G))
print(nx.eigenvector_centrality(G))#特征向量中心性
print(nx.betweenness_centrality(G))
print(nx.closeness_centrality(G))
print(nx.pagerank(G))
print("\n")
print(nx.hits(G))

