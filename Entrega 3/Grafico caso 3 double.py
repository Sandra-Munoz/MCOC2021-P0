# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 18:58:53 2021

@author: sandra
"""


import matplotlib.pylab as plt 


Ns=[]
Dts=[]
Mems=[]
 
for i in range(10):
    fid=open("caso 3 double rendimiento.txt ","r") 
    for line in fid:
        sl=line.split()
        N=int(sl[0])
        dt=float(sl[1])
        Mem=int(sl[2])
        
        Ns.append(N)
        Dts.append(dt)
        Mems.append(Mem)
    
    fid.close()


#tiempo transcurrido
y1_l=["0,1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10 min"]
y1_v=[0.0001,0.001,0.01,0.1,1,10,60,600]

#Memoria
y2_l=["1 KB","10 KB","100 KB","1 MB","10 MB","100 MB","1 GB","10 GB"]
y2_v=[1000,10000,100000,1000000,10000000,100000000,1000000000,10000000000]

#Eje x
x_l=["10","20","50","100","200","500","1000","2000","5000","10000","20000"]
x_v=[10,20,50,100,200,500,1000,2000,5000,10000,20000]

plt.figure(1)

plt.subplot(2,1,1)

plt.ylabel("Tiempo transcurrido")
plt.title("Rendimiento caso 3 double")
plt.loglog(Ns,Dts,marker="o")
plt.yticks(y1_v,y1_l)
plt.xticks(x_v,x_l,rotation=45)
plt.grid(True)
plt.xticks(visible=False)


plt.subplot(2,1,2)

plt.ylabel("Uso memoria")
plt.xlabel("Tamaño matriz N")
plt.loglog(Ns,Mems,marker="o")
plt.yticks(y2_v,y2_l)
plt.xticks(x_v,x_l,rotation=45)
#plt.grid(True)
#plt.xticks(visible=True)

plt.show()