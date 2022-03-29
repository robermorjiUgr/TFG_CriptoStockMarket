# -*- coding: utf-8 -*-
import requests as r
import json
from pandas.io.json import json_normalize
import admindata

#---------------------------------------------- PRECIOS BITCOIN --------------------------------------------------------
#URL que contiene los datos

bitcoin_URL = 'https://www.coinbase.com/graphql/query?&operationName=useGetPricesForAssetPageQuery&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%2259282a0565bfbdc0477f69ad3ae4b687c93d75c808445386bfbfa70be7b4a976%22%7D%7D&variables=%7B%22skip%22%3Afalse%2C%22uuid%22%3A%225b71fc48-3dd3-540c-809b-f8c94d0e68b5%22%2C%22currency%22%3A%22USD%22%7D'
res = r.get(bitcoin_URL)

search_cookies = res.cookies

get_data = {'method':'GET'}
headers = {'user_agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Mobile Safari/537.36'}

res_get=r.get(bitcoin_URL, data=get_data, cookies=search_cookies,headers=headers)   #Lanzamos petición

values = res_get.json()
df = json_normalize(values)
precios_BTC = df['data.assetByUuid.priceDataForAll.quotes'].values[0]   # Precio cada 10 días desde 2013
print("Bitcoin")
for precio in reversed(precios_BTC):
    admindata.insertarDatosPrecios("Bitcoin", precio)

#---------------------------------------------- PRECIOS ETHEREUM -------------------------------------------------------
#URL que contiene los datos
ethereum_URL = 'https://www.coinbase.com/graphql/query?&operationName=useGetPricesForAssetPageQuery&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%2259282a0565bfbdc0477f69ad3ae4b687c93d75c808445386bfbfa70be7b4a976%22%7D%7D&variables=%7B%22skip%22%3Afalse%2C%22uuid%22%3A%22d85dce9b-5b73-5c3c-8978-522ce1d1c1b4%22%2C%22currency%22%3A%22USD%22%7D'
res = r.get(ethereum_URL)

search_cookies = res.cookies

get_data = {'method':'GET'}
headers = {'user_agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Mobile Safari/537.36'}

res_get=r.get(ethereum_URL, data=get_data, cookies=search_cookies,headers=headers)   #Lanzamos petición

values = res_get.json()
df = json_normalize(values)
precios_ETH = df['data.assetByUuid.priceDataForAll.quotes'].values[0]   # Precio cada 10 días desde 2013
print("Ethereum")
for precio in reversed(precios_ETH):
    admindata.insertarDatosPrecios("Ethereum", precio)

#---------------------------------------------- PRECIOS SOLANA -------------------------------------------------------
#URL que contiene los datos
solana_URL = 'https://www.coinbase.com/graphql/query?&operationName=useGetPricesForAssetPageQuery&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%2259282a0565bfbdc0477f69ad3ae4b687c93d75c808445386bfbfa70be7b4a976%22%7D%7D&variables=%7B%22skip%22%3Afalse%2C%22uuid%22%3A%224f039497-3af8-5bb3-951c-6df9afa9be1c%22%2C%22currency%22%3A%22USD%22%7D'
res = r.get(solana_URL)

search_cookies = res.cookies

get_data = {'method':'GET'}
headers = {'user_agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Mobile Safari/537.36'}

res_get=r.get(solana_URL, data=get_data, cookies=search_cookies,headers=headers)   #Lanzamos petición

values = res_get.json()
df = json_normalize(values)
precios_SOL = df['data.assetByUuid.priceDataForAll.quotes'].values[0]   # Precio cada 2 días desde 2020
print("Solana")
for precio in reversed(precios_SOL):
    admindata.insertarDatosPrecios("Solana", precio)

#---------------------------------------------- PRECIOS CARDANO -------------------------------------------------------
#URL que contiene los datos
cardano_URL = 'https://www.coinbase.com/graphql/query?&operationName=useGetPricesForAssetPageQuery&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%2259282a0565bfbdc0477f69ad3ae4b687c93d75c808445386bfbfa70be7b4a976%22%7D%7D&variables=%7B%22skip%22%3Afalse%2C%22uuid%22%3A%2263062039-7afb-56ff-8e19-5e3215dc404a%22%2C%22currency%22%3A%22USD%22%7D'
res = r.get(cardano_URL)

search_cookies = res.cookies

get_data = {'method':'GET'}
headers = {'user_agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Mobile Safari/537.36'}

res_get=r.get(cardano_URL, data=get_data, cookies=search_cookies,headers=headers)   #Lanzamos petición

values = res_get.json()
df = json_normalize(values)
precios_ADA = df['data.assetByUuid.priceDataForAll.quotes'].values[0]   # Precio cada 5 días desde 2017
print("Cardano")
for precio in reversed(precios_ADA):
    admindata.insertarDatosPrecios("Cardano", precio)

#---------------------------------------------- PRECIOS TETHER -------------------------------------------------------
#URL que contiene los datos
tether_URL = 'https://www.coinbase.com/graphql/query?&operationName=useGetPricesForAssetPageQuery&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%2259282a0565bfbdc0477f69ad3ae4b687c93d75c808445386bfbfa70be7b4a976%22%7D%7D&variables=%7B%22skip%22%3Afalse%2C%22uuid%22%3A%22b26327c1-9a34-51d9-b982-9b29e6012648%22%2C%22currency%22%3A%22USD%22%7D'
res = r.get(tether_URL)

search_cookies = res.cookies

get_data = {'method':'GET'}
headers = {'user_agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Mobile Safari/537.36'}

res_get=r.get(tether_URL, data=get_data, cookies=search_cookies,headers=headers)   #Lanzamos petición

values = res_get.json()
df = json_normalize(values)
precios_USDT = df['data.assetByUuid.priceDataForAll.quotes'].values[0]   # Precio cada 5 días desde 2017
print("Tether")
for precio in reversed(precios_USDT):
    admindata.insertarDatosPrecios("Tether", precio)

#---------------------------------------------- PRECIOS BINANCE -------------------------------------------------------
#URL que contiene los datos
binance_URL = 'https://www.coinbase.com/graphql/query?&operationName=useGetPricesForAssetPageQuery&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%2259282a0565bfbdc0477f69ad3ae4b687c93d75c808445386bfbfa70be7b4a976%22%7D%7D&variables=%7B%22skip%22%3Afalse%2C%22uuid%22%3A%22eb8ab5cb-d2a5-5068-88af-21c3ed92757a%22%2C%22currency%22%3A%22USD%22%7D'
res = r.get(binance_URL)

search_cookies = res.cookies

get_data = {'method':'GET'}
headers = {'user_agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Mobile Safari/537.36'}

res_get=r.get(binance_URL, data=get_data, cookies=search_cookies,headers=headers)   #Lanzamos petición

values = res_get.json()
df = json_normalize(values)
precios_BNC = df['data.assetByUuid.priceDataForAll.quotes'].values[0]   # Precio cada 5 días desde 2017
print("Binance")
for precio in reversed(precios_BNC):
    admindata.insertarDatosPrecios("Binance", precio)

#---------------------------------------------- PRECIOS USDCoin -------------------------------------------------------
#URL que contiene los datos
USDCoin_URL = 'https://www.coinbase.com/graphql/query?&operationName=useGetPricesForAssetPageQuery&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%2259282a0565bfbdc0477f69ad3ae4b687c93d75c808445386bfbfa70be7b4a976%22%7D%7D&variables=%7B%22skip%22%3Afalse%2C%22uuid%22%3A%222b92315d-eab7-5bef-84fa-089a131333f5%22%2C%22currency%22%3A%22USD%22%7D'
res = r.get(USDCoin_URL)

search_cookies = res.cookies

get_data = {'method':'GET'}
headers = {'user_agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Mobile Safari/537.36'}

res_get=r.get(USDCoin_URL, data=get_data, cookies=search_cookies,headers=headers)   #Lanzamos petición

values = res_get.json()
df = json_normalize(values)
precios_USDC = df['data.assetByUuid.priceDataForAll.quotes'].values[0]   # Precio cada 5 días desde 2017
print("USDCoin")
for precio in reversed(precios_USDC):
    admindata.insertarDatosPrecios("USDCoin", precio)

#---------------------------------------------- PRECIOS XRP -------------------------------------------------------
#URL que contiene los datos
xrp_URL = 'https://www.coinbase.com/graphql/query?&operationName=useGetPricesForAssetPageQuery&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%2259282a0565bfbdc0477f69ad3ae4b687c93d75c808445386bfbfa70be7b4a976%22%7D%7D&variables=%7B%22skip%22%3Afalse%2C%22uuid%22%3A%22e17a44c8-6ea1-564f-a02c-2a9ca1d8eec4%22%2C%22currency%22%3A%22USD%22%7D'
res = r.get(xrp_URL)

search_cookies = res.cookies

get_data = {'method':'GET'}
headers = {'user_agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Mobile Safari/537.36'}

res_get=r.get(xrp_URL, data=get_data, cookies=search_cookies,headers=headers)   #Lanzamos petición

values = res_get.json()
df = json_normalize(values)
precios_XRP = df['data.assetByUuid.priceDataForAll.quotes'].values[0]   # Precio cada 10 días desde 2013
print("XRP")
for precio in reversed(precios_XRP):
    admindata.insertarDatosPrecios("XRP", precio)

#---------------------------------------------- PRECIOS TERRA ----------------------------------------------------------
#URL que contiene los datos
terra_URL = 'https://www.coinbase.com/graphql/query?&operationName=useGetPricesForAssetPageQuery&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%2259282a0565bfbdc0477f69ad3ae4b687c93d75c808445386bfbfa70be7b4a976%22%7D%7D&variables=%7B%22skip%22%3Afalse%2C%22uuid%22%3A%2205120843-11c1-5b66-9df2-395db6d7ed6b%22%2C%22currency%22%3A%22USD%22%7D'
res = r.get(terra_URL)

search_cookies = res.cookies

get_data = {'method':'GET'}
headers = {'user_agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Mobile Safari/537.36'}

res_get=r.get(terra_URL, data=get_data, cookies=search_cookies,headers=headers)     #Lanzamos petición

values = res_get.json()
df = json_normalize(values)
precios_UST = df['data.assetByUuid.priceDataForAll.quotes'].values[0]   # Precio cada 2 días desde 2019
print("TERRA")
for precio in reversed(precios_UST):
    admindata.insertarDatosPrecios("Terra", precio)


