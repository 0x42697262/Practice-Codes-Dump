import datetime
import string
import random
import threading
import requests
import time
import os
from bs4 import BeautifulSoup
import html5lib



# MiningPH Bot Settings
#########################################################################################################
# User Settings                                                                                         #
USER_ID = "1328685"                                                                                           #
xVal = "1"                                                                                               #
yVal = "1000000"                                                                                               #
COOKIES_COMPLETE = False                                                                                #
COOKIES = {                                                                                             #
    "__cfduid" : "d39927d30f431c556797fdf499b0ed5dc1586496955",                                                                                    #
    "__cf_bm" : "f02aa2cfb75ffe4fc1f9c002752ebe452c9f33d1-1586515923-1800-AYCumt4VyHgeaDXN4ufTeaORceEHYw2W58IftXWAR/DgbTd/S+p7z0Ygj04T+SgZN8BpMgAfmfAUV3nW0DLfBMk=",                                                                                     #
    "ci_session" : "1bu2ho6son6btm1idqu28bkkp2m3sm23",                                                                                  #
    "hashes" : "1000",}                                                                                     #
URL = "https://miningph.com/application/views/user/getHashes.php?xVal={x}&id={id}&yVal={y}".format(     #
    x=xVal, id=USER_ID, y=yVal)                                                                         #
# ----------------------------------------------------------------------------------------------------- #
# System Settings                                                                                       #
HEADERS = {                                                                                             #
    "Host": "miningph.com",                                                                             #
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0",     #
    "Accept": "*/*",                                                                                    #
    "Accept-Language": "en-US,en;q=0.5",                                                                #
    "Accept-Encoding": "gzip, deflate, br",                                                             #
    "X-Requested-With": "XMLHttpRequest",                                                               #
    "DNT": "1",                                                                                         #
    "Connection": "keep-alive",                                                                         #
    "Referer": "https://miningph.com/miner?e={e}".format(e=USER_ID),                                    #
                                                                                   #
    "TE": "Trailers"}                                                                                   #
#########################################################################################################

URLP = 'https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=7000&anonymity=elite&limit=1'

global totalBots
global totalHits
global totalErrors
totalBots = 0
totalHits = 0
totalErrors = 0





def getproxy():
  #return {'https': 'socks5://{}'.format(random.choice(open('proxies.txt').readlines()).rstrip())}
  proxy_ip = '{}'.format(random.choice(open('proxies.txt').readlines()).rstrip())
  #return {'http': proxy_ip, 'https': proxy_ip}
  return {'http': proxy_ip}

def main():
  global totalHits
  global totalErrors
  while True:
    with requests.Session() as s:
      try:
        r = s.get(URL, headers=HEADERS, cookies=COOKIES, proxies=getproxy())
        totalHits += 1
      except (AttributeError, requests.exceptions.SSLError, OSError) as e:
        totalErrors += 1
       

    
class thread_main(threading.Thread):
  
  print("Started!!!!!!!!!!!!!!!!!!!!!")
  def run(self):
    global totalHits
    global totalErrors
    
    while True:
      with requests.Session() as s:
        try:
          r = s.get(URL, headers=HEADERS, cookies=COOKIES)
          totalHits += 1
        except (AttributeError, requests.exceptions.SSLError, OSError) as e:
          totalErrors += 1
          
      

class thread_bot(threading.Thread):
  global totalBots
  global totalHits
  def run(self):
    main()
   
      #print("Hits: {h}\nBots: {b}\n".format(h = totalHits, b = totalBots),end='\r')
     
class thread_print(threading.Thread):
  global totalBots
  global totalHits
  global totalErrors
  
  def run(self):
    ptime = datetime.datetime.now()
    while True:
      phits = totalHits
      time.sleep(1)
      chits = totalHits - phits
      ctime = datetime.datetime.now() - ptime
      print("\nTime Elapsed: {t}\nHits: {h}\nHits per second: {c}\nErrors: {e}".format(h = totalHits, t = ctime,  c=chits, e=totalErrors))
      #print("\nHits: {h}\nHits per second: {c}".format(h = totalHits,c=chits))


def run():
  bot2 = thread_print()
  bot2.start()
 
  for b in range(100):
    global totalBots
    totalBots += 1
    bot = thread_bot()
    bot.start()
    bot3 = thread_main()
    bot3.start()
  
   
def test():
  succ = 0
  fail = 0
  print(getproxy())
  while True:
    try:
      with requests.Session() as s:
        r = s.get('https://httpbin.org/ip', proxies=getproxy())
        
        succ += 1
        print('Success: {s}\nFailed: {f}\nResponse: {r}'.format(s=succ,f=fail,r=r.json()))
    except:
      fail += 1
      print('Success: {s}\nFailed: {f}\n'.format(s=succ,f=fail))

if __name__ == "__main__":
  run()
  #test()
