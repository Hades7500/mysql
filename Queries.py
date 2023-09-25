from datetime import *
import mysql.connector as mycon

def login(username, password):
    global cur
    global con
    try:
        con = mycon.connect(host="localhost", user=f"{username}", passwd=f"{password}")
        cur=con.cursor()
        cur.execute("USE WC2023")
        return True
    except:
        print("Incorrect Username or Password")
        return False
        



def auto_increment():
    cur.execute("SELECT PID FROM Players")
    result = cur.fetchall()
    return [row[0] for row in result]

def delete():
    ...

def search():
    ...

def output(data):
    for row in data:
        for col in row:
            print(col,end="\t")
        print()

#Functions to Insert Records
def add_TeamB_Details():
    cur1=con.cursor()    # Create a cursor object for the database connection
    tid=input("Team ID: ").upper()
    mid=input("Match ID: ").upper()
    pid=input("Player ID: ").upper()
    rm=int(input("Runs Scored: "))
    bp=int(input("Balls Played: "))
    frs=int(input("Fours: "))
    six=int(input("Sixes: "))
    st_rate=(rm/bp)*100
    overs=eval(input("Overs Bowled: "))
    maiden=int(input("Maidens Bowled: "))
    rc=int(input("Runs Conceded: "))
    wt=int(input("Wickets Taken: "))
    print()
    if overs>=1:
        eco=(rc/overs)
    else:
        eco=0
    cur.execute("insert into TeamB_Details values('{}','{}','{}',{},{},{},{},{},{},{},{},{},{})".format(tid,mid,pid,rm,bp,frs,six,st_rate,overs,maiden,rc,wt,eco))
    con.commit()
    cur1.execute(f"UPDATE Players SET runs=runs+{rm}, wickets=wickets+{wt}, fours=fours+{frs}, sixes=sixes+{six} where pid='{pid}'")
    con.commit()
    if rm>=100:
        cur1.execute(f"update players set hundreds=hundreds+1 where pid='{pid}'")
    elif rm>=50:
        cur1.execute(f"update players set fifties=fifties+1 where pid='{pid}'")
    con.commit()
    cur1.execute(f"SELECT MAX(runs_made), MIN(runs_made) FROM teamB_details WHERE pid = '{pid}'")
    max_runs = cur1.fetchone()
    if max_runs is not None:
        x, y = max_runs
        cur1.execute(f"update players set highest_score={x} where pid='{pid}'")
        con.commit()
    else:
        print("No runs made for the specified player.")
    con.commit()
    if wt>=5:
        cur1.execute(f"update players set five_wicket_hauls=five_wicket_hauls+1 where pid='{pid}'")
        con.commit()
def add_TeamA_Details():
    cur1.close()    # Close the cursor
    cur1=con.cursor()    # Create a cursor object for the database connection
    tid=input("Team ID: ").upper()
    mid=input("Match ID: ").upper()
    pid=input("Player ID: ").upper()
    rm=int(input("Runs Scored: "))
    bp=int(input("Balls Played: "))
    frs=int(input("Fours: "))
    six=int(input("Sixes: "))
    st_rate=(rm/bp)*100
    overs=eval(input("Overs Bowled: "))
    maiden=int(input("Maidens Bowled: "))
    rc=int(input("Runs Conceded: "))
    wt=int(input("Wickets Taken: "))
    print()
    if overs>=1:
        eco=(rc/overs)
    else:
        eco=0
    cur.execute(f"INSERT INTO TeamA_Details VALUE ('{tid}','{mid}','{pid}','{rm}','{bp}','{frs}','{six}','{st_rate}','{overs}','{maiden}','{rc}','{wt}','{eco}')")
    con.commit()
    cur1.execute(f"update players set runs=runs+{rm}, wickets=wickets+{wt}, fours=fours+{frs}, sixes=sixes+{six} where pid='{pid}'")
    con.commit()
    if rm>=100:
        cur1.execute(f"update players set hundreds=hundreds+1 where pid='{pid}'")
    elif rm>=50:
        cur1.execute(f"update players set fifties=fifties+1 where pid='{pid}'")
    con.commit()
    cur1.execute(f"SELECT MAX(runs_made), MIN(runs_made) FROM teamA_details WHERE pid = '{pid}'")
    max_runs = cur1.fetchone()
    if max_runs is not None:
        x, y = max_runs
        cur1.execute(f"update players set highest_score={x} where pid='{pid}'")
        con.commit()
    else:
        print("No runs made for the specified player.")
    con.commit()
    if wt>=5:
        cur1.execute(f"update players set five_wicket_hauls=five_wicket_hauls+1 where pid='{pid}'")
        con.commit()
    cur1.close()    # Close the cursor
def add_matches(match_id, team_a, team_b, teama_score,
                teama_wickets, teama_extras, teamb_score,
                teamb_wickets, teamb_extras, mvp, date,
                time, venue, teama_overs, teamb_overs):

    if teama_score > teamb_score:
        loser = team_b
        winner = team_a
        cur.execute(f"UPDATE Points_Table SET Wins = Wins + 1, Points=Points + 2 WHERE TID = '{team_a}'")
        cur.execute(f"UPDATE Points_Table SET Losses = Losses + 1 WHERE TID = '{team_b}'")
        cur.execute(f"INSERT INTO Matches VALUES ('{match_id}','{team_a}','{team_b}',{teama_score},{teamb_score},'{teama_wickets}','{teamb_wickets}','{teama_extras}','{teamb_extras}','{winner}','{loser}','{mvp}','{date}','{time}','{venue}','{teama_overs}','{teamb_overs}')")

    elif teama_score < teamb_score:
        loser = team_a
        winner = team_b
        cur.execute(f"update points_table set wins=wins+1, points=points+2 where tid='{team_b}'")
        cur.execute(f"update points_table set Losses = Losses + 1 where tid='{team_a}'")
        cur.execute(f"INSERT INTO Matches VALUES ('{match_id}','{team_a}','{team_b}',{teama_score},{teamb_score},'{teama_wickets}','{teamb_wickets}','{teama_extras}','{teamb_extras}','{winner}','{loser}','{mvp}','{date}','{time}','{venue}','{teama_overs}','{teamb_overs}')")
    elif teamb_overs < 50 and teamb_wickets < 10 and teamb_score < teama_score:
        cur.execute(f"INSERT INTO Matches VALUES ('{match_id}','{team_a}','{team_b}',{teama_score},{teamb_score},'{teama_wickets}','{teamb_wickets}','{teama_extras}','{teamb_extras}',NULL,NULL,'{mvp}','{date}','{time}','{venue}','{teama_overs}','{teamb_overs}')")
    elif teama_overs < 50 and teama_wickets < 10:
        cur.execute(f"INSERT INTO Matches VALUES ('{match_id}','{team_a}','{team_b}',{teama_score},{teamb_score},'{teama_wickets}','{teamb_wickets}','{teama_extras}','{teamb_extras}',NULL,NULL,'{mvp}','{date}','{time}','{venue}','{teama_overs}','{teamb_overs}')")        
    elif teama_score == teamb_score:
        cur.execute(f"INSERT INTO Matches VALUES ('{match_id}','{team_a}','{team_b}',{teama_score},{teamb_score},'{teama_wickets}','{teamb_wickets}','{teama_extras}','{teamb_extras}',NULL,NULL,'{mvp}','{date}','{time}','{venue}','{teama_overs}','{teamb_overs}')")
        cur.execute(f"UPDATE Points_Table SET Points = Points + 1 WHERE TID = '{team_a}' OR TID = '{team_b}'")

    cur.execute(f"UPDATE Players SET NO_OF_MVP = no_of_mvp+1 where PID='{mvp}'")
    cur.execute(f"UPDATE Points_Table SET No_Of_Matches = no_of_matches+1 where tid='{team_a}'")
    cur.execute(f"UPDATE Points_Table SET No_Of_Matches = no_of_matches+1 where tid='{team_b}'")
    xa=teama_score/teama_overs
    xb=teamb_score/teamb_overs
    if winner==team_a:
        nrr=xa-xb
        nrr=round(nrr,3)
        cur.execute(f"update Points_Table set Net_Run_Rate = Net_Run_Rate+{nrr} where tid='{team_a}'") # replace team_a with winner
        cur.execute(f"update Points_Table set Net_Run_Rate = Net_Run_Rate-{nrr} where tid='{team_b}'")
    elif winner==team_b:
        nrr=xb-xa
        nrr=round(nrr,3)
        cur.execute(f"update points_table set Net_Run_Rate = Net_Run_Rate+{nrr} where tid='{team_b}'")
        cur.execute(f"update points_table set Net_Run_Rate = Net_Run_Rate-{nrr} where tid='{team_a}'")
    con.commit()

def add_player(pid, pname, position, tid):
    print()
    cur.execute(f"INSERT INTO Players (PID, PName, Position, TID) values('{pid}','{pname}','{position}','{tid}')")
    con.commit()

def add_team(tid, tname):
    cur.execute(f"INSERT INTO Teams VALUE ('{tid.upper()}','{tname.capitalize()}')")
    cur.execute(f"INSERT INTO Points_Table (TID) VALUE ('{tid}')")
    con.commit()

def insert():
    while True:
        choice=int(input("1.Add Team\n\
                         2.Add Player\n\
                         3.Add Matches\n\
                         4.Add TeamA_Details\n\
                         5.Add TeamB_Details\n\
                         0.Previous\n\
                         (1/2/3/4/5/0): "))
        if choice==1:
            add_team()
        elif choice==2:
            add_player()
        elif choice==3:
            add_matches()
        elif choice==4:
            add_TeamA_Details()
        elif choice==5:
            add_TeamB_Details()
        elif choice==0:
            break

#Functions to Display Stats
def Sixes_stats():
    cur.execute("SELECT PName,T.TID,Sixes FROM Players P, Teams T WHERE P.TID=T.TID")
    data = cur.fetchall()
    data = sorted(data,key=lambda t:t[2], reverse=True)[:5]
    print("Player Name\t\tTeam\t\tSixes")
    for row in data:
        for val in row:
            print(val,end="\t\t\t")
        print()
def Fours_stats():
    cur.execute("select pname,t.tid,Fours from players p, teams t where p.tid=t.tid")
    data=cur.fetchall()
    data_1=sorted(data,key=lambda t:t[2], reverse=True)[:5]
    print("Player Name\t\tTeam\t\tFours")
    for row in data_1:
        for val in row:
            print(val,end="\t\t\t")
        print()
def Five_Wicket_stats():
    cur.execute("select pname,t.tid,Five_Wicket_Hauls from players p, teams t where p.tid=t.tid")
    data=cur.fetchall()
    data_1=sorted(data,key=lambda t:t[2], reverse=True)[:5]
    print("Player Name\t\tTeam\t\tFive-Wicket Hauls")
    for row in data_1:
        for val in row:
            print(val,end="\t\t\t")
        print()
def Fifties_stats():
    cur.execute("select pname,t.tid,Fifties from players p, teams t where p.tid=t.tid")
    data=cur.fetchall()
    data_1=sorted(data,key=lambda t:t[2], reverse=True)[:5]
    print("Player Name\t\tTeam\t\tFifties")
    for row in data_1:
        for val in row:
            print(val,end="\t\t\t")
        print()
def Hundreds_stats():
    cur.execute("select pname,t.tid,hundreds from players p, teams t where p.tid=t.tid")
    data=cur.fetchall()
    data_1=sorted(data,key=lambda t:t[2], reverse=True)[:5]
    print("Player Name\t\tTeam\t\tHundreds")
    for row in data_1:
        for val in row:
            print(val,end="\t\t\t")
        print()
def Highest_score_stats():
    cur.execute("select pname,t.tid,highest_score from players p, teams t where p.tid=t.tid")
    data=cur.fetchall()
    data_1=sorted(data,key=lambda t:t[2], reverse=True)[:5]
    print("Player Name\t\tTeam\t\tHighest Score")
    for row in data_1:
        for val in row:
            print(val,end="\t\t\t")
        print()
def wickets_stats():
    cur.execute("select Pname,t.TID,wickets from players p,teams t where p.tid=t.tid")
    data=cur.fetchall()
    data_1=sorted(data,key=lambda t:t[2], reverse=True)[:5]
    print("Player Name\t\tTeam\t\tWickets")
    for row in data_1:
        for val in row:
            print(val,end="\t\t\t")
        print()
def runs_stats():
    cur.execute("select Pname,t.TID,runs from players p,teams t where p.tid=t.tid")
    data=cur.fetchall()
    data_1=sorted(data,key=lambda t:t[2], reverse=True)[:5]
    print("Player Name\t\tTeam\t\tRuns")
    for row in data_1:
        for val in row:
            print(val,end="\t\t")
        print()
def display_Stats_menu():
    while True:
        #Prompt the user to enter their choice
        choice=int(input("1.Runs\n\
                         2.Wickets\n\
                         3.Highest Score\n\
                         4.Most Hundreds\n\
                         5.Most Fifties\n\
                         6.Five Wicket Hauls\n\
                         7.Sixes\n\
                         8.Fours\n\
                         0.Back\n\
                         (1/2/3/4/5/6/7/8/0): "))
        print()
        #Check the user's choice and perform the corresponding action
        if choice==1:
            runs_stats()
        elif choice==2:
            wickets_stats()
        elif choice==3:
            Highest_score_stats()
        elif choice==4:
            Hundreds_stats()
        elif choice==5:
            Fifties_stats()
        elif choice==6:
            Five_Wicket_stats()
        elif choice==7:
            Sixes_stats()
        elif choice==8:
            Fours_stats()
        elif choice==0:
            break

#Functions To Display Records
def display_TeamB_Details():
    cur.execute("select teams.TID,mid,pname,Runs_Made,Balls_Played,Fours,Sixes,Strike_Rate,Overs_Bowled,Maiden,Runs_Conceded,Wickets_Taken,Economy from TeamB_details t,players p, teams where t.pid=p.pid and t.tid=teams.tid")
    data=cur.fetchall()
    return[detail for detail in data]
def display_TeamA_Details():
    cur.execute("select teams.TID,mid,pname,Runs_Made,Balls_Played,t.Fours,t.Sixes,Strike_Rate,Overs_Bowled,Maiden,Runs_Conceded,Wickets_Taken,Economy from TeamA_details t,players p, teams where t.pid=p.pid and t.tid=teams.tid")
    data=cur.fetchall()
    return[detail for detail in data]
def display_matches():
    cur.execute("SELECT * FROM Matches ORDER BY LENGTH(MID), MID")
    data = cur.fetchall()
    return [match for match in data]

def display_all_players():
    cur.execute("SELECT * FROM Players ORDER BY LENGTH(PID), PID")
    data = cur.fetchall()
    return [player for player in data]

def display_players_of_a_team():
    tid=input("TeamID: ").upper()
    cur.execute(f"SELECT * FROM Players WHERE TID='{tid}'")
    data=cur.fetchall()
    return [player for player in data]

def display_teams():
    cur.execute("SELECT * FROM Teams")
    data = cur.fetchall()
    return [team for team in data]

def display_points_table():
    cur.execute("SELECT * FROM Points_Table")
    data = cur.fetchall()
    return [points for points in data]

def display_menu():
    while True:
        #Prompt the user to enter their choice
        choice=int(input("1.Display Teams\n\
                         2.Display Players of a team\n\
                         3.Display All Players\n\
                         4.Display All Matches\n\
                         5.Display TeamA_Details\n\
                         6.Display TeamB_Details\n\
                         7.Display Stats\n\
                         0.Previous\n\
                         (1/2/3/4/5/6/7/0): "))
        print()
        #Check the user's choice and perform the corresponding action
        if choice==1:
            display_teams()
        elif choice==2:
            display_players_of_a_team()
        elif choice==3:
            display_all_players()
        elif choice==4:
            display_matches()
        elif choice==5:
            display_TeamA_Details()
        elif choice==6:
            display_TeamB_Details()
        elif choice==7:
            display_Stats_menu()
        elif choice==0:
            break

#Function of Initial Menu
def menu():
    while True:
        #Prompt the user to choose an option
        choice=int(input("1.Display Records\n\
                         2.Insert Records\n\
                         3.Search Records\n\
                         4.Update Records\n\
                         5.Delete Record\n\
                         0.Exit\n\
                         (1/2/3/4/5/0): "))
        print()
        if choice==1:
            display_menu()
        elif choice==2:
            insert()
        elif choice==3:
            search()
        elif choice==4:
            delete()
        elif choice==0:
            print("Bye!!")
            break
