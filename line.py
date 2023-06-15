import matplotlib.pyplot as plt
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


