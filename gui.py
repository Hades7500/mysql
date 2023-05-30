from tkinter import *

root = Tk()
root.title("ICC World Cup 2023")
root.geometry("1600x900")

def viewPlayers():
   # import example
   # example.showPlayers()
   ...

welcome = Label(root, text="Welcome To Cricket App", font=("SaxMono", 50))
welcome.pack()

viewPlayers = Button(root, text="View Players", command=viewPlayers)
viewPlayers.pack()

root.mainloop()