# -*- coding: utf-8 -*-

import os, sys
import re
import json
import requests as rq

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

class objdict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
 
    def __getattr__(self, key):
        return self[key] if key in self.keys() else None
 
    def __setattr__(self, key, value):
        self[key] = value
 
    def __str__(self):
        return "<objdict {}>".format(super().__str__())

def fix_indent(s):
    s = re.sub(r"(\[)", "\\1\n ", s)
    s = re.sub(r"(\])", "\n\\1", s)
    s = re.sub(r"({)", "\\1\n     ", s)
    s = re.sub(r"((\s*)(\s{4}))(.*)(},?)", "\\1\\4\\2\\5", s)
    return s

URL_FORMAT1 = "http://www.anissia.net/anitime/list?w={}"
URL_FORMAT2 = "http://www.anissia.net/anitime/cap?i={}"
DOTW = [ "[{}]".format(x) for x in [ "일", "월", "화", "수", "목", "금", "토" ] ]

def get_json_data(url):
    rs = rq.get(url)
    return json.loads(rs.text if rs.ok else "[]")

def test(dotw, filename='.'.join([ __file__, timestamp("%Y%m%d%H%M%S"), "txt" ])):
    result = [ DOTW[dotw%7], '' ]
    w = [ objdict(x) for x in get_json_data(URL_FORMAT1.format(dotw)) ]
    for a in w:
        s = get_json_data(URL_FORMAT2.format(a.i)) # a["i"]
        result.append("[{}] {}".format(a.s, URL_FORMAT2.format(a.i)))
        result.append(fix_indent(pf(s)))
    with open(filename, "wb") as wbo:
        wbo.write('\n'.join(result).encode())

def main(argc, args):
    test(5)

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)