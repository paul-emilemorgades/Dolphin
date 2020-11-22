from req_get_actifs import *
from computePortefolio import computePortfolio
from sendPortfolio import *
#from listOfAllReturns import a
group_id = "EPITA_GROUPE2"
group_pwd = "PcA7s3Rnzsch6M79"
jump_base_url = 'https://dolphin.jump-technology.com:8443/api/v1/'

#main

#get list of ids of assets which are of type STOCK
asset_ids = get_asset_ids(group_id, group_pwd, jump_base_url)

#get portfolio id, the id to which we will post our portfolio
portfolio_id = get_portfolio_id(group_id, group_pwd, jump_base_url)

#get list of lists of returns at each date for each asset
listOfAllReturns =  create_return_matrix(group_id, group_pwd, jump_base_url, asset_ids)


#listOfAllReturns = a
#compute the 'best' portefolio
portfolio = computePortfolio(listOfAllReturns) 

#get portfolio as dict for PUT request
my_dict = createPortfolio(portfolio, asset_ids)

print_request(sendPortfolio(my_dict, group_id, group_pwd)) # Tanguy
