print 'main'
#try:
import scapy.all as scapy
#except ImportError:
#    import scapy

#try:
    # This import works from the project directory
#import scapy_http.http
#except ImportError:
    # If you installed this package via pip, you just need to execute this

#from scapy.layers import http

print 'begin=>'
packets = scapy.rdpcap('./data/hs/216room_50-3A-A0-52-C8-00.cap')
print '-for-'
for p in packets:
    print '=' * 78
# print p.show()
    for f in p.payload.fields_desc:
        if f.name == 'src' or f.name == 'dst':
            ct = scapy.conf.color_theme
            vcol = ct.field_value
            fvalue = p.payload.getfieldval(f.name)
            reprval = f.i2repr(p.payload, fvalue)
            print "%s : %s" % (f.name, reprval)

    for f in p.payload.payload.fields_desc:
        if f.name == 'load':
            ct = scapy.conf.color_theme
            vcol = ct.field_value
            fvalue = p.payload.getfieldval(f.name)
            reprval = f.i2repr(p.payload, fvalue)
            print "%s : %s" % (f.name, reprval)

print 'End<='