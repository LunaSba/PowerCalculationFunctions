import matplotlib.pyplot as plt  
import time
from decimal import *
import numpy as np
import tkinter

def power(a,b):
    start_time = time.time()
    lx = []
    ly = []
    x = 1
    for i in range(b):
     x = x * a
     lx.append(time.time()-start_time)
     print(time.time())
     ly.append(Decimal(x))
    print(ly)
    tout = [lx,ly]
    
    return tout


 
def graphe(f,w,c,title):
    # global start_time
    '''trace le graphe de la fonction f'''
    j = f(base,puiss)
    plt.subplot(w)
    # print(j)
    plt.plot(j[0],j[1],c,linewidth=0.8, marker="*",label=title)
      

def sm(x, y):
    result = 1 
    lx = []
    ly = []
    ly.append(Decimal(0)) #pour commencer le camcul
    lx.append(0)
    start_time  = time.time()
    # print('------------------------------')
    while y>0:
        if y%2!=0:
            result *= x
            ly.append(Decimal(result))
            lx.append(time.time()-start_time)
        x *= x  
        y //= 2
        print(time.time())
    tout = []
    tout = [lx,ly]
    print(ly)
    return tout

chiffre = False
while(chiffre == False):
 try:
  print("Donner la valeur de la base")
  base = float(input())
  break
 except:
  print("WARNING !","Vous devez saisir un nombre reel ou entier")

while(chiffre == False):
 try:
  print("Donner la valeur de la puissance")
  puiss = int(input())
  break
 except:
   print("WARNING !","Vous devez saisir un nombre entier")
  
graphe(power,211, "r","Execution de power \n les x pour le temps d'execution")
plt.legend()
graphe(sm,212 ,"b","Execution de SM \n les x pour le temps d'execution")
plt.legend()
plt.show()