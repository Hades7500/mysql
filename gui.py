import tkinter as tk
import ttkbootstrap as ttk
import Queries

window = ttk.Window(themename = "darkly")
window.title("World Cup")
window.geometry("1600x900")

team  = tk.StringVar()

def display_teams():
    teams = Queries.display_teams()

    for i in teams:
        team.set(f"{i[0]} {i[1]}")
        print(team.get())
        ttk.Label(window, text = "Hello", textvariable = team.get()).place(x = 10, y = 20)
        window.update()

view_matches = ttk.Button(window, text = "View Matches", command = display_teams)
view_matches.pack()


# run 
window.mainloop()
