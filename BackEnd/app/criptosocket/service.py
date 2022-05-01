from urllib import request
from flask import jsonify
from flask import Blueprint
from flask_restx import Api, Resource
import pandas as pd
import json
import numpy as np
from . import admindata

criptosocket_bp = Blueprint('criptosocket', __name__)

api = Api( criptosocket_bp )
ns_criptosocket = api.namespace('criptosocket', "Proyect api dashboard CriptoSocket:")


@ns_criptosocket.route('/hello',endpoint="hello")
@ns_criptosocket.doc(description="Hello service")
class helloworld(Resource):
    
    def get(self):
        return jsonify({'hello':'world'})

# ------------------------ MICROSERVICIOS DATOS BITCOIN-------------------------
@ns_criptosocket.route('/getExtendedBitcoin', endpoint="getExtendedBitcoin")
@ns_criptosocket.doc(description="Get extended data about Bitcoin")
class BitcoinExtended(Resource):
    def get(self):
        datos_btc = admindata.consultarDatosExtendidos("Bitcoin")
        return jsonify({'Datetime':datos_btc['Datetime'],
                        'Price':datos_btc['Price'],
                        'MarketCap':datos_btc['MarketCap'],
                        'Coins':datos_btc['Coins'],
                        'Volume':datos_btc['Volume'],
                        'Change':datos_btc['Change']})

@ns_criptosocket.route('/getPriceBitcoin', endpoint="getPriceBitcoin")
@ns_criptosocket.doc(description="Get price data about Bitcoin")
class BitcoinPrice(Resource):
    def get(self):
        datos_btc = admindata.consultarPrecios("Bitcoin")
        precios = []
        for i in datos_btc:
            precios.append({'Datetime' : i['Datetime'], 'Price':i['Price']})
        return precios

# ------------------------ MICROSERVICIOS DATOS ETHEREUM-------------------------
@ns_criptosocket.route('/getExtendedEthereum', endpoint="getExtendedEthereum")
@ns_criptosocket.doc(description="Get extended data about Ethereum")
class EthereumExtended(Resource):
    def get(self):
        datos_eth = admindata.consultarDatosExtendidos("Ethereum")
        return jsonify({'Price': datos_eth['Price'],
                        'MarketCap': datos_eth['MarketCap'],
                        'Coins': datos_eth['Coins'],
                        'Volume': datos_eth['Volume'],
                        'Change': datos_eth['Change']})

@ns_criptosocket.route('/getPriceEthereum', endpoint="getPriceEthereum")
@ns_criptosocket.doc(description="Get price data about Ethereum")
class EthereumPrice(Resource):
    def get(self):
        datos_eth = admindata.consultarPrecios("Ethereum")
        precios = []
        for i in datos_eth:
            precios.append({'Datetime': i['Datetime'], 'Price': i['Price']})
        return precios

# ------------------------ MICROSERVICIOS DATOS SOLANA-------------------------
@ns_criptosocket.route('/getExtendedSolana', endpoint="getExtendedSolana")
@ns_criptosocket.doc(description="Get extended data about Solana")
class SolanaExtended(Resource):
    def get(self):
        datos_sol = admindata.consultarDatosExtendidos("Solana")
        return jsonify({'Price': datos_sol['Price'],
                        'MarketCap': datos_sol['MarketCap'],
                        'Coins': datos_sol['Coins'],
                        'Volume': datos_sol['Volume'],
                        'Change': datos_sol['Change']})

@ns_criptosocket.route('/getPriceSolana', endpoint="getPriceSolana")
@ns_criptosocket.doc(description="Get price data about Solana")
class SolanaPrice(Resource):
    def get(self):
        datos_sol = admindata.consultarPrecios("Solana")
        precios = []
        for i in datos_sol:
            precios.append({'Datetime': i['Datetime'], 'Price': i['Price']})
        return precios

# ------------------------ MICROSERVICIOS DATOS CARDANO-------------------------
@ns_criptosocket.route('/getExtendedCardano', endpoint="getExtendedCardano")
@ns_criptosocket.doc(description="Get extended data about Cardano")
class CardanoExtended(Resource):
    def get(self):
        datos_ada = admindata.consultarDatosExtendidos("Cardano")
        return jsonify({'Price': datos_ada['Price'],
                        'MarketCap': datos_ada['MarketCap'],
                        'Coins': datos_ada['Coins'],
                        'Volume': datos_ada['Volume'],
                        'Change': datos_ada['Change']})

@ns_criptosocket.route('/getPriceCardano', endpoint="getPriceCardano")
@ns_criptosocket.doc(description="Get price data about Cardano")
class CardanoPrice(Resource):
    def get(self):
        datos_ada = admindata.consultarPrecios("Cardano")
        precios = []
        for i in datos_ada:
            precios.append({'Datetime': i['Datetime'], 'Price': i['Price']})
        return precios

# ------------------------ MICROSERVICIOS DATOS Tether-------------------------
@ns_criptosocket.route('/getExtendedTether', endpoint="getExtendedTether")
@ns_criptosocket.doc(description="Get extended data about Tether")
class TetherExtended(Resource):
    def get(self):
        datos_usdt = admindata.consultarDatosExtendidos("Tether")
        return jsonify({'Price': datos_usdt['Price'],
                        'MarketCap': datos_usdt['MarketCap'],
                        'Coins': datos_usdt['Coins'],
                        'Volume': datos_usdt['Volume'],
                        'Change': datos_usdt['Change']})

@ns_criptosocket.route('/getPriceTether', endpoint="getPriceTether")
@ns_criptosocket.doc(description="Get price data about Tether")
class TetherPrice(Resource):
    def get(self):
        datos_usdt = admindata.consultarPrecios("Tether")
        precios = []
        for i in datos_usdt:
            precios.append({'Datetime': i['Datetime'], 'Price': i['Price']})
        return precios

# ------------------------ MICROSERVICIOS DATOS Binance-------------------------
@ns_criptosocket.route('/getExtendedBinance', endpoint="getExtendedBinance")
@ns_criptosocket.doc(description="Get extended data about Binance")
class BinanceExtended(Resource):
    def get(self):
        datos_bnc = admindata.consultarDatosExtendidos("Binance")
        return jsonify({'Price': datos_bnc['Price'],
                        'MarketCap': datos_bnc['MarketCap'],
                        'Coins': datos_bnc['Coins'],
                        'Volume': datos_bnc['Volume'],
                        'Change': datos_bnc['Change']})

@ns_criptosocket.route('/getPriceBinance', endpoint="getPriceBinance")
@ns_criptosocket.doc(description="Get price data about Binance")
class BinancePrice(Resource):
    def get(self):
        datos_bnc = admindata.consultarPrecios("Binance")
        precios = []
        for i in datos_bnc:
            precios.append({'Datetime': i['Datetime'], 'Price': i['Price']})
        return precios

# ------------------------ MICROSERVICIOS DATOS USDCoin-------------------------
@ns_criptosocket.route('/getExtendedUSDCoin', endpoint="getExtendedUSDCoin")
@ns_criptosocket.doc(description="Get extended data about USDCoin")
class USDCoinExtended(Resource):
    def get(self):
        datos_usdc = admindata.consultarDatosExtendidos("USDCoin")
        return jsonify({'Price': datos_usdc['Price'],
                        'MarketCap': datos_usdc['MarketCap'],
                        'Coins': datos_usdc['Coins'],
                        'Volume': datos_usdc['Volume'],
                        'Change': datos_usdc['Change']})

@ns_criptosocket.route('/getPriceUSDCoin', endpoint="getPriceUSDCoin")
@ns_criptosocket.doc(description="Get price data about USDCoin")
class USDCoinPrice(Resource):
    def get(self):
        datos_usdc = admindata.consultarPrecios("USDCoin")
        precios = []
        for i in datos_usdc:
            precios.append({'Datetime': i['Datetime'], 'Price': i['Price']})
        return precios

# ------------------------ MICROSERVICIOS DATOS XRP-------------------------
@ns_criptosocket.route('/getExtendedXRP', endpoint="getExtendedXRP")
@ns_criptosocket.doc(description="Get extended data about XRP")
class XRPExtended(Resource):
    def get(self):
        datos_XRP = admindata.consultarDatosExtendidos("XRP")
        return jsonify({'Price': datos_XRP['Price'],
                        'MarketCap': datos_XRP['MarketCap'],
                        'Coins': datos_XRP['Coins'],
                        'Volume': datos_XRP['Volume'],
                        'Change': datos_XRP['Change']})

@ns_criptosocket.route('/getPriceXRP', endpoint="getPriceXRP")
@ns_criptosocket.doc(description="Get price data about XRP")
class XRPPrice(Resource):
    def get(self):
        datos_XRP = admindata.consultarPrecios("XRP")
        precios = []
        for i in datos_XRP:
            precios.append({'Datetime': i['Datetime'], 'Price': i['Price']})
        return precios

# ------------------------ MICROSERVICIOS DATOS Terra-------------------------
@ns_criptosocket.route('/getExtendedTerra', endpoint="getExtendedTerra")
@ns_criptosocket.doc(description="Get extended data about Terra")
class TerraExtended(Resource):
    def get(self):
        datos_Terra = admindata.consultarDatosExtendidos("Terra")
        return jsonify({'Price': datos_Terra['Price'],
                        'MarketCap': datos_Terra['MarketCap'],
                        'Coins': datos_Terra['Coins'],
                        'Volume': datos_Terra['Volume'],
                        'Change': datos_Terra['Change']})

@ns_criptosocket.route('/getPriceTerra', endpoint="getPriceTerra")
@ns_criptosocket.doc(description="Get price data about Terra")
class TerraPrice(Resource):
    def get(self):
        datos_Terra = admindata.consultarPrecios("Terra")
        precios = []
        for i in datos_Terra:
            precios.append({'Datetime': i['Datetime'], 'Price': i['Price']})
        return precios

