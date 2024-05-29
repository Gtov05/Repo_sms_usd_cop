"""
************************************************************************
* Author = Cristian Tovar                                              *
* Date = '27/05/2024'                                                  *
* Description = Envio de mensajes Exchange con Python                  *
************************************************************************
"""

import os
import time
import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
#from tqdm import tqdm
from datetime import datetime
from config import *

from functions import get_date, request_exchange, get_trm, data_frame, send_wa


input_date= get_date()

datos = data_frame(get_trm(request_exchange(ACCESS_KEY, BASE, TO)))

mensaje = send_wa(ACCOUNT_SID, AUTH_TOKEN, input_date, datos, PHONE)

print('Mensaje Enviado con exito ' + mensaje)
