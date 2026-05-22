# Final Skeleton
#
# Hints:
#
# To check the source and destination of an IP packet, you can use
# the header information... For example:
#
# ip_header = packet.find('ipv4')
#
# if ip_header.srcip == "1.1.1.1":
#   print "Packet is from 1.1.1.1"
#
# Important Note: the "is" comparison DOES NOT work for IP address
# comparisons in this way. You must use ==.
# 
# To send an OpenFlow Message telling a switch to send packets out a
# port, do the following, replacing <PORT> with the port number the 
# switch should send the packets out:
#
#    msg = of.ofp_flow_mod()
#    msg.match = of.ofp_match.from_packet(packet)
#    msg.idle_timeout = 30
#    msg.hard_timeout = 30
#
#    msg.actions.append(of.ofp_action_output(port = <PORT>))
#    msg.data = packet_in
#    self.connection.send(msg)
#
# To drop packets, simply omit the action.
#

from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

class Final (object):
  """
  A Firewall object is created for each switch that connects.
  A Connection object for that switch is passed to the __init__ function.
  """
  def __init__ (self, connection):
    # Keep track of the connection to the switch so that we can
    # send it messages!
    self.connection = connection

    # This binds our PacketIn event listener
    connection.addListeners(self)

  def do_final (self, packet, packet_in, port_on_switch, switch_id):
    # This is where you'll put your code. 
    #   - port_on_switch: represents the port that the packet was received on.
    #   - switch_id represents the id of the switch that received the packet.
    #      (for example, s1 would have switch_id == 1, s2 would have switch_id == 2, etc...)
    # You should use these to determine where a packet came from. To figure out where a packet 
    # is going, you can use the IP header information.

    # get headers
    ip_packet = packet.find('ipv4')
    icmp_packet = packet.find('icmp')
    
    # handle non-IP traffic
    if ip_packet is None:
        msg = of.ofp_packet_out()
        msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
        msg.data = packet_in
        msg.in_port = port_on_switch
        self.connection.send(msg)
        return

    # get source and destination IPs
    src_ip = str(ip_packet.srcip)
    dst_ip = str(ip_packet.dstip)

    # prevent h4 from sending ICMP to trusted hosts
    # for some reason it is blocking all packets not just icmp but i have no clue why
    if src_ip == "123.45.67.89" and icmp_packet is not None:
        print("Dropping ICMP from h4 to trusted hosts")
        msg = of.ofp_flow_mod()
        msg.match = of.ofp_match.from_packet(packet)
        msg.idle_timeout = 30
        msg.hard_timeout = 30
        self.connection.send(msg)
        return

    # prevent h4 from sending anything to server
    if src_ip == "123.45.67.89" and dst_ip == "10.5.5.50":
        print("Dropping IP from h4 to server")
        msg = of.ofp_flow_mod()
        msg.match = of.ofp_match.from_packet(packet)
        msg.idle_timeout = 30
        msg.hard_timeout = 30
        self.connection.send(msg)
        return

    # flow table rules
    flow_table = {
        1: {'10.1.1.10': 1, 'default': 2}, # s1
        2: {'10.2.2.20': 1, 'default': 2}, # s2
        3: {'10.3.3.30': 1, 'default': 2}, # s3
        4: {'10.5.5.50': 1, 'default': 2}, # s4
        5: { # s5
            '10.1.1.10': 2,
            '10.2.2.20': 3,
            '10.3.3.30': 4,
            '123.45.67.89': 5,
            '10.5.5.50': 1,
            'default': None
        }
    }

    # get output port from flow table
    switch_table = flow_table.get(switch_id, {})
    out_port = switch_table.get(dst_ip, switch_table.get('default'))

    # handle unknown destination IP
    if out_port is None:
        print("No rule for this dst IP; dropping")
        return

    # send packet!
    msg = of.ofp_flow_mod()
    msg.match = of.ofp_match.from_packet(packet)
    msg.idle_timeout = 30
    msg.hard_timeout = 30
    msg.actions.append(of.ofp_action_output(port=out_port))
    msg.data = packet_in
    self.connection.send(msg)


  def _handle_PacketIn (self, event):
    """
    Handles packet in messages from the switch.
    """
    packet = event.parsed # This is the parsed packet data.
    if not packet.parsed:
      log.warning("Ignoring incomplete packet")
      return

    try:
      packet_in = event.ofp # The actual ofp_packet_in message.
      self.do_final(packet, packet_in, event.port, event.dpid)
    except Exception as e:
      log.warning("Error in do_final: %s", str(e))

def launch ():
  """
  Starts the component
  """
  def start_switch (event):
    log.info("Controlling %s" % (event.connection,))
    Final(event.connection)
  core.openflow.addListenerByName("ConnectionUp", start_switch)