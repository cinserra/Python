import numpy as np
import matplotlib as plt
from pylab import *
from scipy import stats
import random
#graphic part, can be commented out
rc('text', usetex=True)
rc('font',family='Times New Roman')
rc('xtick', labelsize=13)
rc('ytick', labelsize=13)

#commands oto make prettier figures
fig = plt.figure(figsize=(8,8)) #gives the size of the plot
ax=fig.add_subplot(111) #create subplot, 111 configuration means there is only 1 plot

#let's produce some number with two different syntaxes
X = np.linspace(0,20,50) #50 numbers between 0 and 20
Y = np.arange(0,100,2) #numbers from 0 to 100 every 2

#alternatively some random numbers
#comment it if you want those above
X = random.sample(range(1, 100), 20)
Y = random.sample(range(1, 100), 20)

fit = np.polyfit(X, Y, 1) # one way to do a linear regression
pf = np.poly1d(fit)
px = pf(X)

#alternative way
slope, intercept, r_value, p_value, std_err = stats.linregress(X,Y)
#print some info and statitiisitcal results
print ''
print 'Slope: ', slope
print 'Intercept: ', intercept
print 'r-value ', p_value
print 'r-squared ', r_value**2
print 'p-value: ', p_value
print 'Standard deviation: ', std_err
print 'Pearson coefficient: ', stats.pearsonr(X,Y)
print 'Spearman coefficient: ', stats.spearmanr(X,Y)
print ''

lfit = slope * np.array(X) + intercept

#some plotting
#note that the solid blue line (pyplot) and dashed ornage line(linregress) should be identycal
plt.plot(X,Y,marker='s',color='k',ls='None',ms=7)
plt.plot(X,px,ls='-',lw=2)
plt.plot(X, lfit,ls='--',lw=1)
plt.title('Example',fontsize=22)
legend(['Random data','Polyfit regression', 'Linregress regression'],ncol=1,loc=1)
ylabel('Y',fontsize=20)
xlabel('X',fontsize=20)
ax.minorticks_on() #adds minor thick on th eplot

# you can play with the border and with multiple figures even without the graphic api
#fig.subplots_adjust(hspace=0.07,wspace=0.07,left=0.12,right=0.88,top=0.92,bottom=0.09)

plt.show()

# can save the figure in the format you want and other little perks

#fig.savefig('test.pdf',bbox_inches='tight',format='pdf',dpi=1000)
