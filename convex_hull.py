#!/usr/bin/python3

from which_pyqt import PYQT_VER
if PYQT_VER == 'PYQT5':
    from PyQt5.QtCore import QLineF, QPointF
elif PYQT_VER == 'PYQT4':
    from PyQt4.QtCore import QLineF, QPointF
else:
    raise Exception('Unsupported Version of PyQt: {}'.format(PYQT_VER))


import time
import math

class Node:
    point = NULL
    c = NULL
    cc = NULL

class ConvexHullSolver:

        def __init__( self, display ):
            self.points = None
            self.gui_display = display
                                                                #Start with a list of points
        def convex_hull(unsorted_points):
            sorted_points = sorted(unsorted_points, key = lambda p: p.x())
            recurse(sorted_points)                                #recurse through array to find each pnt

        def recurse(sorted_points):
            size = len(sorted_points)
            if size == 1:
                return create_node(sorted_points)
            else:
                half = math.floor(size / 2)                     #continue halving the array until size of 1
                left = recurse(sorted_points[0:half])                  #first half
                right = recurse(sorted_points[half + 1 : size - 1])    #second half
                return combine_hulls(left,right)

        def create_node(sorted_points):
            node = Node()
            node.point = sorted_points[0]
            node.c = node
            node.cc = node

        def combine_hulls(left, right):                         #combine left and right hulls by finding
            upper_tangent = findUpper(left, right)              #upper tangent of left and right hulls and
            btm_tangent = findLower(left, right)                #lower tangent of left and right hulls
            return convex(left, right, upper_tangent, btm_tangent)  #use node struct to create the convex hull

        #should return left and right point of the line that makes top tangent
        def findUpper(left, right):                             #find the upper tangent
            lhs = findRight(left)                               #right most point in left hull
            rhs = findLeft(right)                               #left most point in right hull
            slope = (lhs.y - rhs.y) / (lhs.x - rhs.x)           #compute slope
            tempSlope = NULL                                    #compare slopes

        #Find the right most x-coordinate in the left hull
        def findRight(left):
            right_most = left[0]
            for pnt in left:
                if pnt.x > right_most.x:
                    right_most = pnt
            return right_most

        #Find the left most x-coordinate in the right hull
        def findLeft(right):
            left_most = right[0]
            for pnt in right:
                if pnt.x > left_most.x:
                    left_most = pnt
            return left_most

        def create_convex(l, r, top, btm):
            ltop = l.node
            while(l.node.pt != top.lpt):
                ltop = ltop.c
		



        def compute_hull( self, unsorted_points ):
            assert( type(unsorted_points) == list and type(unsorted_points[0]) == QPointF )

            n = len(unsorted_points)
            print( 'Computing Hull for set of {} points'.format(n) )

            t1 = time.time()
            # TODO: SORT THE POINTS BY INCREASING X-VALUE
            t2 = time.time()
            print('Time Elapsed (Sorting): {:3.3f} sec'.format(t2-t1))

            t3 = time.time()
            # TODO: COMPUTE THE CONVEX HULL USING DIVIDE AND CONQUER


            t4 = time.time()

            USE_DUMMY = True
            if USE_DUMMY:
                # this is a dummy polygon of the first 3 unsorted points
                polygon = [QLineF(unsorted_points[i],unsorted_points[(i+1)%3]) for i in range(3)]

                # when passing lines to the display, pass a list of QLineF objects.  Each QLineF
                # object can be created with two QPointF objects corresponding to the endpoints
                assert( type(polygon) == list and type(polygon[0]) == QLineF )
                self.gui_display.addLines( polygon, (255,0,0) )
            else:
                # TODO: PASS THE CONVEX HULL LINES BACK TO THE GUI FOR DISPLAY
                pass

            print('Time Elapsed (Convex Hull): {:3.3f} sec'.format(t4-t3))
            self.gui_display.displayStatusText('Time Elapsed (Convex Hull): {:3.3f} sec'.format(t4-t3))

            # refresh the gui display
            self.gui_display.update()
