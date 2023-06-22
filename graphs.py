import matplotlib.pyplot as plt

def bargraph():
    label=['IND','NZ','SA','ENG','AUS','WI','SL','BAN','AFG','PAK']
    per=[2516,2169,1906,3198,2701,1969,1621,2278,1831,2025]
    bar=plt.bar(label,per,width = 0.4)
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

def line_graph():

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