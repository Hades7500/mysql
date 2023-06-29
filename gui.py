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
        notebook.config(width = 1151, height = 415)
    elif notebook.select() == ".!notebook.!frame2":
        notebook.config(width = 339, height = 246)
    # else:
    #     notebook.configure


def display_matches():
    global matches_table
    matches = Queries.display_matches()
    matches_table = ttk.Treeview(tab1,
                         columns = ("MID", "TeamA", "TeamB", "Winner",
                                    "Loser", "MVP", "Date", "Time", "Venue"),
                         show = "headings",
                         style = "style.Treeview")

    columns = [("MID", 120), ("TeamA", 112), ("TeamB", 112),
               ("Winner", 112), ("Loser", 112), ("MVP", 120),
               ("Date", 120), ("Time", 120), ("Venue", 120)]
    for column in columns:
        matches_table.column(column[0], width = column[1], stretch = False)

    headings = [("MID", "MatchID"), ("TeamA", "Team A"), ("TeamB", "Team B"),
               ("Winner", "Winner"), ("Loser", "Loser"), ("MVP", "MVP"),
               ("Date", "Date"), ("Time", "Time"), ("Venue", "Venue")]

    for heading in headings:
        matches_table.heading(heading[0], text = heading[1], anchor = "w")

    for match in matches:
        matches_table.insert('', tk.END, text = '',
                             values = (f"{match[0]}", f"{match[1]}", f"{match[2]}", f"{match[3]}",
                                       f"{match[4]}", f"{match[5]}", f"{match[6]}", f"{match[7]}", f"{match[8]}"))

    matches_table.pack(fill = "both", expand = 1)
    matches_table.config(height = 20)

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
    for team in teams:
        team_table.insert('', tk.END, text = '', values=(f"{team[0]}", f"{team[1]}"))

    team_table.pack(fill = "both", anchor = "w")

def display_players():
    global players_table
    players = Queries.display_all_players()
    players_table = ttk.Treeview(tab3,
                         columns = ("PID", "PName", "Position", "Runs",
                                    "Wickets", "Hundreds", "Fifties", "Highest_Score",
                                    "Five_Wicket_Hauls", "TID"),
                         show = "headings",
                         style = "style.Treeview")
    
    columns = [("PID", 150), ("PName", 112), ("Position", 112),
               ("Runs", 80), ("Wickets", 112), ("Hundreds", 120),
               ("Fifties", 120), ("Highest_Score", 120), ("Five_Wicket_Hauls", 120), ("TID", 112)]
    for column in columns:
        players_table.column(column[0], width = column[1], stretch = False)

    headings = [("PID", "Player ID"), ("PName", "Player Name"), ("Position", "Position"),
               ("Runs", "Runs"), ("Wickets", "Wickets"), ("Hundreds", "Hundreds"),
               ("Fifties", "Fifties"), ("Highest_Score", "Highest Score"),
               ("Five_Wicket_Hauls", "Five Wicket Hauls"), ("TID", "Team ID")]
    for heading in headings:
        players_table.heading(heading[0], text = heading[1], anchor = "w")

    players_table.pack(fill = "both", expand = 1)
    players_table.config(height = 20)

def item_select(table):
    print(team_table.selection())
    for i in table.selection():
        print(table.item(i)['values'])

def delete_items(table):
    for i in table.selection():
        table.delete(i)

def create_match(mid, teama, teamb, winner, loser, mvp, date, time, venue):
    Queries.add_matches(mid, teama, teamb, winner, loser, mvp, date, time, venue)

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
    entry = [(match_id, 15), (team_a, 14), (team_b, 14), (winner, 14),
             (loser, 14), (mvp, 15), (date, 15), (time, 15), (venue, 26)]
    for i in entry:
        ttk.Entry(tab1, textvariable = i[0], width = i[1]).pack(side = tk.LEFT)
    ttk.Button(tab1, text = "+",
               command = lambda: create_match(match_id.get(), team_a.get(), team_b.get(), winner.get(),
                                              loser.get(), mvp.get(), date.get(), time.get(), venue.get())).pack(side = "left")

def tab2_widgets():
    display_teams()
    team_id = ttk.StringVar()
    team_name = ttk.StringVar()
    ttk.Entry(tab2, textvariable = team_id, width = 15).pack(side = tk.LEFT)
    ttk.Entry(tab2, textvariable = team_name, width = 25).pack(side = tk.LEFT)
    ttk.Button(tab2, text = "+", command = lambda: create_team(team_id, team_name)).pack(side = tk.LEFT, anchor = "w")

def tab3_widgets():
    display_players()
    

# Notebook
notebook = ttk.Notebook(window)

tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
notebook.add(tab1, text = "Matches")
notebook.add(tab2, text = "Teams")
notebook.add(tab3, text = "Players")

notebook.pack()
tab1_widgets()
tab2_widgets()
display_players()

# Bindings
for table in (matches_table, team_table):
    table.bind("<<TreeviewSelect>>", lambda event: item_select(table))
    table.bind("<Delete>", lambda event: delete_items(table))
notebook.bind("<<NotebookTabChanged>>", resize_notebook)

#scrollbar
scrollbar_table=ttk.Scrollbar(matches_table,orient='vertical',command=table.yview)
table.configure(yscrollcommand=scrollbar_table.set)
scrollbar_table.place(relx=1,rely=0,anchor='ne')


# run
try:
    window.mainloop()
except KeyboardInterrupt:
    print("\nQuitting")
    exit()