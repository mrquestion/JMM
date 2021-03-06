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

URL_FORMAT = "http://www.anissia.net/anitime/list?w={}"
DOTW = [ "일", "월", "화", "수", "목", "금", "토" ]

def get_root_node(url):
    rs = rq.get(url)
    return etree.HTML(rs.content if rs.ok else "<error/>")

def get_json_data(url):
    rs = rq.get(url)
    return json.loads(rs.text if rs.ok and rs.text is not None else "[]")

def test(url, filename='.'.join([ __file__, timestamp("%Y%m%d%H%M%S"), "txt" ])):
    result = []

    p = urlparse(url)
    if len(p.scheme) == 0:
        url = "http://{}".format(url)

    result.append(url)
    p = urlparse(url)

    if re.match(r".*blog\.naver\.com", p.netloc) is not None:
        result.append(" - NAVER")
    elif re.match(r".*blog\.me", p.netloc) is not None:
        result.append(" - NAVER")
    elif re.match(r".*egloos\.com", p.netloc) is not None:
        result.append(" - EGLOOS")
    elif re.match(r".*tistory\.com", p.netloc) is not None:
        result.append(" - TISTORY")
    elif re.match(r".*blog\.fc2\.com", p.netloc) is not None:
        result.append(" - FC2")
    else:
        if p.path.startswith("/xe/"):
            result.append(" - XE")
        else:
            root = get_root_node(url)
            if len(root.xpath('//frame[@id="screenFrame" and @src]')) > 0:
                result.append(" - NAVER")
            elif len(root.xpath('//script[re:test(text(),"user\.tistory\.com")]', namespaces=etree.namespaces)) > 0:
                result.append(" - TISTORY")
            else:
                result.append(" - Unverified")
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

        "kwangwaul.egloos.com/5864557", # EGLOOS

        "fuko.tistory.com/1584", # TISTORY
        "prisis.tistory.com", # TISTORY: post not specified 1
        "asterix.tistory.com/", # TISTORY: post not specified 2
        "kiribasi.moe/140", # TISTORY: user domain
        "tosso.kr/category/%ED%8E%98%EC%96%B4%EB%A6%AC%20%ED%85%8C%EC%9D%BC", # TISTORY: user domain
        "bbmi.kr", # TISTORY: user domain, post not specified 3

        "haniani.net/xe/167517", # XE

        "hakerano.blog.fc2.com/", # FC2: post not specified 1
        "feder07.blog.fc2.com/", # FC2: post not specified 2
    ]
    for x in case:
        test(x)

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)