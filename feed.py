from pyfacebook import GraphAPI
from pyfacebook.api.facebook.client import FacebookApi

# Your keys. Pick one.
facebook_access_token = open('keys/facebook_access_token').read()
facebook_user_token = open('keys/facebook_user_token').read()

# Connection to FB. Pick one.
api = GraphAPI(access_token=facebook_access_token)
fb = FacebookApi(access_token=facebook_access_token)

# Connection with broader auth. Pick one.
#app_id = None
#app_secret = None 
#api = GraphAPI(app_id=app_id, app_secret=app_secret, application_only_auth=True)
#fb = FacebookApi(app_id=app_id, app_secret=app_secret, application_only_auth=True)

# Check.
user_id = None
user=fb.user.get_info(user_id=user_id)

# Own wall.
data=api.get_connection("me", "posts")
for i, post in enumerate(data['data']):
 	print(i)
 	print(post)
 	print()

# Friend wall.

# Page wall.
