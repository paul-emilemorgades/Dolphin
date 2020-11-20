from req_get_actifs import *
from computePortefolio import computePortfolio
group_id = "EPITA_GROUPE2"
group_pwd = "PcA7s3Rnzsch6M79"
jump_base_url = 'https://dolphin.jump-technology.com:8443/api/v1/'

#print result from request getting all actifs unfiltered
print_request(get_all_actifs(group_id, group_pwd, jump_base_url))

#main

asset_ids = get_asset_ids(group_id, group_pwd, jump_base_url)#Claire
listOfAllReturns =  create_return_matrix(group_id, group_pwd, jump_base_url, asset_ids)#Claire
portfolio = computePortfolio(listOfAllReturns) #Pio
jsonPortfolio = portfolioToJson(portfolio)
sendPortfolio(jsonPortfolio) # Tanguy
