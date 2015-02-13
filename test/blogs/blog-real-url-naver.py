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

    if p.netloc == "blog.naver.com":
        if p.path == "/PostView.nhn" and "blogId" in qs.keys() and "logNo" in qs.keys():
            a, b, c, d, e, f = p
            e = '&'.join('&'.join("{}={}".format(k, v2) for v2 in v1) for k, v1 in sorted(qs.items()) if k in [ "blogId", "logNo" ])
            return urlunparse([ a, b, c, d, e, f ])
        elif p.path == "/PostList.nhn" and "blogId" in qs.keys() and "categoryNo" in qs.keys():
            a, b, c, d, e, f = p
            e = '&'.join('&'.join("{}={}".format(k, v2) for v2 in v1) for k, v1 in sorted(qs.items()) if k in [ "blogId", "categoryNo" ])
            return urlunparse([ a, b, c, d, e, f ])
        else:
            root = get_root_node(url)
            frames = root.xpath('//frame[@id="mainFrame" and @src]')
            if len(frames) > 0:
                a, b, c, d, e, f = p
                src = frames[0].get("src")
                p = urlparse(src)
                if len(p.scheme) > 0:
                    c = p.path
                else:
                    c = src
                return get_real_url(urlunparse([ a, b, c, d, e, f ]))
            else:
                if re.match(r"^/Post.*\.nhn$", p.path) and "blogId" in qs.keys():
                    a, b, c, d, e, f = p
                    e = '&'.join('&'.join("{}={}".format(k, v2) for v2 in v1) for k, v1 in sorted(qs.items()) if k == "blogId" )
                    return urlunparse([ a, b, c, d, e, f ])
    else:
        root = get_root_node(url)
        frames = root.xpath('//frame[@id="screenFrame" and @src]')
        if len(frames) > 0:
            a, b, c, d, e, f = p
            src = frames[0].get("src")
            p = urlparse(src)
            if len(p.scheme) > 0:
                c = p.path
            else:
                c = src
            b = "blog.naver.com"
            return get_real_url(urlunparse([ a, b, c, d, e, f ]))

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
        "blog.naver.com/baby1255/220259031830", # NAVER
        "parang567.blog.me/220259001214", # NAVER: blog.me
        "blog.noitamina.moe/220258972586", # NAVER: user domain
        "r-kai.wo.tc", # NAVER: user domain, post not specified
    ]
    for x in case:
        test(x)

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)