#!/usr/bin/env python
import math,sys
import json
import urllib

def gsearch(searchfor):
  query = urllib.urlencode({'q': searchfor})
  url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
  search_response = urllib.urlopen(url)
  search_results = search_response.read()
  results = json.loads(search_results)
  data = results['responseData']
  return data
  
args = sys.argv[1:]
m = 45000000000
if len(args) != 2:
        print "need two words as arguments"
        exit
n0 = int(gsearch(args[0])['cursor']['estimatedResultCount'])
n1 = int(gsearch(args[1])['cursor']['estimatedResultCount'])
n2 = int(gsearch(args[0]+" "+args[1])['cursor']['estimatedResultCount'])
l1 = max(math.log10(n0),math.log10(n1))-math.log10(n2)
l2 = math.log10(m)-min(math.log10(n0),math.log10(n1))
distance = l1/l2
print distance
