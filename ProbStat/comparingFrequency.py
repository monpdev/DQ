rookies = wnba[wnba['Exp_ordinal'] == 'Rookie']
little_xp = wnba[wnba['Exp_ordinal'] == 'Little experience']
experienced = wnba[wnba['Exp_ordinal'] == 'Experienced']
very_xp = wnba[wnba['Exp_ordinal'] == 'Very experienced']
veterans =  wnba[wnba['Exp_ordinal'] == 'Veteran']


import seaborn as sns
sns.countplot(x = 'Exp_ordinal', hue = 'Pos', data = wnba,
              order = ['Rookie', 'Little experience', 'Experienced', 'Very experienced', 'Veteran'],
              hue_order = ['C','F','F/C','G','G/F']
             )
                   



sns.countplot(x = 'age_mean_relative', hue = 'min_mean_relative',data = wnba)
result = 'rejection'

import matplotlib.pyplot as plt
wnba[wnba.Age >= 27]['MIN'].plot.hist(histtype = 'step', label = 'Old', legend = True)
wnba[wnba.Age < 27]['MIN'].plot.hist(histtype = 'step',label = 'Young', legend = True)
plt.axvline(497,label = 'Average')
plt.legend()
plt.show

wnba[wnba.Age >= 27]['MIN'].plot.kde(label = 'Old', legend = True)
wnba[wnba.Age < 27]['MIN'].plot.kde(label = 'Young',legend = True)
plt.axvline(497, label = 'Average')
plt.legend()
plt.show()

#Strip plots
sns.stripplot(x = 'Pos', y = 'Weight', data = wnba, jitter = True)
plt.show()


#Box plots
sns.boxplot(x = 'Pos', y = 'Weight', data = wnba)
plt.show()


# Outliers
iqr = 29-22
lower_bound = 22 - (1.5 *iqr)
upper_bound = 29+(1.5*iqr)
outliers_low = sum(wnba['Games Played'] < lower_bound)
outliers_high = sum(wnba['Games Played'] > upper_bound)
sns.boxplot(wnba['Games Played'])
plt.show()