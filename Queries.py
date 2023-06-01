import mysql.connector as mycon
try:
    #username=input("UserName: ")
    #password=input("Password: ")
    #con=mycon.connect(host="localhost",user=f"{username}",passwd=f"{password}")
    con=mycon.connect(host="localhost",user=f"Maddy",passwd=f"1234")
    cur=con.cursor()
except:
    print("Username or Password Doesn't Match")
    exit()
cur.execute("use WC2023")
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
    mid=input("MatchID: ")
    Team_A=input("Team A: ")
    Team_B=input("Team B: ")
    date=input("Date: ")
    time = input("Time: ")
    venue=input("Venue: ")
    toss_winner=input("Toss Winner: ")
    winner=input("Winner: ")
    mvp=input("Man of the Match: ")
    cur.execute(f"INSERT INTO Matches VALUE ('{mid}', '{Team_A}', '{Team_B}', '{date}', '{time}', '{venue}', '{toss_winner}', '{winner}', '{mvp}')")
def add_player():
    pid=input("PlayerID: ")
    pname=input("Player Name: ")
    pos=input("Position: ")
    mvp=int(input("Man of the Match: "))
    runs=int(input("Runs: "))
    wickets=int(input("Wickets: "))
    tid=input("TeamID: ")
    cur.execute("INSERT INTO Players VALUE ('{}','{}','{}',{},{},{},'{}')".format(pid,pname,pos,mvp,runs,wickets,tid))
    con.commit()
def add_team():
    tid=input("TeamID: ")
    tname=input("Team Name: ")
    cur.execute("INSERT INTO Teams VALUE ('{}','{}')".format(tid,tname))
    con.commit()
def insert():
    while True:
        choice=int(input("1.Add Team \n2.Add Player\n3.Add Matches\n4.Add Stats\n5.Add Team Points\n0.Previous\n(1/2/3/4/5/0): "))
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
    ...
def display_teams():
    cur.execute("select * from Teams")
    data=cur.fetchall()
    print("TeamID\tTeamName")
    teams = [team for team in data]
    return teams
def display():
    while True:
        choice=int(input("1.Display Teams \n2.Display Players of a team \n3.Display All Players \n4.Display All Matches \n0.Previous\n(1/2/3/4/0): "))
        if choice==1:
            display_teams()
        if choice==1:
            display_players_of_a_team()
        if choice==1:
            display_all_players()
        if choice==1:
            display_matches()
        if choice==1:
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
