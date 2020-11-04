import appJar


# create documents
def appendDocument(PROFILE, API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
    f = open("tbs_save.txt", "a")
    f.write(PROFILE+","+API_KEY+","+API_SECRET_KEY+","+ACCESS_TOKEN+","+ACCESS_TOKEN_SECRET+"\n")
    f.close()


# return documents
def returnDocument(PROFILE):
    with open("tbs_save.txt") as textFile:
        data = [data.strip().split(",") for data in textFile]
    for i in range(len(data)):
        if PROFILE == data[i][0]:
            return data[i]


# GUI
app = appJar.gui("Profile Selection", "500x400", showIcon=True)
app.setIcon("favicon.ico")
app.setBg("red")
app.setResizable(canResize=False)
app.startFrame(title="pfl-sel-upper", sticky="NEW")
app.addLabel("pfl-sel-title", "Select a profile or make a new one")
app.setLabelBg("pfl-sel-title", "black")
app.setLabelFg("pfl-sel-title", "white")
app.stopFrame()

if __name__ == "__main__":
    app.go()
