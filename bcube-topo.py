"""
BCube Topology - A server-centric data center topology specifically focused on Shipping container based modular data centers.
The BCube paper says its a recursive structure. But IMHO, it is not. The network devices layout can be derived recursively, but the connections are all converging to the final hosts level.
author: Narendran Thangarajan (narendran.thangarajan@gmail.com)
"""

from mininet.topo import Topo, Node

N = 4
L = 1
pref = ()
subBCubeCount = -1
subBCubeCountDict = {}
switches = {}
hosts = {}

class BCubeTopo (Topo) :

	"BCube Topo - The buildBCube function gets a level and a prefix"

	def buildBCube(self,prefix,level):
		if level == 0:
			switchPrefix = (level,)
			switchPrefix = switchPrefix.__add__(prefix)
			switchPrefix = switchPrefix.__add__((0,))
			switches[switchPrefix] = self.getUID(switchPrefix) + 10000
			self.add_node(switches[switchPrefix], Node(is_switch=True))
			print switchPrefix
			print " Level 0 switch created"

			" Hosts creation "
			for i in xrange(0,N):
				hostPrefix = (192,subBCubeCount, subBCubeCountDict[subBCubeCount],)
				subBCubeCountDict[subBCubeCount] = subBCubeCountDict[subBCubeCount] + 1
				hosts[hostPrefix] = self.getUID(hostPrefix)
				self.add_node(hosts[hostPrefix], Node(is_switch=False))
				self.add_edge(switches[switchPrefix],hosts[hostPrefix])

			return

		"Create N^level switches"
		for i in xrange(0,pow(N,level)):
			switchPrefix = (level,)
			switchPrefix = switchPrefix.__add__(prefix)
			switchPrefix = switchPrefix.__add__((i,))
			# print "Creating level " + str(level) + "switch "
			# print switchPrefix
			switches[switchPrefix] = self.getUID(switchPrefix) + 10000
			self.add_node(switches[switchPrefix], Node(is_switch=True))

		" Recursively create lower level BCubes "
		for i in xrange(0,N):
			if level == L:
				global subBCubeCount
				subBCubeCount = subBCubeCount + 1
				subBCubeCountDict[subBCubeCount] = 0
			self.buildBCube(prefix.__add__((i,)),level-1)

		" Network connections "
		for i in xrange(0,N):
			for j in xrange(0,subBCubeCount):
				for k in xrange(0,pow(N,L),pow(N,level)):
					lookupPrefix = (level,)
					lookupPrefix = lookupPrefix.__add__(prefix)
					lookupPrefix = lookupPrefix.__add__((i,))
					self.add_edge(switches[lookupPrefix],hosts[(192,j,k)])



	""" Function to calculate the UID given the prefix """
	def getUID(self,prefix):
		uid = 0
		i = 0
		revprefix = prefix[::-1]
		for value in revprefix :
			if i == 0:
				uid = uid + value
			else :
				uid = uid + (value * 100 * i)
			i = i + 1
		return uid

	def __init__(self,enable_all=True):
		"Call Super constructor"
		super(BCubeTopo,self).__init__();
		self.buildBCube(pref,L)
		self.enable_all();


"The following line allows users to pass --topo bcubetopo from command line"
topos = { "bcubetopo" : (lambda :BCubeTopo())}

if __name__ == "__main__":
 	bcube = BCubeTopo()