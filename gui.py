import tkinter as tk
import ttkbootstrap as ttk
import Queries

window = ttk.Window(themename = "darkly")
window.title("World Cup")
window.geometry("1600x900")

ttk.Label(window, text = "World Cup 2023", font = "SaxMono 50")

output_frame = ttk.Frame()
output_frame.place(x = 100, y = 100)

def display_teams():
    teams = Queries.display_teams()

    e = ttk.Entry(output_frame, width=20, font=('Arial',16,'bold'))
    e.grid(row = 0, column = 0)
    e.insert(0, "TeamID")
    e.configure(state = "readonly")
    e = ttk.Entry(output_frame, width=20, font=('Arial',16,'bold'))
    e.grid(row = 0, column = 1)
    e.insert(0, "TeamName")
    e.configure(state = "readonly")
    
    for i in range(len(teams)):
        for j in range(len(teams[0])):
                
            e = ttk.Entry(output_frame, width=20, font=('Arial',16,'bold')) 
            e.grid(row = i + 1, column = j)
            e.insert(0, f"{teams[i][j]}")
            e.configure(state = "readonly")

view_matches = ttk.Button(window, text = "View Matches", command = display_teams)
view_matches.pack()

#Bindings
output_frame.bind_class('Entry', '<FocusIn>', lambda event: print("works"))

# run 
window.mainloop()