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
    # dict for to record timestamp and text of tweets. Allows us to discard
    # duplicates, since the tweet id is unique
    tweets = {}
    
    # counter for loop
    index = 0
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
        # check if suspected duplicates have same text; print message if different
        if tweet['id'] in tweets.keys():
            if tweets[tweet['id']][1] != tweet['text']:
                print("DIFFERENT!")
        tweets[tweet['id']] = [tweet['created_at'], tweet['text']]
        index += 1
    print("Encountered {} missing leading brackets.".format(leading_err))
    print("Encountered {} missing trailing brackets.".format(trailing_err))
    print("{} lines in tweet file".format(index))
    return tweets


def tweet_categorizer(tweets):
    """ takes tweet dictionary and creates two new lists 
    for if tweet referencing obama and one for Romney"""
    obama_list = ["obama", "barack", "barry", "obummer", "bammy", "odummy"]
    romney_list = ["mitt", "romney", "robme", "romnuts"]

    obama_tweets = []
    romney_tweets = []

    uncategorized_count = 0
    for tweet in tweets.values():
        count = 0
        tweet_text = tweet[1]
        for tag in obama_list:
            if tag in tweet_text.lower():
                obama_tweets.append(tweet)
                count += 1 
                break
        for tag in romney_list:
            if tag in tweet_text.lower():
                romney_tweets.append(tweet)
                count += 1
                break
        if count == 0:
            uncategorized_count += 1
    print(" {} uncategorized tweets".format(uncategorized_count))
    return obama_tweets, romney_tweets


def tweet_time_series(obama_tweets, romney_tweets):
    """ create time object dates, plots timeseries data and formats the plot """
    tweets_list = [obama_tweets, romney_tweets]
    for canidate in tweets_list:
        print(canidate[0])
        for tweet in canidate:
            try:
                tweet[0] = time.strptime(tweet[0][:19],"%a, %d %b %Y %H")
            except TypeError:
                pass
        plt.plot(canidate)
    plt.show()

tweets = data_loader("data/HW03_twitterData.json.txt.gz")
print("recovered {} unique tweets".format(len(tweets)))

obama_tweets, romney_tweets = tweet_categorizer(tweets)
print(len(obama_tweets)+len(romney_tweets))

tweet_time_series(obama_tweets, romney_tweets)
