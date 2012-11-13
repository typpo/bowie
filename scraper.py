#!/usr/bin/env python

import urllib
from collections import deque
from bs4 import BeautifulSoup

URL_FORMAT = 'http://www.rhapsody.com/artist/%s/similar-artists'
START_POINT = 'david-bowie'
REVERSE_START_POINTS = [
    'lady-gaga', 'kesha', 'far*east-movement', 'dev', 'taylor-swift', 'justin-bieber',
    'nicki-minaj', 'kanye-west', 'jay-z', 'katy-perry', 'one-direction', 'rihanna',
    'adele', 'david-guetta', 'beyonce', 'bruno-mars', 'jessie-j', 'alicia-keys',
    'amy-winehouse', 'queen', 'scissor-sisters', 'panic-at-the-disco', 'the-killers',
    'muse', 'chris-brown', 'cee-lo-green', 'weezer', 'coldplay', 'drake', 'lil-b'
]
OUTPUT = 'graph.dat'
REVERSE_MODE = True

def create_url(slug):
  return URL_FORMAT % slug

def append_link(influencer, influenced):
  f = open(OUTPUT, 'a')
  f.write(('%s|%s\n') % (influencer, influenced))
  f.close()

if REVERSE_MODE:
  Q = deque(REVERSE_START_POINTS)
else:
  Q = deque([START_POINT])

visited = set()

while len(Q) > 0:
  slug = Q.popleft()
  if slug in visited:
    continue
  visited.add(slug)
  print slug, '...'
  soup = BeautifulSoup(urllib.urlopen(create_url(slug)).read())

  if REVERSE_MODE:
    influences_section = soup.find('h4', {'class': 'artist-headers'}, text='Influences')
    if not influences_section:
      print '\t no influences'
      continue

    ilist = influences_section.findNext('ul')
    for x in ilist.findAll('a'):
      influence = x['href'].replace('/artist/', '')
      append_link(influence, slug)
      Q.append(influence)
  else:
    followers_section = soup.find('h4', {'class': 'artist-headers'}, text='Followers')
    if not followers_section:
      print '\t no followers'
      continue

    flist = followers_section.findNext('ul')
    for x in flist.findAll('a'):
      follower = x['href'].replace('/artist/', '')
      append_link(slug, follower)
      Q.append(follower)
