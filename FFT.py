#! /usr/bin/python

# Created by Cosimo Inserra
# GitHub: https://github.com/cinserra
# @COSMO_83
#
# Script using Fast Fourier Transform
import scipy.fftpack as fftp

fh = open ( 'FFT_question_data2.txt', 'r' )
str1 = fh.read() #to read the array
#fstr1 = float(str1)
x = [float(i) for i in str1.split()] #to float the array
#print x
myfft = fftp.fft(x)
#print myfft
n = myfft.size
newfft = fftp.fftshift(myfft)
freq = fftp.fftfreq(n,d=10)
print freq
