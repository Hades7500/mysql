import matplotlib.pyplot as plt
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
