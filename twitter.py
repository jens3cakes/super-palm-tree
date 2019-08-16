#!usr/bin/python3

import requests
from bs4 import BeautifulSoup

url = "https://twitter.com/search"

results = requests.get(url,
params={'q':'Devleague'}, 
 
headers={
     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel   Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.     3809.100 Safari/537.36'
 }
)

soup = BeautifulSoup(results.text, 'html.parser')

#print(soup.div.prettify())

usernames = soup.select("div.tweet strong.fullname")

tweets = soup.select("div.js-tweet-text-container")

text_file = open("dleague.txt", "w")

for username in usernames:
    print(results)    
    print(username.text)
    text_file.write("\nUser: " + (username.text).encode("utf-8"))

    for tweet in tweets:
        print(tweet.text)
        text_file.write("\nComment: " + (tweet.text).encode("utf-8"))
        



