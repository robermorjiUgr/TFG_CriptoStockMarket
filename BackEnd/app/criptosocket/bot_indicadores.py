# -*- coding: utf-8 -*-
import admindata as data
import pandas as pd
from dateutil.parser import parse
import statistics

def calcularIndicadores(cripto):
    datos = data.consultarPrecios(cripto)
    datos_cripto = pd.DataFrame(datos)
    # Configuramos el index, asi como convertimos los datetime
    for i in datos_cripto.index:
         datos_cripto['Datetime'][i] = parse(datos_cripto['Datetime'][i])
    datos_cripto['Datetime'] =(pd.to_datetime(datos_cripto['Datetime'], format="yyyy-mm-dd hh:mm:ss"))

    rentabilidades = []
    for i in range(1,(len(datos_cripto)-1)):
        if(datos_cripto['Datetime'][i].year >= 2021):
            rentabilidad = (datos_cripto['Price'][i] - datos_cripto['Price'][i-1])/datos_cripto['Price'][i-1]
            if (rentabilidad<5 and rentabilidad > -5):
                rentabilidades.append(rentabilidad)

    rentabilidad_cripto = statistics.mean(rentabilidades) * 100
    riesgo_cripto = statistics.stdev(rentabilidades) * 100

    data.insertarIndicadoresFinancieros(cripto, rentabilidad_cripto, riesgo_cripto)

def main():
    calcularIndicadores("Bitcoin")
    calcularIndicadores("Ethereum")
    calcularIndicadores("Solana")
    calcularIndicadores("Cardano")
    calcularIndicadores("Tether")
    calcularIndicadores("Binance")
    calcularIndicadores("USDCoin")
    calcularIndicadores("XRP")
    calcularIndicadores("Terra")


if __name__ == '__main__':
    main()