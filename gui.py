import tkinter as tk
import ttkbootstrap as ttk
import Queries

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

def resize_notebook(_):
    if notebook.select() == ".!notebook.!frame":
        notebook.config(width = 1920, height = 415)
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

def TeamA_Details():
    global TeamA_Details
    TeamA = Queries.display_TeamA_Details()
    TeamA_Details = ttk.Treeview(tab4,
                         columns = ("TID", "MID", "PID", "Runs_made",
                                    "Balls_played", "Fours", "Sixes", "Strike_rate",
                                    "Over_Bowled", "Runs_conceded","Wickets_Taken","Economy"),
                         show = "headings",
                         style = "style.Treeview", selectmode = "browse")

    columns = [("TID",150),("MID",150),("PID", 150), ("Runs_made", 180), ("Balls_played", 135),
               ("Fours", 80), ("Sixes", 120), ("Strike_rate", 125),
               ("Over_Bowled", 120), ("Runs_conceded", 210), ("Wickets_Taken", 385), ("Economy", 112)]
    for column in columns:
        TeamA_Details.column(column[0], width = column[1], stretch = False)

    headings = [("TID", "Team ID"), ("MID", "Match ID"), ("Balls_played", "Balls_played"),
               ("Runs_made", "Runs_made"),("Fours", "Fours"), ("Sixes", "Sixes"),
               ("Strike_rate", "Strike_rate"), ("Over_Bowled", "Over_Bowled"),
               ("Runs_conceded", "Runs_conceded"), ("Wickets_Taken", "Wickets_Taken"),("Economy","Economy")]
    for heading in headings:
        TeamA_Details.heading(heading[0], text = heading[1], anchor = "w")

    for team in TeamA_Details:
        TeamA_Details.insert('', tk.END, text = '',
                             values = team)
    TeamA_Details.pack(fill = "both", expand = 1)
    TeamA_Details.config(height = 20)

def TeamB_Details():
    global TeamB_Details
    TeamB = Queries.display_TeamB_Details()
    TeamB_Details = ttk.Treeview(tab5,
                         columns = ("TID", "MID", "PID", "Runs_made",
                                    "Balls_played", "Fours", "Sixes", "Strike_rate",
                                    "Over_Bowled", "Runs_conceded","Wickets_Taken","Economy"),
                         show = "headings",
                         style = "style.Treeview", selectmode = "browse")

    columns = [("TID",150),("MID",150),("PID", 150), ("Runs_made", 180), ("Balls_played", 135),
               ("Fours", 80), ("Sixes", 120), ("Strike_rate", 125),
               ("Over_Bowled", 120), ("Runs_conceded", 210), ("Wickets_Taken", 385), ("Economy", 112)]
    for column in columns:
        TeamB_Details.column(column[0], width = column[1], stretch = False)

    headings = [("TID", "Team ID"), ("MID", "Match ID"), ("Balls_played", "Balls_played"),
               ("Runs_made", "Runs_made"),("Fours", "Fours"), ("Sixes", "Sixes"),
               ("Strike_rate", "Strike_rate"), ("Over_Bowled", "Over_Bowled"),
               ("Runs_conceded", "Runs_conceded"), ("Wickets_Taken", "Wickets_Taken"),("Economy","Economy")]
    for heading in headings:
        TeamB_Details.heading(heading[0], text = heading[1], anchor = "w")

    TeamB_Details.pack(fill = "both", expand = 1)
    TeamB_Details.config(height = 20)

def points_table():
    global points_table
    points_table = Queries.display_points_table()
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

    points_table.pack(fill = "both", expand = 1)
    points_table.config(height = 20)





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
    match_id, team_a, team_b, teama_score,\
    teama_wickets, teama_extras, teamb_score,\
    teamb_wickets, teamb_extras, winner,\
    loser, mvp, date, time, venue, teama_overs, teamb_overs = [ttk.StringVar() for _ in range(17)]
    entry = [(match_id, 15), (team_a, 14), (team_b, 14), (teama_score, 14),
             (teama_extras, 14), (teama_wickets, 14),(teamb_score, 14),
             (teamb_wickets, 14), (teamb_extras, 14), (winner, 14),
             (loser, 14), (mvp, 15), (date, 15), (time, 15), (venue, 26),
             (teama_overs, 14), (teamb_overs, 14)]
    for i in entry:
        ttk.Entry(tab1, textvariable = i[0], width = i[1]).pack(side = tk.LEFT)
    ttk.Button(tab1, text = "Add Match",
               command = lambda: create_match(match_id.get(), team_a.get(), team_b.get(), teama_score.get(),
                                                teama_wickets.get(), teama_extras.get(), teamb_score.get(),
                                                teamb_wickets.get(), teamb_extras.get(), winner.get(),
                                                loser.get(), mvp.get(), date.get(), time.get(),
                                                venue.get(), teama_overs.get(), teamb_overs.get())).pack(side = "left")

def tab2_widgets():
    display_teams()
    team_id = ttk.StringVar()
    team_name = ttk.StringVar()
    ttk.Entry(tab2, textvariable = team_id, width = 15).pack(side = tk.LEFT)
    ttk.Entry(tab2, textvariable = team_name, width = 25).pack(side = tk.LEFT)
    ttk.Button(tab2, text = "+", command = lambda: create_team(team_id, team_name)).pack(side = tk.LEFT, anchor = "w")

def tab3_widgets():
    display_players()
    
def tab4_widgets():
    TeamA_Details()
    
def tab5_widgets():
    TeamB_Details()

def tab6_widgets():
    points_table()
window = ttk.Window(themename = "darkly")
window.title("World Cup")
window.geometry("1600x900")

ttk.Label(window, text = "World Cup 2023", font = "SaxMono 50").pack()

style = ttk.Style()

style.configure("style.Treeview", font = ("SaxMono", 15), tabposition = tk.NSEW)
style.configure("style.Treeview.Heading", font = ("SaxMono", 20))


# Notebook
notebook = ttk.Notebook(window)

tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
notebook.add(tab1, text = "Matches")
notebook.add(tab2, text = "Teams")
notebook.add(tab3, text = "Players")

login_box()
try:
    notebook.pack(side = "top")
    notebook.config(width = 1150, height = 415)
    tab1_widgets()
    tab2_widgets()
    display_players()
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
