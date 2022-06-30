#!/bin/sh

source /Users/juliocamposrodriguez/Desktop/TFG/Proyecto/TFG_CriptoStockMarket/BackEnd/criptoEnv/bin/activate
python3 /Users/juliocamposrodriguez/Desktop/TFG/Proyecto/TFG_CriptoStockMarket/BackEnd/app/criptosocket/bot_prices.py
python3 /Users/juliocamposrodriguez/Desktop/TFG/Proyecto/TFG_CriptoStockMarket/BackEnd/app/criptosocket/bot_indicadores.py