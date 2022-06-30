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

# Creamos dos colecciones para registrar la informacion de cada criptomoneda, y en cada una de las bases de datos:
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

# Creamos otra coleccion para registrar la informacion sobre los indicadores financieros
financial_collectionBTC = dbBTC["financial_indicators"]

financial_collectionETH = dbETH["financial_indicators"]

financial_collectionSOL = dbSOL["financial_indicators"]

financial_collectionADA = dbADA["financial_indicators"]

financial_collectionUSDT = dbUSDT["financial_indicators"]

financial_collectionBNC = dbBNC["financial_indicators"]

financial_collectionUSDC = dbUSDC["financial_indicators"]

financial_collectionXRP = dbXRP["financial_indicators"]

financial_collectionUST = dbUST["financial_indicators"]

# Creamos otra coleccion para registrar los resultados de la prediccion
prediction_collectionBTC = dbBTC["predictions"]

prediction_collectionETH = dbETH["predictions"]

prediction_collectionSOL = dbSOL["predictions"]

prediction_collectionADA = dbADA["predictions"]

prediction_collectionUSDT = dbUSDT["predictions"]

prediction_collectionBNC = dbBNC["predictions"]

prediction_collectionUSDC = dbUSDC["predictions"]

prediction_collectionXRP = dbXRP["predictions"]

prediction_collectionUST = dbUST["predictions"]



# Devuelve true en el caso en el que la fecha1 sea mas reciente que fecha2
def masReciente(fecha1, fecha2):
    mas_reciente = False

    date1 = parse(fecha1)
    date2 = parse(fecha2)

    if date1 > date2:     # date1 es mas reciente que date2
        mas_reciente = True

    return mas_reciente


# Insercion de diferentes datos de criptomonedas en cada BD
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


# Inserta en la coleccion de precios de cada criptomoneda aquellos valores que no haya introducido aun
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


# Insercion de diferentes datos de criptomonedas en cada BD
def insertarIndicadoresFinancieros(cripto, rentabilidad, riesgo):
    registro_indicadores = {
        "Datetime": datetime.now(),
        "Profitability": rentabilidad,
        "Risk": riesgo
    }
    if cripto == "Bitcoin":
        financial_collectionBTC.insert_one(registro_indicadores)
    if cripto == "Ethereum":
        financial_collectionETH.insert_one(registro_indicadores)
    if cripto == "Solana":
        financial_collectionSOL.insert_one(registro_indicadores)
    if cripto == "Cardano":
        financial_collectionADA.insert_one(registro_indicadores)
    if cripto == "Tether":
        financial_collectionUSDT.insert_one(registro_indicadores)
    if cripto == "Binance":
        financial_collectionBNC.insert_one(registro_indicadores)
    if cripto == "USDCoin":
        financial_collectionUSDC.insert_one(registro_indicadores)
    if cripto == "XRP":
        financial_collectionXRP.insert_one(registro_indicadores)
    if cripto == "Terra":
        financial_collectionUST.insert_one(registro_indicadores)

# Insercion de diferentes datos de criptomonedas en cada BD
def insertarPredicciones(cripto, datetime, prediccion):
    registro_predicciones = {
        "Datetime": datetime,
        "Prediction": prediccion,
    }
    if cripto == "Bitcoin":
        prediction_collectionBTC.insert_one(registro_predicciones)
    if cripto == "Ethereum":
        prediction_collectionETH.insert_one(registro_predicciones)
    if cripto == "Solana":
        prediction_collectionSOL.insert_one(registro_predicciones)
    if cripto == "Cardano":
        prediction_collectionADA.insert_one(registro_predicciones)
    if cripto == "Tether":
        prediction_collectionUSDT.insert_one(registro_predicciones)
    if cripto == "Binance":
        prediction_collectionBNC.insert_one(registro_predicciones)
    if cripto == "USDCoin":
        prediction_collectionUSDC.insert_one(registro_predicciones)
    if cripto == "XRP":
        prediction_collectionXRP.insert_one(registro_predicciones)
    if cripto == "Terra":
        prediction_collectionUST.insert_one(registro_predicciones)


# Devuelve valores actuales de una criptomoneda referidos a precio, capitalizacion, volumen y variacion
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


# Devuelve un historico de precios de una criptomoneda junto a la fecha en la que tomo ese valor
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

# Devuelve valores referidos a los indicadores de una determinada criptomoneda
def consultarIndicadores(cripto):
    if cripto == "Bitcoin":
        datos = financial_collectionBTC.find_one(sort=[('_id', -1)])
    if cripto == "Ethereum":
        datos = financial_collectionETH.find_one(sort=[('_id', -1)])
    if cripto == "Solana":
        datos = financial_collectionSOL.find_one(sort=[('_id', -1)])
    if cripto == "Cardano":
        datos = financial_collectionADA.find_one(sort=[('_id', -1)])
    if cripto == "Tether":
        datos = financial_collectionUSDT.find_one(sort=[('_id', -1)])
    if cripto == "Binance":
        datos = financial_collectionBNC.find_one(sort=[('_id', -1)])
    if cripto == "USDCoin":
        datos = financial_collectionUSDC.find_one(sort=[('_id', -1)])
    if cripto == "XRP":
        datos = financial_collectionXRP.find_one(sort=[('_id', -1)])
    if cripto == "Terra":
        datos = financial_collectionUST.find_one(sort=[('_id', -1)])

    return datos

# Devuelve valores referidos a los resultados de la prediccion
def consultarPrediction(cripto):
    if cripto == "Bitcoin":
        datos = prediction_collectionBTC.find({'Datetime': {"$gte": datetime.now()}})
    if cripto == "Ethereum":
        datos = prediction_collectionETH.find({'Datetime': {"$gte": datetime.now()}})
    if cripto == "Solana":
        datos = prediction_collectionSOL.find({'Datetime': {"$gte": datetime.now()}})
    if cripto == "Cardano":
        datos = prediction_collectionADA.find({'Datetime': {"$gte": datetime.now()}})
    if cripto == "Tether":
        datos = prediction_collectionUSDT.find({'Datetime': {"$gte": datetime.now()}})
    if cripto == "Binance":
        datos = prediction_collectionBNC.find({'Datetime': {"$gte": datetime.now()}})
    if cripto == "USDCoin":
        datos = prediction_collectionUSDC.find({'Datetime': {"$gte": datetime.now()}})
    if cripto == "XRP":
        datos = prediction_collectionXRP.find({'Datetime': {"$gte": datetime.now()}})
    if cripto == "Terra":
        datos = prediction_collectionUST.find({'Datetime': {"$gte": datetime.now()}})

    return datos



