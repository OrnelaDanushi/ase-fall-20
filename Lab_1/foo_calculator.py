#!/usr/bin/python

#make a class which exploits the modules calculator
import calculator as c

class foo_calculator:
  #empty constructor
  def __init__(self): #self is a formal argument, the self passes itself
    pass

  def sum(self,m,n):
    return c.sum(m,n)

  def divide(self,m,n):
    return c.divide(m,n)

  def subtract(self,m,n):
    return c.subtract(m,n)

  def multiply(self,m,n):
    return c.multiply(m,n)

  def gcd(self,m,n):
    return c.gcd(m,n)

fc = foo_calculator()
print(fc.sum(10, 10))
print(fc.sum(10, -10))
print(fc.divide(-10,5))
print(fc.divide(10,-5))
print(fc.divide(10,5))
print(fc.subtract(10,5))
print(fc.multiply(10,5))
print(fc.gcd(10,5))