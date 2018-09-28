# STAT/CS 287
# HW 01
#
# Name: Michael Arnold
# Date: 09-12-18

import numpy as np
import matplotlib.pyplot as plt
from problem2_mvarnold import coin_flip

def dependent_coin_flip(p, q1, q2):
    """ returns a tuple representing the flip outcomes of two coins with the
    probablities of the second depend on the first"""

    X = coin_flip(p)
    if X == "H":
        Y = coin_flip(q1)
    else:
        Y = coin_flip(q2)
    return (X,Y)

def coin_test_dependent(p,q1,q2,N=1000):
    """flip coins 1000 times and run statistics"""
    coin_histories = []
    for i in range(N):
        coin_histories.append(dependent_coin_flip(p,q1,q2))

    # count number of times unique event occur
    event_count = {"HH":0,"HT":0,"TH":0,"TT":0}
    for X,Y in coin_histories:
        if X=="H":
            if Y =="H":
                event_count["HH"]+=1
            else:
                event_count["HT"]+=1
        else:
            if Y =="H":
                event_count["TH"]+=1
            else:
                event_count["TT"]+=1

    return coin_histories, event_count




def compute_joint_prob(event_count,i,count):
    """prints a table of the joint probability given the count of unique events"""
    print("-"*31)
    print("for p = {} q1 = {} q2 = {}".format(i[0],i[1],i[2]))
    print("-"*31)
    if count:
        print("event     count")
        print("-"*31)
        for key,value in event_count.items():
            print(key.ljust(10) + str(value).ljust(6))
    else:    
        print("event     joint prob")
        print("-"*31)
        for key,value in event_count.items():
            print(("P("+key[0]+","+key[1]+')').ljust(10) + str(value/1000).ljust(6))
    print()




def dependence_test(event_count,tol=0.05):
    """ marginalizes to find probablities of each coin,
    and looks to see if equal to joint probability"""
    for event,count in event_count.items():
        event_count[event] = count/1000
    P_H1 = event_count["HH"]+event_count["HT"]
    P_T1 = event_count["TH"]+event_count["TT"]
    P_H2 = event_count["HH"]+event_count["TH"]
    P_T2 = event_count["TT"]+event_count["HT"]
    
    if in_range(event_count['HH'],P_H1*P_H2,tol) and \
    in_range(event_count['HT'],P_H1*P_T2,tol) and \
    in_range(event_count['TH'],P_T1*P_H2,tol) and \
    in_range(event_count['TT'],P_T1*P_T2,tol):
        print("independent")
    else:
        print('dependent')

def in_range(x,y,tol):
    """tests if two values are within tol of each other"""
    if abs(x-y) < tol:
        return True
    





def plotting_dependence_test(N,c,p,q1,q2):
    """ flips N coins and analyses the history"""

    coin_histories = []
    event_count = {"HH":0,"HT":0,"TH":0,"TT":0}
    HH = np.array([])
    HT = np.array([])
    TH = np.array([])
    TT = np.array([])
    for i in range(1,N):
        X,Y = dependent_coin_flip(p,q1,q2)

    # count number of times unique event occur
        if X=="H":
            if Y =="H":
                event_count["HH"]+=1
            else:
                event_count["HT"]+=1
        else:
            if Y =="H":
                event_count["TH"]+=1
            else:
                event_count["TT"]+=1
        HH=np.append(HH,event_count["HH"]/i)
        TT=np.append(TT,event_count["TT"]/i)
        TH=np.append(TH,event_count["TH"]/i)
        HT=np.append(HT,event_count["HT"]/i)
    plt.title('p = {} q1 = {} q2 = {}'.format(p,q1,q2))
    colors = ['k','b']
    #plt.semilogx(HH,'r.',label="P(H,H)")
    plt.loglog(np.abs((HH+HT)*(TH+HH)-HH),'+',color = colors[c],ms=3,label="P(H)*P(H)")
    #plt.semilogx(HT,'g.', label="P(H,T)") 
    #plt.semilogx(np.abs((HH+HT)*(TT+HT)-HT),'g+',ms=3,label = "P(H)*P(T)")
    #plt.semilogx(TH,'b.',label="P(T,H)")
    #plt.semilogx(np.abs((TH+TT)*(TH+HH)-TH),'b+',ms=3,label = "P(T)*P(H)")
    #plt.semilogx(TT,'k.',label= 'P(T,T)')
    #plt.semilogx(np.abs((TH+TT)*(TT+HT)-TT),'k+',ms=3,label ="P(T)*P(T)" )
    plt.xlabel("coin flips")
    plt.ylabel("Probabilities")
    plt.legend(bbox_to_anchor=(1.05, 1.0))






# inputs = [(0.5,0.75,0.25),(0.2,0.75,0.25)] # first inputs
inputs = [(0.2,0.4,0.4),(0.2,0.75,0.25)]
index = -1
for i in inputs:
    index += 1
    history, count = coin_test_dependent(*i)
    #compute_joint_prob(count,i,False)
    dependence_test(count)
    for j in range(100):
        plotting_dependence_test(1000, index, *i)
plt.show()
