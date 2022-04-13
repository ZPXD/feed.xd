from pyfacebook import GraphAPI
from pyfacebook.api.facebook.client import FacebookApi

from config import MY

# Połaczenie za pomocą wygenerowanego tokeny w wersji długiej -> bezpieczniejsze
api = GraphAPI(access_token=MY.user_long_token)
fb = FacebookApi(access_token=MY.user_long_token)

# Połaczenie z autoryzacją
#api = GraphAPI(app_id=MY.app_id, app_secret=MY.app_secret, application_only_auth=True)
#fb = FacebookApi(app_id=MY.app_id, app_secret=MY.app_secret, application_only_auth=True)

user=fb.user.get_info(user_id="3311065259218411")
print(user)