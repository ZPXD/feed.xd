# bazuje na źródło: https://drgabrielharris.medium.com/python-how-making-facebook-api-calls-using-facebook-sdk-ea18bec973c8
#
# w stosunku do oryginalnej wersji poprawiono URL o wskazanie wersji GRAPH API oraz wyniesiono na zewnątrz dane uwierzytelniające
#
# Skrypt pozyskuje nowy token w formacie długim, który zapisujemy do pliku config.py
#

import logging
import requests

logging.basicConfig(
    level=logging.INFO, format="[%(asctime)s] %(message)s", datefmt="%d/%m/%y %H:%M:%S"
)

from config import MY

app_id = MY.app_id
app_secret = MY.app_secret
user_long_token = MY.user_long_token

url = "https://graph.facebook.com/v13.0/oauth/access_token"

payload = {
    "grant_type": "fb_exchange_token",
    "client_id": app_id,
    "client_secret": app_secret,
    "fb_exchange_token": user_long_token,
}

try:
    response = requests.get(
        url,
        params=payload,
        timeout=5,
    )

except requests.exceptions.Timeout as e:
    logging.error("TimeoutError", e)

else:

    try:
        response.raise_for_status()

    except requests.exceptions.HTTPError as e:
        logging.error("HTTPError", e)

    else:
        response_json = response.json()
        logging.info(response_json)
        user_long_token = response_json["access_token"]
