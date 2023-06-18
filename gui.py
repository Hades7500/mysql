import tkinter as tk
import ttkbootstrap as ttk
import Queries

window = ttk.Window(themename = "darkly",)
window.title("World Cup")
window.geometry("1600x900")

ttk.Label(window, text = "World Cup 2023", font = "SaxMono 50").pack()

style = ttk.Style()

def clear_frame(parent):
   for widgets in parent.winfo_children():
      widgets.destroy()

def display_teams():
    global table
    teams = Queries.display_teams()
    style.configure("style.Treeview", font = ("SaxMono", 15))
    style.configure("style.Treeview.Heading", font = ("SaxMono", 20))
    table = ttk.Treeview(tab2, columns = ("TeamID", "TeamName"), show = "headings", style = "style.Treeview")
    table.column("TeamID", width = 110, stretch = False)
    table.column("TeamName", stretch = False)
    table.heading("TeamID", text = "TeamID", anchor = "w")
    table.heading("TeamName", text = "Team Name", anchor = "w")
    for i in teams:
        table.insert('', tk.END, text = '', values=(f"{i[0]}", f"{i[1]}"))
    
    table.pack(fill = "both", expand = 1, anchor = "w")

def item_select(_):
    print(table.selection())
    for i in table.selection():
        print(table.item(i)['values'])

def delete_items(_):
    # Queries.delete
    for i in table.selection():
        table.delete(i)

def create_team(tid, tname):
    if len(tname.get()) == 0 or len(tid.get()) == 0:
        ttk.Label(tab2, text = "Enter valid tid or tname").pack()
    elif len(tname.get()) > 30:
        ttk.Label(tab2, text = "Lenth of Team Name cant be greater than 30").pack()
    else:
        Queries.add_team(tid.get(), tname.get())
        clear_frame(tab2)
        tab2_widgets()

def tab2_widgets():
    display_teams()

    team_id = ttk.StringVar()
    team_name = ttk.StringVar()
    tid_entry = ttk.Entry(tab2, textvariable = team_id, width = 15)
    tid_entry.pack(side = tk.LEFT)
    tname_entry = ttk.Entry(tab2, textvariable = team_name)
    tname_entry.pack(side = tk.LEFT)
    add_team = ttk.Button(tab2, text = "+", command = lambda: create_team(team_id, team_name))
    add_team.pack(side = tk.LEFT, fill = "x", expand = 1, anchor = "w")

# Notebook
notebook = ttk.Notebook(window, width = 350)

tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
notebook.add(tab1, text = "Matches")
notebook.add(tab2, text = "Teams")

notebook.pack()
tab2_widgets()

# Bindings
table.bind("<<TreeviewSelect>>", item_select)
table.bind('<Delete>', delete_items)

# run 
window.mainloop()