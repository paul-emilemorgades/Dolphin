import requests
import json

url_post_portfolio = "https://dolphin.jump-technology.com:8443/api/v1/portfolio/2201/dyn_amount_compo"

#this does not seem to work for now : 404 error
def getPortfolio(usr: str, pwd: str, base_url: str, portfolio_id: str):
  portfolio_url = base_url
  portfolio_url += 'portfolio/'
  portfolio_url += portfolio_id
  portfolio_url += 'dyn_amount_compo'

  r = requests.get(portfolio_url, auth=(usr, pwd))
  return r


def createPortfolio(portfolio: list, assets: list):
  assets_list = []
  for ind in portfolio:
    asset_id = str(assets[ind])
    asset_dict = { 'asset': asset_id,
                   'quantity': 1 #this should probably be modified
                 }
    portfolio_asset = { 'asset': asset_dict }
    assets_list.append(portfolio_asset)
  
  #build dict to send
  dict_values = { '2013-06-14': assets_list } #written in the subject
  dict_currency = { 'code': 'EUR'}
  dict_portfolio = { 'label': 'EPITA_PTF_1',
                     'currency': dict_currency,
                     'type': 'front', #written in the subject
                     'values' : dict_values
                   }

  return dict_portfolio


def sendPortfolio(jsonPortfolio: dict, usr:str, pwd:str):
    req = requests.put(url_post_portfolio, data=jsonPortfolio, auth=(usr, pwd))
    return req
