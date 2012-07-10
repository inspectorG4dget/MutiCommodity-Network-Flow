'''
Created on Dec 5, 2011

@author: ashwin
'''
class Edge:
	_ID = 1
	def __init__(self, u, v, w, c,f=0):
		self.id = self._ID; self.__class__._ID += 1
		self.src = u
		self.dest = v
		self.weight = w
		self.capacity = c
		self.flow = f
		
	def __eq__(self, e):
		return self.id == e.id
		
	def __ne__(self, e):
		return self.id != e.id

	def __contains__(self, v):
		if type(v) == int:
			return self.src.id == v or self.dest.id == v
		else:
			return self.src == v or self.dest == v
	
	def __str__(self):
		return str(self.id)
	
	def __repr__(self):
		return str(self.id)
	
	def __hash__(self):
		return self.id
	
class Node:
	_ID = 0
	def __init__(self, t=None):
		self.residents = t if t else set()
		self.id = self._ID; self.__class__._ID += 1
	
	def __eq__(self, n):
		if type(n) == int:
			return self.id == n
		else:
			return self.id == n.id
	
	def __ne__(self, n):
		if type(n) == int:
			return self.id != n
		else:
			return self.id != n.id
	
	def __str__(self):
		return str(self.id)
	
	def __repr__(self):
		return str(self.id)
	
	def __hash__(self):
		return self.id

def datagen():
	V, E = set(), set()
	PATHS = {}
	
	################################################
	# ADDING ALL VERTICES
	################################################
	
	V.add(Node())				# node 0
	V.add(Node(range(0 , 9)))	# node 1
	V.add(Node(range(9 , 17)))	# node 2
	V.add(Node(range(17 , 29)))	# node 3
	V.add(Node(range(29 , 41)))	# node 4
	V.add(Node(range(41 , 55)))	# node 5
	V.add(Node(range(55 , 63)))	# node 6
	V.add(Node(range(63 , 67)))	# node 7
	V.add(Node(range(67 , 83)))	# node 8
	V.add(Node(range(83 , 89)))	# node 9
	V.add(Node(range(89 , 99)))	# node 10
	V.add(Node(range(99 , 129)))	# node 11
	V.add(Node(range(129 , 144)))	# node 12
	V.add(Node(range(144 , 153)))	# node 13
	V.add(Node(range(153 , 155)))	# node 14
	V.add(Node(range(155 , 157)))	# node 15
	V.add(Node(range(157 , 166)))	# node 16
	V.add(Node(range(166 , 178)))	# node 17
	V.add(Node(range(178 , 180)))	# node 18
	V.add(Node(range(180 , 195)))	# node 19
	V.add(Node(range(195 , 209)))	# node 20
	V.add(Node(range(209 , 221)))	# node 21
	V.add(Node(range(221 , 225)))	# node 22
	V.add(Node(range(225 , 231)))	# node 23
	
	for i in xrange(51): V.add(Node())	# the rest of the 74 nodes
	NODES = dict(((v.id, v) for v in V))
	for i in [41, 42, 43]: NODES.pop(i)
	
	inf = sum((len(v.residents) for v in V))
	
	################################################
	# ADDING ALL EDGES
	################################################
	
	E.add(Edge(NODES[1], NODES[2], 1, inf, 0))	# edge 1
	E.add(Edge(NODES[1], NODES[2], 1, inf, 0))	# edge 2
	E.add(Edge(NODES[1], NODES[2], 1, inf, 0))	# edge 3
	E.add(Edge(NODES[1], NODES[27], 4, 32, 0))	# edge 4
	E.add(Edge(NODES[2], NODES[24], 2, 32, 0))	# edge 5
	E.add(Edge(NODES[24], NODES[25], 3, 32, 0))	# edge 6
	E.add(Edge(NODES[25], NODES[26], 1, 32, 0))	# edge 7
	E.add(Edge(NODES[25], NODES[28], 2, 32, 0))	# edge 8
	E.add(Edge(NODES[27], NODES[28], 4, 32, 0))	# edge 9
	E.add(Edge(NODES[26], NODES[29], 3, 32, 0))	# edge 10
	E.add(Edge(NODES[28], NODES[29], 2, 32, 0))	# edge 11
	E.add(Edge(NODES[29], NODES[30], 1, 32, 0))	# edge 12
	E.add(Edge(NODES[30], NODES[5], 3, 32, 0))	# edge 13
	E.add(Edge(NODES[30], NODES[31], 5, 32, 0))	# edge 14
	E.add(Edge(NODES[31], NODES[32], 4, 32, 0))	# edge 15
	E.add(Edge(NODES[31], NODES[7], 1, 32, 0))	# edge 16
	E.add(Edge(NODES[32], NODES[6], 7, 32, 0))	# edge 17
	E.add(Edge(NODES[6], NODES[7], 2, inf, 0))	# edge 18
	E.add(Edge(NODES[6], NODES[5], 3, inf, 0))	# edge 19
	E.add(Edge(NODES[6], NODES[5], 3, inf, 0))	# edge 20
	E.add(Edge(NODES[29], NODES[33], 5, 31, 0))	# edge 21
	E.add(Edge(NODES[33], NODES[32], 4, 31, 0))	# edge 22
	E.add(Edge(NODES[32], NODES[44], 1, 31, 0))	# edge 23
	E.add(Edge(NODES[33], NODES[34], 5, 31, 0))	# edge 24
	E.add(Edge(NODES[33], NODES[40], 15, 31, 0))	# edge 25
	E.add(Edge(NODES[34], NODES[8], 1, 31, 0))	# edge 26
	E.add(Edge(NODES[34], NODES[35], 5, 40, 0))	# edge 27
	E.add(Edge(NODES[35], NODES[38], 6, 40, 0))	# edge 28
	E.add(Edge(NODES[35], NODES[3], 5, 30, 0))	# edge 29
	E.add(Edge(NODES[3], NODES[36], 10, 30, 0))	# edge 30
	E.add(Edge(NODES[3], NODES[4], 3, inf, 0))	# edge 31
	E.add(Edge(NODES[3], NODES[4], 3, inf, 0))	# edge 32
	E.add(Edge(NODES[36], NODES[37], 1, 30, 0))	# edge 33
	E.add(Edge(NODES[36], NODES[38], 3, 30, 0))	# edge 34
	E.add(Edge(NODES[38], NODES[47], 20, 40, 0))	# edge 35
	E.add(Edge(NODES[38], NODES[39], 4, 30, 0))	# edge 36
	E.add(Edge(NODES[39], NODES[40], 3, 30, 0))	# edge 37
	E.add(Edge(NODES[33], NODES[40], 10, 30, 0))	# edge 38
	E.add(Edge(NODES[40], NODES[45], 15, 30, 0))	# edge 39
	E.add(Edge(NODES[9], NODES[10], 2, inf, 0))	# edge 40
	E.add(Edge(NODES[9], NODES[10], 2, inf, 0))	# edge 41
	E.add(Edge(NODES[9], NODES[44], 1, 30, 0))	# edge 42
	E.add(Edge(NODES[44], NODES[11], 30, 40, 0))	# edge 43
	E.add(Edge(NODES[10], NODES[45], 3, 30, 0))	# edge 44
	E.add(Edge(NODES[10], NODES[11], 11, inf, 0))	# edge 45
	E.add(Edge(NODES[45], NODES[49], 20, 30, 0))	# edge 46
	E.add(Edge(NODES[37], NODES[46], 20, 30, 0))	# edge 47
	E.add(Edge(NODES[46], NODES[54], 15, 30, 0))	# edge 48
	E.add(Edge(NODES[47], NODES[54], 15, 40, 0))	# edge 49
	E.add(Edge(NODES[48], NODES[49], 10, 50, 0))	# edge 50
	E.add(Edge(NODES[48], NODES[53], 15, 50, 0))	# edge 51
	E.add(Edge(NODES[49], NODES[50], 7, 30, 0))	# edge 52
	E.add(Edge(NODES[49], NODES[11], 5, 40, 0))	# edge 53
	E.add(Edge(NODES[11], NODES[50], 4, 32, 0))	# edge 54
	E.add(Edge(NODES[50], NODES[51], 7, 32, 0))	# edge 55
	E.add(Edge(NODES[54], NODES[0], 1, 90, 0))	# edge 56
	E.add(Edge(NODES[0], NODES[55], 5, 30, 0))	# edge 57
	E.add(Edge(NODES[0], NODES[56], 1, 90, 0))	# edge 58
	E.add(Edge(NODES[0], NODES[53], 3, 110, 0))	# edge 59
	E.add(Edge(NODES[53], NODES[57], 2, 70, 0))	# edge 60
	E.add(Edge(NODES[57], NODES[58], 5, 30, 0))	# edge 61
	E.add(Edge(NODES[53], NODES[52], 15, 50, 0))	# edge 62
	E.add(Edge(NODES[52], NODES[51], 15, 50, 0))	# edge 63
	E.add(Edge(NODES[51], NODES[59], 20, 30, 0))	# edge 64
	E.add(Edge(NODES[59], NODES[60], 3, 30, 0))	# edge 65
	E.add(Edge(NODES[60], NODES[13], 5, 30, 0))	# edge 66
	E.add(Edge(NODES[59], NODES[61], 10, 35, 0))	# edge 67
	E.add(Edge(NODES[58], NODES[12], 1, 30, 0))	# edge 68
	E.add(Edge(NODES[58], NODES[62], 5, 30, 0))	# edge 69
	E.add(Edge(NODES[62], NODES[63], 3, 30, 0))	# edge 70
	E.add(Edge(NODES[56], NODES[63], 10, 70, 0))	# edge 71
	E.add(Edge(NODES[63], NODES[19], 10, 60, 0))	# edge 72
	E.add(Edge(NODES[55], NODES[64], 5, 30, 0))	# edge 73
	E.add(Edge(NODES[64], NODES[65], 10, 30, 0))	# edge 74
	E.add(Edge(NODES[64], NODES[70], 10, 30, 0))	# edge 75
	E.add(Edge(NODES[65], NODES[66], 4, 30, 0))	# edge 76
	E.add(Edge(NODES[66], NODES[67], 5, 30, 0))	# edge 77
	E.add(Edge(NODES[67], NODES[68], 1, 30, 0))	# edge 78
	E.add(Edge(NODES[68], NODES[69], 4, 30, 0))	# edge 79
	E.add(Edge(NODES[69], NODES[17], 5, 30, 0))	# edge 80
	E.add(Edge(NODES[70], NODES[16], 1, 30, 0))	# edge 81
	E.add(Edge(NODES[70], NODES[18], 9, 30, 0))	# edge 82
	E.add(Edge(NODES[16], NODES[18], 1, inf, 0))	# edge 83
	E.add(Edge(NODES[16], NODES[18], 1, inf, 0))	# edge 84
	E.add(Edge(NODES[18], NODES[19], 3, inf, 0))	# edge 85
	E.add(Edge(NODES[19], NODES[71], 5, 40, 0))	# edge 86
	E.add(Edge(NODES[71], NODES[74], 5, 40, 0))	# edge 87
	E.add(Edge(NODES[74], NODES[22], 7, 30, 0))	# edge 88
	E.add(Edge(NODES[22], NODES[23], 2, inf, 0))	# edge 89
	E.add(Edge(NODES[71], NODES[20], 5, 30, 0))	# edge 90
	E.add(Edge(NODES[20], NODES[74], 5, 35, 0))	# edge 91
	E.add(Edge(NODES[20], NODES[21], 1, inf, 0))	# edge 92
	E.add(Edge(NODES[20], NODES[21], 1, inf, 0))	# edge 93
	E.add(Edge(NODES[21], NODES[73], 10, 30, 0))	# edge 94
	E.add(Edge(NODES[73], NODES[22], 5, 30, 0))	# edge 95
	E.add(Edge(NODES[73], NODES[23], 2, 30, 0))	# edge 96
	E.add(Edge(NODES[13], NODES[61], 2, 30, 0))	# edge 97
	E.add(Edge(NODES[61], NODES[72], 7, 30, 0))	# edge 98
	E.add(Edge(NODES[72], NODES[15], 2, 30, 0))	# edge 99
	E.add(Edge(NODES[72], NODES[14], 1, 30, 0))	# edge 100
	E.add(Edge(NODES[13], NODES[14], 5, inf, 0))	# edge 101
	E.add(Edge(NODES[14], NODES[15], 1, inf, 0))	# edge 102
	E.add(Edge(NODES[4], NODES[36], 1, 30, 0))	# edge 103
	E.add(Edge(NODES[16], NODES[17], 3, inf, 0))	# edge 104
	E.add(Edge(NODES[5], NODES[7], 2, inf, 0))	# edge 105
	
	EDGES = dict(((e.id, e) for e in E))
	
	################################################
	# ADDING ALL PATHS
	################################################
	
	p = [(0,54), (54,47), (47,38), (38,35), (35,34), (34,33), (33,29), (29,28), (28,27), (27,1)]
	for i in range(9): PATHS[i] = p[:]	# everyone in neighborhood 1
	
	p = [(0,54), (54,47), (47,38), (38,35), (35,34), (34,33), (33,29), (29,28), (28,25), (25,24), (24,2)]
	for i in range(9, 17): PATHS[i] = p[:]	# everyone in neighborhood 2
	
	p = [(0,54), (54,46), (46,37), (37,36), (36,3)]
	for i in range(17 , 29): PATHS[i] = p[:]	# everyone in neighborhood 3
	
	p = [(0,54), (54,46), (46,37), (37,36), (36,4)]
	for i in range(29 , 41): PATHS[i] = p[:]	# everyone in neighborhood 4
	
	p = [(0,53), (53,48), (48,49), (49,11), (11,44), (44,32), (32,6), (6,5)]
	for i in range(41 , 55): PATHS[i] = p[:]	# everyone in neighborhood 5
	
	p = [(0,53), (53,48), (48,49), (49,11), (11,44), (44,32), (32,6)]
	for i in range(55 , 63): PATHS[i] = p[:]	# everyone in neighborhood 6
	
	p = [(0,53), (53,48), (48,49), (49,11), (11,44), (44,32), (32,31), (31,7)]
	for i in range(63 , 67): PATHS[i] = p[:]	# everyone in neighborhood 7
	
	p = [(0,54), (54,47), (47,38), (38,35), (35,34), (34,8)]
	for i in range(67 , 83): PATHS[i] = p[:]	# everyone in neighborhood 8
	
	p = [(0,53), (53,48), (48,49), (49,11), (11,44), (44,9)]
	for i in range(83 , 89): PATHS[i] = p[:]	# everyone in neighborhood 9
	
	p = [(0,53), (53,48), (48,49), (49,45), (45,10)]
	for i in range(89 , 99): PATHS[i] = p[:]	# everyone in neighborhood 10
	
#	p = [(0,53), (53,48), (48,49), (49,11)]
	p = [(0,53), (53,48), (48,49), (49,50), (50,11)]
	for i in range(99 , 129): PATHS[i] = p[:]	# everyone in neighborhood 11
	
	p = [(0,53), (53,57), (57,58), (58,12)]
	for i in range(129 , 144): PATHS[i] = p[:]	# everyone in neighborhood 12
	
	p = [(0,53), (53,52), (52,51), (51,59), (59,61), (61,13)]
	for i in range(144 , 153): PATHS[i] = p[:]	# everyone in neighborhood 13
	
	p = [(0,53), (53,52), (52,51), (51,59), (59,61), (61,72), (72,14)]
	for i in range(153 , 155): PATHS[i] = p[:]	# everyone in neighborhood 14
	
	p = [(0,53), (53,52), (52,51), (51,59), (59,61), (61,72), (72,15)]
	for i in range(155 , 157): PATHS[i] = p[:]	# everyone in neighborhood 15
	
	p = [(0,55), (55,64), (64,70), (70,16)]
	for i in range(157 , 166): PATHS[i] = p[:]	# everyone in neighborhood 16
	
	p = [(0,55), (55,64), (64,65), (65,66), (66,67), (67,68), (68,69), (69,17)]
	for i in range(166 , 178): PATHS[i] = p[:]	# everyone in neighborhood 17
	
	p = [(0,55), (55,64), (64,70), (70,18)]
	for i in range(178 , 180): PATHS[i] = p[:]	# everyone in neighborhood 18
	
	p = [(0,56), (56,63), (63,19)]
	for i in range(180 , 195): PATHS[i] = p[:]	# everyone in neighborhood 19
	
	p = [(0,56), (56,63), (63,19), (19,71), (71,20)]
	for i in range(195 , 209): PATHS[i] = p[:]	# everyone in neighborhood 20
	
	p = [(0,56), (56,63), (63,19), (19,71), (71,74), (74,22), (22,73), (73,21)]
	for i in range(209 , 221): PATHS[i] = p[:]	# everyone in neighborhood 21
	
	p = [(0,56), (56,63), (63,19), (19,71), (71,74), (74,22)]
	for i in range(221 , 225): PATHS[i] = p[:]	# everyone in neighborhood 22
	
	p = [(0,56), (56,63), (63,19), (19,71), (71,74), (74,22), (22,23)]
	for i in range(225 , 231): PATHS[i] = p[:]	# everyone in neighborhood 23
	
	for k,path in PATHS.iteritems():
		PATHS[k] = [findedge(i, E) for i in path]
		
	for k,path in PATHS.iteritems():
		for edge in path:
			edge.flow += 1
	
	return V, E, PATHS, inf

def findedge(e, E):
#	print e	##
	answer = max((i for i in E if e[0] in i and e[1] in i))
	return answer

if __name__ == "__main__":
	V, E, paths, inf = datagen()
	print sorted((e.weight for e in filter(lambda x: x.capacity==inf, E)))
