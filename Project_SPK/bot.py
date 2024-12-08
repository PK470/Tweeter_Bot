from tweepy import Client, API, OAuth1UserHandler
import os
from dotenv import load_dotenv
from to_script import translate
from t1 import News
import hashlib
import json

load_dotenv()

HASHES_FILE = "tweet_hashes.json"

client = Client(
    bearer_token=os.getenv('BEARER_TOKEN'),
    consumer_key=os.getenv('API_KEY'),
    consumer_secret=os.getenv('API_SECRET'),
    access_token=os.getenv('ACCESS_TOKEN'),
    access_token_secret=os.getenv('ACCESS_TOKEN_SECRET')
)

def clean_text(text):
    
    if text.startswith('"') and text.endswith('"'):
        text = text[1:-1]
    
    return text.strip()

def create_tweet():
    s = News()
    p = s.g_news()
    t = None
    for n in p:
        n = n.text.strip()
        #print("it is n :-: "+ n)
        if is_new_tweet(n):
            t = n
            print(t)
            break
    
    if t is None:
        return None
    k = translate(t)
    print("translate function output :-"+ k)
    tweet = clean_text(k)
    print("it is tweet  :-: "+ tweet)
    try:
        client.create_tweet(text=tweet)
    except Exception as e:
        print(f"An error occurred: {e}")

def load_hashes():
    if os.path.exists(HASHES_FILE):
        with open(HASHES_FILE, "r") as file:
            return json.load(file)
    return []

def save_hashes(hashes):
    with open(HASHES_FILE, "w") as file:
        json.dump(hashes, file)

def hash_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def is_new_tweet(text): #checking if already posted
    tweet_hash = hash_text(text)
    hashes = load_hashes()
    if tweet_hash in hashes:
        return False
    hashes.append(tweet_hash)
    save_hashes(hashes)
    return True

create_tweet()