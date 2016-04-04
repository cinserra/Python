#! /usr/bin/python

# Created by Cosimo Inserra
# GitHub: https://github.com/cinserra
# @COSMO_83
#
# Fibonacci function. Note that python function of this level ar usually slower than a simple loop
print "Fibonacci python script"
n = int(raw_input("Please introduce n  "))

def fib(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
#print n, fib(n)
    else:
        return fib(n-2) + fib(n-1)

print n,"^th elements of the series is", fib(n)
