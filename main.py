import appJar
from time import sleep
import threading


# defining threads
def wait():
    sleep(5)
    while True:
        content = [app.label("pfl-response"), app.label("pfl-create-response")]
        if content != "":
            sleep(3)
            app.setLabel("pfl-response", "")
            app.setLabel("pfl-create-response", "")


update_thread = threading.Thread(target=wait)
update_thread.start()


# create documents
def appendDocument(PROFILE, API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
    can_create = True
    with open("tbs_save.txt") as textFile:
        data = [data.strip().split(",") for data in textFile]
    for i in range(len(data)):
        if PROFILE == data[i][0]:
            can_create = False
            app.setLabel("pfl-create-response", "Profile has already been created in that slot")
    if can_create:
        try:
            f = open("tbs_save.txt")
            f.write(PROFILE+","+API_KEY+","+API_SECRET_KEY+","+ACCESS_TOKEN+","+ACCESS_TOKEN_SECRET+"\n")
            f.close()
        except:
            app.setLabel("pfl-create-response", "Cannot create empty profile")


# return documents
def returnDocument(PROFILE):
    try:
        with open("tbs_save.txt") as textFile:
            data = [data.strip().split(",") for data in textFile]
        for i in range(len(data)):
            if PROFILE == data[i][0]:
                return data[i]
            else:
                app.setLabel("pfl-response", "No profile has been created")
    except:
        app.setLabel("pfl-response", "No profile has been created")


def profileMenu(button):
    if button == "Profile 1":
        userdata = returnDocument("1")
        print(userdata)
    if button == "Profile 2":
        userdata = returnDocument("2")
        print(userdata)
    if button == "Create Profile":
        app.hide()
        app.showSubWindow("Create Profile")
    if button == "Save":
        profile = app.getEntry("profile-number")
        API_KEY = app.getEntry("profile-API_KEY")
        API_SECRET_KEY = app.getEntry("profile-API_SECRET_KEY")
        ACCESS_TOKEN = app.getEntry("profile-ACCESS_TOKEN")
        ACCESS_TOKEN_SECRET = app.getEntry("profile-ACCESS_TOKEN_SECRET")
        appendDocument(str(profile), str(API_KEY), str(API_SECRET_KEY), str(ACCESS_TOKEN), str(ACCESS_TOKEN_SECRET))
        app.setEntry("profile-number", "")
        app.setEntry("profile-API_KEY", "")
        app.setEntry("profile-API_SECRET_KEY", "")
        app.setEntry("profile-ACCESS_TOKEN", "")
        app.setEntry("profile-ACCESS_TOKEN_SECRET", "")
    if button == "Back To Profile Selection":
        app.hideSubWindow("Create Profile")
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
app.addLabel("pfl-response", "")
app.startFrame(title="pfl-sel-lower", sticky="SEW")
app.setPadding([20, 10])
app.addButton("Create Profile", profileMenu)
app.stopFrame()


# Edit Profile
app.startSubWindow("Create Profile", modal=True)
app.setResizable(canResize=False)
app.setSize("500x400")
app.startFrame(title="edt-upper", sticky="NEW")
app.addLabel("Enter Profile Number")
app.addEntry("profile-number")
app.addLabel("Enter API Key")
app.addEntry("profile-API_KEY")
app.addLabel("Enter API Secret Key")
app.addEntry("profile-API_SECRET_KEY")
app.addLabel("Enter Access Token")
app.addEntry("profile-ACCESS_TOKEN")
app.addLabel("Enter Secret Access Token")
app.addEntry("profile-ACCESS_TOKEN_SECRET")
app.stopFrame()
app.addLabel("pfl-create-response", "")
app.startFrame(title="edt-lower", sticky="SEW")
app.setPadding([0, 10])
app.addButton("Save", profileMenu, row=0)
app.addButton("Back To Profile Selection", profileMenu, row=1)
app.stopFrame()
app.stopSubWindow()

if __name__ == "__main__":
    app.go()
