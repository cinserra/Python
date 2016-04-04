#! /usr/bin/python

# Created by Cosimo Inserra
# GitHub: https://github.com/cinserra
# @COSMO_83
#
# Linear dataset/regresssion + random noise + goodness of the fit
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

x = np.arange(100)
y = (-2.99*x)+0.792
ny = (0.1*y)+y
ty = y-(.1*y)
a = ny+ty
print a, y
slope, intercept, r_value, p_value, std_err = stats.linregress(x,a)
print "r-squared:", r_value**2
print std_err
plt.plot(x,y,'ro',x,ny,'b.',x,ty,'g.')

plt.show()
