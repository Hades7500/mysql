import matplotlib.pyplot as plt
def line():
    plt.figure(facecolor='aqua')
    y1=(1,2,3,4,5,6,7,8,9)
    x1=[230,352,0,336,224,268,306,314,265]
    x2=[105,348,0,266,212,308,241,230,315]
    x3=[137,248,173,0,245,291,237,243,186]
    x4=[207,309,227,29,131,241,259,206,325]
    x5=[311,334,386,213,397,212,221,337,305]
    x6=[209,288,352,307,334,381,285,243,315]
    x7=[108,273,0,212,321,286,143,315,311]
    x8=[330,244,280,0,322,333,262,286,221]
    x9=[136,201,0,0,247,232,203,338,264]
    x10=[207,152,172,125,247,213,262,227,288]
    ax=plt.axes()
    ax.set_facecolor('white')
    font1 = {'family':'fantasy','color':'blue','size':19}
    font2 = {'family':'monospace','color':'darkred','size':13}
    plt.title("Runs Scored",fontdict=font1)
    plt.xlabel("Matches",fontdict = font2)
    plt.ylabel("Runs",fontdict = font2)
    team_data = [(x1, "India", "royalblue"), (x1, "India", "royalblue"),
                 (x1, "India", "royalblue"), (x1, "India", "royalblue"),
                 (x1, "India", "royalblue"), (x1, "India", "royalblue"),
                 (x1, "India", "royalblue"), (x1, "India", "royalblue")]
    plt.plot(y1,x1, '-',linewidth = '1.8',label='India',color='royalblue')
    plt.plot(y1,x2, '-',linewidth = '1.8',label='Pakistan',color='darkgreen')
    plt.plot(y1,x3, '-',linewidth = '1.8',label='New Zealand',color='black')
    plt.plot(y1,x4, '-',linewidth = '1.8',label='South Africa',color='springgreen')
    plt.plot(y1,x5, '-',linewidth = '1.8',label='England',color='Aqua')
    plt.plot(y1,x6, '-',linewidth = '1.8',label='Australia',color='gold')
    plt.plot(y1,x7, '-',linewidth = '1.8',label='West Indies',color='maroon')
    plt.plot(y1,x8, '-',linewidth = '1.8',label='Bangladesh',color='green')
    plt.plot(y1,x9, '-',linewidth = '1.8',label='Srilanka',color='blue')
    plt.plot(y1,x10, '-',linewidth = '1.8',label='Afghanistan')
    plt.legend()
    plt.grid(color='lime',linewidth = '0.27')
    plt.show()

def bar_graph():
    team_name=['IND','NZ','SA','ENG','AUS','WI','SL','BAN','AFG','PAK']
    per=[2516,2169,1906,3198,2701,1969,1621,2278,1831,2025]
    bar=plt.bar(team_name,per,width = 0.4)
    team_colors = ["royalblue", "black", "lime", "lightblue", "yellow" ,"blue", "darkgreen", "green"]
    bar[0].set_color("royalblue")
    bar[1].set_color("black")
    bar[2].set_color("lime")
    bar[3].set_color("lightblue")
    bar[4].set_color("Yellow")
    bar[5].set_color("maroon")
    bar[6].set_color("blue")
    bar[9].set_color("darkgreen")
    bar[7].set_color("green")
    plt.xlabel('Teams',fontsize=20)
    plt.ylabel('Runs',fontsize=20)
    plt.title('Total Runs scored by each team')
    plt.show()

def pie():
    labels='R Sharma','V kohli','Kl rahul','H pandya','Ms dhoni','S dhawan','R pant','R jadeja','K jadhav','V shankar'
    plt.figure(facecolor='aqua')
    votes=[648,443,361,226,273,125,116,77,80,58]
    sizes=votes
    colors=['red','yellow','green','blue','magenta','lightblue','gold','orange','Aquamarine','lime']
    explode=(0.1,0,0,0,0,0,0,0,0,0)
    plt.pie(sizes,explode=explode,colors=colors,shadow=True,startangle=140,autopct='%.0f%%')
    plt.legend(labels)
    plt.show()

def pie2():
    labels='D Warner','A Finch','S Smith','A Carey','U khawaja','G Maxwell','Nc Nile','M stoinis','M stac','P cummins'
    plt.figure(facecolor='aqua')
    votes=[647,507,379,375,316,177,98,77,68,51]
    sizes=votes
    colors=['red','yellow','green','blue','magenta','lightblue','gold','orange','Aquamarine','lime']
    explode=(0.1,0,0,0,0,0,0,0,0,0)
    plt.pie(sizes,explode=explode,colors=colors,shadow=True,startangle=140,autopct='%.0f%%')
    plt.legend(labels)
    plt.show()

def pie3():
    labels='JE Root','J Bairstow','B stokes','J Roy','E Morgan','J Butler','M ali','L Plunkett','A rashid','J vince'
    plt.figure(facecolor='aqua')
    votes=[556,532,465,443,371,312,134,62,45,40]
    sizes=votes
    colors=['red','yellow','green','blue','magenta','lightblue','gold','orange','Aquamarine','lime']
    explode=(0.1,0,0,0,0,0,0,0,0,0)
    plt.pie(sizes,explode=explode,colors=colors,shadow=True,startangle=140,autopct='%.0f%%')
    plt.legend(labels)
    plt.show()

def pie4():
    labels='KS Williamson','LRPL Taylor','JDS Neesham','C de Grandhomme ','M Guptil','T latham','C munro','H nicholls','M santner'
    plt.figure(facecolor='aqua')
    votes=[578,350,232,190,186,155,125,91,72]
    sizes=votes
    colors=['red','yellow','green','blue','magenta','lightblue','gold','orange','Aquamarine','lime']
    explode=(0.1,0,0,0,0,0,0,0,0)
    plt.pie(sizes,explode=explode,colors=colors,shadow=True,startangle=140,autopct='%.0f%%')
    plt.legend(labels)
    plt.show()

def pie5():
    labels='Babar Azam','Imam-ul-Haq','Mohammad Hafeez','Haris Sohail','Fakhar Zaman','Imad Wasim','Sarfraz Ahmed','Wahab Riaz','Hasan ali','Shadab khan'
    plt.figure(facecolor='aqua')
    votes=[474,305,253,198,186,162,143,88,43,43]
    sizes=votes
    colors=['red','yellow','green','blue','magenta','lightblue','gold','orange','Aquamarine','lime']
    explode=(0.1,0,0,0,0,0,0,0,0,0)
    plt.pie(sizes,explode=explode,colors=colors,shadow=True,startangle=140,autopct='%.0f%%')
    plt.legend(labels)
    plt.show()

def pie6():
    labels='Shakib Al Hasan','Mushfiqur Rahim','Tamim Iqbal','Mahmudullah','Soumya Sarkar','Mosaddek Hossain','Mohammad Saifuddin','Mohammad Mithun','Mehidy Hasan Miraz','Sabbir Rahman'
    plt.figure(facecolor='aqua')
    votes=[606,367,235,219,166,116,87,47,37,36]
    sizes=votes
    colors=['red','yellow','green','blue','magenta','lightblue','gold','orange','Aquamarine','lime']
    explode=(0.1,0,0,0,0,0,0,0,0,0)
    plt.pie(sizes,explode=explode,colors=colors,shadow=True,startangle=140,autopct='%.0f%%')
    plt.legend(labels)
    plt.show()

def pie7():
    labels='N Pooran','S Hope','S Hetmyer','C Gayle','J Holder','C Brathwaite','E Lewis','F Allen','S Ambris'
    plt.figure(facecolor='aqua')
    votes=[367,274,257,242,170,154,131,51,36]
    sizes=votes
    colors=['red','yellow','green','blue','magenta','lightblue','gold','orange','Aquamarine','lime']
    explode=(0.1,0,0,0,0,0,0,0,0)
    plt.pie(sizes,explode=explode,colors=colors,shadow=True,startangle=140,autopct='%.0f%%')
    plt.legend(labels)
    plt.show()


def pie8():
    labels='F du Plessis','Q de Kock','HM amla','A Markram','D Miller','A Phehlukwayo','J Duminy','K Rabada'
    plt.figure(facecolor='aqua')
    votes=[387,305,203,140,136,133,70,58]
    sizes=votes
    colors=['red','yellow','green','blue','magenta','lightblue','gold','orange','Aquamarine','lime']
    explode=(0.1,0,0,0,0,0,0,0)
    plt.pie(sizes,explode=explode,colors=colors,shadow=True,startangle=140,autopct='%.0f%%')
    plt.legend(labels)
    plt.show()

def pie9():
    labels='MDKJ Perera','AD Mathews ','FDM Karunaratne','W Fernando','H THirimanne','B Mendis','D de silva','N perera','I Udana'
    plt.figure(facecolor='aqua')
    votes=[273,244,222,203,143,143,108,61,45]
    sizes=votes
    colors=['red','yellow','green','blue','magenta','lightblue','gold','orange','Aquamarine','lime']
    explode=(0.1,0,0,0,0,0,0,0,0)
    plt.pie(sizes,explode=explode,colors=colors,shadow=True,startangle=140,autopct='%.0f%%')
    plt.legend(labels)
    plt.show()

def pie10():
    labels='Rahmat Shah','Najibullah Zadran','Hashmatullah Shahidi ','Gulbadin Naib','Asghar Afghan','Ikram Alikhil','M Nabi','R Khan','H Zazai','Samiullah Shinwari','Noor Ali'
    plt.figure(facecolor='aqua')
    votes=[254,230,197,194,154,142,107,105,96,74,63]
    sizes=votes
    colors=['red','yellow','green','blue','magenta','lightblue','gold','orange','Aquamarine','lime']
    explode=(0.1,0,0,0,0,0,0,0,0,0,0)
    plt.pie(sizes,explode=explode,colors=colors,shadow=True,startangle=140,autopct='%.0f%%')
    plt.legend(labels)
    plt.show()

print('Main Menu')
print('1.Line Graph')
print('2.Bar Graph')
print('3.Pie Charts')
l=input('Please Select type of analysis')
if l=='1':
    line()
elif l=='2':
    bar_graph()
elif l=='3':
    n = input('1.India/2.Australia/3.England/4.New zealand/5.Pakistan/6.Bangladesh/7.West Indies/8.South Africa/9.Sri lanka/10.Afghanistan')
    if n == 1:
        pie()
    elif n == 2:
        pie2()
    elif n == 3:
        pie3()
    elif n == 4:
        pie4()
    elif n == 5:
        pie5()
    elif n == 6:
        pie6()
    elif n == 7:
        pie7()
    elif n == 8:
        pie8()
    elif n == 9:
        pie9()
    elif n == 10:
        pie10()