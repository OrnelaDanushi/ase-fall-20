#make a class which exploits the modules calculator
import calculator as c

class FooCalculator:
  #empty constructor
  def __init__(self): #self is a formal argument, the self passes itself
    pass

  def sum(self,m,n):
    return c.sum(m,n)

  def divide(self,m,n):
    return c.divide(m,n)