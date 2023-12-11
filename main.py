import sys, json, os
from time import sleep
from random import random
from flask import Flask, request, make_response
from flask_cors import CORS
from grapp import get_plain_train_route
from options import get_options
from requests import post
from threading import Thread

options = get_options(sys.argv[1:])

port = options.get("p", 3333)
mother_url = options.get("m", "http://192.168.0.171:3333") + "/cached-routes"

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

def cache_logging(train_id, yet, total):
  os.system('cls')
  print(f"Caching train {train_id} - {yet}/{total}", end='\r')
  

@app.post("/")
def index():
  body = request.get_json()
  def cache_train(**kwargs):
    train_ids = kwargs.get("trains_ids", [])
    trains = {}
    print(f"Getting routes of {len(train_ids)} trains")
    make_response(f"Getting routes of {len(train_ids)} trains", 200)

    for train_id in train_ids:
      cache_logging(train_id, len(trains) + 1, len(train_ids))
      trains[train_id] = get_plain_train_route(train_id)
      #sleep(0.2 + (0.6 * random()))

    post(url=mother_url, json=trains)
  Thread(target=cache_train, kwargs={"trains_ids": body}).start()
  return make_response(f"Getting routes of {len(body)} trains", 200)
  
app.run(host='0.0.0.0', port=port)