#! /usr/bin/env python
# -*- coding: utf-8 -*-

__autor__ = "edgar"

import json
import urllib2 as urllib


for i in xrange(100):
    response = urllib.urlopen("http://search.twitter.com/search.json?q=linux&page=" + str(i + 1))
    results = json.load(response)[u'results']
    if len(results) > 0:
        for each_result in results:
            print each_result[u'text']
    else:
        break
