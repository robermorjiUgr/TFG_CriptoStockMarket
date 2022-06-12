import sys
import fileinput
import requests
import json
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from CriptoTracking.forms import RegisterForm
from collections import OrderedDict

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/accounts/login")
    else:
        form = RegisterForm()

    return render(request, "registration/register.html", {"form": form})

def home(request):
    datos = get_datos()
    return render(request, "home.html", {"Data": datos})

def get_datos():
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

def resumen_criptomonedas(request):
    datos = get_datos()
    datos_ordenados = ordenarCripto(datos,"MarketCap", "-1")
    return render(request, "cripto-overview.html", {"Data": datos_ordenados, "TotalMC" : datos["TotalMC"], "Datetime": datos['BTC']['Datetime']})

def userProfile(request):
    return render(request, "registration/userProfile.html")