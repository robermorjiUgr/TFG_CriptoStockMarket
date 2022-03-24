import sys
import fileinput
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from CriptoTracking.forms import RegisterForm

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
    return render(request, "home.html")

def visualizar_criptomoneda(request, criptomoneda):
    archivo = './CriptoTracking/static/js/main.js'
    for line in fileinput.input([archivo], inplace=True):
        if line.strip().startswith('"symbol": '):
            if (criptomoneda == 'Bitcoin'):
                line = '\t\t\t\t"symbol": "BITSTAMP:BTCUSD",\n'
            if (criptomoneda == 'Ethereum'):
                line = '\t\t\t\t"symbol": "COINBASE:ETHUSD",\n'
            if (criptomoneda == 'Solana'):
                line = '\t\t\t\t"symbol": "FTX:SOLUSD",\n'
            if (criptomoneda == 'Cardano'):
                line = '\t\t\t\t"symbol": "COINBASE:ADAUSD",\n'
            if (criptomoneda == 'Tether'):
                line = '\t\t\t\t"symbol": "COINBASE:USDTUSD",\n'
            if (criptomoneda == 'Binance'):
                line = '\t\t\t\t"symbol": "FTX:BNBUSD",\n'
            if (criptomoneda == 'USDCoin'):
                line = '\t\t\t\t"symbol": "BINANCEUS:USDCUSD",\n'
            if (criptomoneda == 'XRP'):
                line = '\t\t\t\t"symbol": "BITSTAMP:XRPUSD",\n'
            if (criptomoneda == 'Terra'):
                line = '\t\t\t\t"symbol": "COINBASE:USTUSD",\n'
        sys.stdout.write(line)

    return redirect("/")

