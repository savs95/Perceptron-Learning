'''
Created on May 24, 2015

@author: savs95
'''
import random
import matplotlib.pyplot as plt
import numpy as np

def generate_points (no):
    lst=[]
    for i in range(no) :
        x,y=[random.uniform(-1,1) for j in range(2)]
        temp_array = np.array([1,x,y])
        lst.append(temp_array)
    return lst    

print "Please enter number of points"
inp = input()

#Points for target Function
x1,x2,y1,y2 = [random.uniform(-1,1) for i in range(4)]
#Function Array
TF = np.array([x2*y1-x1*y2, y2-y1, x1-x2])
#Random Data Points
lst = []
lst = generate_points(inp)
plt.axis([-1,1,-1,1])
l = np.linspace(-1,1)
for i in lst :
    if(np.sign(TF.dot(i)) < 0):
        plt.plot(i[1],i[2],'ro')
    else :
        plt.plot(i[1],i[2],'go')
        
plt.plot(l,(-TF[1]/TF[2])*l+(-TF[0]/TF[2]),'y-')


