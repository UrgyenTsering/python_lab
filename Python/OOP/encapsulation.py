
class BankAccount:
  def __init__(self, owner, balance=0):
    self.owner = owner
    # self.balance = balance
    self.__balance = balance #this __ will make balance private or not accessible outside of class
  
  def __repr__(self):
    return f"{self.owner} has balance of rs {self.__balance}"

  def deposit(self, amount):
    if(amount>0):
      self.__balance =self.__balance+amount
      
      
a1=BankAccount("Rabindra")
print(a1)

# Balance should not be accessible.
a1.balance=1000
print(a1) 

# to access and add balance into account, we had defind function inside class
a1.deposit(500)

#name mangling: we can access the private data, if anyhow 
