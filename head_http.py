#!/usr/bin/env python
"""
Description

head_http.py - print URL http response header

Usage

    python head_http.py url

Output

    #$>#  python head_http.py http://github.com
    http://github.com:
    
    Server: GitHub.com
    Date: Wed, 03 Jun 2015 21:03:18 GMT
    Content-Type: text/html; charset=utf-8
    Transfer-Encoding: chunked
    Connection: close
    Status: 200 OK
    ...

Note

 - works with python 2.7 and 3.5

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

    # check parameters
    if len(sys.argv) == 2:
        url = sys.argv[1]
    else:
        print("Usage: python head_http.py url")
        sys.exit(-1)

    if not re.match('(?:http|https)://', url):
        url = "http://" + url

    try:
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        time.sleep(timeout)
    except urllib2.URLError as e:
        print(url + " error : \n" + str(e.reason))
        sys.exit(-1)

    print(url + ":\n")
    # print ("Status: " + str(response.getcode()))
    print(response.info())

if __name__ == "__main__":
    main()
