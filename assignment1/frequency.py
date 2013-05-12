#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json

my_tweets = {}


def read_tweet(tweet_data):
    global my_tweets
    try:
        tweet_words = tweet_data[u'text'].strip()
        tweet_words = tweet_words.split(' ')
        tweet_words = [s.strip("#@!:)(\n\r\t,.:").replace("\n", "").replace("\r", "").encode('utf-8') for s in
                       tweet_words]
        for each_word in tweet_words:
            if len(each_word) == 0:
                continue
            if each_word in my_tweets:
                my_tweets[each_word] += 1
            else:
                my_tweets[each_word] = 1
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
    for each_key in my_tweets.keys():
        print "%s %0.3f" % (each_key, float(my_tweets[each_key]) / float(len(my_tweets)))


def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)


if __name__ == '__main__':
    main()
