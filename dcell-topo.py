"""
DCell Topology
author: Narendran Thangarajan (narendran.thangarajan@gmail.com)
"""

from mininet.topo import Topo, Node

LEVEL = 1
N = 4
pref = (198,)
nodes = {}
hosts = {}
class DCellTopo (Topo) :
	
	"DCell Topology - Main function gets a network prefix and level"

	def getT(self,level):
		if level==0 :
			return N;
		x = self.getT(level-1);
		return (x+1)*x;

	def getG(self,level):
		if level==0 :
			return 1;
		return 1+self.getT(level-1);
	
	def buildDCells(self,prefix, l):

		"If level is 0, return create the DCell0"
		if l==0:
			" Create the DCell0 switch"
			"TODO modularize node creation"
			print prefix
			print " Dcell0 in progress"
			nodes[prefix] = self.getUID(prefix) + 10000
			self.add_node(nodes[prefix], Node(is_switch=True))
			" Create the DCell nodes"
			for i in xrange(0,N):
				newprefix = prefix.__add__((i,))
				" Converting a host into a host+switch combo to mock routing in hosts in DCell topology "
				nodes[newprefix] = self.getUID(newprefix) + 20000
				self.add_node(nodes[newprefix], Node(is_switch=True))
				self.add_edge(nodes[prefix],nodes[newprefix])
				hosts[newprefix] = self.getUID(newprefix)
				self.add_node(hosts[newprefix], Node(is_switch=False))
				self.add_edge(nodes[newprefix],hosts[newprefix])
				print newprefix
				print " Server in progress"
			return

		"If level not zero, create Gl number of DCell(l-1)s"
		for i in xrange(0,self.getG(l)):
			self.buildDCells(pref.__add__((i,)),l-1)

		"Connect node[i,j-1] to [j,i]"
		for i in xrange(0,self.getT(l-1)):
			for j in xrange(i+1,self.getG(l)):
				self.add_edge(nodes[pref.__add__((i,)).__add__((j-1,))],nodes[pref.__add__((j,)).__add__((i,))])
					

	def getUID(self,prefix):
		uid = 0
		i = 0
		revprefix = prefix[::-1]
		for value in revprefix :
			if i==LEVEL+1:
				break
			if i == 0:
				uid = uid + value
			else :
				uid = uid + (value * self.getT(i-1))
			i = i + 1
		return uid

	def __init__(self,enable_all=True):
		"Call Super constructor"
		super(DCellTopo,self).__init__();
		self.buildDCells(pref,LEVEL)
		self.enable_all();
		# print self.getG(3);



"The following line allows users to pass --topo myringtopo from command line"
topos = { "dcelltopo" : (lambda :DCellTopo())}

# if __name__ == "__main__":
# 	dcell = DCellTopo()
