import requests

def get_all_actifs(usr : str, pwd : str, base_url : str):
  actifs_url = base_url
  actifs_url += 'asset'
  r = requests.get(actifs_url, auth=(usr, pwd))
  return r

def print_request(request):
  print('----TYPE----')
  print(type(request))
  print('----STATUS----')
  print(request.status_code)
  print('----HEADERS----')
  print(request.headers)
  print('----TEXT----')
  print(request.text)
