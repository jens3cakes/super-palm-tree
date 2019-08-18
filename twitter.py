#!usr/bin/python3

import requests
from bs4 import BeautifulSoup

url = "https://twitter.com/search"
subj_to_search = input("What would you like to find")

results = requests.get(url,
params={'q':subj_to_search},
headers={
     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel   Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.     3809.100 Safari/537.36'
 }
)

soup = BeautifulSoup(results.text, 'html.parser')
recipe_for_soup = open("twitter_soup.txt", "a")

def search_tweets(param):
    usernames = soup.select("div.content strong.fullname")
    for username in usernames:
        tweet_searcher()
        img_searcher()
        recipe_for_soup.write("\nThis is the username: " + username.text + "\nThis is the tweet left: " + tweet_searcher() + "\nThis is the pic: " + img_searcher())
    #recipe_for_soup.close()

def tweet_searcher():
    tweets = soup.select("div.content p.tweet-text")
    for tweet in tweets:
        return(tweet.get_text()) 

def img_searcher():
    images = soup.select("div.content div.AdaptiveMedia-photoContainer img")
    for image in images:
        return(image['src'])
    else:
        return("No image found")

if __name__ == "__main__":
    search_tweets(subj_to_search)
    tweet_searcher()
    img_searcher()
    


