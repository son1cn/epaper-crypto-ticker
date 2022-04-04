#!/usr/bin/python3

from papirus import PapirusTextPos
from papirus import Papirus
import time
import requests
#checkval.py used to pull beacon chain validator data. Contains private key so not in this repo
import checkval
from datetime import datetime
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

text=PapirusTextPos(False, rotation = 0)

#date
text.AddText("1", 0,0 , Id="date", size =35)

#Eth header
text.AddText("ETH:", 0,35 , Id="eth", size =28)
text.AddText("moon", 0,60 , Id="ethcng", size =25)

#ETH Gas price
text.AddText("g", 0,85 , Id="gas", size =30)

#validator
text.AddText("val", 0,125 , Id="val", size =28)
text.AddText("valvalue", 0,148 , Id="valvalue", size=28)

def getETH():
    #get ETH gas price and 24 hr change from CoinGecko
    prices = cg.get_price(ids='ethereum', vs_currencies='usd', include_24hr_change='true')

    eth_usd= (prices["ethereum"]['usd'])
    eth_change= (prices["ethereum"]['usd_24h_change'])

    #get my validator stats from the beacon chain api
    #wrote checkval.py to pull the info and kept it in another file due to containing personal API key
    ethval = checkval.check_val()


    #get current ETH gas price
    url = "https://ethergas.io/json"
    gas = requests.request("GET", url).json()['standard']
    print(gas)

    #get current date-time
    now = datetime.now()
    current_time = now.strftime("%d.%m %H:%M")
    #update screen with formatting
    text.UpdateText("date", current_time)
    
    text.UpdateText("eth","ETH:$"+str(eth_usd))
    text.UpdateText("ethcng", (u"\u25B2" if eth_change>0 else u"\u25BC")+format(eth_change,'.2f')+"% 24hr")
    
    text.UpdateText("gas","Gas:"+str(gas))
    
    text.UpdateText("val", "Val1:"+format(ethval,'.6f'))
    text.UpdateText("valvalue","$"+format(ethval*eth_usd,'.2f'))
    text.WriteAll()

    return

data=getETH()
