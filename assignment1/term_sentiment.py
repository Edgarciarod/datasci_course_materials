#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json

new_scores = {}


def extractor(scores, tweet_data):
    global new_scores
    sentiment_score = 0.0
    try:
        tweet_words = tweet_data[u'text'].strip()
        tweet_words = tweet_words.lower().split(' ')
        tweet_words = [s.strip("#@!:)(.,\"\' ").encode('utf-8').replace('\n', '').replace('\r', '') for s in
                       tweet_words]
        #print(tweet_words)
        for each_word in tweet_words:
            try:
                sentiment_score += float(scores[each_word])
            except KeyError:
                continue
        for each_word in tweet_words:
            if not (each_word in scores):
                if not each_word in new_scores:
                    new_scores[each_word] = sentiment_score
                else:
                    new_scores[each_word] = float(new_scores[each_word] + sentiment_score) / 2.0
    except KeyError:
        pass


def hw(sent_file, tweet_file):
    scores = {}  # initialize an empty dictionary#
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
    for each_key in new_scores.keys():
        print "%s %.3f" % (each_key, new_scores[each_key])


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)


if __name__ == '__main__':
    main()
