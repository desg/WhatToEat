import requests
from requests_oauthlib import OAuth1

def yelpRequest(hostURL, payload, consumer_key, consumer_secret, token, token_secret):

    auth = OAuth1(consumer_key, consumer_secret,
                    token, token_secret)
    con = requests.get(hostURL, params=payload, auth=auth).json()
    return con
