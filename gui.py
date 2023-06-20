import tkinter as tk
import ttkbootstrap as ttk
import Queries

window = ttk.Window(themename = "darkly",)
window.title("World Cup")
window.geometry("1600x900")

ttk.Label(window, text = "World Cup 2023", font = "SaxMono 50").pack()

style = ttk.Style()

style.configure("style.Treeview", font = ("SaxMono", 15))
style.configure("style.Treeview.Heading", font = ("SaxMono", 20))

def clear_frame(parent):
    for widgets in parent.winfo_children():
        widgets.destroy()

def resize_notebook(_):
    if notebook.select() == ".!notebook.!frame":
        notebook.config(width = 1050, height = 400)
    elif notebook.select() == ".!notebook.!frame2":
        notebook.config(width = 400, height = 247)
    # else:
    #     notebook.configure

def display_teams():
    global team_table
    teams = Queries.display_teams()
    team_table = ttk.Treeview(tab2,
                              columns = ("TeamID", "TeamName"),
                              show = "headings",
                              style = "style.Treeview")
    
    team_table.column("TeamID", width = 120, stretch = False)
    team_table.column("TeamName", stretch = False)
    team_table.heading("TeamID", text = "TeamID", anchor = "w")
    team_table.heading("TeamName", text = "Team Name", anchor = "w")
    for i in teams:
        team_table.insert('', tk.END, text = '', values=(f"{i[0]}", f"{i[1]}"))

    team_table.pack(fill = "both", anchor = "w")

def display_matches():
    global matches_table
    matches = Queries.display_matches()
    matches_table = ttk.Treeview(tab1,
                         columns = ("MID", "TeamA", "TeamB", "Winner", "Loser", "MVP", "Date", "Time", "Venue"),
                         show = "headings",
                         style = "style.Treeview")
    
    matches_table.column("MID", width = 120, stretch = False)
    matches_table.column("TeamA", width = 110, stretch = False)
    matches_table.column("TeamB", width = 110, stretch = False)
    matches_table.column("Winner", width = 110, stretch = False)
    matches_table.column("Loser", width = 110, stretch = False)
    matches_table.column("MVP", width = 120, stretch = False)
    matches_table.column("Date", width = 120, stretch = False)
    matches_table.column("Time", width = 120, stretch = False)
    matches_table.column("Venue", width = 120, stretch = False)

    matches_table.heading("MID", text = "MatchID", anchor = "w")
    matches_table.heading("TeamA", text = "Team A", anchor = "w")
    matches_table.heading("TeamB", text = "Team B", anchor = "w")
    matches_table.heading("Winner", text = "Winner", anchor = "w")
    matches_table.heading("Loser", text = "Loser", anchor = "w")
    matches_table.heading("MVP", text = "MVP", anchor = "w")
    matches_table.heading("Date", text = "Date", anchor = "w")
    matches_table.heading("Time", text = "Time", anchor = "w")
    matches_table.heading("Venue", text = "Venue", anchor = "w")


    matches_table.pack(fill = "both", expand = 1)

def item_select(table):
    print(team_table.selection())
    for i in table.selection():
        print(table.item(i)['values'])

def delete_items(table):
    for i in table.selection():
        table.delete(i)

def create_team(tid, tname):
    if len(tname.get()) == 0 or len(tid.get()) == 0:
        ttk.Label(tab2, text = "Enter valid tid or tname").pack()
    elif len(tname.get()) > 30:
        ttk.Label(tab2, text = "Lenth of Team Name cant be greater than 30").pack(side = "bottom")
    else:
        Queries.add_team(tid.get(), tname.get())
        clear_frame(tab2)
        tab2_widgets()

def tab1_widgets():
    display_matches()
    match_id = ttk.StringVar()
    team_a = ttk.StringVar()
    team_b = ttk.StringVar()
    winner = ttk.StringVar()
    loser = ttk.StringVar()
    mvp = ttk.StringVar()
    date = ttk.StringVar()
    time = ttk.StringVar()
    venue = ttk.StringVar()
    l = [match_id, team_a, team_b, winner, loser, mvp, date]
    for i in l:
        ttk.Entry(tab1, textvariable = i).pack(side = tk.LEFT)

def tab2_widgets():
    display_teams()

    team_id = ttk.StringVar()
    team_name = ttk.StringVar()
    ttk.Entry(tab2, textvariable = team_id, width = 15).pack(side = tk.LEFT)
    ttk.Entry(tab2, textvariable = team_name, width = 25).pack(side = tk.LEFT)
    ttk.Button(tab2, text = "+", command = lambda: create_team(team_id, team_name)).pack(side = tk.LEFT, anchor = "w")

# Notebook
notebook = ttk.Notebook(window)

tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
notebook.add(tab1, text = "Matches")
notebook.add(tab2, text = "Teams")

notebook.pack()
tab2_widgets()
tab1_widgets()
display_matches()

# Bindings
matches_table.bind("<<TreeviewSelect>>", lambda event: item_select(matches_table))
matches_table.bind("<Delete>", lambda event: delete_items(matches_table))
team_table.bind("<<TreeviewSelect>>", lambda event: item_select(team_table))
team_table.bind("<Delete>", lambda event: delete_items(team_table))
notebook.bind("<<NotebookTabChanged>>", resize_notebook)

# run
window.mainloop()
