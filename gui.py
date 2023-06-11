import tkinter as tk
import ttkbootstrap as ttk
import Queries

window = ttk.Window(themename = "darkly")
window.title("World Cup")
window.geometry("1600x900")

ttk.Label(window, text = "World Cup 2023", font = "SaxMono 50").pack()

output_frame = ttk.Frame(window)
output_frame.place(x = 100, y = 100)

style = ttk.Style()


notebook = ttk.Notebook(window)

tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
notebook.add(tab1, text = "Teams")
notebook.add(tab2, text = "Players")

notebook.pack()

def display_teams():
    ...

    teams = Queries.display_teams()
    style.configure("Treeview", font = ("SaxMono", 15))
    style.configure("Treeview.Headings", font = ("SaxMono", 30))
    table = ttk.Treeview(tab1, columns = ("TeamID", "TeamName"), show = "headings", style = "Treeview")
    table.column("TeamID", width = 100)
    table.heading("TeamID", text = "TeamID")
    table.heading("TeamName", text = "Team Name")
    for i in teams:
        table.insert('', tk.END, text = '', values=(f"{i[0]}", f"{i[1]}"), tags = "t")
    
    table.pack(fill = "both", expand = True)

view_teams = ttk.Button(window, text = "View Teams", command = display_teams)
view_teams.pack()

#Bindings
output_frame.bind_class('Entry', '<FocusIn>', lambda event: print("works"))

# run 
window.mainloop()