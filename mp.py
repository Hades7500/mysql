import matplotlib.pyplot as plt
label=['IND','NZ','SA','ENG','AUS','WI','SL','BAN','AFG','PAK']
per=[10,1200,50,16,13,25,19,21,19,19]
bar = plt.bar(label, per)
bar[1].set_color("Yellow")
plt.xlabel('Teams',fontsize=20)
plt.ylabel('Runs',fontsize=20)
plt.title('Total Runs scored by each team')
plt.show()