#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
import operator

my_hashtags = {}


def read_tweet(tweet_data):
    global my_hashtags
    try:
        tweet_hashtags = tweet_data[u'entities'][u'hashtags']
        for each_hashtag_data in tweet_hashtags:
            each_hashtag = each_hashtag_data[u'text'].encode('utf-8')
            if each_hashtag in my_hashtags:
                my_hashtags[each_hashtag] += 1
            else:
                my_hashtags[each_hashtag] = 1
    except KeyError:
        pass


def hw(tweet_file):
    all_tweets = tweet_file.readlines()
    for tweet in all_tweets:
        try:
            tweet_data = json.loads(tweet)
            read_tweet(tweet_data)
        except ValueError:
            continue
    for each_key in sorted(my_hashtags.items(), key=operator.itemgetter(1), reverse=True)[0:10]:
        print "%s %0.1f".encode('utf-8') % (each_key[0], float(my_hashtags[each_key[0]]))


def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)


if __name__ == '__main__':
    main()
