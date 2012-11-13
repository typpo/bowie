#!/usr/bin/env python
import networkx as nx
import difflib
import json
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

def lookup(query):
  matches = difflib.get_close_matches(query, G.nodes())
  if len(matches) < 0:
    return json.dumps({'success': False, 'reason': "Couldn't find this artist"})
  try:
    path = shortest_path(G, matches[0], 'david-bowie')
  except:
    return json.dumps({'success': False, 'reason': "Couldn't find a path"})

  return json.dumps({'success': True, 'path': path})

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

if __name__ == "__main__":
  while True:
    ask()
