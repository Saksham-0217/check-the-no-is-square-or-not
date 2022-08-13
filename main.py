a = int(input("enter the no you want to check\n"))

def rsq():
  

  def s():
    global a
    i = 1
    if(a>0):
      while(a>0):
        a = a - i 
        i = i + 2
    if (a==0):
      print ("your number is a perfect square")
    else:
      print("your no is not a no square")  
  s()


tell = int(input("press 1 if you want to check the no is square or not"))
if (tell== 1):
  rsq()





