import math, datetime
from requests import get

token = None
cookie = None

def get_token():
  if True:
    request = get(url='https://grapp.spravazeleznic.cz/')
    parts = request.text.split('<input type="hidden" id="token" value="')
    token = parts[1].split('"')[0]
    cookie = request.cookies.get_dict()['ASP.NET_SessionId']
  
  return token, cookie

def get_plain_train_route(train_id):
  token, cookie = get_token()
  timestamp = math.floor(datetime.datetime.timestamp(datetime.datetime.now())) * 1000
  url = "https://grapp.spravazeleznic.cz/OneTrain/RouteInfo/" + token
  params = { "trainId": train_id, "_": timestamp }

  response = get(url=url, params=params, cookies={"ASP.NET_SessionId": cookie})

  return response.content.decode('utf-8')