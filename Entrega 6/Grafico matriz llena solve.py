# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 23:09:30 2021

@author: sandra
"""


import matplotlib.pylab as plt 


Ns=[]
Dts=[] #se guardan lista de listas de tiempo de ensamblado
Mems=[]#se guardan lista de listas de tiempo de solución
var=0

Nss=[]
Dtss=[]
Memss=[]

for i in range(1):
    fid=open("CasoMatriz llena solve.txt","r") 
    for line in fid:
        var+=1
        print(line)
        sl=line.split()
        N=int(sl[0])
        dt=float(sl[1])
        Mem=float(sl[2])
        
        
        Nss.append(N)
        Dtss.append(dt)
        
        Memss.append(Mem)
        
  
        if var==10:
            Ns.append(Nss)
            Nss=[]
            Dts.append(Dtss)
            Dtss=[]
            Mems.append(Memss)
            Memss=[]
            
            var=0
            
    fid.close()
    
import matplotlib.pylab as plt 



x_v=[10,100,1000,2000,2000,4000,5000,6000,7000,8000]

x1_l = ["10","100","1000","2000","2000","4000","5000","6000","7000","8000"]
x1_v = [10,100,1000,2000,2000,4000,5000,6000,7000,8000]

y1_l=["0,1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10 min"]
y1_v=[0.0001,0.001,0.01,0.1,1,10,60,600]




plt.figure(1)

plt.subplot(2,1,1)
plt.title("Rendimiento A@B")
plt.loglog(x_v,Dts[0],marker="o")
plt.loglog(x_v,Dts[1],marker="o")
plt.loglog(x_v,Dts[2],marker="o")
plt.loglog(x_v,Dts[3],marker="o")
plt.loglog(x_v,Dts[4],marker="o")
plt.loglog(x_v,Dts[5],marker="o")
plt.loglog(x_v,Dts[6],marker="o")
plt.loglog(x_v,Dts[7],marker="o")
plt.loglog(x_v,Dts[8],marker="o")
plt.loglog(x_v,Dts[9],marker="o")




plt.xticks(x1_v,x1_l)
plt.yticks(y1_v,y1_l)
plt.grid(True)
plt.xticks(visible=True)
plt.ylabel("Tiempo de ensamblado")


plt.subplot(2,1,2)





plt.ylabel("Tiempo de solución")
plt.xlabel("Tamaño matriz N")
plt.loglog(x_v,Mems[0],marker="o")
plt.loglog(x_v,Mems[1],marker="o")
plt.loglog(x_v,Mems[2],marker="o")
plt.loglog(x_v,Mems[3],marker="o")
plt.loglog(x_v,Mems[4],marker="o")
plt.loglog(x_v,Mems[5],marker="o")
plt.loglog(x_v,Mems[6],marker="o")
plt.loglog(x_v,Mems[7],marker="o")
plt.loglog(x_v,Mems[8],marker="o")
plt.loglog(x_v,Mems[9],marker="o")
#plt.loglog(Ns,Mems,marker="o")
plt.yticks(y1_v,y1_l)
plt.xticks(x1_v,x1_l,rotation=45)
#plt.grid(True)
#plt.xticks(visible=True)



plt.show()


