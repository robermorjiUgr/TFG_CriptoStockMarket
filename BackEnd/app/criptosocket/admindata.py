import pymongo
from datetime import datetime
from dateutil.parser import parse
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

def masReciente(fecha1, fecha2):
    mas_reciente = False

    date1 = parse(fecha1)
    date2 = parse(fecha2)

    if date1 > date2:     # date1 es mas reciente que date2
        mas_reciente = True

    return mas_reciente

# Funcion para la insercion de los precios en cada base de datos
def insertarDatosExtendidos(cripto, precio, capital, monedas, volumen, variacion):
    registro_datosextendidos = {
        "Datetime": datetime.now(),
        "Price": precio,
        "MarketCap": capital,
        "Coins": monedas,
        "Volume": volumen,
        "Change": variacion,
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

def insertarDatosPrecios(cripto, precio):
    # Creamos el registro
    registro_precio = {
        "Datetime": precio['timestamp'],
        "Price": float(precio['price']),
    }

    if cripto == "Bitcoin":
        if price_collectionBTC.find_one(sort=[('_id', -1)]) != None:
            lastdate = price_collectionBTC.find_one(sort=[('_id', -1)])['Datetime']
            if masReciente(precio['timestamp'], lastdate):
                price_collectionBTC.insert_one(registro_precio)
        else:
            price_collectionBTC.insert_one(registro_precio)

    if cripto == "Ethereum":
        if price_collectionETH.find_one(sort=[('_id', -1)]) != None:
            lastdate = price_collectionETH.find_one(sort=[('_id', -1)])['Datetime']
            if masReciente(precio['timestamp'], lastdate):
                price_collectionETH.insert_one(registro_precio)
        else:
            price_collectionETH.insert_one(registro_precio)

    if cripto == "Solana":
        if price_collectionSOL.find_one(sort=[('_id', -1)]) != None:
            lastdate = price_collectionSOL.find_one(sort=[('_id', -1)])['Datetime']
            if masReciente(precio['timestamp'], lastdate):
                price_collectionSOL.insert_one(registro_precio)
        else:
            price_collectionSOL.insert_one(registro_precio)
    if cripto == "Cardano":
        if price_collectionADA.find_one(sort=[('_id', -1)]) != None:
            lastdate = price_collectionADA.find_one(sort=[('_id', -1)])['Datetime']
            if masReciente(precio['timestamp'], lastdate):
                price_collectionADA.insert_one(registro_precio)
        else:
            price_collectionADA.insert_one(registro_precio)

    if cripto == "Tether":
        if price_collectionUSDT.find_one(sort=[('_id', -1)]) != None:
            lastdate = price_collectionUSDT.find_one(sort=[('_id', -1)])['Datetime']
            if masReciente(precio['timestamp'], lastdate):
                price_collectionUSDT.insert_one(registro_precio)
        else:
            price_collectionUSDT.insert_one(registro_precio)

    if cripto == "Binance":
        if price_collectionBNC.find_one(sort=[('_id', -1)]) != None:
            lastdate = price_collectionBNC.find_one(sort=[('_id', -1)])['Datetime']
            if masReciente(precio['timestamp'], lastdate):
                price_collectionBNC.insert_one(registro_precio)
        else:
            price_collectionBNC.insert_one(registro_precio)

    if cripto == "USDCoin":
        if price_collectionUSDC.find_one(sort=[('_id', -1)]) != None:
            lastdate = price_collectionUSDC.find_one(sort=[('_id', -1)])['Datetime']
            if masReciente(precio['timestamp'], lastdate):
                price_collectionUSDC.insert_one(registro_precio)
        else:
            price_collectionUSDC.insert_one(registro_precio)

    if cripto == "XRP":
        if price_collectionXRP.find_one(sort=[('_id', -1)]) != None:
            lastdate = price_collectionXRP.find_one(sort=[('_id', -1)])['Datetime']
            if masReciente(precio['timestamp'], lastdate):
                price_collectionXRP.insert_one(registro_precio)
        else:
            price_collectionXRP.insert_one(registro_precio)

    if cripto == "Terra":
        if price_collectionUST.find_one(sort=[('_id', -1)]) != None:
            lastdate = price_collectionUST.find_one(sort=[('_id', -1)])['Datetime']
            if masReciente(precio['timestamp'], lastdate):
                price_collectionUST.insert_one(registro_precio)
        else:
            price_collectionUST.insert_one(registro_precio)


def consultarDatosExtendidos(cripto):
    if cripto == "Bitcoin":
        datos = extended_collectionBTC.find_one(sort=[('_id', -1)])
    if cripto == "Ethereum":
        datos = extended_collectionETH.find_one(sort=[('_id', -1)])
    if cripto == "Solana":
        datos = extended_collectionSOL.find_one(sort=[('_id', -1)])
    if cripto == "Cardano":
        datos = extended_collectionADA.find_one(sort=[('_id', -1)])
    if cripto == "Tether":
        datos = extended_collectionUSDT.find_one(sort=[('_id', -1)])
    if cripto == "Binance":
        datos = extended_collectionBNC.find_one(sort=[('_id', -1)])
    if cripto == "USDCoin":
        datos = extended_collectionUSDC.find_one(sort=[('_id', -1)])
    if cripto == "XRP":
        datos = extended_collectionXRP.find_one(sort=[('_id', -1)])
    if cripto == "Terra":
        datos = extended_collectionUST.find_one(sort=[('_id', -1)])

    return datos

def consultarPrecios(cripto):
    if cripto == "Bitcoin":
        datos = price_collectionBTC.find()
    if cripto == "Ethereum":
        datos = price_collectionETH.find()
    if cripto == "Solana":
        datos = price_collectionSOL.find()
    if cripto == "Cardano":
        datos = price_collectionADA.find()
    if cripto == "Tether":
        datos = price_collectionUSDT.find()
    if cripto == "Binance":
        datos = price_collectionBNC.find()
    if cripto == "USDCoin":
        datos = price_collectionUSDC.find()
    if cripto == "XRP":
        datos = price_collectionXRP.find()
    if cripto == "Terra":
        datos = price_collectionUST.find()

    return datos

