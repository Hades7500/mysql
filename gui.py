import tkinter as tk
import ttkbootstrap as ttk
import Queries

window = ttk.Window(themename = "darkly",)
window.title("World Cup")
window.geometry("1600x900")

ttk.Label(window, text = "World Cup 2023", font = "SaxMono 50").pack()

style = ttk.Style()

style.configure("style.Treeview", font = ("SaxMono", 15), tabposition = tk.NSEW)
style.configure("style.Treeview.Heading", font = ("SaxMono", 20))

def login_box():
    global login_frame
    login_frame = ttk.Toplevel()
    login_frame.geometry("300x160")
    login_frame.maxsize(width = 300, height = 160)
    login_frame.minsize(width = 300, height = 160)
    login_frame.title("Login")

    username = ttk.StringVar(value = "Username")
    password = ttk.StringVar(value = "Password")
    user_entry = ttk.Entry(login_frame, textvariable = username, foreground = "Light Gray")
    user_entry.grid(column = 2, row = 1, columnspan = 2, padx = 75, pady = 5)
    pass_entry = ttk.Entry(login_frame, textvariable = password, foreground = "Light Gray", show = "*")
    pass_entry.grid(column = 2, row = 2, columnspan = 2, padx = 75, pady = 5)
    user_entry.bind("<FocusIn>", lambda event: username.set(""))
    pass_entry.bind("<FocusIn>", lambda event: password.set(""))
    
    login_button = ttk.Button(login_frame, text = "Login", command = lambda: login(username.get(), password.get()))
    login_button.grid(column = 2, row = 3, sticky = "e", padx = 2)
    pass_entry.bind("<Return>", lambda event: login(username.get(), password.get()))
    
    cancel_button = ttk.Button(login_frame, text = "Cancel", command = quit)
    cancel_button.grid(column = 3, row = 3, sticky = "w", padx = 2)
    
    window.wait_window(login_frame)

def login(username, password):
    result = Queries.login(username, password)
    login_frame.destroy()
    login_frame.update()
    if not(result):
        exit()

def quit():
    login_frame.destroy()
    exit()

def clear_frame(parent):
    for widgets in parent.winfo_children():
        widgets.destroy()

def resize_notebook(_):
    if notebook.select() == ".!notebook.!frame":
        notebook.config(width = 1150, height = 415)
    elif notebook.select() == ".!notebook.!frame2":
        notebook.config(width = 339, height = 246)
    elif notebook.select() == ".!notebook.!frame3":
        notebook.config(width = 1150, height = 415)
    # else:
    #     notebook.configure


def display_matches():
    global matches_table
    matches = Queries.display_matches()
    matches_table = ttk.Treeview(tab1,
                         columns = ("MID", "TeamA", "TeamB", "TeamA_Score", "TeamA_Wickets",
                                    "TeamA_Extras", "TeamB_Score", "TeamB_Wickets", "TeamB_Extras", "Winner",
                                    "Loser", "MVP", "Date", "Time", "Venue", "TeamA_Overs", "TeamB_Overs"),
                         show = "headings",
                         style = "style.Treeview")

    columns = [("MID", 120), ("TeamA", 112), ("TeamB", 112),
               ("TeamA_Score", 112), ("TeamA_Wickets", 112), ("TeamA_Extras", 112),
               ("TeamB_Score", 112), ("TeamB_Wickets", 112), ("TeamB_Extras", 112),
               ("Winner", 112), ("Loser", 112), ("MVP", 120),
               ("Date", 120), ("Time", 120), ("Venue", 120),
               ("TeamA_Overs", 112), ("TeamB_Overs", 112)]
    for column in columns:
        matches_table.column(column[0], width = column[1], stretch = False)

    headings = [("MID", "MatchID"), ("TeamA", "Team A"), ("TeamB", "Team B"),
               ("TeamA_Score", "Team A Score"), ("TeamA_Wickets", "Team A Wickets"), ("TeamA_Extras", "Team A Extras"),
               ("TeamB_Score", "Team B Score"), ("TeamB_Wickets", "Team B Wickets"), ("TeamB_Extras", "Team B Extras"),
               ("Winner", "Winner"), ("Loser", "Loser"), ("MVP", "MVP"),
               ("Date", "Date"), ("Time", "Time"), ("Venue", "Venue"),
               ("TeamA_Overs", "Team A Overs"), ("TeamB_Overs", "Team B Overs")]

    for heading in headings:
        matches_table.heading(heading[0], text = heading[1], anchor = "w")

    for match in matches:
        matches_table.insert('', tk.END, text = '',
                             values = match)

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
        team_table.insert('', tk.END, text = '', values = team)

    team_table.pack(fill = "both", anchor = "w")

def display_players():
    global players_table
    players = Queries.display_all_players()
    players_table = ttk.Treeview(tab3,
                         columns = ("PID", "PName", "Position", "Runs",
                                    "Wickets", "Hundreds", "Fifties", "Highest_Score",
                                    "Five_Wicket_Hauls", "TID"),
                         show = "headings",
                         style = "style.Treeview", selectmode = "browse")

    columns = [("PID", 150), ("PName", 180), ("Position", 135),
               ("Runs", 80), ("Wickets", 120), ("Hundreds", 125),
               ("Fifties", 120), ("Highest_Score", 210), ("Five_Wicket_Hauls", 385), ("TID", 112)]
    for column in columns:
        players_table.column(column[0], width = column[1], stretch = False)

    headings = [("PID", "Player ID"), ("PName", "Player Name"), ("Position", "Position"),
               ("Runs", "Runs"), ("Wickets", "Wickets"), ("Hundreds", "Hundreds"),
               ("Fifties", "Fifties"), ("Highest_Score", "Highest Score"),
               ("Five_Wicket_Hauls", "Five Wicket Hauls"), ("TID", "Team ID")]
    for heading in headings:
        players_table.heading(heading[0], text = heading[1], anchor = "w")

    for player in players:
        players_table.insert('', tk.END, text = "",
                             values = player)

    players_table.pack(fill = "both", expand = 1)
    players_table.config(height = 20)

def item_select(table_name):
    for i in table_name.selection():
        print(table_name.item(i)['values'])

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
               command = lambda: create_match(match_id.get(), team_a.get(),
                                              team_b.get(), winner.get(),
                                              loser.get(), mvp.get(), date.get(),
                                              time.get(), venue.get())).pack(side = "left")

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

notebook.pack(side = "top")
login_box()
tab1_widgets()
tab2_widgets()
display_players()

# Bindings
for table in [matches_table, team_table]:
    table.bind("<<TreeviewSelect>>", lambda event: item_select(table))
    table.bind("<Delete>", lambda event: delete_items(table))
notebook.bind("<<NotebookTabChanged>>", resize_notebook)

#scrollbar
for table in [matches_table, players_table]:
    scrollbar = ttk.Scrollbar(table, orient = 'horizontal', command = table.xview)
    table.configure(xscrollcommand = scrollbar.set)
    scrollbar.place(relx=0, rely=1, relwidth = 1, anchor = "sw")


# run
try:
    window.mainloop()
except KeyboardInterrupt:
    print("\nQuitting")
    exit()