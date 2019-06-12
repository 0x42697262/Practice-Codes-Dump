import random
import string
import base64
import urllib.request
import urllib.parse

header = {
    'User-Agent': "curl/7.{curl_minor}.{curl_revision} (x86_64-pc-linux-gnu) libcurl/7.{curl_minor}.{curl_revision} "
                  "OpenSSL/0.9.8{openssl_revision} zlib/1.2.{zlib_revision}".format(
        curl_minor=random.randint(8, 22), curl_revision=random.randint(1, 9),
        openssl_revision=random.choice(string.ascii_lowercase), zlib_revision=random.randint(2, 6))}
url = 'http://pastebin.xyz/api/v1/paste.php'
text = base64.b64encode(bytes('This is good bye.', 'ascii')).decode('utf-8')

mydata = [("code", text)]
mydata = urllib.parse.urlencode(mydata)
binary_data = mydata.encode('ascii')
print(mydata)

req = urllib.request.Request(url, binary_data, headers=header)
page = urllib.request.urlopen(req).read()
print(page.decode('utf-8'))
