"""
************************************************************************
* Author = Cristian Tovar                                              *
* Date = '27/05/2024'                                                  *
* Description = Envio de mensajes Exchange con Python                  *
************************************************************************
"""

import os
import twilio
from twilio.rest import Client
import pandas as pd
from datetime import datetime
import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json 

def get_date():

	input_date = datetime.now()
	input_date = input_date.strftime("%Y-%m-%d")

	return input_date

def request_exchange(api_key, base, to):
	
	url_exchange = 'https://financialmodelingprep.com/api/v3/fx/'+base+to+'?apikey='+api_key

	try:
		response = requests.get(url_exchange).json()
	except Exception as e:
		print(e)

	return response

def get_trm(response):

	convert = response[0]['ticker']
	trm = float(response[0]['open'])
	
	return convert, trm

def data_frame(data):

	datos = []
	datos.append(data)
	col = ['Type','Value']
	df = pd.DataFrame(datos,columns=col)
	df.set_index('Type', inplace = True)

	return df

def send_wa(account, token, input_date, data_f, phone):
	account_sid = account
	auth_token = token
	client = Client(account_sid, auth_token)

	message = client.messages.create(
	                              body='\nHola! \n\n\n El cambio de moneda del dia '+ input_date +' es : \n\n\n ' + str(data_f),
	                              from_=phone,
	                              to='+573104802443'
	                          )
	return message.sid