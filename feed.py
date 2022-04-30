from pyfacebook import GraphAPI
from pyfacebook.api.facebook.client import FacebookApi

# Your keys. Pick one.
facebook_access_token = "EAAvQZCWoDQfQBAJuu2MlRxdWxZA1zebgghvEYQYiN8WZCo9ZA2M8hgtNE3MCeaBAiryYYqp3qf6SF8KP0YBaQu2vbrtWZBdKoly7PDZC1kjhwElWf8uWbxsrz7XKZB7PyDdaFs7Wa4FKGekZBbZBzEIKUgw5zUIHjrkgIwX0yvOiYqrTd9ptA9JQ2rhyFi8LE6bhWlZBUSdBCA3uBbUpXcfZAr8fNOJKM3NYGDlJkeBRshHyGkX8fDeuOnz" #open('keys/facebook_access_token').read()
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
#user_id = None
#user=fb.user.get_info(user_id=user_id)

# Own wall.
data=api.get_connection("me", "posts")
for i, post in enumerate(data['data']):

 	msg = post.message
 	post_id = post.id
 	cereated_at = post.created_time

 	for k, v in post.items():
 		print(k, v)

# Friend wall.

# Page wall.

