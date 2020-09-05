wnba['Exp_ordinal'].value_counts().iloc[[3,0,2,1,4]].plot.bar()

wnba['Exp_ordinal'].value_counts().iloc[[3,0,2,1,4]].plot.barh(title = 'Number of players in WNBA by level of experience')


#Pie chart
wnba['Exp_ordinal'].value_counts().plot.pie()



#Customizing a Pie Chart
wnba['Exp_ordinal'].value_counts().plot.pie(figsize = (6,6), autopct = '%.2f%%',
title = 'Percentage of players in WNBA by level of experience')
plt.ylabel('')



#Histograms
wnba['PTS'].plot.hist()


#The Statistics Behind Histograms
wnba['Games Played'].describe()
wnba['Games Played'].plot.hist()

#Binning for Histograms
wnba['Games Played'].plot.hist(range = (1,32), bins = 8, title = 'The distribution of players by games played')
plt.xlabel('Games played')