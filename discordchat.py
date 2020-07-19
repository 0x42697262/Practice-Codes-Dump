import requests
import time

requestHeaders = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
	'Accept': '*/*',
	'Accept-Language': 'en-US',
	'Accept-Encoding': 'gzip, deflate, br',
	'Authorization': '[redacted]',
	'x-super-properties': '[redacted]',
	'Origin': 'https://discord.com',
	'Referrer': 'https://discord.com/channels/[redacted]/[redacted]'
}
requestCookies = {
	'__stripe_mid': '[redacted]',
	'__cfduid': '[redacted]',
	'locale': 'en-US',
	'__cfruid': '[redacted]'
}



tries = 1


while tries != 100:

	tcont = 'Q: How many times have I sent this message?\nA: {} times.'.format(tries)

	requestBody = {"content":"{}".format(tcont),"nonce":"","tts":'false'}


	with requests.Session() as s:
		r = s.post('https://discord.com/api/v6/channels/[redacted]/messages', headers=requestHeaders, cookies=requestCookies, data=requestBody)
		print('successfully sent {} messages'.format(tries))
	tries += 1
	time.sleep(30) # sleep for 30 seconds
