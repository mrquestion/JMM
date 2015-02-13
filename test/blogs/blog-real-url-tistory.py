# -*- coding: utf-8 -*-

import os, sys
import re
import json
import requests as rq
from urllib.parse import urlparse, urlunparse, parse_qs
from lxml import etree
etree.namespaces = dict(re="http://exslt.org/regular-expressions")

import time, datetime
def timestamp(format="%Y%m%d-%H%M%S"):
    return datetime.datetime.fromtimestamp(time.time()).strftime(format)

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

    if re.match(r"([^.]+)\.tistory\.com", p.netloc) is not None:
        return url
    else:
        root = get_root_node(url)
        scripts = root.xpath('//script[contains(text(),"__pageTracker")]')
        for x in scripts:
            svcdomain = author = None
            for m in re.finditer(r'\s+__pageTracker\.__addParam\("([^"]+)".*,.*"([^"]+)"\);.*', x.text):
                k, v = m.groups()
                if k == "svcdomain":
                    svcdomain = v
                elif k == "author":
                    author = v

                if svcdomain is not None and author is not None:
                    a, b, c, d, e, f = p
                    b = svcdomain.replace("user", author)
                    return urlunparse([ a, b, c, d, e, f ])

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
        "fuko.tistory.com/1584", # TISTORY
        "prisis.tistory.com", # TISTORY: post not specified 1
        "asterix.tistory.com/", # TISTORY: post not specified 2
        "kiribasi.moe/140", # TISTORY: user domain
        "tosso.kr/category/%ED%8E%98%EC%96%B4%EB%A6%AC%20%ED%85%8C%EC%9D%BC", # TISTORY: user domain
        "bbmi.kr", # TISTORY: user domain, post not specified 3
    ]
    for x in case:
        test(x)

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)