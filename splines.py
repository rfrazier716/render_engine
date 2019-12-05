'''
Created on Dec 3, 2019

@author: rfraz
'''
import numpy as np

class CubicBezier(): 
    __m_basis_transform=np.array([[1,-3,3,-1],[0,3,-6,3],[0,0,3,3],[0,0,0,1]])
    # A 4 point Bezier Curve, extendable for multiple dimensions
    def __init__(self,points):
        self.bernstein_matrix=points
        self.polynomial_matrix=np.matmul(np.linalg.inv(self.__m_basis_transform),self.bernstein_matrix)
        #Pass in a list of tuples
    
    def get_bernstein_vector(self,dimension):
        if dimension.lower() in "xyz":
            #If a letter was provided, translate that to a coordinate and return
            dimension='xyz'.find(dimension.lower())
    

def main():
    points=np.array([[0,0],[1,1],[2,-1],[3,0]])
    bz=CubicBezier(points)
    print(bz.polynomial_matrix)
    print("Hello World")
    
if __name__=="__main__":
    main()