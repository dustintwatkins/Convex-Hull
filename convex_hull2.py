from which_pyqt import PYQT_VER
if PYQT_VER == 'PYQT5':
    from PyQt5.QtCore import QLineF, QPointF
elif PYQT_VER == 'PYQT4':
    from PyQt4.QtCore import QLineF, QPointF
else:
    raise Exception('Unsupported Version of PyQt: {}'.format(PYQT_VER))


import time
import math


def convex_hull(sorted_points):
    if len(sorted_points) <= 1:
        return sorted_points

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]



class ConvexHullSolver:

        def __init__( self, display ):
            self.points = None
            self.gui_display = display
                                                                       #Start with a list of points

        def compute_hull( self, unsorted_points ):
            assert( type(unsorted_points) == list and type(unsorted_points[0]) == QPointF )

            n = len(unsorted_points)
            print( 'Computing Hull for set of {} points'.format(n) )

            t1 = time.time()
            # TODO: SORT THE POINTS BY INCREASING X-VALUE

            #O(nlog(n))
            sorted_points = sorted(unsorted_points, key = lambda p: p.x())
            print('size of list = ', len(sorted_points))

            t2 = time.time()
            print('Time Elapsed (Sorting): {:3.3f} sec'.format(t2-t1))
            t3 = time.time()
            # TODO: COMPUTE THE CONVEX HULL USING DIVIDE AND CONQUER


            hull_points = convex_hull(sorted_points)

            t4 = time.time()
            print("done with solving")
            #iterate through the linked list to make a list to draw lines


            print("size of list = ", len(hull_points))

            USE_DUMMY = False
            if USE_DUMMY:
                # this is a dummy polygon of the first 3 unsorted points
                polygon = [QLineF(unsorted_points[i],unsorted_points[(i+1)%3]) for i in range(3)]

                # when passing lines to the display, pass a list of QLineF objects.  Each QLineF
                # object can be created with two QPointF objects corresponding to the endpoints
                assert( type(polygon) == list and type(polygon[0]) == QLineF )
                self.gui_display.addLines( polygon, (255,0,0) )
            else:
                # TODO: PASS THE CONVEX HULL LINES BACK TO THE GUI FOR DISPLAY

                polygon = [QLineF(hull_points[i], hull_points[(i+1)]) for i in range(len(hull_points) - 1)]
                assert( type(polygon) == list and type(polygon[0]) == QLineF )
                self.gui_display.addLines( polygon, (255,0,0) )
                pass

            print('Time Elapsed (Convex Hull): {:3.3f} sec'.format(t4-t3))
            self.gui_display.displayStatusText('Time Elapsed (Convex Hull): {:3.3f} sec'.format(t4-t3))

            # refresh the gui display
            self.gui_display.update()
