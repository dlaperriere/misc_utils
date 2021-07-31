#!/usr/bin/env python
"""
Description

ip.py - get public IP address

Usage

    python ip.py

Output

      https://duckduckgo.com/?q=what+is+my+ip&ia=answer:
      
      IP: x.x.x.x
      
      http://checkip.dyndns.com/:
      
      IP: x.x.x.x

Note

 - works with python 2.7 and 3.6

Author

  David Laperriere <dlaperriere@outlook.com>

"""
import re
import sys
import time

try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

__version_info__ = (1, 0)
__version__ = '.'.join(map(str, __version_info__))
__author__ = "David Laperriere dlaperriere@outlook.com"


def main():
    timeout = 3

    urls = ["https://duckduckgo.com/?q=what+is+my+ip&ia=answer",
            "https://ipinfo.io/",
            "http://checkip.dyndns.com/"]

    ip_regexp = re.compile(b'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')

    for url in urls:
        try:
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
        except urllib2.URLError as e:
            print(url + " error : \n" + str(e.reason) + "\n")
            continue

        print(url + ":\n")
        data = response.read()
        ip = ip_regexp.search(data)
        if ip:
            print("IP: {}".format(ip.group().decode("utf-8")))
            sys.exit(0)
        else:
            print("not found")
        print(" ")
        time.sleep(timeout)

if __name__ == "__main__":
    main()
