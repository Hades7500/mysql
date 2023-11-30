import tkinter as tk
import ttkbootstrap as ttk
from PIL import ImageTk, Image
import Queries

def login_box():
    global login_frame
    login_frame = ttk.Toplevel(title = "Login", resizable = (False, False))
    login_frame.geometry(f"300x160+{int(SCREEN_WIDTH/2) - 150}+{int(SCREEN_HEIGHT/2) - 80}")

    username = ttk.StringVar(value = "Username")
    password = ttk.StringVar(value = "Password")
    user_entry = ttk.Entry(login_frame, textvariable = username, foreground = "Black")
    user_entry.grid(column = 2, row = 1, columnspan = 2, padx = 75, pady = 5)
    pass_entry = ttk.Entry(login_frame, textvariable = password, foreground = "Black", show = "*")
    pass_entry.grid(column = 2, row = 2, columnspan = 2, padx = 75, pady = 5)
    user_entry.bind("<FocusIn>", lambda event: username.set(""))
    pass_entry.bind("<FocusIn>", lambda event: password.set(""))
    
    login_button = ttk.Button(login_frame, text = "Login", command = lambda: login(username.get(), password.get()))
    login_button.grid(column = 2, row = 3, sticky = "e", padx = 2)
    pass_entry.bind("<Return>", lambda event: login(username.get(), password.get()))
    
    cancel_button = ttk.Button(login_frame, text = "Cancel", command = quit)
    cancel_button.grid(column = 3, row = 3, sticky = "w", padx = 2)
    
    window.wait_window(login_frame)

def login(username: str, password: str):
    result = Queries.login(username, password)
    login_frame.destroy()
    if not(result):
        exit()

def quit():
    window.destroy()
    exit()

def clear_frame(parent):
    for widgets in parent.winfo_children():
        widgets.destroy()

def raise_error(msg):
    error = ttk.Toplevel(title = "Error", resizable = (False, False))
    error.geometry(f"300x160+{int(SCREEN_WIDTH/2) - 150}+{int(SCREEN_HEIGHT/2) - 80}")
    ttk.Label(error, text = msg).pack(pady = 20)
    ttk.Button(error, text = "Ok", command = error.destroy).pack()


def resize_notebook(_):
    if notebook.select() == ".!notebook.!frame":
        notebook.config(width = 1150, height = 415)
    elif notebook.select() == ".!notebook.!frame2":
        notebook.config(width = 300, height = 246)
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
               ("TeamA_Score", 198), ("TeamA_Wickets", 242), ("TeamA_Extras", 220),
               ("TeamB_Score", 198), ("TeamB_Wickets", 242), ("TeamB_Extras", 220),
               ("Winner", 112), ("Loser", 112), ("MVP", 100),
               ("Date", 100), ("Time", 100), ("Venue", 176),
               ("TeamA_Overs", 198), ("TeamB_Overs", 198)]
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

    team_table.pack(fill = "none", anchor = "center")

def display_players():
    global players_table
    players = Queries.display_all_players()
    players_table = ttk.Treeview(tab3,
                         columns = ("PID", "PName", "Position", "Runs",
                                    "Wickets", "Hundreds", "Fifties", "Sixes",
                                    "Fours", "Highest_Score",
                                    "Five_Wicket_Hauls", "No_Of_MVP", "TID"),
                         show = "headings",
                         style = "style.Treeview", selectmode = "browse")

    columns = [("PID", 150), ("PName", 180), ("Position", 135),
               ("Runs", 80), ("Wickets", 120), ("Hundreds", 125),
               ("Fifties", 120), ("Sixes", 112), ("Fours", 112), ("Highest_Score", 210),
               ("Five_Wicket_Hauls", 330), ("No_Of_MVP", 190), ("TID", 112)]
    for column in columns:
        players_table.column(column[0], width = column[1], stretch = False)

    headings = [("PID", "Player ID"), ("PName", "Player Name"), ("Position", "Position"),
               ("Runs", "Runs"), ("Wickets", "Wickets"), ("Hundreds", "Hundreds"),
               ("Fifties", "Fifties"), ("Sixes", "Sixes"), ("Fours", "Fours"), ("Highest_Score", "Highest Score"),
               ("Five_Wicket_Hauls", "Five Wicket Hauls"), ("No_Of_MVP", "No Of MVP"), ("TID", "Team ID")]
    for heading in headings:
        players_table.heading(heading[0], text = heading[1], anchor = "w")

    for player in players:
        players_table.insert('', tk.END, text = "",
                             values = player)

    players_table.pack(fill = "both", expand = 1)
    players_table.config(height = 20)

def display_run_stats():
    global run_stats
    stats = Queries.runs_stats()
    run_stats = ttk.Treeview(tab7,
                             columns = ("PName", "TID", "Runs"),
                             show = "headings",
                             style = "style.Treeview")
    run_stats.column("PName", width = 220)
    run_stats.heading("PName", text = "Player Name", anchor = "w")
    run_stats.heading("TID", text = "TID", anchor = "w")
    run_stats.heading("Runs", text = "Runs", anchor = "w")
    for stat in stats:
        run_stats.insert('', tk.END, text = '', values = stat)

    run_stats.pack(fill = "both", expand = 1)

def display_wicket_stats():
    global wicket_stats
    stats = Queries.wickets_stats()
    wicket_stats = ttk.Treeview(tab8,
                             columns = ("PName", "TID", "Wickets"),
                             show = "headings",
                             style = "style.Treeview")
    wicket_stats.column("PName", width = 220)
    wicket_stats.heading("PName", text = "Player Name", anchor = "w")
    wicket_stats.heading("TID", text = "TID", anchor = "w")
    wicket_stats.heading("Wickets", text = "Wickets", anchor = "w")
    for stat in stats:
        wicket_stats.insert('', tk.END, text = '', values = stat)

    wicket_stats.pack(fill = "both", expand = 1)

def highest_score_stats():
    global score_stats
    stats = Queries.Highest_score_stats()
    score_stats = ttk.Treeview(tab9,
                             columns = ("PName", "TID", "Highest_Score"),
                             show = "headings",
                             style = "style.Treeview")
    score_stats.column("PName", width = 220)
    score_stats.heading("PName", text = "Player Name", anchor = "w")
    score_stats.heading("TID", text = "TID", anchor = "w")
    score_stats.heading("Highest_Score", text = "Highest Score", anchor = "w")
    for stat in stats:
        score_stats.insert('', tk.END, text = '', values = stat)

    score_stats.pack(fill = "both", expand = 1)

def display_hundreds_stats():
    global hundreds_stats
    stats = Queries.Hundreds_stats()
    hundreds_stats = ttk.Treeview(tab10,
                             columns = ("PName", "TID", "Hundreds"),
                             show = "headings",
                             style = "style.Treeview")
    hundreds_stats.column("PName", width = 220)
    hundreds_stats.heading("PName", text = "Player Name", anchor = "w")
    hundreds_stats.heading("TID", text = "TID", anchor = "w")
    hundreds_stats.heading("Hundreds", text = "Hundreds", anchor = "w")
    for stat in stats:
        hundreds_stats.insert('', tk.END, text = '', values = stat)

    hundreds_stats.pack(fill = "both", expand = 1)

def display_fifties_stats():
    global fifties_stats
    stats = Queries.Fifties_stats()
    fifties_stats = ttk.Treeview(tab11,
                             columns = ("PName", "TID", "Fifties"),
                             show = "headings",
                             style = "style.Treeview")
    fifties_stats.column("PName", width = 220)
    fifties_stats.heading("PName", text = "Player Name", anchor = "w")
    fifties_stats.heading("TID", text = "TID", anchor = "w")
    fifties_stats.heading("Fifties", text = "Fifties", anchor = "w")
    for stat in stats:
        fifties_stats.insert('', tk.END, text = '', values = stat)

    fifties_stats.pack(fill = "both", expand = 1)


def display_five_wickets_stats():
    global five_wickets_stats
    stats = Queries.Five_Wicket_stats()
    five_wickets_stats = ttk.Treeview(tab12,
                             columns = ("PName", "TID", "Five_Wicket_Hauls"),
                             show = "headings",
                             style = "style.Treeview")
    five_wickets_stats.column("PName", width = 220)
    five_wickets_stats.heading("PName", text = "Player Name", anchor = "w")
    five_wickets_stats.heading("TID", text = "TID", anchor = "w")
    five_wickets_stats.heading("Five_Wicket_Hauls", text = "Five Wicket Hauls", anchor = "w")
    for stat in stats:
        five_wickets_stats.insert('', tk.END, text = '', values = stat)

    five_wickets_stats.pack(fill = "both", expand = 1)

def display_fours_stats():
    global fours_stats
    stats = Queries.Fours_stats()
    fours_stats = ttk.Treeview(tab13,
                             columns = ("PName", "TID", "Fours"),
                             show = "headings",
                             style = "style.Treeview")
    fours_stats.column("PName", width = 220)
    fours_stats.heading("PName", text = "Player Name", anchor = "w")
    fours_stats.heading("TID", text = "TID", anchor = "w")
    fours_stats.heading("Fours", text = "Fours", anchor = "w")
    for stat in stats:
        fours_stats.insert('', tk.END, text = '', values = stat)

    fours_stats.pack(fill = "both", expand = 1)

def display_sixes_stats():
    global sixes_stats
    stats = Queries.Sixes_stats()
    sixes_stats = ttk.Treeview(tab14,
                             columns = ("PName", "TID", "Sixes"),
                             show = "headings",
                             style = "style.Treeview")
    sixes_stats.column("PName", width = 220)
    sixes_stats.heading("PName", text = "Player Name", anchor = "w")
    sixes_stats.heading("TID", text = "TID", anchor = "w")
    sixes_stats.heading("Sixes", text = "Sixes", anchor = "w")
    for stat in stats:
        sixes_stats.insert('', tk.END, text = '', values = stat)

    sixes_stats.pack(fill = "both", expand = 1)

def TeamA_Details():
    global TeamA_Table
    Teams = Queries.display_TeamA_Details()
    TeamA_Table = ttk.Treeview(tab4,
                                columns = ("TID", "MID", "PID", "Runs_made",
                                            "Balls_played", "Fours", "Sixes", "Strike_rate",
                                            "Over_Bowled", "Runs_conceded","Wickets_Taken","Economy"),
                                show = "headings",
                                style = "style.Treeview", selectmode = "browse")

    columns = [("TID",150),("MID",150),("PID", 150), ("Runs_made", 180), ("Balls_played", 135),
               ("Fours", 80), ("Sixes", 120), ("Strike_rate", 125),
               ("Over_Bowled", 120), ("Runs_conceded", 210), ("Wickets_Taken", 385), ("Economy", 112)]
    for column in columns:
        TeamA_Table.column(column[0], width = column[1], stretch = False)

    headings = [("TID", "Team ID"), ("MID", "Match ID"), ("Balls_played", "Balls_played"),
               ("Runs_made", "Runs_made"),("Fours", "Fours"), ("Sixes", "Sixes"),
               ("Strike_rate", "Strike_rate"), ("Over_Bowled", "Over_Bowled"),
               ("Runs_conceded", "Runs_conceded"), ("Wickets_Taken", "Wickets_Taken"),("Economy","Economy")]
    for heading in headings:
        TeamA_Table.heading(heading[0], text = heading[1], anchor = "w")

    for team in Teams:
        TeamA_Table.insert('', tk.END, text = '',
                            values = team)
    TeamA_Table.pack(fill = "both", expand = 1)
    TeamA_Table.config(height = 20)

def TeamB_Details():
    global TeamB_Table
    Teams = Queries.display_TeamB_Details()
    TeamB_Table = ttk.Treeview(tab5,
                         columns = ("TID", "MID", "PID", "Runs_made",
                                    "Balls_played", "Fours", "Sixes", "Strike_rate",
                                    "Over_Bowled", "Runs_conceded","Wickets_Taken","Economy"),
                         show = "headings",
                         style = "style.Treeview", selectmode = "browse")

    columns = [("TID",150),("MID",150),("PID", 150), ("Runs_made", 180), ("Balls_played", 135),
               ("Fours", 80), ("Sixes", 120), ("Strike_rate", 125),
               ("Over_Bowled", 120), ("Runs_conceded", 210), ("Wickets_Taken", 385), ("Economy", 112)]
    for column in columns:
        TeamB_Table.column(column[0], width = column[1], stretch = False)

    headings = [("TID", "Team ID"), ("MID", "Match ID"), ("Balls_played", "Balls_played"),
               ("Runs_made", "Runs_made"),("Fours", "Fours"), ("Sixes", "Sixes"),
               ("Strike_rate", "Strike_rate"), ("Over_Bowled", "Over_Bowled"),
               ("Runs_conceded", "Runs_conceded"), ("Wickets_Taken", "Wickets_Taken"),("Economy","Economy")]
    for heading in headings:
        TeamB_Table.heading(heading[0], text = heading[1], anchor = "w")

    for team in Teams:
        TeamA_Table.insert('', tk.END, text = '',
                            values = team)

    TeamB_Table.pack(fill = "both", expand = 1)
    TeamB_Table.config(height = 20)

def display_points_table():
    global points_table
    points = Queries.display_points_table()
    points_table = ttk.Treeview(tab6,
                         columns = ("TID","Matches", "Wins", "Losses", "Net_Runrate",
                                    "Points",),
                         show = "headings",
                         style = "style.Treeview", selectmode = "browse")

    columns = [("TID",150),("Matches",150),("Wins", 150), ("Losses", 180), ("Net_Runrate", 135),
               ("Points", 80)]
    for column in columns:
        points_table.column(column[0], width = column[1], stretch = False)

    headings = [("TID", "Table ID"), ("Matches", "Matches"), ("Wins", "Wins"),
               ("Losses", "Losses"),("Net_Runrate","NRR"),("Points","Points")]
    for heading in headings:
        points_table.heading(heading[0], text = heading[1], anchor = "w")

    for point in points:
        points_table.insert('', tk.END, text = '', values = point)

    points_table.pack(fill = "both", expand = 1)
    points_table.config(height = 20)

def item_select(table_name):
    for i in table_name.selection():
        print(table_name.item(i)['values'])

def delete_items(table):
    for i in table.selection():
        table.delete(i)

def create_match():
    match_id, team_a, team_b, winner,\
    loser, mvp, date, time, venue = [ttk.StringVar() for _ in range(9)]
    
    teama_score, teama_wickets, teama_extras, teamb_score,\
    teamb_wickets, teamb_extras = [ttk.IntVar() for _ in range(6)]

    teama_overs, teamb_overs = [ttk.DoubleVar() for _ in range(2)]

    new_match = ttk.Toplevel(title = "Add New Match")
    data = [("MID", match_id), ("Team A", team_a), ("Team B", team_b),
            ("Team A Score", teama_score), ("Team A Wickets", teama_wickets), ("Team A Extras", teama_extras),
            ("Team B Score",teamb_score), ("Team B Wickets", teamb_wickets), ("Team B Extras", teamb_extras),
            ("MVP", mvp),
            ("Date", date), ("Time", time), ("Venue", venue),
            ("Team A Overs", teama_overs), ("Team B Overs", teamb_overs)]
    for row_num, column_data in enumerate(data, 1):
        ttk.Label(new_match, text = column_data[0]).grid(column = 0, row = row_num)
        ttk.Entry(new_match, textvariable = column_data[1]).grid(column = 1, row = row_num, padx = 10)
    date = ttk.DateEntry(new_match, dateformat = "%Y-%m-%d")
    date.grid(column = 1, row = 11, padx = 10)


    arguments = (match_id, team_a, team_b, teama_score,\
                 teama_wickets, teama_extras, teamb_score,\
                 teamb_wickets, teamb_extras, \
                 mvp, date.entry, time, venue, teama_overs, teamb_overs)
    ttk.Button(new_match, text = "Add Match", command = lambda: check_match_details(arguments, new_match)).grid(column = 0, columnspan = 2, pady = 5)

def check_match_details(arguments, toplevel_window):
    
    teams = dict(Queries.display_teams())
    players = Queries.display_all_players()
    if  (arguments[1].get() not in teams) or (arguments[2].get() not in teams):
        raise_error("Team Not Found")
    elif not len([player for player in players if player[0] == arguments[9].get()]):
        raise_error("Player Not Found")
    else:
        Queries.add_matches(*(var.get() for var in arguments))
        toplevel_window.destroy()
        clear_frame(tab1)
        tab1_widgets()

def create_team():
    tid, tname = (ttk.StringVar() for _ in range(2))
    new_team = ttk.Toplevel(title = "Add New Team")
    data = [("TID", tid), ("TName", tname)]
    for row_num, column_data in enumerate(data, 1):
        ttk.Label(new_team, text = column_data[0]).grid(column = 0, row = row_num)
        ttk.Entry(new_team, textvariable = column_data[1]).grid(column = 1, row = row_num, padx = 10)

    ttk.Button(new_team, text = "Add Team", command = lambda: check_team_details(tid.get(), tname.get(), new_team)).grid(column = 0, columnspan = 2, pady = 5)

def check_team_details(tid, tname, toplevel_window):
    teams = dict(Queries.display_teams())
    if len(tname) == 0 or len(tid) == 0:
        raise_error("Invalid TID or TName")
    elif len(tname) > 30:
        raise_error("Lenth of Team Name cant be greater than 30")
    elif tid in teams:
        raise_error("Team already exists")
    else:
        Queries.add_team(tid, tname)
        toplevel_window.destroy()
        clear_frame(tab2)
        tab2_widgets()

def add_player():
    pid, pname, position, tid = [ttk.StringVar() for _ in range(4)]

    data = [("PID", pid), ("PName", pname), ("Position", position), ("TID", tid)]
    
    new_player = ttk.Toplevel(title = "Add New Player")
    for row_num, column_data in enumerate(data, 1):
        ttk.Label(new_player, text = column_data[0]).grid(column = 0, row = row_num)
        ttk.Entry(new_player, textvariable = column_data[1]).grid(column = 1, row = row_num, padx = 10)

    arguments = (pid, pname, position, tid)

    ttk.Button(new_player, text = "Add Player", command = lambda: check_player_details(arguments, new_player)).grid(column = 0, columnspan = 2, pady = 5)

def check_player_details(arguments, toplevel_window):
    teams = dict(Queries.display_teams())
    players = Queries.display_all_players()
    if len(arguments[0].get()) == 0 or len(arguments[1].get()) == 0:
        raise_error("Invalid PID or PName")
    elif arguments[3].get() not in teams:
        raise_error("Team does not exist")
    elif arguments[0].get() in [player[0] for player in players]:
        raise_error("Player already exists")
    else:
        Queries.add_player(*(var.get() for var in arguments))
        toplevel_window.destroy()
        clear_frame(tab3)
        tab3_widgets()

def tab1_widgets():
    display_matches()
    ttk.Button(tab1, text = "Add Match",
               command = create_match).pack()

def tab2_widgets():
    display_teams()
    ttk.Button(tab2, text = "Add Team",
               command = create_team).pack()

def tab3_widgets():
    display_players()
    ttk.Button(tab3, text = "Add Player",
               command = add_player).pack()
    
def tab4_widgets():
    TeamA_Details()
    
def tab5_widgets():
    TeamB_Details()

def tab6_widgets():
    display_points_table()

window = ttk.Window(themename = "flatly")
window.title("World Cup")
SCREEN_HEIGHT = window.winfo_screenheight()
SCREEN_WIDTH = window.winfo_screenwidth()
window.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
bg = ImageTk.PhotoImage(Image.open("background.jpeg").resize(size = (1920, 1080)))
bg_label = ttk.Label(window, image = bg)
bg_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

ttk.Label(window, text = "World Cup 2023", font = "SaxMono 50").pack()

style = ttk.Style()

style.configure("style.Treeview", font = ("SaxMono", 15), tabposition = tk.NSEW)
style.configure("style.Treeview.Heading", font = ("SaxMono", 20))

# Notebook
notebook = ttk.Notebook(window)

tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
tab4 = ttk.Frame(notebook)
tab5 = ttk.Frame(notebook)
tab6 = ttk.Frame(notebook)
tab7 = ttk.Frame(notebook)
tab8 = ttk.Frame(notebook)
tab9 = ttk.Frame(notebook)
tab10 = ttk.Frame(notebook)
tab11 = ttk.Frame(notebook)
tab12 = ttk.Frame(notebook)
tab13 = ttk.Frame(notebook)
tab14 = ttk.Frame(notebook)

notebook.add(tab1, text = "Matches")
notebook.add(tab2, text = "Teams")
notebook.add(tab3, text = "Players")
notebook.add(tab4, text = "Team A Details")
notebook.add(tab5, text = "Team B Details")
notebook.add(tab6, text = "Points")
notebook.add(tab7, text = "Runs")
notebook.add(tab8, text = "Wicket")
notebook.add(tab9, text = "Highest Score")
notebook.add(tab10, text = "Hundreds")
notebook.add(tab11, text = "Fifties")
notebook.add(tab12, text = "Five Wicket Hauls")
notebook.add(tab13, text = "Fours")
notebook.add(tab14, text = "Sixes")

login_box()
# Code continues executing and tries to use mySQL even after entering wrong password is entered
# throws error because mySQL cursor does not exist
try:
    notebook.pack(side = "bottom")
    notebook.config(width = 1150, height = 415)
    tab1_widgets()
    tab2_widgets()
    tab3_widgets()
    tab4_widgets()
    tab5_widgets()
    tab6_widgets()
    display_run_stats()
    display_wicket_stats()
    highest_score_stats()
    display_hundreds_stats()
    display_fifties_stats()
    display_five_wickets_stats()
    display_fours_stats()
    display_sixes_stats()
except Exception as err:
    print(err)
    exit()

# Bindings
for table in [matches_table, team_table]:
    table.bind("<<TreeviewSelect>>", lambda event: item_select(table))
    table.bind("<Delete>", lambda event: delete_items(table))
notebook.bind("<<NotebookTabChanged>>", resize_notebook)

for table in [matches_table, team_table, players_table]:
    table.bind("<Motion>", "break")

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
