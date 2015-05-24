'''
Created on May 24, 2015

@author: savs95
'''
import numpy as np
import matplotlib as plt
import random
import target

def misclassified_no (vec) :
    count = 0
    for i in target.lst:
        if np.sign(vec.dot(i)) != np.sign(target.TF.dot(i)) :
            count+=1
    return count

def misclassifies_pt (vec) :
    if(misclassified_no(vec)==0) :
        return None
    else :
        temp =[]
        for i in target.lst:
            if np.sign(vec.dot(i)) != np.sign(target.TF.dot(i)) :
                temp.append(i)
        return temp[random.randrange(0,len(temp))]        

#PLA
weight = np.array([0,0,0])
iterator_pla = 0
while misclassified_no(weight) != 0 :
    iterator_pla += 1 
    pt = misclassifies_pt(weight)
    #print pt
    y = np.sign(target.TF.dot(pt))
    #print y
    #print pt*y
    weight = weight+pt*y

k = np.linspace(-1,1)
target.plt.plot(k, (-weight[1]/weight[2])*k+(-weight[0]/weight[2]), 'b-')
target.plt.show()    
    
    
                                             
                                              
        
    