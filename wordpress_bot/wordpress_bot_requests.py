# DAMN LIBRARIES THAT WE FUCKING NEED

import requests
from bs4 import BeautifulSoup

import random
from random import choice
from random import randrange
import string


# UGHHHH THE NECESSARY SHITS???
ran_username = random.choice(open('usernames.txt').readlines()).rstrip()
ran_mail = random.choice(open('mailprovider.txt').readlines()).rstrip()
ran_num = randrange(101)

email = "{username}@{mail}".format(username=ran_username,mail=ran_mail)
username = "{username}{num}".format(username=ran_username,num=ran_num)
password = "Password_Generated143"


random_user_agent = "curl/7.{curl_minor}.{curl_revision} (x86_64-pc-linux-gnu) libcurl/7.{curl_minor}.{curl_revision} OpenSSL/0.9.8{openssl_revision} zlib/1.2.{zlib_revision}".format(curl_minor=random.randint(8, 22), curl_revision=random.randint(1, 9), openssl_revision=random.choice(string.ascii_lowercase), zlib_revision=random.randint(2, 6))

request_headers = {
	
	'Host': 'public-api.wordpress.com',
	'Accept': '*/*',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate, br',
	'Origin': 'https://wordpress.com',
	'DNT': '1',
	'Connection': 'keep-alive',
	'Pragma': 'no-cache',
	'Cache-Control': 'no-cache',
	'TE': 'Trailers'
}
request_cookies = {
	"ccpa_applies":"true",
	"country_code":"unknown",
	"landingpage_currency":"SGD",
	"usprivacy":"1YNN"
}
request_body = {
	"username":username,
	"password":password,
	"email": email,
	"extra":'{"first_name":"","last_name":""}',
	"ab_test_variations":'{}',
	"validate": "false",
	"signup_flow_name":"onboarding",
	"nux_q_site_type":"site",
	"nux_q_question_primary":"",
	"g-recaptcha-response":"03AERD8XpB-R_Cde0oGtDfC9J8vNW6wdI76DJJ2EMyg8b2J5vUxUProxBa-XqmuKZWebUL8G_D3i2Axk4QaPuRQaekAIG5cwh1V7QKnGn2eWGWFYkiCwwHChtta9wFsezai6Vhnoip695ZmPtuE4gDOcv5FyX_51y7hQ8gKDljRKwXGkFoT-VqDxHJesM7FQGxrsKzKdJzNTSKnIR1NJbb-lQwcg7NxA7uDF34qdUEYfZvG4TqkO7xX72hv6qFIf-anhBBZi7h1dxK-yoMr7nysTIa8bybPLb26zWWrcxIBvD_0QhqVL2ShQytWsj8twvvpX6Qw59fa1ubpEUQchqd-9fu2JOLmU5TxTbOKIA5Wa1pO6k_Vb-hM3CxLSu6lNlHgZjI2K4NWNDBOydK2ZRGT_kobzUfXYXavw",
	"client_id":"39911",
	"client_secret":"cOaYKdrkgXz8xY7aysv4fU6wL6sK5J8a6ojReEIAPwggsznj4Cb6mW0nffTxtYT8",
	"locale":"en"
}

response_headers = {}
response_cookies = {}
response_body = {}

like_request_headers = {
	'Host': 'public-api.wordpress.com',
	'Accept': '*/*',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate, br',
	'Origin': 'https://public-api.wordpress.com',
	'DNT': '1',
	'Connection': 'keep-alive',
	'Referer': 'https://public-api.wordpress.com/wp-admin/rest-proxy/',
	'TE': 'Trailers'
}
like_request_cookies = {
	
}

wordpress_request_url = "https://public-api.wordpress.com/rest/v1.1/users/new?http_envelope=1"
g_recaptcha_request_url = "https://www.google.com/recaptcha/api2/reload?k=6LdoXcAUAAAAAM61KvdgP8xwnC19YuzAiOWn5Wtn"


request_headers['User-Agent'] = random_user_agent
like_request_headers['User-Agent'] = random_user_agent

# OF COURSE WE SHALL NOT FORGET THE PROXIES. THOSE DAMN PROXIES


# FINALLY, THE SCRIPT WHICH IS DIVIDED INTO 3 PARTS: ACCOUNT CREATION, LOGIN, AND AUTOMATION(LIKES, COMMENTS, & FOLLOWERS)

with requests.Session() as s:
	r = s.post(wordpress_request_url, headers=request_headers, data=request_body)
	print(BeautifulSoup(r.content, 'html5lib'))
		
	acc_resp_cookies = r.cookies.items()
	like_request_cookies['recognized_logins'] = acc_resp_cookies[0][1]
	like_request_cookies['wordpress_logged_in'] = acc_resp_cookies[1][1]
	like_request_cookies['wordpress_sec'] = acc_resp_cookies[2][1]

	ck_rl = acc_resp_cookies[0][1]
	ck_wli = acc_resp_cookies[1][1]
	ck_ws = acc_resp_cookies[2][1]

	
	r = s.get("https://public-api.wordpress.com/wp-admin/rest-proxy/", headers={'User-Agent': random_user_agent}, cookies=like_request_cookies)
	acc_resp_cookies = r.cookies.items()
	like_request_cookies['wp_api_sec'] = acc_resp_cookies[0][1]
	like_request_cookies['wp_api'] = acc_resp_cookies[1][1]

	ck_was = acc_resp_cookies[0][1]
	ck_wa = acc_resp_cookies[1][1]
	for cookie_items in like_request_cookies:
		print("{}: 			{}".format(cookie_items, like_request_cookies[cookie_items]))
	

	like_request_headers['Authorization'] = 'X-WPCOOKIE {}:1:https://widgets.wp.com'.format(acc_resp_cookies[1][1])


	r = s.get("https://public-api.wordpress.com/rest/v1.1/notifications/?http_envelope=1") # This is to acquire the _wpndash and wpc_wpc
	acc_resp_cookies = r.cookies.items()
	like_request_cookies['_wpndash'] = acc_resp_cookies[0][1]
	like_request_cookies['wpc_wpc'] = acc_resp_cookies[1][1]

	ck_wpn = acc_resp_cookies[0][1]
	ck_wpc = acc_resp_cookies[1][1]

	
	like_request_headers['Cookie'] = 'landingpage_currency=PHP; ccpa_applies=true; usprivacy=1YNN; country_code=unknown; wordpress_test_cookie=WP+Cookie+check; recognized_logins={rl}; wordpress_logged_in={wli}; wp_api_sec={was}; _wpndash={_w}; wpc_wpc={wpc}'.format(rl=ck_rl,wli=ck_wli,was=ck_was,_w=ck_wpn,wpc=ck_wpc)
	print("\n\n\n\n")
	print(like_request_headers['Cookie'])
	r = s.post("https://public-api.wordpress.com/rest/v1/sites/172592039/posts/50/likes/new?http_envelope=1&source=post_flair", headers=like_request_headers)
	print(BeautifulSoup(r.content, 'html5lib'))

	print("Email: {e}\nUsername: {u}\nPassword: {p}".format(e=email,u=username,p=password))

# DO SOMETHING WILL YOU!



#
