import json
import requests

class BtcService:
    def __init__(self):
        pass
    def get_realtime_btc(self):
        
        key = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

        data = requests.get(key)  
        data = data.json()
        return data['price'][:-4]
