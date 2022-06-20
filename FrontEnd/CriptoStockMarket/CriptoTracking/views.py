import sys
import fileinput
import requests
import pandas as pd
import json
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from CriptoTracking.forms import RegisterForm
from CriptoTracking.forms import UpdateUserForm

from django.core.exceptions import ValidationError
from collections import OrderedDict

# Consulta los datos extendidos de cada criptomoneda mediante consultas a los microservicios
def get_datos_resumen():
    # GET BITCOIN DATA
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    url_req = 'http://localhost:5000/criptosocket/getExtendedBitcoin'
    req = requests.get(url=url_req, headers=headers)
    btc_data = req.json()
    # GET ETHEREUM DATA
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    url_req = 'http://localhost:5000/criptosocket/getExtendedEthereum'
    req = requests.get(url=url_req, headers=headers)
    eth_data = req.json()
    # GET SOLANA DATA
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    url_req = 'http://localhost:5000/criptosocket/getExtendedSolana'
    req = requests.get(url=url_req, headers=headers)
    sol_data = req.json()
    # GET CARDANO DATA
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    url_req = 'http://localhost:5000/criptosocket/getExtendedCardano'
    req = requests.get(url=url_req, headers=headers)
    ada_data = req.json()
    # GET TETHER DATA
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    url_req = 'http://localhost:5000/criptosocket/getExtendedTether'
    req = requests.get(url=url_req, headers=headers)
    usdt_data = req.json()
    # GET BINANCE DATA
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    url_req = 'http://localhost:5000/criptosocket/getExtendedBinance'
    req = requests.get(url=url_req, headers=headers)
    bnc_data = req.json()
    # GET USDCoin DATA
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    url_req = 'http://localhost:5000/criptosocket/getExtendedUSDCoin'
    req = requests.get(url=url_req, headers=headers)
    usdc_data = req.json()
    # GET XRP DATA
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    url_req = 'http://localhost:5000/criptosocket/getExtendedXRP'
    req = requests.get(url=url_req, headers=headers)
    xrp_data = req.json()
    # GET TERRA DATA
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    url_req = 'http://localhost:5000/criptosocket/getExtendedTerra'
    req = requests.get(url=url_req, headers=headers)
    terra_data = req.json()

    marketcap_total = btc_data['MarketCap'] + eth_data['MarketCap'] + sol_data['MarketCap'] + ada_data['MarketCap'] + usdt_data['MarketCap'] + bnc_data['MarketCap'] + usdc_data['MarketCap'] + xrp_data['MarketCap'] + terra_data['MarketCap']
    datos = {'BTC': btc_data,
             'ETH': eth_data,
             'SOL': sol_data,
             'ADA': ada_data,
             'USDT': usdt_data,
             'BNC': bnc_data,
             'USDC': usdc_data,
             'XRP' : xrp_data,
             'Terra': terra_data,
             'TotalMC': marketcap_total
            }

    datos['BTC']['img'] = 'images/coins/BTC.png'
    datos['ETH']['img'] = 'images/coins/ETH.png'
    datos['SOL']['img'] = 'images/coins/SOL.png'
    datos['ADA']['img'] = 'images/coins/ADA.png'
    datos['USDT']['img'] = 'images/coins/USDT.png'
    datos['BNC']['img'] = 'images/coins/BNC.png'
    datos['USDC']['img'] = 'images/coins/USDC.png'
    datos['XRP']['img'] = 'images/coins/XRP.png'
    datos['Terra']['img'] = 'images/coins/Terra.png'

    return datos

# Consulta los indicadores de cada criptomoneda mediante consultas a los microservicios
def get_indicadores():
    # GET BITCOIN DATA
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    url_req = 'http://localhost:5000/criptosocket/getIndicatorsBitcoin'
    req = requests.get(url=url_req, headers=headers)
    btc_data = req.json()
    # GET ETHEREUM DATA
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    url_req = 'http://localhost:5000/criptosocket/getIndicatorsEthereum'
    req = requests.get(url=url_req, headers=headers)
    eth_data = req.json()
    # GET SOLANA DATA
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    url_req = 'http://localhost:5000/criptosocket/getIndicatorsSolana'
    req = requests.get(url=url_req, headers=headers)
    sol_data = req.json()
    # GET CARDANO DATA
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    url_req = 'http://localhost:5000/criptosocket/getIndicatorsCardano'
    req = requests.get(url=url_req, headers=headers)
    ada_data = req.json()
    # GET BINANCE DATA
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    url_req = 'http://localhost:5000/criptosocket/getIndicatorsBinance'
    req = requests.get(url=url_req, headers=headers)
    bnc_data = req.json()
    # GET XRP DATA
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    url_req = 'http://localhost:5000/criptosocket/getIndicatorsXRP'
    req = requests.get(url=url_req, headers=headers)
    xrp_data = req.json()
    # GET TERRA DATA
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    url_req = 'http://localhost:5000/criptosocket/getIndicatorsTerra'
    req = requests.get(url=url_req, headers=headers)
    terra_data = req.json()

    datos = {'BTC': btc_data,
             'ETH': eth_data,
             'SOL': sol_data,
             'ADA': ada_data,
             'BNC': bnc_data,
             'XRP' : xrp_data,
             'Terra': terra_data,
            }

    datos['BTC']['img'] = 'images/coins/BTC.png'
    datos['ETH']['img'] = 'images/coins/ETH.png'
    datos['SOL']['img'] = 'images/coins/SOL.png'
    datos['ADA']['img'] = 'images/coins/ADA.png'
    datos['BNC']['img'] = 'images/coins/BNC.png'
    datos['XRP']['img'] = 'images/coins/XRP.png'
    datos['Terra']['img'] = 'images/coins/Terra.png'

    return datos

# Permite ordenar las criptomonedas dado un campo de los *datos extendidos* y un orden (asc o desc)
def ordenarCripto(datos, field, orden):
    lista_monedas = []
    for moneda in datos.items():
        if (moneda[0] != "TotalMC"):
            lista_monedas.append(moneda)
    n = len(lista_monedas)

    for i in range(n):
        for j in range(n - i - 1):
            if (orden == '1'):
                if (lista_monedas[j][1][field]) > (lista_monedas[j+1][1][field]):
                    lista_monedas[j], lista_monedas[j + 1] = lista_monedas[j + 1], lista_monedas[j]
            if(orden == '-1'):
                if (lista_monedas[j][1][field]) < (lista_monedas[j+1][1][field]):
                    lista_monedas[j], lista_monedas[j + 1] = lista_monedas[j + 1], lista_monedas[j]
    return lista_monedas

def getRanking():
    datos = get_indicadores()
    data = pd.DataFrame(datos)
    rentabilidad_max = data.loc['Profitability'].max()
    volatilidad_min = data.loc['Risk'].min()

    datos['BTC']['Puntuacion']=(data['BTC']['Profitability']/rentabilidad_max)*5.0 + (volatilidad_min/data['BTC']['Risk'])*5.0
    datos['ETH']['Puntuacion']=(data['ETH']['Profitability']/rentabilidad_max)*5.0 + (volatilidad_min/data['ETH']['Risk'])*5.0
    datos['SOL']['Puntuacion']=(data['SOL']['Profitability']/rentabilidad_max)*5.0 + (volatilidad_min/data['SOL']['Risk'])*5.0
    datos['ADA']['Puntuacion']=(data['ADA']['Profitability']/rentabilidad_max)*5.0 + (volatilidad_min/data['ADA']['Risk'])*5.0
    datos['BNC']['Puntuacion']=(data['BNC']['Profitability']/rentabilidad_max)*5.0 + (volatilidad_min/data['BNC']['Risk'])*5.0
    datos['XRP']['Puntuacion']=(data['XRP']['Profitability']/rentabilidad_max)*5.0 + (volatilidad_min/data['XRP']['Risk'])*5.0
    datos['Terra']['Puntuacion']=(data['Terra']['Profitability']/rentabilidad_max)*5.0 + (volatilidad_min/data['Terra']['Risk'])*5.0
    datos_ordenados = ordenarCripto(datos, "Puntuacion", "-1")

    return datos_ordenados

# ------------------------------------------- VISTAS DE LA APP -----------------------------------------------

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/accounts/login")
    else:
        form = RegisterForm()

    return render(request, "registration/register.html", {"form": form})

def userProfile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            return redirect('/')
    else:
        user_form = UpdateUserForm(instance=request.user)

    return render(request, 'registration/userProfile.html', {'user_form': user_form})

def home(request):
    datos = get_datos_resumen()
    return render(request, "home.html", {"Data": datos})

def visualizar_criptomoneda(request, criptomoneda):
    archivo = './CriptoTracking/static/js/main.js'
    for line in fileinput.input([archivo], inplace=True):
        if line.strip().startswith('"symbol": '):
            if (criptomoneda == 'Bitcoin'):
                line = '\t\t\t\t"symbol": "COINBASE:BTCUSD",\n'
            if (criptomoneda == 'Ethereum'):
                line = '\t\t\t\t"symbol": "COINBASE:ETHUSD",\n'
            if (criptomoneda == 'Solana'):
                line = '\t\t\t\t"symbol": "COINBASE:SOLUSD",\n'
            if (criptomoneda == 'Cardano'):
                line = '\t\t\t\t"symbol": "COINBASE:ADAUSD",\n'
            if (criptomoneda == 'Tether'):
                line = '\t\t\t\t"symbol": "COINBASE:USDTUSD",\n'
            if (criptomoneda == 'Binance'):
                line = '\t\t\t\t"symbol": "FTX:BNBUSD",\n'
            if (criptomoneda == 'USDCoin'):
                line = '\t\t\t\t"symbol": "BINANCEUS:USDCUSD",\n'
            if (criptomoneda == 'XRP'):
                line = '\t\t\t\t"symbol": "COINBASE:XRPUSD",\n'
            if (criptomoneda == 'Terra'):
                line = '\t\t\t\t"symbol": "COINBASE:USTUSD",\n'
        sys.stdout.write(line)

    return redirect('/')

def resumen_criptomonedas(request):
    print(request.POST.getlist('criptos'))
    datos = get_datos_resumen()
    datos_ordenados = ordenarCripto(datos,"MarketCap", "-1")
    return render(request, "cripto-overview.html", {"Data": datos_ordenados, "TotalMC" : datos["TotalMC"], "Datetime": datos['BTC']['Datetime']})

def comparar_criptomonedas(request, criptomoneda1, criptomoneda2):
    datos_resumen = get_datos_resumen()
    datos_indicadores = get_indicadores()
    resumen_criptomoneda1= datos_resumen[criptomoneda1]
    indicadores_criptomoneda1 = datos_indicadores[criptomoneda1]
    resumen_criptomoneda2 = datos_resumen[criptomoneda2]
    indicadores_criptomoneda2 = datos_indicadores[criptomoneda2]
    return render(request, "comparar_criptomonedas.html", {"resumen_cripto1":resumen_criptomoneda1, "resumen_cripto2":resumen_criptomoneda2, "indicadores_cripto1":indicadores_criptomoneda1, "indicadores_cripto2":indicadores_criptomoneda2, "Cripto1": criptomoneda1, "Cripto2": criptomoneda2})

def ranking_criptomonedas(request):
    datos_puntuados = getRanking()
    datos_ordenados = datos_puntuados
    return render(request, "cripto-ranking.html", {"Data": datos_ordenados})