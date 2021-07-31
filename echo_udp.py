#!/usr/bin/env python
"""
Description

 echo_udp.py - UDP Echo Server

Usage

      python echo_udp.py host port

Output

      #$># python echo_udp.py localhost 12345
     starting up on localhost port 12345
    
     waiting to receive message
     received 4 bytes from ('127.0.0.1', 52837)
     PING
     sent 4 bytes back to ('127.0.0.1', 52837)
     
     waiting to receive message

 Note

  - Based on http://pymotw.com/2/socket/udp.html
  - works with python 2.7 and 3.6

Author

  David Laperriere <dlaperriere@outlook.com>

"""
import socket
import sys

__version_info__ = (1, 0)
__version__ = '.'.join(map(str, __version_info__))
__author__ = "David Laperriere dlaperriere@outlook.com"


def main():
    """ Main check parameters & start udp echo server """

    # check parameters
    if len(sys.argv) == 3:
        host = sys.argv[1]
        port = int(sys.argv[2])
    else:
        print("Usage: python echo_udp.py host port")
        sys.exit(0)

    # start server
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = (host, port)
    print('starting up on %s port %s' % server_address)
    sock.bind(server_address)

    # wait for message
    while True:
        print('\nwaiting to receive message')
        data, address = sock.recvfrom(4096)

        print('received %s bytes from %s' % (len(data), address))
        print(data)

        if data:
            sent = sock.sendto(data, address)
            print('sent %s bytes back to %s' % (sent, address))

if __name__ == "__main__":
    main()
