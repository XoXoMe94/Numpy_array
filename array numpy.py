# -*- coding: utf-8 -*-
"""


@author: sara
"""

import numpy as np 


#ex1 make a array 1 dim
a=np.array([1,2,3])
print(a) #[1 2 3]
print(a.ndim)   #1
print(a.shape)   #(3,1)
a.dtype   #dtype('int32')



#ex2 make a array 2 dim
b=np.array([[1,2,3],[4,5,6]])
print(b)     #[[1 2 3]
             #[4 5 6]]
print(b.ndim)  #2
print(b.shape)  #(2, 3)
b.dtype  #dtype('int32')



#ex3 float
c=np.array([1.1,5,2.3])
c.dtype   #dtype('float64')
c   #array([1.1, 5. , 2.3])  5 auto to float



#ex4 array zeros
d=np.zeros((2,3)) 
print(d)     #[[0. 0. 0.]
             #[0. 0. 0.]]
             
             
             
#ex5 array ones
e=np.ones((2,3))  
print(e)       #[[1. 1. 1.]
                #[1. 1. 1.]]
                





#ex full
array=np.array([1,2,3])
a=np.full(3, 20)   
print(a)        #[20 20 20]      


modify_array=array-a
print(modify_array) #[-19 -18 -17]




                
#ex6 random
np.random.rand(2,3)
               #array([[0.60888433, 0.94771844, 0.05959367],
                    # [0.0561195 , 0.15465892, 0.97477083]])
                
                
                
                
#ex7 arange
f=np.arange(10,50,2)  #start bond,end bond,difference between            
print(f) #[10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48]

f=np.arange(10,50,2).reshape(2,10)  
print(f)     #[[10 12 14 16 18 20 22 24 26 28]
              #[30 32 34 36 38 40 42 44 46 48]]        





#ex8 linspace
g=np.linspace(0, 2,15) #start,end,how many number
print(g)      #[0.         0.14285714 0.28571429 0.42857143 0.57142857 0.71428571
                #0.85714286 1.         1.14285714 1.28571429 1.42857143 1.57142857
                #1.71428571 1.85714286 2.        ]
                
                
                
                
#ex9 operation on array
a=np.array([1,2,3,4])
b=np.array([6,3,7,9])  
c=a-b
print(c)   #[-5 -1 -4 -5]
d=a+b
print(d)   #[ 7  5 10 13]
e=a*b
print(e)    #[ 6  6 21 36]
f=a/b  
print(f)    #[0.16666667 0.66666667 0.42857143 0.44444444]  





#ex10 convert fahrenheit to celsius
   #celsius= (fahrenheit-31) * 5.9
f=np.array([1,0,-4,-60,38])
c=(f-31)*5.9
print(c)    #[-177.  -182.9 -206.5 -536.9   41.3]
c>-20       #array([False, False, False, False,  True])
c%2==0      #array([False, False, False, False, False])




#ex11   (* normal)  (@ matrix)
a=np.array([[1,3],[4,6]])
b=np.array([[11,13],[14,16]])
print(a*b)       #[[11 39]
                 #[56 96]]
               
print(a@b)         # [[ 53  61]
                     #[128 148]]   
                     
                     

#ex12 int float
a=np.array([1,2,3])
b=np.array([6.8,3.5,7.9]) 
c=a+b
print(c.dtype)  #float64




#ex13 sum max min mean
a=np.array([1,2,3])
print(a.max())  #3
print(a.min())   #1
print(a.sum())   #6
print(a.mean())    #2.0





#ex14      index
a=np.array([1,5,3,8]) 
print(a[2])              #3


b=np.array([[1,2,3],[6,4,8]]) 
print(b[1,2])  #row 1 #colomn2 start from 0    #8





                     