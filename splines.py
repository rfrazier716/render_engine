'''
Created on Dec 3, 2019

@author: rfraz
'''
import numpy as np

class CubicBezier(): 
    __m_basis_transform=np.array([[1,-3,3,-1],[0,3,-6,3],[0,0,3,3],[0,0,0,1]])
    # A 4 point Bezier Curve, extendable for multiple dimensions
    def __init__(self,points):
        self.bernstein_vector=points
        self.polynomial_ve=np.matmul(np.linalg.inv(self.__m_basis_transform),self.bernstein_vector)
        #Pass in a list of tuples
    

def main():
    print("Hello World")
    
if __name__=="__main__":
    main()