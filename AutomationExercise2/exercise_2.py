import requests
from dotenv import load_dotenv
import os

def json_data():
    load_dotenv()
    api = os.getenv('api')
    z = requests.get(api)
    data=z.json()
    Status=data['status']
    draw_ID=data['drawId']
    game_type=data["pricePoints"]["addOn"][1]["gameType"]
    return  draw_ID,Status,game_type,data