import requests
import json
from req_get_actifs import changeCommaInPoint, get_quote_for_asset
url_post_portfolio = "https://dolphin.jump-technology.com:8443/api/v1/portfolio/1821/dyn_amount_compo"

#this does not seem to work for now : 404 error
def getPortfolio(usr: str, pwd: str, base_url: str, portfolio_id: str):
  portfolio_url = base_url
  portfolio_url += 'portfolio/'
  portfolio_url += portfolio_id
  portfolio_url += 'dyn_amount_compo'
  r = requests.get(portfolio_url, auth=(usr, pwd))
  return r

def getPriceinDollar(asset_id):
    usr = "EPITA_GROUPE2"
    pwd = "PcA7s3Rnzsch6M79"
    base_url = 'https://dolphin.jump-technology.com:8443/api/v1/'
    quote_asset_req = get_quote_for_asset(usr, pwd, base_url, asset_id)
    quote_dict = json.loads(quote_asset_req.text)
    price= 0
    for i in quote_dict:
        if i["date"]["value"]== "2016-06-01":
            price = float(changeCommaInPoint(i["nav"]["value"]))
            break
    quote_url = base_url
    quote_url += 'asset/' + asset_id + '/'
    r = requests.get(quote_url, auth=(usr, pwd))
    asset = json.loads(r.text)
    device = asset["CURRENCY"]["value"]
    if(device == "EUR"):
        return price * 1.11
    return price

assert(getPriceinDollar("2110")==101.51)   
#def normalize()

def createPortfolio(portfolio: list, assets: list):
  assets_list = []
  for ind in portfolio:
    asset_id = assets[ind]
    asset_dict = { "asset": int(asset_id),
                   "quantity": 1 #this should probably be modified
                 }
    portfolio_asset = { "asset": asset_dict }
    assets_list.append(portfolio_asset)
  
  #build dict to send
  dict_values = { "2016-06-01": assets_list } #written in the subject
  dict_currency = { "code": "EUR" }
  dict_portfolio = { "label": "EPITA_PTF_2",
                     "currency": dict_currency,
                     "type": "front", #written in the subject
                     "values" : dict_values
                   }

  return dict_portfolio


def sendPortfolio(jsonPortfolio: dict, usr:str, pwd:str):
  req = requests.put(url_post_portfolio, data=json.dumps(jsonPortfolio), auth=(usr, pwd))
  return req
