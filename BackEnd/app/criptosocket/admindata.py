import pymongo
from datetime import datetime
import json

# Establecemos conexion y creamos las bases de datos (una para cada cripto)
connection = pymongo.MongoClient('localhost', 27017)
dbBTC = connection["dbBitcoin"]
dbETH = connection["dbEthereum"]
dbSOL = connection["dbSolana"]
dbADA = connection["dbCardano"]
dbUSDT = connection["dbTether"]
dbBNC = connection["dbBinance"]
dbUSDC = connection["dbUSDCoin"]
dbXRP = connection["dbXRP"]
dbUST = connection["dbTerra"]

# Creamos dos colecciones para cada una de las bases de datos:
#   - La primera de ellas sera para llevar un registro historico extenso del precio
#   - La segunda sera para llevar un registro de datos mas alla del precio
price_collectionBTC = dbBTC["price_data"]
extended_collectionBTC = dbBTC["extended_data"]

price_collectionETH = dbETH["price_data"]
extended_collectionETH = dbETH["extended_data"]

price_collectionSOL = dbSOL["price_data"]
extended_collectionSOL = dbSOL["extended_data"]

price_collectionADA = dbADA["price_data"]
extended_collectionADA = dbADA["extended_data"]

price_collectionUSDT = dbUSDT["price_data"]
extended_collectionUSDT = dbUSDT["extended_data"]

price_collectionBNC = dbBNC["price_data"]
extended_collectionBNC = dbBNC["extended_data"]

price_collectionUSDC = dbUSDC["price_data"]
extended_collectionUSDC = dbUSDC["extended_data"]

price_collectionXRP = dbXRP["price_data"]
extended_collectionXRP = dbXRP["extended_data"]

price_collectionUST = dbUST["price_data"]
extended_collectionUST = dbUST["extended_data"]


# Funcion para la insercion de los precios en cada base de datos
def insertarPrecios(cripto, precio):
    registro_precio = {
        "Datetime": datetime.now(),
        "Price": precio,
    }
    if cripto == "Bitcoin":
        price_collectionBTC.insert_one(registro_precio)
    if cripto == "Ethereum":
        price_collectionETH.insert_one(registro_precio)
    if cripto == "Solana":
        price_collectionSOL.insert_one(registro_precio)
    if cripto == "Cardano":
        price_collectionADA.insert_one(registro_precio)
    if cripto == "Tether":
        price_collectionUSDT.insert_one(registro_precio)
    if cripto == "Binance":
        price_collectionBNC.insert_one(registro_precio)
    if cripto == "USDCoin":
        price_collectionUSDC.insert_one(registro_precio)
    if cripto == "XRP":
        price_collectionXRP.insert_one(registro_precio)
    if cripto == "Terra":
        price_collectionUST.insert_one(registro_precio)

# Funcion para la insercion de los precios en cada base de datos
def insertarDatosExtendidos(cripto, precio, capital, monedas, volumen, variacion):
    registro_datosextendidos = {
        "Datetime": datetime.now(),
        "Price": precio,
        "MarketCap": capital,
        "Coins": monedas,
        "Volume": volumen,
        "%": variacion,
    }
    if cripto == "Bitcoin":
        extended_collectionBTC.insert_one(registro_datosextendidos)
    if cripto == "Ethereum":
        extended_collectionETH.insert_one(registro_datosextendidos)
    if cripto == "Solana":
        extended_collectionSOL.insert_one(registro_datosextendidos)
    if cripto == "Cardano":
        extended_collectionADA.insert_one(registro_datosextendidos)
    if cripto == "Tether":
        extended_collectionUSDT.insert_one(registro_datosextendidos)
    if cripto == "Binance":
        extended_collectionBNC.insert_one(registro_datosextendidos)
    if cripto == "USDCoin":
        extended_collectionUSDC.insert_one(registro_datosextendidos)
    if cripto == "XRP":
        extended_collectionXRP.insert_one(registro_datosextendidos)
    if cripto == "Terra":
        extended_collectionUST.insert_one(registro_datosextendidos)

