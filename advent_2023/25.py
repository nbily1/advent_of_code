raise Exception("part 2 not solved")

# %% 1
import pandas as pd
import networkx as nx
from pyvis.network import Network

raw = []

with open("advent_2023/25.txt", "r") as file:
    raw = [x.strip() for x in file if x.strip() != ""]

# print(raw)

conns = {}

conns1 = {"Source": [], "Target": [], "Type": [], "weight": []}

for x in raw:
    src = x.split(": ")[0]
    trgt = [y for y in x.split(": ")[1].split()]
    # conns[src] = trgt.copy()
    for t in trgt:
        conns1["Source"] += [src]
        conns1["Type"] += ["Undirected"]
        conns1["weight"] += ["1"]
    conns1["Target"] += trgt

# print(conns)
# print(conns1)

df = pd.DataFrame(conns1)

df = df[(df.Source != "jct") | (df.Target != "rgv")]
df = df[(df.Source != "rgv") | (df.Target != "jct")]
df = df[(df.Source != "krf") | (df.Target != "crg")]
df = df[(df.Source != "crg") | (df.Target != "krf")]
df = df[(df.Source != "fmr") | (df.Target != "zhg")]
df = df[(df.Source != "zhg") | (df.Target != "fmr")]

# Got these from analyzing the drawn network
# jct -> rgv
# krf -> crg
# fmr -> zhg

c = nx.from_pandas_edgelist(df, source="Source", target="Target", edge_attr="weight")

net = Network(notebook=False)
net.from_nx(c)
# net.generate_html("network.html")
# net.write_html("network.html")
# net.show("network.html")

# Generate connected components and select the largest:
largest_component = max(nx.connected_components(c), key=len)

# Create a subgraph of G consisting only of this component:
c2 = c.subgraph(largest_component)

print(c.order())
print(c2.order())
print(c.order() - c2.order())
print((c.order() - c2.order()) * c2.order())
