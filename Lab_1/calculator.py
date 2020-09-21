#!/usr/bin/python
#otherwise compile with $ python calculator.py instead of ./calculator.py

#the module must work on integers in Z (both positive and negative numbers)

def sum(m, n):  
  #perform n increments (+1) to the value of m and return the result

  """
  if n>0:
    for _ in range(n): #for i in range(n):
      m += 1
  else: 
    for _ in range(abs(n)):
      m -= 1
  """
  """
  while n!=0 :  
    if n>0:     
      m += 1 
      n -= 1
    else:
      m -= 1
      n += 1
  """
  sign = 1 if n>0 else -1
  n = abs(n)
  while n!=0 :
    m += sign
    n -= 1
  return m
#print(str(sum(3,5)))

def divide(m, n):
  #substract n from m until it gets to 0 and return the result

  result=0 
  negativeResult= m>0 and n<0 or m<0 and n>0
  n=abs(n)
  m=abs(m)  
  if n==0:
    raise ZeroDivisionError('n should be not 0')
  else:
    while( m-n>=0 ):
      m-=n       #m=sum(m,-n) 
      result+=1
    result= -result if negativeResult else result
  return result
#print(str(divide(10,5)))

def subtract(m,n):
  #perform n decrements (-1) to the value of m and return the result  

  sign = 1 if n>0 else -1
  n = abs(n)
  while n!=0 :
    m -= sign
    n -= 1
  return m

def multiply(m,n):
  #sum the value of m for n times and return the result

  negativeResult= m>0 and n<0 or m<0 and n>0
  n=abs(n)
  m=abs(m)  
  if n==0:
    return 0
  else: 
    i=0 #start to sum from 0
    while n>0:
      i += m
      n -= 1
    i = -i if negativeResult else i
    return i

def gcd(m,n):
  #implement Euclid's Algorithm

  result=0
  while n!=0: 
    result=m%n
    m=n
    n=result
  return m