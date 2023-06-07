import mysql.connector as mycon
try:
    con=mycon.connect(host="localhost",user="hades79",passwd="1234")
    cur=con.cursor()
    cur.execute("use WC2023")
except:
    print("Username or Password Doesn't Match")
    exit()
def delete():
    ...
def update():
    ...
def search():
    ...
def add_team_points():
    ...
def add_stats():
    ...
def add_matches():
    cur1=con.cursor()
    Team_A=input("TeamA_ID: ")
    Team_B=input("TeamB_ID: ")
    date=input("Date: ")
    time=input("Time: ")
    venue=input("Venue: ")
    toss_winner=input("TossWinner_TID: ")
    winner=input("Winner_TID: ")
    mvp=input("MVP_PID: ")
    loser=input("Loser_TID: ")
    mid=input("MatchID: ")
    cur.execute("insert into matches values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(mid,Team_A,Team_B,date,time,venue,toss_winner,loser,winner,mvp))
    cur1.execute(f"update players set no_of_mvp = no_of_mvp+1 where PID='{mvp}'")
    con.commit()
    cur1.close()
def add_player():
    pid=input("PlayerID: ")
    pname=input("Player Name: ")
    pos=input("Position: ")
    runs=int(input("Runs: "))
    wickets=int(input("Wickets: "))
    tid=input("TeamID: ")
    cur.execute("insert into players (PID, PName, Position, Runs, Wickets, TID) values('{}','{}','{}',{},{},'{}')".format(pid,pname,pos,runs,wickets,tid))
    con.commit()
def add_team():
    tid=input("TeamID: ")
    tname=input("Team Name: ")
    cur.execute("insert into teams values('{}','{}')".format(tid,tname))
    con.commit()
def insert():
    while True:
        choice=int(input("1.Add Team \n2.Add Player\n3.Add Matches\n4.Add Stats\n5.Add Team Points\n0.Previous\n(1/2/3/4/5/0): "))
        print()
        if choice==1:
            add_team()
        elif choice==2:
            add_player()
        elif choice==3:
            add_matches()
        elif choice==4:
            add_stats()
        elif choice==5:
            add_team_points()
        elif choice==0:
            break
def display_matches():
    ...
def display_all_players():
    ...
def display_players_of_a_team():
    cur.execute("select * from Players")
    data=cur.fetchall()
    print("PID\t\tPName\t\tPosition\tNo_of_MVP\tRuns\t\tWickets\t\tTID")
    for row in data:
        for col in row:
            print(col,end="\t\t")
        print()
def display_teams():
    cur.execute("select * from Teams")
    data=cur.fetchall()
    print("TeamID\tTeamName")

    return [team for team in data]
def display():
    while True:
        choice=int(input("1.Display Teams \n2.Display Players of a team \n3.Display All Players \n4.Display All Matches \n0.Previous\n(1/2/3/4/0): "))
        if choice==1:
            display_teams()
        elif choice==2:
            display_players_of_a_team()
        elif choice==3:
            display_all_players()
        elif choice==4:
            display_matches()
        elif choice==0:
            break
def menu():
    while True:
        choice=int(input("1.Display Records\n2.Insert Records\n3.Search Records\n4.Update Records\n5.Delete Record\n0.Exit\n(1/2/3/4/5/0): "))
        print()
        if choice==1:
            display()
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