__author__ = 'Brendan'

# I'm noticing the cascading retweet structure of this dataset
# think I remember reading about that, todo take a look at hierarchical retweets in social science literature

# 1. in the meantime try to grab a single retweet tree and visualize it
# 2. work towards plotting retweet trees and word-similarity relationships among their root nodes

###################################
import json
import re
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import matplotlib.pyplot as plt
import igraph as ig

###############################
# grab the tweets and their users # todo use elastic search in later iterations

load_name = "sample_tweets_MLK.json"

loadfile = open(load_name,'r')
# read in from json file

tweetList = json.load(loadfile)
loadfile.close()

print "first entry"
print tweetList[0]
print tweetList[0]['screen_name']
print tweetList[0]['created_at']
print tweetList[0]['text']

################################
# set up a smarter infrastructure to search if necessary

# alphabetical by screen name? tree?             keep it simple for now
# temporal order by 'created_at'
# alphabetical by tweet text

screen_names = []
for entry in tweetList:
    screen_names.append(entry['screen_name'].lower())             # lower case only


################################################
# helper functions for traversing the tweets
def searchUp(tweet_ref):   # find a parent or return []

    # check if it's a retweet
    print tweet_ref['text'][0:2]
    prefix = tweet_ref['text'][0:2]
    if prefix == "RT":
        isRT = True

        # grab the parent user and text
        words = tweet_ref['text'].split() # we knw this will yield at least 3 words from the structure of a retweet
        parentUser = words[1][1:] # pick off the '@' in the first position
        parentUser = parentUser[:-1] # pick off the ':' in the lst position
        parentText = ' '.join(words[2:])
    else:
        isRT = False
        parentUser = "Null"
        parentText = "Null"
    print "parent user: " + parentUser
    print "parent text: " + parentText


    # attempt to find parent in database
    print "candidate matches"
    candidateTweets = []
    for i,tweet in enumerate(tweetList):
        if tweet['screen_name']==parentUser:
            candidateTweets.append(i)
            print ' '
            print tweet

    print "candidate tweets " + str(candidateTweets)

    # make a lazy check for equality on the tweet itself
    parentTweet = []
    for idx in candidateTweets:
        if tweetList[idx]['text']==parentText:
            parentTweet = idx
            print "found parent tweet: " + tweetList[idx]['text']

    return parentTweet # todo probably will have to do a better job keeping track of indices too

def searchDown(tweet_ref):
    children = []
    for idx,child_candidate in enumerate(tweetList):     # this is an expesive search, obviously - could use smarter data type or elastic database
        child_text = child_candidate['text']
        if child_text[0:2]=="RT":
            words = child_text.split()
            RT_user = words[1][1:-1] # pick off the '@' and the ':'
            if RT_user == tweet_ref['screen_name']:
                children.append(idx)
    return children

# check upward and downward from the parent tweet
# todo, upward

# downward:





#################################
# traverse a retweet tree (if applicable)

idx = np.random.randint(0,len(tweetList)) # grab a random tweet
tweet_ref = tweetList[idx]
print "reference tweet: "
print tweet_ref['screen_name']
print tweet_ref['created_at']
print tweet_ref['text']

parentTweet = searchUp(tweet_ref)

#################################
# traverse a retweet tree (if applicable)

idx = np.random.randint(0,len(tweetList)) # grab a random tweet
tweet_ref = tweetList[idx]
print "reference tweet: "
print tweet_ref['screen_name']
print tweet_ref['created_at']
print tweet_ref['text']

parentTweet = searchUp(tweet_ref)