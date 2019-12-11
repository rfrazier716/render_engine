'''
Created on Dec 3, 2019

@author: rfraz
'''

def import_dependencies():
    global np
    global plt
    import numpy as np
    from matplotlib import pyplot as plt 


class CubicBezier(): 
    def __init__(self,points):
        #points is an np array in the order of [[p00,p01,...,p0n],...,[p30,p31,...,p3n]] where for a 2d spline it takes the form [[x0,y0],...,[x3,y3]]
        self.control_points=points
    def get_basis(self,t_vals):
        try:
            return np.array([[(1-t)**3,3*t*(1-t)**2,3*t**2*(1-t),t**3] for t in t_vals])
        except TypeError:
            return [(1-t_vals)**3,3*t_vals*(1-t_vals)**2,3*t_vals**2*(1-t_vals),t_vals**3]
    def sample(self,t):
        return np.matmul(self.get_basis(t),self.control_points)

    

def main():
    pts=np.array([[0, 0], [1, 1], [2, -1], [3, 0]])
    bz=CubicBezier(pts)
    t_arr=np.linspace(0,1,100)
    ft=np.array([bz.sample(pt) for pt in t_arr])
    plt.plot(ft[:,0],ft[:,1])
    #plt.show()

    
if __name__=="__main__":
    print("Importing Dependencies")
    import_dependencies()
    print("Done")
    main()