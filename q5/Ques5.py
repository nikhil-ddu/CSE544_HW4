
# coding: utf-8

# In[61]:


import numpy as np
import matplotlib.pyplot as plt
import pylab

option = "5a" ## give 5a to see the results for 5a or 5b to see 
##the results of 5b

if(option == "5a"):
    x=np.genfromtxt('q5_sigma3.dat',dtype="double",delimiter=",")

    sigma=3
    a=0
    b2=1
    alst=[]
    blst=[]

    for i in range(5):
        mn=np.mean(x[i,:])
        se2=sigma*sigma/x[i,:].shape[0]
        a=((b2*mn)+(se2*a))/(b2 +se2)
        b2=(b2*se2)/(b2+se2)
        alst.append(a)
        blst.append(b2)
    print("Iteration      Mean                Variance")
    for i in range(5):
        print(i+1,"         ",alst[i],"  ",blst[i])

    legend = ['1st Posterior','2nd posterior','3rd posterior','4th posterior','5th posterior']  
    for j in range(5):
        z=4
        X = np.arange(alst[j]-z*np.sqrt(blst[j]), alst[j]+z*np.sqrt(blst[j]), 0.0001)
        P=[]
        for i in X:
            P.append(np.exp(-(i - alst[j])**2 / (2*blst[j]) ) / np.sqrt(2*np.pi*blst[j]))
        plt.figure('Probability Distribution')
        plt.plot(X, P,label=legend[j])
        #x_axis = np.arange(alst[j]-z*np.sqrt(blst[j]),alst[j]+z*np.sqrt(blst[j]), 1)
        x_axis=np.arange(3,6,0.5)
        y_axis = np.arange(0, 3, 0.2)
        plt.xticks(x_axis)
        plt.yticks(y_axis)
        plt.xlabel('theta')
        plt.ylabel('Pr[theta|X]')
    pylab.legend(loc='upper left')   
    plt.show() 
    
    


# #### 

# In[63]:


elif(option == "5b"):
    x=np.genfromtxt('q5_sigma100.dat',dtype="double",delimiter=",")

    sigma=100
    a=0
    b2=1
    alst=[]
    blst=[]

    for i in range(5):
        mn=np.mean(x[i,:])
        se2=sigma*sigma/x[i,:].shape[0]
        a=((b2*mn)+(se2*a))/(b2 +se2)
        b2=(b2*se2)/(b2+se2)
        alst.append(a)
        blst.append(b2)
    print("Iteration      Mean                Variance")
    for i in range(5):
        print(i+1,"         ",alst[i],"  ",blst[i])

    legend = ['1st Posterior','2nd posterior','3rd posterior','4th posterior','5th posterior'] 
    for j in range(5):
        z=4
        X = np.arange(alst[j]-z*np.sqrt(blst[j]), alst[j]+z*np.sqrt(blst[j]), 0.001)
        P=[]
        for i in X:
            P.append(np.exp(-(i - alst[j])**2 / (2*blst[j]) ) / np.sqrt(2*np.pi*blst[j]))
        plt.figure('Probability Distribution')
        plt.plot(X, P,label=legend[j])
        #x_axis = np.arange(alst[j]-z*np.sqrt(blst[j]),alst[j]+z*np.sqrt(blst[j]), 1)
        x_axis=np.arange(-5,5,1)
        y_axis = np.arange(0, 0.5, 0.05)
        plt.xticks(x_axis)
        plt.yticks(y_axis)
        plt.xlabel('theta')
        plt.ylabel('Pr[theta|X]')
    pylab.legend(loc='upper left') 
    plt.show()
    

