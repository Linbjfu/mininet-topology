from mininet.topo import Topo

class MyTopo( Topo ):

    def __init__( self ):

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        Host1 = self.addHost( 'h1' )
	Host3 = self.addHost( 'h3' )
	Host4 = self.addHost( 'h4' )
	Host5 = self.addHost( 'h5' )
	Host6 = self.addHost( 'h6' )
	Host7 = self.addHost( 'h7' )
	Host8 = self.addHost( 'h8' )

        Switch1 = self.addSwitch( 's1' )
	Switch2 = self.addSwitch( 's2' )
	Switch3 = self.addSwitch( 's3' )
	Switch4 = self.addSwitch( 's4' )
	Switch5 = self.addSwitch( 's5' )
	Switch6 = self.addSwitch( 's6' )
	Switch7 = self.addSwitch( 's7' )

        # Add links
	self.addLink( Switch1, Switch2 )
	self.addLink( Switch1, Switch3 )
	self.addLink( Switch2, Switch4 )
	self.addLink( Switch2, Switch5 )
	self.addLink( Switch3, Switch6 )
	self.addLink( Switch3, Switch7 )

        self.addLink( Host1, Switch4 )
        self.addLink( Host2, Switch4 )
	self.addLink( Host3, Switch5 )
	self.addLink( Host4, Switch5 )
	self.addLink( Host5, Switch6 )
	self.addLink( Host6, Switch6 )
	self.addLink( Host7, Switch7 )
	self.addLink( Host8, Switch7 )

topos = { 'mytopo': ( lambda: MyTopo() ) }
