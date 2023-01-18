import numpy as np
import random
import matplotlib.pyplot as plt
import time
from copy import deepcopy

random.seed(80)
rand_x = np.array(random.choices(range(1,501),k=50))
rand_y = np.array(random.choices(range(1,501),k=50))

class Delaunay_Triangulation:
    def __init__(self, x = rand_x, y = rand_y):
        self.point = [rand_x,rand_y]
        self.points = [[ix,iy] for (ix,iy) in zip(x,y)]
        self.centers = []
        self.lines = []
        
        self.show_point()

    def show_point(self):
        plt.plot(self.point[0],self.point[1],'ro')
        # plt.show()
        
    def show_centers(self):
        for p in self.centers:
            # continue
            plt.plot(p[0],p[1],'bo')
        # plt.show()
        
    def show_lines(self):
        for ln in self.lines:
            plt.plot([ln[0][0],ln[1][0]],[ln[0][1],ln[1][1]])
            
        # plt.axis([0, 500, 0, 500])
        plt.show()

    def get_circumcenter(self, p1, p2, p3):
        x1,y1 = p1
        x2,y2 = p2
        x3,y3 = p3
        
        A = x2 - x1
        B = y2 - y1
        C = x3 - x1
        D = y3 - y1
        E = A * (x1 + x2) + B * (y1 + y2)
        F = C * (x1 + x3) + D * (y1 + y3)
        G = 2.0 * (A * (y3 - y2) - B * (x3 - x2))
        if G == 0:
            return p1

        center = [(D * E - B * F) / G, (A * F - C * E) / G]
        return center

    def calcdis(self, a, b):
        dis = ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5
        return dis

    def is_centers(self, pre_center, i, j, k):
        point = deepcopy(self.points)
        point.remove(i)
        point.remove(j)
        point.remove(k)
        
        dis1 = ((k[0]-pre_center[0])**2 + (k[1]-pre_center[1])**2)**0.5
        for p in point:
            p = np.array(p)
            dis2 = ((p[0]-pre_center[0])**2 + (p[1]-pre_center[1])**2)**0.5
            if dis1 > dis2:
                return False
            
        self.centers.append(pre_center)
        return True    
    
    def Delaunay_Triangulation(self):
        start = time.time()
        point = self.points
        for i in range(0,len(point)):
            for j in range(i+1,len(point)):
                for k in range(j+1,len(point)):
                    pre_center = self.get_circumcenter(point[i],point[j],point[k])
                    # plt.plot(pre_center[0],pre_center[1],'b*')
                    _is = self.is_centers(pre_center,point[i],point[j],point[k])
                    if _is:
                        self.lines.append([point[i],point[j]])
                        self.lines.append([point[j],point[k]])
                        self.lines.append([point[k],point[i]])
        print(time.time()-start)
        #self.show_centers()
        self.show_lines()
                            
DT = Delaunay_Triangulation()
DT.Delaunay_Triangulation()