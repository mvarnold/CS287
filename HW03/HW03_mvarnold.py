# Homework 03
# Michael Arnold

import json
import gzip
import datetime
import time
import matplotlib.pyplot as plt
import matplotlib.dates
import numpy as np
import string

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
    labels = ["Obama Tweets", "Romeny Tweets"]
    colors = ['b', 'r']
    index = 0
    for canidate in tweets_list:
        date_dict = {}
        for tweet in canidate:
            date = datetime.datetime(*time.strptime(tweet[0][:19],"%a, %d %b %Y %H")[:4])
            if date in date_dict.keys():
                date_dict[date] += 1
            else:
                date_dict[date] = 1
        
        dates = np.array([[matplotlib.dates.date2num(key),value] for key,value in date_dict.items()])
        dates = dates[dates[:,0].argsort()]
        plt.plot_date(dates[:,0], dates[:,1],'.-',color = colors[index],label = labels[index])
        index += 1
    plt.legend(bbox_to_anchor = (0.5,1.0))
    plt.ylabel("# of tweets")
    plt.xlabel("Tweet Date")
    plt.title("Number of Tweets about Presidential Candidates")
    plt.xticks(rotation=70)
    plt.subplots_adjust(hspace=0, bottom=0.3)
    plt.savefig('timeseries.pdf')
    return


def word_counter(corpus):
    """counts the number of words in a corpus"""
    word_dict = {}
    punctuation = "!$%&'()*+,-./:;<=>?[\]^_`{|}~"
    for tweet in corpus:
        for word in [i.split(punctuation) for i in tweet[1].split()]:
            if word[0] in word_dict.keys():
                word_dict[word[0]] += 1
            else:
                word_dict[word[0]] = 1

    return word_dict


def slant_coeffecient(obama_words, romney_words):
    """computes the coeffecient"""
    coeff_dict = {}
    for word in obama_words.keys():
        if word in romney_words.keys():
            coeff_dict[word] = (obama_words[word]-romney_words[word]) / \
            (obama_words[word]+romney_words[word])
    return coeff_dict


tweets = data_loader("data/HW03_twitterData.json.txt.gz")
print("recovered {} unique tweets".format(len(tweets)))

obama_tweets, romney_tweets = tweet_categorizer(tweets)
print(len(obama_tweets)+len(romney_tweets))

tweet_time_series(obama_tweets, romney_tweets)

obama_words = word_counter(obama_tweets)
#print(sorted(obama_words.items(),key=lambda kv:kv[1]))
romney_words = word_counter(romney_tweets)

top_r = sorted(slant_coeffecient(obama_words, romney_words).items(), key=lambda kv: kv[1])
top_o = sorted(slant_coeffecient(obama_words, romney_words).items(), key=lambda kv: kv[1],reverse=True)

f = open('words.txt', 'w')

for i in range(100):
    f.write('{0} {1:.6f} {2} {3:.6f}\n'.format(top_o[i][0],top_o[i][1],top_r[i][0],top_r[i][1]))
f.close()
