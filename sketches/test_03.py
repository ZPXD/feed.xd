from pyfacebook import GraphAPI
from pyfacebook.api.facebook.client import FacebookApi

from config import MY

api = GraphAPI(access_token=MY.user_long_token)

data=api.get_connection("me","friends", fields="name")
print(data)