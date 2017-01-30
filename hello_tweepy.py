__author__ = 'Brendan'



import tweepy

# https://apps.twitter.com/app/13290014/keys
# owner  cpchiptabernacl
# ownerid  	2569037840

consumer_key = "7M6nOHsYYKR4017OgL9DdgVtR"
consumer_secret = "WYNXMAOBTR37yENNVIPK3wVbFGlm17A7GOKhrFWmhRvnNADpEX"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

access_token = "2569037840-pKDmLnVgJ6MHv8ikkQE3gyN2AbHV7C4ZoHadDLF"
access_token_secret = "ABbnsSv5Owzs6M0HVFYNUmH1KDiuBS9nmhGdloEUx49U5"
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text