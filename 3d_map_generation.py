import numpy as np
import matplotlib.pyplot as plt
import random
import math
import perlin_noise
def threeD_map(size,a,b,pts_x,pts_y):
    alt_map,coord_mat,x_tab,y_tab=perlin_noise.map_generator(size,a,b,pts_x,pts_y)
    alt_map=10+(alt_map/np.max(alt_map))
    ax=plt.figure().add_subplot(projection='3d')
    X,Y=np.meshgrid(x_tab,y_tab)
    ax.plot_surface(X,Y,alt_map,cmap="viridis")
    ax.set_xlabel("X label")
    ax.set_ylabel("Y label")
    ax.set_zlabel("Z label")
    ax.set_zlim(0,11)
    plt.show()
    
    
if __name__=="__main__": 
    "size of the domain , a,b number of lines in the grid (for x and y axis) , pts x and pts y the number of points for each axis"
    threeD_map(size=10,a=10,b=10,pts_x=100,pts_y=100)
    

