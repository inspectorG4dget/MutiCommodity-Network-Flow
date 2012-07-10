'''
Created on Nov 29, 2011

@author: ashwin
'''

from Data import *
from random import choice as choose
from itertools import combinations as combos
from copy import deepcopy as clone
from time import sleep
from itertools import product as cross

class TabuList:
	def __init__(self, size):
		self.size = size
		self.list = []
	
	def __contains__(self, i):
		return i in self.list
	
	def add(self, e):
		self.list.insert(0, e)
		if len(self.list) > self.size:
			self.list.pop()


def routable(node, paths):
	for r in node.residents:
		if all((e.capacity - e.flow  > 0 for e in paths[r])):
			return True
	return False

#def reroute((V,E), paths, a, u, n):
#	''' Reroute agent a through node n to node u'''
#	best = '', None	# cost, path
#	for r in n.residents:
#		path = paths[r]
#		cost = sum((e.weight for e in path)) + min((e.weight for e in E if (u in e and n in e) ))
#		if cost < best[0]:
#			best = cost, path+[min((e for e in E if (u in e and n in e) ), key=lambda x : x.weight)]
#		
#		paths[a] = best[1]
#	return (V,E), paths, a, u, n

def getNeighbor((VV,EE), paths, dist, rerouts):
	""" rerouts = [(terminal node, rerouted through)]"""
#	print 'getNeighbor'	##
	V,E = clone(VV), clone(EE)
	u, n = None, None
	while u is None:
		try:
			us = [v for v in V if v.residents and (rerouts and v.id not in [r[0] for r in rerouts]) and \
															any( (e for e in E if v in e and e.capacity==inf and \
															routable(e.src if v==e.dest else e.dest, paths) and \
															e.weight <= dist) ) ]
			
			U = max(paths, key=lambda a: sum((e.weight for e in paths[a])) )
			for v in V:
				if U in v.residents:
					u = v
					break
			else:
				u = choose(us)
			
		except:
			u = None
	
	while not n:
		try:
			n = filter( lambda v: min( (e.weight for e in E if (v in e and u in e) ))  <= dist,
						(v for v in V if (u!=v and any(( (v in e and u in e and e.capacity==inf) for e in E)) )) )
		except: 
			n = False
	n = choose(n)
	ress = list(u.residents)
	r = choose(ress)
	u.residents = set(u.residents); u.residents.remove(r)
	n.residents = set(n.residents); n.residents.add(r)#; n.residents = set(n.residents)
	
	for edge in paths[r]:
		edge.flow -= 1
	
	p = min(( paths[_r] for _r in n.residents if all((e for e in paths[_r] if e.capacity-e.flow >0)) ), 
		key=lambda path: sum(edge.weight for edge in path) )
	for edge in p:
		edge.flow += 1
	paths[r] = p[:]
	paths[r].append(min((e for e in E if u in e and n in e), key=lambda e: e.weight))
	
#	(V,E), paths, r, u, n = reroute((clone(V),clone(E)), clone(paths), r, u, n)
	
	return (V,E), paths, u.id, n.id

def evaluate(paths):
	return sum((sum(e.weight for e in path) for path in paths))

def tabuSearch((V,E), PATHS, N, dist, T, CMAX, fpath):
	tabu = TabuList(T)
	answer = ''
	c, time = 0, ''
	n = (V,E)
	tabu.add(n)
#	with open(fpath, 'w') as f:
	with open('data.txt') as f:
		while c < CMAX:
			print c, '\t',
#			f.write("%s\t"%c)
			c += 1
			neighborhood = []
			reroutsched = []
			while len(neighborhood) < N:
#				print 'rerouts:', reroutsched	##
				(v,e),paths, u, uu = getNeighbor(n, clone(PATHS), dist, reroutsched)
					
				if paths not in tabu:
					neighborhood.append( ((v,e),paths) )
					reroutsched.append((u,uu))

			neighborhood.sort(key=lambda x: evaluate(x[1].values()))
			i = min((i for i in xrange(len(neighborhood)) if neighborhood[i] not in tabu))
			n,nn = clone(neighborhood[i])
			tabu.add(n)
			
			t = evaluate(nn.values())
			if t < time:
				answer = t
				time = answer
			print t, time	##
#			f.write("%s\t%s\n" %(t, time))
			
		return answer

if __name__ == "__main__":
	print 'starting'
	
	_Ns = [15]
	_dists = [5, 7, 9, 11]
	_T = 10
	_CMAX = 600
	
	for _N, _dist in cross(_Ns, _dists):
		print 'N%sD%sT%sC%s' %(_N, _dist, _T, _CMAX)
		V, E, PATHS, inf = datagen()
		fpath = 'data/N%s_D%s_T%s_C%s' %(_N, _dist, _T, _CMAX)
		answer = tabuSearch((V, E), PATHS, N=_N, dist=_dist, T=_T, CMAX=_CMAX, fpath=fpath)
		print "answer", answer
		E.pop().__class__._ID = 1
		V.pop().__class__._ID = 0
	print 'done'
