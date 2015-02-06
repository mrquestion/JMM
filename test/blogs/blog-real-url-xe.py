# -*- coding: utf-8 -*-

import os, sys
import re
import json
import requests as rq
from urllib.parse import urlparse, urlunparse, parse_qs
from lxml import etree
etree.namespaces = dict(re="http://exslt.org/regular-expressions")

import time, datetime
def timestamp(format="%Y%m%d-%H%M%S", time=time.time(), rfc=None):
    return datetime.datetime.fromtimestamp(time).strftime(format)

import inspect, pprint
#def args(f): return inspect.getargspec(f)
#def mems(o): return inspect.getmembers(o)
def pp(s): pprint.pprint(s, indent=4, width=80)
def pf(s): return pprint.pformat(s, indent=4, width=80)
#def ppargs(f): pp(args(f))
#def ppmems(o): pp(mems(o))

def get_root_node(url):
    rs = rq.get(url)
    return etree.HTML(rs.content if rs.ok else "<error/>")

def get_real_url(url):
    p = urlparse(url)
    qs = parse_qs(p.query)

    if p.path.startswith("/xe/"):
        return url

def test(url, filename='.'.join([ __file__, timestamp("%Y%m%d%H%M%S"), "txt" ])):
    result = []

    p = urlparse(url)
    if len(p.scheme) == 0:
        url = "http://{}".format(url)

    result.append(url)
    result.append(" - {}".format(get_real_url(url)))
    result.append('')
    result.append('')

    with open(filename, "ab") as wbo:
        wbo.write('\n'.join(result).encode())

def main(argc, args):
    case = [
        "haniani.net/xe/167517", # XE
    ]
    for x in case:
        test(x)

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)