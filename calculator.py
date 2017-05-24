import networkx as nx;
#load('graph.sage')

#DONT FORGET TO CHANGE THIS
#change graph name
G = Graph({0:[1,2],1:[3],2:[3],3:[4,5],4:[6],5:[6],6:[7,8],7:[9],8:[9],9:[]})
start = 0
dest = order(G)-1

#if you get an error...your destination is probably wrong

plot(G)
dist = G.shortest_path_length(start,dest)

m = matrix(1, dist+1)

i = 0
for p in nx.all_shortest_paths(G,source=start,target=dest):
    i=i+1;
    b = matrix(p);
    m = m.insert_row(i,b[0]);
m = m.delete_rows([0]);

paths = len(m.rows())

SPGAM = matrix(paths,paths);

print m,dist,paths
print 'The Length of the Shortest Path is', dist
print 'There are', paths, 'unique paths in the graph.' 

for i in range(paths):
    for j in range(paths):
        if i == j:
            SPGAM[i,j] = 3;
        else:
            if j < i:
                SPGAM[i,j] = 3;

#print m
#print i
for i in range(paths):
    j = i+1;
    while j < paths:
        differences = 0;
        for k in range(dist):
            if m[i][k] != m[j][k]:
                differences = differences + 1;
        if differences == 1:
            SPGAM[i,j] = 1;
        else:
            if i == j:
                SPGAM[i,j]=3;
            else:
                SPGAM[i,j] = 0;
        j = j + 1;

#print SPGAM

Output = Graph()

for i in range(paths):
    for j in range(paths):
        if SPGAM[i][j] == 1:
            Output.add_edge(i,j);

plot(Output)
