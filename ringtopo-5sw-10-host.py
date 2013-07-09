"""
Custom ring topology

author: Narendran Thangarajan (narendran.thangarajan@gmail.com)
"""

from mininet.topo import Topo, Node

class MyRingTopo (Topo) :
	"Simple Ring Topology with 5 switches and 2 hosts connected to each - A precursor to DCell"

	def __init__(self,enable_all=True):
		"Call Super constructor"
		super(MyRingTopo,self).__init__();

		"""
		Following is the topology (just the switches):
				
				1

			5		2

			4		3
		
		"""

		topSwitch = 1
		midRightSwitch = 2
		bottomRightSwitch = 3
		bottomLeftSwitch = 4
		midLeftSwitch = 5

		host1 = 1001
		host2 = 1002
		host3 = 1003
		host4 = 1004
		host5 = 1005
		host6 = 1006
		host7 = 1007
		host8 = 1008
		host9 = 1009
		host10 = 1010

		"Add nodes to topology"
		self.add_node(topSwitch, Node(is_switch=True))
		self.add_node(midRightSwitch, Node(is_switch=True))
		self.add_node(midLeftSwitch, Node(is_switch=True))
		self.add_node(bottomRightSwitch, Node(is_switch=True))
		self.add_node(bottomLeftSwitch, Node(is_switch=True))

		"Add hosts"
		self.add_node(host1, Node(is_switch=False))
		self.add_node(host2, Node(is_switch=False))
		self.add_node(host3, Node(is_switch=False))
		self.add_node(host4, Node(is_switch=False))
		self.add_node(host5, Node(is_switch=False))
		self.add_node(host6, Node(is_switch=False))
		self.add_node(host7, Node(is_switch=False))
		self.add_node(host8, Node(is_switch=False))
		self.add_node(host9, Node(is_switch=False))
		self.add_node(host10, Node(is_switch=False))

		"Add edges to nodes"
		self.add_edge(topSwitch,host1)
		self.add_edge(topSwitch,host2)

		self.add_edge(midRightSwitch,host3)
		self.add_edge(midRightSwitch,host4)

		self.add_edge(bottomRightSwitch,host5)
		self.add_edge(bottomRightSwitch,host6)

		self.add_edge(bottomLeftSwitch,host7)
		self.add_edge(bottomLeftSwitch,host8)

		self.add_edge(midLeftSwitch,host9)
		self.add_edge(midLeftSwitch,host10)

		"Ring connection of switches"

		self.add_edge(topSwitch,midRightSwitch)
		self.add_edge(midRightSwitch,bottomRightSwitch)
		self.add_edge(bottomRightSwitch,bottomLeftSwitch)
		self.add_edge(bottomLeftSwitch,midLeftSwitch)
		self.add_edge(midLeftSwitch,topSwitch)

		self.enable_all();



"The following line allows users to pass --topo myringtopo from command line"
topos = { "myringtopo" : (lambda : MyRingTopo())}