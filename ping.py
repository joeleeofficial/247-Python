from flask import Flask
from threading import Thread
import random

app = Flask('')

@app.route('/')
def home():
    return "OK THIS IS HOW YOU KEEP YOUR BOT ONLINE !"

def run():
  app.run(host='0.0.0.0',port=random.randint(2000,9000)) 

def awake():  
    t = Thread(target=run)
    t.start()
