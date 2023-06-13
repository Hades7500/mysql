import tkinter as tk
import ttkbootstrap as ttk
import Queries

window = ttk.Window(themename = "darkly")
window.title("World Cup")
window.geometry("1600x900")

ttk.Label(window, text = "World Cup 2023", font = "SaxMono 50").pack()

style = ttk.Style()

# Notebook
notebook = ttk.Notebook(window)

tab1 = ttk.Frame(notebook)
tab1.configure()
tab2 = ttk.Frame(notebook)
notebook.add(tab1, text = "Teams")
notebook.add(tab2, text = "Players")

notebook.pack()

def display_teams():
    teams = Queries.display_teams()
    style.configure("m.Treeview", font = ("SaxMono", 15))
    style.configure("m.Treeview.Heading", font = ("SaxMono", 20))
    table = ttk.Treeview(tab1, columns = ("TeamID", "TeamName"), show = "headings", style = "m.Treeview")
    table.column("TeamID", width = 90)
    table.heading("TeamID", text = "TeamID")
    table.heading("TeamName", text = "Team Name")
    for i in teams:
        table.insert('', tk.END, text = '', values=(f"{i[0]}", f"{i[1]}"), tags = "t")
    
    table.pack(fill = "both", expand = True)

def add_team():
    ...

add_team = ttk.Button(window, text = "View Teams", command = add_team)
add_team.pack()

# Bindings

# run 
window.mainloop()