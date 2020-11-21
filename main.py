from req_get_actifs import *
from computePortefolio import computePortfolio
from sendPortfolio import *

group_id = "EPITA_GROUPE2"
group_pwd = "PcA7s3Rnzsch6M79"
jump_base_url = 'https://dolphin.jump-technology.com:8443/api/v1/'

#main

asset_ids = get_asset_ids(group_id, group_pwd, jump_base_url)#Claire
listOfAllReturns =  create_return_matrix(group_id, group_pwd, jump_base_url, asset_ids)#Claire
portfolio = computePortfolio(listOfAllReturns) #Pio
jsonPortfolio = portfolioToJson(portfolio)
print_request(sendPortfolio(jsonPortfolio, group_id, group_pwd)) # Tanguy
