#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json


def extractor(scores, tweet_data):
    sentiment_score = 0
    try:
        tweet_words = tweet_data[u'text'].strip()
        tweet_words = tweet_words.lower().split(' ')
        tweet_words = [s.strip("#@!:)(") for s in tweet_words]
        #print(tweet_words)
        for each_word in tweet_words:
            try:
                sentiment_score += scores[each_word]
                #print "---->"+each_word
            except KeyError:
                continue
        print (float(sentiment_score))
    except KeyError:

        print (float(sentiment_score))
        return


def hw(sent_file, tweet_file):
    scores = {}  # initialize an empty dictionary
    for line in sent_file:
        term, score = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
        #print scores.items()  # Print every (term, score) pair in the dictionary
    all_tweets = tweet_file.readlines()
    for tweet in all_tweets:
        try:
            tweet_data = json.loads(tweet)
            extractor(scores, tweet_data)
        except ValueError:
            continue


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)


if __name__ == '__main__':
    main()
