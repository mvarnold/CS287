# Homework 03
# Michael Arnold

import json
import gzip
import datetime
import time

def data_loader(filename):
    """ Takes a gzipped file of twitter data, and attempts to repair,
    and read each line"""

    # counters for errors
    leading_err = 0
    trailing_err = 0
    # list for to record timestamp and text of tweets
    tweets = []

    for line in gzip.open(filename, 'rt', encoding='utf-8'):
        if line[0] != '{':
            line = '{' + line
            leading_err += 1
        if line[-2] != '}':
            line = line[:-1] + '}' + line[-1]
            trailing_err += 1
        try: 
            tweet = json.loads(line.strip())
        except json.decoder.JSONDecodeError:
            print("error!")
            print(line)
        tweets.append([time.strptime(tweet['created_at'],"%a, %d %b %Y %H:%M:%S"),tweet['text']])
    print("Encountered {} missing leading brackets.".format(leading_err))
    print("Encountered {} missing trailing brackets.".format(trailing_err))
    return tweets

data = data_loader("data/HW03_twitterData.json.txt.gz")
print(data)
