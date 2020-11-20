import requests
import json

#get unfiltered assets
def get_all_assets(usr : str, pwd : str, base_url : str):
  actifs_url = base_url
  actifs_url += 'asset'
  r = requests.get(actifs_url, auth=(usr, pwd))
  return r


#get all quotation values between two dates
def get_quote_for_asset(usr: str, pwd: str, base_url: str, asset_id: str):
  #interval at which we should get asset quote
  start_date = '2016-06-01'
  end_date = '2020-09-30'
  
  #building the request URL
  quote_url = base_url
  quote_url += 'asset/' + asset_id + '/'
  quote_url += 'quote?start_date=' + start_date + '&end_date=' + end_date

  #create request to return
  r = requests.get(quote_url, auth=(usr, pwd))
  return r


#test print function for requests
def print_request(request):
  print('----TYPE----')
  print(type(request))
  print('----STATUS----')
  print(request.status_code)
  print('----HEADERS----')
  print(request.headers)
  print('----TEXT----')
  print(request.text)

#create list of asset ids
def get_asset_ids(usr: str, pwd: str, base_url: str):
  all_assets_req = get_all_assets(usr, pwd, base_url)
  assets_dict = json.loads(all_assets_req.text)
  list_asset_id = []

  #get all asset ids into a list
  for asset in assets_dict:
    asset_id_json = asset['ASSET_DATABASE_ID']
    list_asset_id.append(asset_id_json['value'])

  return list_asset_id


#parse requests to get all returns from all assets during the interval
def create_return_matrix(usr: str, pwd: str, base_url: str, list_asset_id: list):
  #get all returns of assets in list of lists
  list_returns = []
  for asset_id in list_asset_id:
    asset_returns = []
    quote_asset_req = get_quote_for_asset(usr, pwd, base_url, asset_id)
    quote_dict = json.loads(quote_asset_req.text)
    for quote in quote_dict:
      quote_return = quote['return']
      asset_returns.append(quote_return['value'])
    list_returns.append(asset_returns)
  return list_returns

