# -*- coding: utf-8 -*-
import os
import time
import admindata
import requests
import selenium.webdriver as webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
from bs4 import BeautifulSoup
import pandas as pd

# Convierte texto en formato: [1..9].[1..9][M or B] a número
def textToNumber(texto):
        numero =''
        contador_decimales = 0
        contar = False
        for caracter in texto:
                if contar and caracter !='M' and caracter !='B':
                        contador_decimales += 1
                if caracter != '.' and caracter!= 'M' and caracter !='B':
                        numero += caracter
                else:
                        contar = True
                if caracter == 'M':
                        i = 0
                        while i < (6-contador_decimales):
                                numero += '0'
                                i += 1
                if caracter == 'B':
                        i = 0
                        while i < (9-contador_decimales):
                                numero += '0'
                                i += 1

        return float(numero)

# Convierte texto en formato: [1..9]% a número
def percentToNumber(texto):
        numero =''
        for caracter in texto:
                if caracter !='%':
                        numero += caracter

        return float(numero.replace('−', '-'))

def main():
        #----------------------------------- WEBSCRAPING ------------------------------------

        # Indicamos el navegador a utilizar y quien va a realizar esa operacion
        user_agent = 'Mozilla (macOS Big Sur 11.6) JulioCampos Firefox 98.0.1'
        FireFoxProfile = webdriver.FirefoxProfile()
        FireFoxProfile.set_preference("general.useragent.override", user_agent);
        # Lanzamos el navegador, indicando como opciones que no es necesario abrirlo
        option = Options()
        option.add_argument('--headless')
        browser = webdriver.Firefox(options=option,
                executable_path="/Users/juliocamposrodriguez/Desktop/TFG/Proyecto/TFG_CriptoStockMarket/BackEnd/geckodriver",
                firefox_profile=FireFoxProfile)
        browser.implicitly_wait(10)  # Si no devuelve nada en 10 segundos dara error
        # Indicamos la url que queremos visitar
        url = "https://es.tradingview.com/markets/cryptocurrencies/prices-all/"
        browser.get(url)
        df = pd.read_html(browser.page_source)[1]      # Dataframe que contiene la tabla con la que información

        # Seleccionamos unicamente las filas de la tabla que nos interesan
        bitcoin = df.loc[df["NombreNo se encontraron coincidencias"]=='Bitcoin']
        ethereum = df.loc[df["NombreNo se encontraron coincidencias"]=='Ethereum']
        solana = df.loc[df["NombreNo se encontraron coincidencias"]=='Solana']
        cardano = df.loc[df["NombreNo se encontraron coincidencias"]=='Cardano']
        tether = df.loc[df["NombreNo se encontraron coincidencias"]=='Tether']
        binance = df.loc[df["NombreNo se encontraron coincidencias"]=='Binance Coin']
        usdc = df.loc[df["NombreNo se encontraron coincidencias"]=='USD Coin']
        xrp = df.loc[df["NombreNo se encontraron coincidencias"]=='XRP']
        terra = df.loc[df["NombreNo se encontraron coincidencias"]=='TerraUSD']

        precio = bitcoin["Última"].values
        cap = textToNumber(bitcoin["Capitalización de mercado"].values[0])
        coins = textToNumber(bitcoin["Total monedas"].values[0])
        volume = textToNumber(bitcoin["Volumen negociado"].values[0])
        change = percentToNumber(bitcoin["% de cambio"].values[0])
        admindata.insertarDatosExtendidos("Bitcoin", precio[0], cap, coins, volume, change)

        precio = ethereum["Última"].values
        cap = textToNumber(ethereum["Capitalización de mercado"].values[0])
        coins = textToNumber(ethereum["Total monedas"].values[0])
        volume = textToNumber(ethereum["Volumen negociado"].values[0])
        change = percentToNumber(ethereum["% de cambio"].values[0])
        admindata.insertarDatosExtendidos("Ethereum", precio[0], cap, coins, volume, change)

        precio = solana["Última"].values
        cap = textToNumber(solana["Capitalización de mercado"].values[0])
        coins = textToNumber(solana["Total monedas"].values[0])
        volume = textToNumber(solana["Volumen negociado"].values[0])
        change = percentToNumber(solana["% de cambio"].values[0])
        admindata.insertarDatosExtendidos("Solana", precio[0], cap, coins, volume, change)

        precio = cardano["Última"].values
        cap = textToNumber(cardano["Capitalización de mercado"].values[0])
        coins = textToNumber(cardano["Total monedas"].values[0])
        volume = textToNumber(cardano["Volumen negociado"].values[0])
        change = percentToNumber(cardano["% de cambio"].values[0])
        admindata.insertarDatosExtendidos("Cardano", precio[0], cap, coins, volume, change)

        precio = tether["Última"].values
        cap = textToNumber(tether["Capitalización de mercado"].values[0])
        coins = textToNumber(tether["Total monedas"].values[0])
        volume = textToNumber(tether["Volumen negociado"].values[0])
        change = percentToNumber(tether["% de cambio"].values[0])
        admindata.insertarDatosExtendidos("Tether", precio[0], cap, coins, volume, change)

        precio = binance["Última"].values
        cap = textToNumber(binance["Capitalización de mercado"].values[0])
        coins = textToNumber(binance["Total monedas"].values[0])
        volume = textToNumber(binance["Volumen negociado"].values[0])
        change = percentToNumber(binance["% de cambio"].values[0])
        admindata.insertarDatosExtendidos("Binance", precio[0], cap, coins, volume, change)

        precio = usdc["Última"].values
        cap = textToNumber(usdc["Capitalización de mercado"].values[0])
        coins = textToNumber(usdc["Total monedas"].values[0])
        volume = textToNumber(usdc["Volumen negociado"].values[0])
        change = percentToNumber(usdc["% de cambio"].values[0])
        admindata.insertarDatosExtendidos("USDCoin", precio[0], cap, coins, volume, change)

        precio = xrp["Última"].values
        cap = textToNumber(xrp["Capitalización de mercado"].values[0])
        coins = textToNumber(xrp["Total monedas"].values[0])
        volume = textToNumber(xrp["Volumen negociado"].values[0])
        change = percentToNumber(xrp["% de cambio"].values[0])
        admindata.insertarDatosExtendidos("XRP", precio[0], cap, coins, volume, change)

        precio = terra["Última"].values
        cap = textToNumber(terra["Capitalización de mercado"].values[0])
        coins = textToNumber(terra["Total monedas"].values[0])
        volume = textToNumber(terra["Volumen negociado"].values[0])
        change = percentToNumber(terra["% de cambio"].values[0])
        admindata.insertarDatosExtendidos("Terra", precio[0], cap, coins, volume, change)


if __name__ == '__main__':
    main()