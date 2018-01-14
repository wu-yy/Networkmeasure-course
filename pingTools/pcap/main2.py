# coding=gbk
import dpkt
import os
from dpkt.compat import  compat_ord
import socket
import datetime

#import pdb

#pdb.set_trace()
def mac_addr(address):
    """Convert a MAC address to a readable/printable string

       Args:
           address (str): a MAC address in hex form (e.g. '\x01\x02\x03\x04\x05\x06')
       Returns:
           str: Printable/readable MAC address
    """
    return ':'.join('%02x' % compat_ord(b) for b in address)

def inet_to_str(inet):
    """Convert inet object to a string

        Args:
            inet (inet struct): inet network address
        Returns:
            str: Printable/readable IP address
    """
    # First try ipv4 and then ipv6
    try:
        return socket.inet_ntop(socket.AF_INET, inet)
    except ValueError:
        return socket.inet_ntop(socket.AF_INET6, inet)

#读取cap文件
#cap_path = r'data\hs\BW000030_78-A3-51-00-00-30.cap'
cap_path = r'data\hs\fenxi-shuju-NotDone.pcapng'
for file in os.listdir(r'data'):
      #print 'list:' + file
      file_cap = open( cap_path,'rb')
      string_data = dpkt.pcap.Reader(file_cap)

      #对cap文件进行解析
      pkts_num = 0
      pkts_len = []
      dpktEth = dpkt.ethernet
      print string_data

      for Pkt in string_data:
            # Print out the timestamp in UTC
            print('Timestamp: ', str(datetime.datetime.utcfromtimestamp(Pkt[0])))

            '''
            eth = dpkt.ethernet.Ethernet(Pkt[1])
            #print('Ethernet Frame: ', mac_addr(eth.src), mac_addr(eth.dst), eth.type)

            # Make sure the Ethernet data contains an IP packet
            if not isinstance(eth.data, dpkt.ip.IP):
                  #print('Non IP Packet type not supported %s\n' % eth.data.__class__.__name__)
                  continue

                  # Now unpack the data within the Ethernet frame (the IP packet)
                  # Pulling out src, dst, length, fragment info, TTL, and Protocol
            ip = eth.data

                  # Pull out fragment information (flags and offset all packed into off field, so use bitmasks)
            do_not_fragment = bool(ip.off & dpkt.ip.IP_DF)
            more_fragments = bool(ip.off & dpkt.ip.IP_MF)
            fragment_offset = ip.off & dpkt.ip.IP_OFFMASK

                  # Print out the info
            print('IP: %s -> %s   (len=%d ttl=%d DF=%d MF=%d offset=%d)\n' % \
                        (inet_to_str(ip.src), inet_to_str(ip.dst), ip.len, ip.ttl, do_not_fragment, more_fragments,
                         fragment_offset))

            content = eth#.data.data.data
            if len(content) != 0:
                  pkts_len.append(len(content))
            #text_cap.write('****'+ content +'\n' )
            pkts_num += 1
            '''
      #print pkts_len
      print '-----PKTs:', pkts_num

      file_cap.flush()
      file_cap.close()
      '''
      #argdsize
      while input('plz input 1 or 0:')!= 0 :
            dsize = 0
            start = input('plz input a int:')
            end = input('plz input a int:')
            num = end - start + 1
            pkt_lens = pkts_len[start -1 : end]
            for i in pkt_lens:
                  #print i
                  dsize = dsize + i
            argdsize = dsize/num
            print 'argdsize: %d (%d-%d)' % (argdsize, start, end)
'''