# ENGR2050_02_jasayles.py
# Ethan Sayles
# Feb 09, 2017
import numpy as np

#function to solve for the stretch in a series of spring connected end to end. 
def spring_stretch(n, k, w):                   #n = number of springs, k = list of spring constant values, w = list of weights attachted to the springs.
    if len(k) != n or len(w) != n:                #Check to ensure that k and w are lists of the correct size.
        return None
    else:
        a = np.zeros(shape=(n,n))               #Create an nxn matrix filled with zeroes
        for i in range(1,n-1):                        #Fill the 2nd to n-1th h with the equation -ki(x(i-1)) + (ki+k(i+1)) -k(i+1)x(i+1) = wi
            a[i][i-1] = -k[i]
            a[i][i] = k[i]+k[i+1]
            a[i][i+1]=-k[i+1]
        a[0][0] = k[0]+k[1]                         #make the first row: (k0+k1)x1-k2x2=w1
        a[0][1] = -k[1]
        a[n-1][n-2] = -k[n-1]                       #make the last row: -k(n-1)x(n-1) + knxn = wn
        a[n-1][n-1] = k[n-1]
        b = np.array(w)                                #make the list of weights an array
        c = np.linalg.solve(a,b)                    #solve the equation for the x values
        return (c)                                         #return the list of x values
    
#Conditional to check for test cases
if __name__ == '__main__':
    print (spring_stretch(5,[10,10,10,5,5],[100,50,100,50,100] ))   #n=5, k1=k2=k3=10, k4=k5=5, w1=w3=w5=100, w2=w4=50
   
