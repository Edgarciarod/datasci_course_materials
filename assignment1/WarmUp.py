#! /usr/bin/env python
# -*- coding: utf-8 -*-

__autor__ = "edgar"

import json
import urllib2 as urllib


for i in xrange(100):
    response = urllib.urlopen("http://search.twitter.com/search.json?q=linux&page={}".format(i + 1))
    print json.load(response)[u'results'][0][u'text']
