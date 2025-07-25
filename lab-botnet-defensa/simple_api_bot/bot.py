from dotenv import load_dotenv
import os
import tweepy 
import time
import random


load_dotenv()
API_KEY = os.getenv("API_KEY")
API_KEY_SECRET = os.getenv("API_KEY_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuth1UserHandler(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def tarea_principal():
    while True:
        ahora = time.strftime("%H:%M:%S")
        try:
            api.update_status(f"[{ahora}] VOLVIMOS")
            print(f"Tweet publicado [{ahora}]")
        except Exception as e:
            print("Error al publicar:", e)
        time.sleep(random.randint(10, 15))  # Jitter de 1 a 2 minutos

if __name__ == "__main__":
    tarea_principal()