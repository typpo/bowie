#!/usr/bin/env python
import networkx as nx
from networkx import shortest_path, average_shortest_path_length
from networkx.exception import NetworkXNoPath

GRAPH_FILE = 'full2.dat'
CONTEMP_FILE = 'full_contemp2.dat'

G = nx.DiGraph()

for line in open(GRAPH_FILE):
  parts = line.replace('\n', '').split('|')
  if len(parts) != 2:
    continue
  influencer = parts[0]
  influence = parts[1]

  # edge pointing to influencer
  G.add_edge(influence, influencer, weight=2)

for line in open(CONTEMP_FILE):
  parts = line.replace('\n', '').split('|')
  if len(parts) != 2:
    continue
  influencer = parts[0]
  influence = parts[1]

  # edge pointing to contemp
  G.add_edge(influence, influencer, weight=1)


print len(G), 'nodes'

def ask():
  q = raw_input('Enter an artist: ')
  target = 'david-bowie'

  if q not in G:
    print 'Not in graph'
    return

  # Graph is not connected
  #print average_shortest_path_length(G)
  try:
    print shortest_path(G, q, target)
  except:
    print 'no path :('

while True:
  ask()
