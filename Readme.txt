Readme

This project was created at Clemson University for undergrad graph theory research for Dr. Beth Novick by Jared Frager and Tyler LeVaur, spring 2017.


This repository contains a sage, now cocalc, script that run on an input graph to output a shortest path graph of the base graph. This project uses the networkx package in order to setup a graph, run a shortest path algorithm on that graph, and then call the networkx tool in order to find all shortest paths, returned as a list of all paths. A matrix is then created the size of the shortest path and then a symmetric difference is run on these paths in order determine if two paths are adjacent or not. If they are, the matrix is has a value of 1 for the corresponding edge. If they are not, a value of 3 in placed into the matrix. A new graph variable is then created and plotted from this matrix. 

The output is primarily the plotted shortest path graph, but any of the variables used along the way can be uncommented in order to see the process by which the SPG was created.

mainwahtever.something is the main file that contains the actual program that runs. This needs to have an input graph specified for the variable ___, so that it can compute the shortest path and adjacency matrix on that graph. 

something.graph contains  a list of graphs that can be used to run the program with. The graph file is loaded in at runtime, so the graph variable in the main file simply needs to match a corresponding graph variable name in the graph file. 

Graphs are created in the format of :

name = {{[first],[adjacent adjacent]}, {[second, [adj,adj]}} etc, where the adjacent nodes much be of greater value than the value of the vertex they are adjacent to.

for instance [5],[0,1] is NOT valid, as the adjacent vertices are higher than the node they are adjacent to.

However, [0],[5] and [1],[5] IS valid, as both 0 and 1 are less than 5.

Another example is ----


This program is free to use by anyone who may find use for it.
