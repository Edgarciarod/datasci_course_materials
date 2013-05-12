#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json


states_table = {
    "AL": "Alabama",
    "AK": "Alaska",
    "AS": "American Samoa",
    "AZ": "Arizona",
    "AR": "Arkansas",
    "CA": "California",
    "CO": "Colorado",
    "CT": "Connecticut",
    "DE": "Delaware",
    "DC": "District Of Columbia",
    "FM": "Federated States Of Micronesia",
    "FL": "Florida",
    "GA": "Georgia",
    "GU": "Guam",
    "HI": "Hawaii",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "IA": "Iowa",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "ME": "Maine",
    "MH": "Marshall Islands",
    "MD": "Maryland",
    "MA": "Massachusetts",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MS": "Mississippi",
    "MO": "Missouri",
    "MT": "Montana",
    "NE": "Nebraska",
    "NV": "Nevada",
    "NH": "New Hampshire",
    "NJ": "New Jersey",
    "NM": "New Mexico",
    "NY": "New York",
    "NC": "North Carolina",
    "ND": "North Dakota",
    "MP": "Northern Mariana Islands",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    "PW": "Palau",
    "PA": "Pennsylvania",
    "PR": "Puerto Rico",
    "RI": "Rhode Island",
    "SC": "South Carolina",
    "SD": "South Dakota",
    "TN": "Tennessee",
    "TX": "Texas",
    "UT": "Utah",
    "VT": "Vermont",
    "VI": "Virgin Islands",
    "VA": "Virginia",
    "WA": "Washington",
    "WV": "West Virginia",
    "WI": "Wisconsin",
    "WY": "Wyoming"
}

for i in states_table.keys():
    states_table[i] = 0


def extractor(scores, tweet_data):
    global states_table
    try:
        if tweet_data[u'lang'] != u'en' or tweet_data[u'place'] == None or tweet_data[u'place'][
            u'country'] != u'United States':
            return
        code_state = tweet_data[u'place'][u'full_name'].split(', ')[1]
        if len(code_state) != 2:
            return
        tweet_words = tweet_data[u'text'].strip()
        tweet_words = tweet_words.lower().split(' ')
        tweet_words = [s.strip("#@!:)(\n\r\t").replace("\n", "").replace("\r", "") for s in tweet_words]
        for each_word in tweet_words:
            if each_word in scores:
                if code_state in states_table:
                    states_table[code_state] += scores[each_word]
    except KeyError:
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
    #print(states_table)
    maximo = -99999999
    maximo_code = ""
    for code_state in states_table.keys():
        if states_table[code_state] > maximo:
            maximo = states_table[code_state]
            maximo_code = code_state
    print(maximo_code)


if __name__ == '__main__':
    main()
