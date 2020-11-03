# create documents
def appendDocument(PROFILE, API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
    f = open("tbs_save.txt", "a")
    f.write(PROFILE+","+API_KEY+","+API_SECRET_KEY+","+ACCESS_TOKEN+","+ACCESS_TOKEN_SECRET+"\n")
    f.close()
