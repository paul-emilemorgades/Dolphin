import requests
import json

url_post_portfolio = "https://dolphin.jump-technology.com:8443/api/v1/portfolio/2201/dyn_amount_compo"

def sendPortfolio(jsonPortfolio:json, usr:str, pwd:str):
    req = requests.put(url_post_portfolio, jsonPortfolio, auth=(usr, pwd))
    return req
