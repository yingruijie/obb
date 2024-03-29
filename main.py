import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from box import box_3d
from utils.plot_shape import plot_shape_3d, get_point_3d
from obb import obb_3d_check

if __name__ == '__main__':
    ax = plt.subplot(111, projection = '3d')

    o1 = box_3d()
    o1.get_by_axis(1,2,3,  0.7,0.3,-0.1, 2,2,2, 100)
    o1.plot_shape(ax, 'r')
    o1.plot_scatter(ax, 'r')

    o2 = box_3d()
    o2.get_by_axis(0,1,-2, 1.2,-0.1,0.7, 3,1,3, 100)
    o2.plot_shape(ax, 'b')
    o2.plot_scatter(ax, 'b')
    plt.title('scatter_fitting')
    plt.savefig('images_output/scatter_fitting.png')
    plt.show()

    is_intersect = 'true' if obb_3d_check(o1, o2) == True else 'false'
    
    ax = plt.subplot(111, projection = '3d')
    o1.plot_shape(ax, 'r')
    o2.plot_shape(ax, 'b')
    plt.title('is_intersect = ' + is_intersect)
    plt.savefig('images_output/result.png')
    plt.show()