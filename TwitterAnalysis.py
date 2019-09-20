#install twitter library
!pip install tweepy
#############################################

import tweepy

#create a developers account in twitter and get below keys

consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token = "your_access_token"
access_token_secret = "Your_access_token_secret"

authentication_info = tweepy.OAuthHandler(consumer_key, consumer_secret)
authentication_info.set_access_token(access_token, access_token_secret)

twitter_api = tweepy.API(authentication_info)
twitter_tweets = twitter_api.search("#iPhone11")

for tweet in twitter_tweets:
    print(tweet.text)
    
from textblob import TextBlob
senti = TextBlob(tweet.text)
print("**********************************")

print('Tweet- {0} | Polarity -{1} | Subjectivity -{2}'.format(tweet.text, senti.sentiment.polarity,    senti.sentiment.subjectivity))
        


print(senti.sentiment)

print("**********************************")

if senti.polarity >0 and senti.polarity <0.5 :
 print("good")
elif senti.polarity >=0.5 and senti.polarity <=1 :
 print("That's awesome")
elif senti.polarity <=0 and senti.polarity <= -0.5 :
 print("That's sad")
else :
 print("That's aweful")
