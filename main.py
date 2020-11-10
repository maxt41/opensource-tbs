import appJar


# create documents
def appendDocument(PROFILE, API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
    f = open("tbs_save.txt", "a")
    f.write(PROFILE+","+API_KEY+","+API_SECRET_KEY+","+ACCESS_TOKEN+","+ACCESS_TOKEN_SECRET+"\n")
    f.close()


# return documents
def returnDocument(PROFILE):
    try:
        with open("tbs_save.txt") as textFile:
            data = [data.strip().split(",") for data in textFile]
        for i in range(len(data)):
            if PROFILE == data[i][0]:
                return data[i]
    except:
        print("Create a profile before trying to use one.")


def profileMenu(button):
    if button == "Edit profile":
        print("window for new profile")
    if button == "Profile 1":
        userdata = returnDocument("1")
    if button == "Profile 2":
        userdata = returnDocument("2")
    if button == "Edit Profile":
        app.hide()
        app.showSubWindow("Edit Profile")
    if button == "Back To Profile Selection":
        app.hideSubWindow("Edit Profile")
        app.show()


# GUI
app = appJar.gui("Profile Selection", "500x400", showIcon=True)
app.setIcon("favicon.ico")
app.setBg("whitesmoke")
app.setResizable(canResize=False)
app.startFrame(title="pfl-sel-upper", sticky="NEW")
app.addLabel("pfl-sel-title", "Select a profile")
app.stopFrame()
app.startFrame(title="pfl-sel-middle", sticky="EW")
app.setPadding([10, 10])
app.addButton("Profile 1", profileMenu, row=0, column=0)
app.addButton("Profile 2", profileMenu, row=0, column=1)
app.stopFrame()
app.startFrame(title="pfl-sel-lower", sticky="SEW")
app.setPadding([20, 10])
app.addButton("Edit Profile", profileMenu)
app.stopFrame()


# Edit Profile
app.startSubWindow("Edit Profile", modal=True)
app.setResizable(canResize=False)
app.setSize("500x400")
app.startFrame(title="edt-upper", sticky="NEW")
app.addLabel("Enter Profile Number")
app.addEntry("profile-number")
app.addLabel("Enter API Key")
app.addEntry("profile-API_KEY")
app.addLabel("Enter API Secret Key")
app.addEntry("profile-API_SECRET_KEY")
app.stopFrame()
app.startFrame(title="edt-lower", sticky="SEW")
app.setPadding([0, 10])
app.addButton("Save", profileMenu, row=0)
app.addButton("Back To Profile Selection", profileMenu, row=1)
app.stopFrame()
app.stopSubWindow()

if __name__ == "__main__":
    app.go()
