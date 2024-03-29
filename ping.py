#!/usr/bin/env python
"""
Description

  ping.py - check a remote host for reachability

Usage

    python ping.py host port


 Output

    #$># sudo python ping.py 192.168.1.99 8888
    ping 192.168.1.99 port 8888
        - icmp is reachable
        -  tcp is NOT reachable
        -  udp is reachable

Note
  - Require administrator/sudo privileges
  - Use GPLv2 code from https://github.com/samuel/python-ping/blob/master/ping.py
  - works with python 2.7 and 3.6

Author

  David Laperriere <dlaperriere@outlook.com>

"""
import os
import sys
import socket
import struct
import select
import time

__version_info__ = (1, 0)
__version__ = '.'.join(map(str, __version_info__))
__author__ = "David Laperriere dlaperriere@outlook.com"

ICMP_ECHO_REQUEST = 8
TIMEOUT = 5

if sys.platform == "win32":
    # On Windows, the best timer is time.clock()
    default_timer = time.clock
else:
    # On most other platforms the best timer is time.time()
    default_timer = time.time


# Python version compat
if sys.version_info[0] <= 2:
    Py3 = False
elif sys.version_info[0] >= 3:
    Py3 = True


# methods

def icmp(host, timeout=TIMEOUT):
    """
     Send/receive ICMP packet to host

    """
    delay = None
    try:
        delay = do_one(host, timeout)
    except socket.gaierror as e:
        print(" - icmp is NOT reachable (socket error: '%s')" % e)

    if delay is None:
        print(" - icmp is NOT reachable (timeout within %ssec.)" % timeout)

    else:
        delay = delay * 1000
        # print "get ping in %0.4fms" % delay
        print(" - icmp is reachable")


def tcp(host, port, timeout=TIMEOUT):
    """
    Open/close a TCP connection to host:port
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    s.settimeout(timeout)
    result = s.connect_ex((host, port))
    if result == 0:
        print(" -  tcp is reachable")
    else:
        print(" -  tcp is NOT reachable")
    s.close()


def udp(host, port, timeout=TIMEOUT):
    """
     Send UDP echo ping at host:port

      The script echo.py can be used as a server
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    s.settimeout(timeout)

    result = s.connect_ex((host, port))
    if Py3:
        s.send(bytes("PING", "ascii"))
    else:
        s.send('PING')

    try:
        reply, address = s.recvfrom(1024)
        # print "  Received '"+ str(reply) + "' from " + str(address)
        result = 1

    except socket.error as serror:
        result = -1
        # print "\t"+str(serror)

    if result >= 0:
        print(" -  udp is reachable ")
    else:
        print(" -  udp is NOT reachable ")
    s.close()

# icmp methods from
# https://github.com/samuel/python-ping/blob/master/ping.py
# GPLv2


def checksum(source_string):
    """
    I'm not too confident that this is right but testing seems
    to suggest that it gives the same answers as in_cksum in ping.c
    """
    csum = 0
    countTo = (len(source_string) // 2) * 2
    count = 0
    while count < countTo:
        if Py3:
            thisVal = source_string[count + 1] * 256 + source_string[count]
        else:
            thisVal = ord(source_string[count + 1]) * \
                256 + ord(source_string[count])
        csum = csum + thisVal
        csum = csum & 0xffffffff  # Necessary?
        count = count + 2

    if countTo < len(source_string):
        csum = csum + ord(source_string[len(source_string) - 1])
        csum = csum & 0xffffffff  # Necessary?

    csum = (csum >> 16) + (csum & 0xffff)
    csum = csum + (csum >> 16)
    answer = ~csum
    answer = answer & 0xffff

    # Swap bytes. Bugger me if I know why.
    answer = answer >> 8 | (answer << 8 & 0xff00)

    return answer

# from  https://github.com/samuel/python-ping/blob/master/ping.py


def receive_one_ping(my_socket, ID, timeout):
    """
    receive the ping from the socket.
    """
    timeLeft = timeout
    while True:
        startedSelect = default_timer()
        whatReady = select.select([my_socket], [], [], timeLeft)
        howLongInSelect = (default_timer() - startedSelect)
        if whatReady[0] == []:  # Timeout
            return

        timeReceived = default_timer()
        recPacket, addr = my_socket.recvfrom(1024)
        icmpHeader = recPacket[20:28]
        itype, code, checksum, packetID, isequence = struct.unpack(
            "bbHHh", icmpHeader
        )
        # Filters out the echo request itself.
        # This can be tested by pinging 127.0.0.1
        # You'll see your own request
        if itype != 8 and packetID == ID:
            bytesInDouble = struct.calcsize("d")
            timeSent = struct.unpack("d", recPacket[28:28 + bytesInDouble])[0]
            return timeReceived - timeSent

        timeLeft = timeLeft - howLongInSelect
        if timeLeft <= 0:
            return

# from  https://github.com/samuel/python-ping/blob/master/ping.py


def send_one_ping(my_socket, dest_addr, ID):
    """
    Send one ping to the given >dest_addr<.
    """
    dest_addr = socket.gethostbyname(dest_addr)

    # Header is type (8), code (8), checksum (16), id (16), sequence (16)
    my_checksum = 0

    # Make a dummy heder with a 0 checksum.
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, my_checksum, ID, 1)
    bytesInDouble = struct.calcsize("d")
    data = (192 - bytesInDouble) * "Q"
    if Py3:
        data = struct.pack("d", default_timer()) + bytes(data, "ascii")
    else:
        data = struct.pack("d", default_timer()) + data

    # Calculate the checksum on the data and the dummy header.
    my_checksum = checksum(header + data)

    # Now that we have the right checksum, we put that in. It's just easier
    # to make up a new header than to stuff it into the dummy.
    header = struct.pack(
        "bbHHh", ICMP_ECHO_REQUEST, 0, socket.htons(my_checksum), ID, 1
    )
    packet = header + data
    my_socket.sendto(packet, (dest_addr, 1))  # Don't know about the 1

# from  https://github.com/samuel/python-ping/blob/master/ping.py


def do_one(dest_addr, timeout):
    """
    Returns either the delay (in seconds) or none on timeout.
    """
    icmp = socket.getprotobyname("icmp")
    try:
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
    except socket.error as serror:
        (errno, msg) = serror.args
        if errno == 1:
            # Operation not permitted
            msg = msg + (
                " - Note that ICMP messages can only be sent from processes"
                " running as root."
            )
            raise socket.error(msg)
        raise  # raise the original error

    my_ID = os.getpid() & 0xFFFF

    send_one_ping(my_socket, dest_addr, my_ID)
    delay = receive_one_ping(my_socket, my_ID, timeout)

    my_socket.close()
    return delay

# from  https://github.com/samuel/python-ping/blob/master/ping.py


def verbose_ping(dest_addr, timeout=2, count=4):
    """
    Send >count< ping to >dest_addr< with the given >timeout< and display
    the result.
    """
    for i in range(count):
        print("ping %s..." % dest_addr)
        try:
            delay = do_one(dest_addr, timeout)
        except socket.gaierror as e:
            print("failed. (socket error: '%s')" % e[1])
            break

        if delay is None:
            print("failed. (timeout within %ssec.)" % timeout)
        else:
            delay = delay * 1000
            print("get ping in %0.4fms" % delay)
    print()


# main


def main():
    """ Main check parameters & ping host with icmp/tcp/udp """
    if len(sys.argv) == 2:
        host = sys.argv[1]
        port = 80
    elif len(sys.argv) == 3:
        host = sys.argv[1]
        port = int(sys.argv[2])
    else:
        print("Usage: python ping.py host port")
        sys.exit(0)

    print("ping " + host + " port " + str(port))
    try:
        icmp(host)
        tcp(host, port)
        udp(host, port)
    except socket.error as msg:
        print('Connection failed : ' + str(msg))
        sys.exit(-1)

if __name__ == "__main__":
    main()
