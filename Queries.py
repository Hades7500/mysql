from datetime import *  # In case gives error, run pip install datetime
import maskpass  # In case gives error, run pip install maskpass
import mysql.connector as mycon
from dateutil import parser

while True:
        username=input("UserName: ")
        password = maskpass.askpass(prompt="Password: ", mask="*")
        con=mycon.connect(host="localhost",user=f"{username}",passwd=f"{password}")
        if con.is_connected():
            cur=con.cursor()
            cur.execute("use WC2023")
            break
        else:
            print("Username or Password Doesn't Match")
            continue

def auto_increment():
    cur.execute("SELECT PID FROM Players")
    result = cur.fetchall()
    return [row[0] for row in result]
def delete():
    ...
def update():
    ...
def search():
    ...

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
    cur1.execute(f"update players set runs=runs+{rm}, wickets=wickets+{wt}, fours=fours+{frs}, sixes=sixes+{six} where pid='{pid}'")
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
    cur1.close()    # Close the cursor
def add_TeamA_Details():
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
    cur.execute("insert into TeamA_Details values('{}','{}','{}',{},{},{},{},{},{},{},{},{},{})".format(tid,mid,pid,rm,bp,frs,six,st_rate,overs,maiden,rc,wt,eco))
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
def add_matches():
    m_id=input("Match ID:").upper()
    cur.execute("select tid from teams")
    data=cur.fetchall()
    while True:    
        if data:
            print(data)
            tA_id=input("TeamA_id:").upper()
            if (tA_id,) not in data:
                print("TeamA_ID doesn't exist")
                continue
            else:
                pass
            tB_id=input("TeamB_id:").upper()
            if (tB_id,) not in data:
                print("TeamB_ID doesn't exist")
                continue
            else:
                break
    while True:
        TeamA_Score=int(input("TeamA_SCORE: "))
        if TeamA_Score<=600:
            break
    while True:
        TeamB_Score=int(input("TeamB_SCORE: "))
        if TeamB_Score<=600:
            break
    while True:
        TeamA_Wickets=int(input("TeamA_WICKETS: "))
        if 0<=TeamA_Wickets<=10:
            break
    while True:
        TeamB_Wickets=int(input("TeamB_WICKETS: "))
        if 0<=TeamB_Wickets<=10:
            break
    while True:
        TeamA_Extras=int(input("TeamA_EXTRAS: "))
        if 0<=TeamA_Extras<=100:
            break
    while True:
        TeamB_Extras=int(input("TeamB_EXTRAS: "))
        if 0<=TeamB_Extras<=100:
            break
    if TeamA_Score>TeamB_Score:
        loser=tB_id
        winner=tA_id
        cur.execute(f"update points_table set wins=wins+1, points=points+2 where tid='{tA_id}'")
        cur.execute(f"update points_table set loses=loses+1 where tid='{tB_id}'")
    elif TeamA_Score<TeamB_Score:
        loser=tA_id
        winner=tB_id
        cur.execute(f"update points_table set wins=wins+1, points=points+2 where tid='{tB_id}'")
        cur.execute(f"update points_table set loses=loses+1 where tid='{tA_id}'")
    else:
        loser=winner="Tie"
    cur.execute(f"select pid from players where tid='{tA_id}' or tid='{tB_id}' ")
    data=cur.fetchall()
    while True:
        if data:
            print(data)
            mvp=input("MVP_PID: ").upper()
            if (mvp,) not in data:
                continue
            else:
                break
    while True:
        date_string = input("Enter a date (format: DD-MM-YYYY): ")
        try:
            parsed_date = parser.parse(date_string, dayfirst=True).date()
            today = date.today()
            if parsed_date > today:
                print("The entered date is a future date.")
                continue
            else:
                break
        except ValueError:
            print("Incorrect data format")
    time=input("Time: ")  
    while True:  
        venue=input("Venue: ").title()
        if len(venue)<=30:
            break
    TeamA_Overs=int(input("TeamA_Overs: "))
    TeamB_Overs=int(input("TeamB_Overs: "))
    print()
    cur.execute("insert into matches values('{}','{}','{}',{},{},{},{},{},{},'{}','{}','{}','{}','{}','{}',{},{})".format(m_id,tA_id,tB_id,TeamA_Score,TeamB_Score,TeamA_Wickets,TeamB_Wickets,TeamA_Extras,TeamB_Extras,loser,winner,mvp,parsed_date,time,venue,TeamA_Overs,TeamB_Overs))
    cur.execute(f"update players set no_of_mvp = no_of_mvp+1 where PID='{mvp}'")
    cur.execute(f"update points_table set no_of_matches=no_of_matches+1 where tid='{tA_id}'")
    cur.execute(f"update points_table set no_of_matches=no_of_matches+1 where tid='{tB_id}'")
    xa=TeamA_Score/TeamA_Overs
    xb=TeamB_Score/TeamB_Overs
    if winner==tA_id:
        nrr=xa-xb
        nrr=round(nrr,3)
        cur.execute(f"update points_table set nrr=nrr+{nrr} where tid='{tA_id}'")
        cur.execute(f"update points_table set nrr=nrr-{nrr} where tid='{tB_id}'")
    elif winner==tB_id:
        nrr=xb-xa
        nrr=round(nrr,3)
        cur.execute(f"update points_table set nrr=nrr+{nrr} where tid='{tB_id}'")
        cur.execute(f"update points_table set nrr=nrr-{nrr} where tid='{tA_id}'")
    con.commit()
def add_player():
    while True:
        pname=input("Player Name: ").upper()
        if len(pname)>30:
            print("Maximum length of player name is 30 characters only ")
            continue
        else:
            break
    while True:
        pos=input("Position(batter/wicket-keeper/bowler/all-rounder): ").upper()
        if pos.lower() in ['batter','wicket-keeper','bowler','all-rounder']:
            break
        else:
            continue
    while True:
        cur.execute("select tid from teams")
        data=cur.fetchall()
        if data:
            print(data)
            tid=input("TeamID: ").upper()
            if (tid,) not in data:
                print("TeamID is not in the table")
                continue
            else:
                break
    print()
    cur.execute(f"insert into players (PID, PName, Position, TID) values('{auto_increment()}','{pname}','{pos}','{tid}')")
    con.commit()
def add_team():
    tid=input("TeamID: ").upper()
    while True:
        tname=input("Team Name: ").upper()
        if len(tname)>30:
            print("Maximum length of team name is 30 characters only ")
            continue
        else:
            break

    print()
    cur.execute("insert into teams values('{}','{}')".format(tid,tname))
    con.commit()
    cur.execute(f"insert into points_table(tid) values('{tid}')")
    con.commit()
def insert():
    while True:
        choice=int(input("1.Add Team \n2.Add Player\n3.Add Matches\n4.Add TeamA_Details\n5.Add TeamB_Details\n0.Previous\n(1/2/3/4/5/0): "))
        print()
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
    cur.execute("select pname,t.tid,Sixes from players p, teams t where p.tid=t.tid")
    data=cur.fetchall()
    data_1=sorted(data,key=lambda t:t[2], reverse=True)[:5]
    print("Player Name\t\tTeam\t\tSixes")
    for row in data_1:
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
        choice=int(input("1.Runs\n2.Wickets\n3.Highest Score\n4.Most Hundreds\n5.Most Fifties\n6.Five Wicket Hauls\n7.Sixes\n8.Fours\n0.Back\n(1/2/3/4/5/6/7/8/0): "))
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
    if data:
        print("TID\tMID\tPID\tRuns Made\tBalls Played\tNo. of Fours\tNo. of Sixes\tStrike Rate\tOvers Bowled\tMaidens\tRuns Conceded\tWickets Taken\tEconomy")
        for row in data:
            for col in row:
                print(col,end="\t")
            print()
    else:
        print("No Records found")
def display_TeamA_Details():
    cur.execute("select teams.TID,mid,pname,Runs_Made,Balls_Played,t.Fours,t.Sixes,Strike_Rate,Overs_Bowled,Maiden,Runs_Conceded,Wickets_Taken,Economy from TeamA_details t,players p, teams where t.pid=p.pid and t.tid=teams.tid")
    data=cur.fetchall()
    if data:
        print("TID\tMID\tPID\tRuns Made\tBalls Played\tNo. of Fours\tNo. of Sixes\tStrike Rate\tOvers Bowled\tMaidens\tRuns Conceded\tWickets Taken\tEconomy")
        for row in data:
            for col in row:
                print(col,end="\t")
            print()
    else:
        print("No Records found")
def display_matches():
    cur.execute("select * from Matches")
    data=cur.fetchall()
    if data:
        print("MID\tTEAM_A TID\tTEAM_B TID\tTEAM_A score\tTEAM_B score\tTEAM_A WICKETS\tTEAM_B WICKETS\tTEAM_A EXTRAS\tTEAM_B EXTRAS\tLOSER\tWINNER\tMAN OF THE MATCH\tDATE\tTIME\tVENUE")
        for row in data:
            for col in row:
                print(col,end="\t")
            print()
    else:
        print("No matches found")
def display_all_players():
    cur.execute("select * from Players")
    data=cur.fetchall()
    if data:
        print("PID\t\tPName\t\tPosition\tRuns\t\tWickets\t\tHundredst\t\tFifties\t\tFours\t\tSixes\t\tHighest Score\t\tFive Wicket Haul\t\tNo_of_MVP\t\tTID")
        for row in data:
            for col in row:
                print(col,end="\t\t")
            print()
    else:
        print("Players not found")
def display_players_of_a_team():
    tid=input("TeamID: ").upper()
    cur.execute(f"select * from Players where tid='{tid}'")
    data=cur.fetchall()
    if data:
        print("PID\t\tPName\t\tPosition\tNo_of_MVP\tRuns\t\tWickets\t\tTID")
        for row in data:
            for col in row:
                print(col,end="\t\t")
            print()
    else:
        print("Team not Found")
def display_teams():
    cur.execute("select * from Teams")
    data=cur.fetchall()
    print("TeamID\tTeamName")
    for row in data:
        for col in row:
            print(col,end="\t")
        print()
def display_menu():
    while True:
        #Prompt the user to enter their choice
        choice=int(input("1.Display Teams\n2.Display Players of a team\n3.Display All Players\n4.Display All Matches\n5.Display TeamA_Details\n6.Display TeamB_Details\n7.Display Stats\n0.Previous\n(1/2/3/4/5/6/7/0): "))
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
        choice=int(input("1.Display Records\n2.Insert Records\n3.Search Records\n4.Update Records\n5.Delete Record\n0.Exit\n(1/2/3/4/5/0): "))
        print()
        if choice==1:
            display_menu()
        elif choice==2:
            insert()
        elif choice==3:
            search()
        elif choice==4:
            update()
        elif choice==5:
            delete()
        elif choice==0:
            print("Bye!!")
            break
menu()
