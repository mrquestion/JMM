# -*- coding: utf-8 -*-

import os, sys
import re
import json
#import socket
#socket.INADDR_ANY = "0.0.0.0"
import requests as rq
#from urllib.parse import urlparse, urlunparse, parse_qs
#from bs4 import BeautifulSoup
#from lxml import etree
#etree.namespaces = dict(re="http://exslt.org/regular-expressions")

#import hashlib
#def md5(s):
#   e = hashlib.md5(str(s).encode("utf-8"))
#   return e.hexdigest()

import time, datetime
def timestamp(format="%Y%m%d-%H%M%S", time=time.time(), rfc=None):
    return datetime.datetime.fromtimestamp(time).strftime(format)

#import ctypes
#def alert(s, title="Test"):
#    ctypes.windll.user32.MessageBoxW(0, str(s), title, 0)

import inspect, pprint
#def args(f): return inspect.getargspec(f)
#def mems(o): return inspect.getmembers(o)
def pp(s): pprint.pprint(s, indent=4, width=80)
def pf(s): return pprint.pformat(s, indent=4, width=80)
#def ppargs(f): pp(args(f))
#def ppmems(o): pp(mems(o))

def fix_indent(s):
    s = re.sub(r"(\[)", "\\1\n ", s)
    s = re.sub(r"(\])", "\n\\1", s)
    s = re.sub(r"({)", "\\1\n     ", s)
    s = re.sub(r"((\s*)(\s{4}))(.*)(},?)", "\\1\\4\\2\\5", s)
    return s

URL_FORMAT = "http://www.anissia.net/anitime/list?w={}"
DOTW = [ "일", "월", "화", "수", "목", "금", "토" ]

def get_json_data(url):
    rs = rq.get(url)
    return json.loads(rs.text if rs.ok and rs.text is not None else "[]")

def test(filename='.'.join([ __file__, timestamp("%Y%m%d%H%M%S"), "txt" ])):
    result = []
    """ 0: Sunday,
        1: Monday
        ...
        6: Saturday
    """
    for i in range(7):
        result.append("[{}] {}".format(DOTW[i], URL_FORMAT.format(i)))
        result.append('')
        w = get_json_data(URL_FORMAT.format(i))
        w = fix_indent(pf(w))
        result.append(w)
        result.append('')
        result.append('')

    with open(filename, "wb") as wbo:
        wbo.write('\n'.join(result).encode())

def main(argc, args):
    test()

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)