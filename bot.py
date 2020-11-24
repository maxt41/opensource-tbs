import tweepy

class Bot:
    def __init__(self, API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
        auth = tweepy.OAuthHandler(str(API_KEY), str(API_SECRET_KEY))
        auth.set_access_token(str(ACCESS_TOKEN), str(ACCESS_TOKEN_SECRET))
        api = tweepy.API(auth)
        self.api = api

    def verify(self):
        result = self.api.verify_credentials()
        if result != False:
            print("Authenticated")
        else:
            print("Error during authentication")
        

