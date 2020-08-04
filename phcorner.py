import requests
import re
import random
import json
import time
import hashlib
import sys
import datetime

URL = 'https://[redacted]/threads/[redacted]/add-reply' # [redacted] Thread to POST
qURL = 'https://anime-chan.herokuapp.com/api/quotes/random' # Anime Quotes
keys = {'keyTime': '1596544785',
'keyHash': '[redacted]'
}

dataHeaders = {
'Host': '[redacted]',
'User-Agent': '[redacted]',
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'Content-Type': 'multipart/form-data; boundary=---------------------------@unique@',
'X-Requested-With': 'XMLHttpRequest',
'Origin': 'https://[redacted]',
'Referer': 'https://[redacted]/threads/[redacted]/'}
dataCookies = {"xf_csrf":"[redacted]",
"xf_push_notice_dismiss":"1",
"xf_session":"[redacted]",
"xf_user":"[redacted]"}
dataBody = """-----------------------------@unique@
Content-Disposition: form-data; name="message_html"

<strong><em>"@quote@"</em></strong><p><em>— @character@</em></p>
-----------------------------@unique@
Content-Disposition: form-data; name="attachment_hash"

@hash@
-----------------------------@unique@
Content-Disposition: form-data; name="attachment_hash_combined"

{"type":"post","context":{"thread_id":914391},"hash":"@hash@"}
-----------------------------@unique@
Content-Disposition: form-data; name="last_date"

@time@
-----------------------------@unique@
Content-Disposition: form-data; name="last_known_date"

@time@
-----------------------------@unique@
Content-Disposition: form-data; name="_xfToken"

@key.time@,@key.hash@
-----------------------------@unique@
Content-Disposition: form-data; name="_xfRequestUri"

/threads/[redacted]/
-----------------------------@unique@
Content-Disposition: form-data; name="_xfWithData"

1
-----------------------------@unique@
Content-Disposition: form-data; name="_xfToken"

@key.time@,@key.hash@
-----------------------------@unique@
Content-Disposition: form-data; name="_xfResponseType"

json
-----------------------------@unique@--
"""

def getQuotes():    # Function for acquiring anime quotes
    with requests.Session() as s:
        r = s.get(qURL)
        r = json.loads(r.content.decode('utf-8'))   # get response as json then decode as utf-8 to avoid character errors
        return {'quote': r[0]['quote'], 'character': r[0]['character']}
        
def optionals(value):   # Function for the dynamic data to POST. "value" is used for randomization
    boundary = ''
    while len(boundary) != 30:
        r = random.randint(0,9)
        boundary += str(r)
    return {'md5hash': hashlib.md5(value.encode()).hexdigest(), 
    'timestamp': int(time.time()), 
    'unique': boundary}


def postReply(sent, q, c, rBody):
    global sentMessages
    global keys
    with requests.Session() as s:
        r = s.post(URL, headers=dataHeaders, cookies=dataCookies, data=rBody.encode('utf-8'))
        r = json.loads(r.content)
        keys['keyTime'] = r['lastDate']
        p = re.search('\w{32}', str(r)) # regex pattern that looks for the xfToken
        try:
            keys['keyHash'] = str(p.group())
        except:
            print('Failed to acquire new xfToken... using old value.')
        if r['status'] == 'ok':
            print(f'\n\n---------------------\nSent {sent} quotes\nQuote: {q}\nCharacter: {c}\n---------------------')
        else:
            sentMessages = 1
            main(sentMessages)
        

dataBody = dataBody.replace('@key.time@', keys['keyTime'])
dataBody = dataBody.replace('@key.hash@', keys['keyHash'])


def main(sent):
    global dataBody
    global dataHeaders
    rdataBody = dataBody # make a copy of Body
    rdataHeaders = dataHeaders # make a copy of Headers
    
    rJson = getQuotes() # call function
    rOptionals = optionals(rJson['quote']) # call function
    
    # --- Proceed replacing strings --- #
    rdataHeaders['Content-Type'] = f"multipart/form-data; boundary=---------------------------{rOptionals['unique']}"
    rdataBody = rdataBody.replace('@unique@', rOptionals['unique'])
    rdataBody = rdataBody.replace('@quote@', rJson['quote'])
    rdataBody = rdataBody.replace('@character@', rJson['character'])
    rdataBody = rdataBody.replace('@time@', str(rOptionals['timestamp']))
    rdataBody = rdataBody.replace('@hash@', rOptionals['md5hash'])
    
    postReply(sent, rJson['quote'], rJson['character'], rdataBody)
    
    


print('Acquiring new keys...')
with requests.Session() as s:
    r = s.get(URL, cookies=dataCookies)
    p = re.search('\w{32}', r.text)
    keys['keyHash'] = p.group()
print(f"Successfully acquired new key: {keys['keyHash']}")

sentMessages = 1
while True:
    try:
        
        main(sentMessages)
        sentMessages += 1
        time.sleep(20)
    except KeyboardInterrupt:
        sys.exit(f'Posts sent: {sentMessages-1}\nTerminating...')
