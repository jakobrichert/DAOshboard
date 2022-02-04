from webbrowser import get
import requests
import json
def get_data():
    url = 'https://api.covalenthq.com/v1/1/uniswap_v3/pools/?quote-currency=USD&format=JSON&page-size=10000&key=yourkey'
    r = requests.get(url)
    data = json.loads(r.text)
    logolist = []
    addresslist = []
    tickerlist = []
    namelist = []

    for x in (data['data']['items']):
        logolist.append((x['token_0']['logo_url']))
        addresslist.append((x['token_0']['contract_address']))
        tickerlist.append((x['token_0']['contract_ticker_symbol']))
        namelist.append((x['token_0']['contract_name']))

    logos = dict(zip(addresslist, logolist))
    address = dict(zip(namelist, addresslist))
    ticker = dict(zip(addresslist, tickerlist))
    name = dict(zip(addresslist, namelist))



    
    
    return (logos,address,ticker,name)

#Give address of DAO and it will compute the transparency score, returns a dict with contract address keys and
#Transparency score
def get_transparency(name):
    transparency = 0
    url = 'https://api.covalenthq.com/v1/1/tokens/'+ name +'/token_holders/?quote-currency=USD&format=JSON&page-size=10000&key=yourkey'
    r = requests.get(url)
    data = json.loads(r.text)
    #### Start of the transparency calculation ####
    #### This would need to be updated to be more complex in the future ####
    
    try:
        holders = len(data['data']['items'])
        if holders>= 100000:
            transparency+=5
        elif holders>= 10000:
            transparency+=3
        elif holders>= 1000:
            transparency+= 1
    except:
        transparency = 'NA'
    
    
    transparent_dict = {name:transparency}


    
    
    return transparent_dict






#for y in range(10):
#    print(get_transparency(newaddress[20+y]))











