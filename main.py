import time
from instabot import Bot
import random
from tkinter import *

pencere = Tk()
pencere.geometry("400x400")
pencere.title("Instagram Delete Post")

def deletePost():
    u=username.get()
    p=pas.get()
    bot=Bot()
    bot.login(username=u,password=p)
    medias=bot.get_total_user_medias(bot.user_id)

    for media in medias:
        try:
            bot.delete_media(media)
            time.sleep(random.randrange(7,12)) #Random post delete time 
        except:
            print("Hata")
            time.sleep(random.randrange(100,200))
    

usernameLabel=Label(text="Account:")
passLabel=Label(text="Password:")
username=Entry()
pas=Entry()
usernameLabel.pack()
username.pack()
passLabel.pack()
pas.pack()
deleteButton = Button(text="All Post Delete!", command=deletePost)
deleteButton.pack()

mainloop()




