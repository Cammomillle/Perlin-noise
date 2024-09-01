import numpy as np
import matplotlib.pyplot as plt
import random
import math
"Implements a 2D perlin noise generator !"
def perlin_noise(size,a,b):
    #generation of the grid, a is the number of lines per size
    step_x=size/a 
    step_y=size/b
    Points=[]
    x_points=[]
    y_points=[]
    Grad_vects=[]
    my_dict={}
    for j in range(0,b+1):
        for i in range(0,a+1):
            temp=np.round([step_x*i,step_y*j],3)
            sample=random.sample(range(-50,50),2)
            u=sample[0]
            v=sample[1]
            temp_vect=[u,v]
            temp_vect=temp_vect/np.linalg.norm(temp_vect)
            Points.append(temp)
            x_points.append(temp[0])
            y_points.append(temp[1])
            Grad_vects.append(temp_vect)
            my_dict['{0}'.format(temp)]=temp_vect
    return Points,my_dict,x_points,y_points,Grad_vects

"""
   Now, for each given point of the domain (x,y) we must know in which cell it lies. 
   The vector that links the given point to each of the corners of the cells will be the displacement vector
   The dot product between the displacement vector and the gradient vector of the given point is to be computed
"""

def perlin_mapping(size,step_x,step_y,x,y,Points,my_dict,x_points,y_points):

    x_min=0
    x_min=size
    k_x=int(x // step_x)
    k_y=int(y // step_y)
    #print("k_x,k_y",k_x,k_y)
    x_min=k_x*step_x
    #print("x_points",x_points)
    x2=x_min+step_x
    if(x_min==size):
        x2=x_min-step_x
    y_min=k_y*step_y
    y2=y_min+step_y
    if(y_min==size):
        y2=y_min-step_y
    Pts=[[x_min,y_min],[x2,y_min],[x2,y2],[x_min,y2]]
    #print("x,y",x,y)
    #print("x_min,y_min",x_min,y_min)
    #print("Points",Points)
    value=0
    for p in Pts:
        v=my_dict['{0}'.format(np.round(p,4))]
        x_,y_=p
        disp_vect=[x-x_,y-y_]
        #print("x,y",x,y)
        #print("x_,y_",x_,y_)
        dot_prod=np.dot(disp_vect,v)
        #print("dot_prod",dot_prod)
        #print("v",v)
        #print("disp_vect",disp_vect)
        value=value+np.dot(disp_vect,dot_prod)[0] #4 perlin noise values ! 
    return value/4 #interpolation = on prend la moyenn
    #for i in range(len(Points)):
     #   for j in range(len(Pts)):
      #      if(list(np.round(Pts[j],6))==list(np.round(Points[i],6))):
       #         orders.append(i)
    #print("orders",orders)
        

def perlin_mapping_stupid(size,step_x,step_y,x,y,Points,my_dict,x_points,y_points,Grad_vects):       
    tab_dist=[]
    for p in Points:
        tab_dist.append(math.dist([x,y],p))
    order=np.argsort(tab_dist)
    value=0
    for i in range(4):
        x_,y_=Points[order[i]]
        disp_vect=[x-x_,y-y_]
        dot_prod=np.dot(disp_vect,Grad_vects[order[i]])
        value=value+np.dot(disp_vect,dot_prod)[0] #4 perlin noise values ! 
    return value/4 #interpolation = on prend la moyenne"""
def map_generator(size,a,b,pts_x,pts_y):
    Points,my_dict,x_points,y_points,Grad_vects=perlin_noise(size,a,b)
    x_points=list(set(x_points))
    y_points=list(set(y_points))
    x_tab=np.linspace(0,size,pts_x)
    step_x=size/a
    step_y=size/b
    y_tab=np.linspace(0,size,pts_y)
    value_mat=np.zeros((pts_x,pts_y))
    Coord_mat=np.zeros((pts_x,pts_y),dtype=object)
    for j in range(len(y_tab)):
        for i in range(len(x_tab)):
           value_mat[i,j]=perlin_mapping(size,step_x,step_y,x_tab[i],y_tab[j],Points,my_dict,x_points,y_points)
           Coord_mat[i,j]=[x_tab[i],y_tab[j]]
        print("cool ass method",y_tab[j])
    plt.figure()
    heatmap, ax = plt.subplots()
    im = ax.imshow(value_mat,cmap='plasma',interpolation='nearest',origin='lower',aspect='auto')
    ax.set(xlabel='x', ylabel='y')
    cbar = heatmap.colorbar(im)
    cbar.ax.set_ylabel('Perlin noise')
    plt.savefig("hola.png",bbox_inches="tight")
    plt.show()
    """for j in range(len(y_tab)):
        for i in range(len(x_tab)):
           value_mat[i,j]=perlin_mapping_stupid(size,step_x,step_y,x_tab[i],y_tab[j],Points,my_dict,x_points,y_points,Grad_vects)
        print("stupid ass method",y_tab[j])
    plt.figure()
    heatmap, ax = plt.subplots()
    im = ax.imshow(value_mat,cmap='inferno',interpolation='nearest',origin='lower',aspect='auto')
    ax.set(xlabel='x', ylabel='y')
    cbar = heatmap.colorbar(im)
    cbar.ax.set_ylabel('Perlin noise (Dumb version)')"""
    return value_mat,Coord_mat,x_tab,y_tab
    
    
    
    
if __name__=="__main__": 
    "size of the domain , a,b number of lines in the grid (for x and y axis) , pts x and pts y the number of points for each axis"
    map_generator(size=10,a=100,b=100,pts_x=100,pts_y=100)