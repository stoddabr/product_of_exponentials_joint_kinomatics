#!/usr/bin/env python

""" implementation of astar """


import numpy as np
from helper import *
from node import *
from queue import PriorityQueue
import matplotlib.pyplot as plt


def get_astar_path(start,goal):
    """
        returns path using A* path planning algorithm
    """

    path = []
    start_node = AstarNode(start,None)
    goal_node = AstarNode(goal,None)
    start_node.h = get_dist(start_node,goal_node)
    start_node.f = start_node.g + start_node.h
    openlist = PriorityQueue()
    openlist.put((0,start_node))
    openlist_nodes = [start]  # list of node_coordinates in openlist
    closedlist = []         #list of already visited node_coordinates

    while not openlist.empty():

        cur_node = openlist.get()[1]
        # print("cur node = ",cur_node) 
        openlist_nodes.remove(cur_node.get_coords())
        closedlist.append(cur_node.get_coords())

        if is_equal(cur_node,goal_node):
            goal_node.parent = cur_node
            final_path = extract_path(cur_node,start_node,goal_node)
            # path_cost = cur_node.g + np.sqrt((cur_node.x-goal_node.x)**2 + (cur_node.y - goal_node.y)**2 + (cur_node.theta-goal_node.theta)**2)
            return final_path

        for neighbour in get_valid_neighbours(cur_node):
            # neighbour is [x,y,theta]
            if neighbour in closedlist:
                continue

            dist = np.sqrt((cur_node.x-neighbour[0])**2 + (cur_node.y-neighbour[1])**2 + (cur_node.theta-neighbour[2])**2)
            temp_g_cost = cur_node.g + dist  

            if neighbour not in openlist_nodes:

                neighbour_node = AstarNode(neighbour,None)
                neighbour_node.g = temp_g_cost
                neighbour_node.h = get_dist(neighbour_node,goal_node)
                neighbour_node.f = round(neighbour_node.g + neighbour_node.h,4)
                neighbour_node.parent = cur_node
                openlist_nodes.append(neighbour)
                openlist.put((neighbour_node.f,neighbour_node))
            else:

                old_neigh = get_neighbour(neighbour,openlist)
                old_neigh.h = get_dist(old_neigh,goal_node)
                old_neigh.parent = cur_node
                if temp_g_cost<old_neigh.g:
                    old_neigh.g = temp_g_cost   
                    old_neigh.f = round(old_neigh.g + old_neigh.h,4)
                    # openlist.put((old_neigh.f,old_neigh))
                    # openlist_nodes.append(old_neigh.get_coords())
    # return path





if __name__ == "__main__":

    start_config = [2,3,0.5]
    goal_config = [6,10,2.5]

    AstarPath = get_astar_path(start_config,goal_config)
    # print(AstarPath)
    x_coord = []
    y_coord = []
    theta_coord=[]
    for point in AstarPath:
        x_coord.append(point[0])
        y_coord.append(point[1])
        theta_coord.append(point[2])
   
    ### plotting the path 
    plt.plot(x_coord,y_coord,'g^-')
    plt.xlabel('x coord')
    plt.ylabel('y coord')
    plt.title('A* path from (2,3) to (6,10)')
    plt.show()