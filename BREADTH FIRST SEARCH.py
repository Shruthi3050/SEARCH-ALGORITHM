#!/usr/bin/env python
# coding: utf-8

# ## GRAPH REPRESENTATION

# In[1]:


my_graph = {
    
    'S':['A','B','C'],
    'A':['S','B','D'],
    'B':['S','A','D','H'],
    'C':['S','L'],
    'D':['A','B','F'],
    'H':['B','F','G'],
    'L':['C','I','J'],
    'F':['D','H'],    
    'G':['H','E'],
    'I':['L','K'],
    'J':['L','K'],
    'E':['G','K'],
    'K':['I','J','E']    
}


# ## IMPORT DEQUE

# In[2]:


from collections import deque


# ## BREADTH FIRST SEARCH

# In[3]:


def bfs(graph,start,goal):
    visited = []
    queue=deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited :
            visited.append(node)
            print("Have visited: ",node)
            neighbours = graph[node]
            if node == goal :
                return("Goal is reached via path: ",visited)
            for neighbours in neighbours :
                queue.append(neighbours)
    


# ## STARTING NODE - S, ENDING NODE - F

# In[4]:


bfs(my_graph,'S','F')


# ## STARTING NODE - S, ENDING NODE - E

# In[5]:


bfs(my_graph,'S','E')


# ## WORK DESCRIPTION BREADTH FIRST SEARCH
# ### INTRODUCTION
# * Breadth-first search is a recursive graph traversal algorithm that starts traversing the graph from the root node and      explores all the neighboring nodes. 
# * Then, it selects the nearest node and explores all the unexplored nodes.
# * BFS puts every vertex of the graph into two categories - visited  non-visited. 
# ### ALGORITHM
# * STEP 1 - Start with the source node.
# * STEP 2 - Add that node at the front of the queue to the visited list.
# * STEP 3 - Make a list of the nodes as visited that are close to that vertex.
# * STEP 4 - Dequeue the nodes once they are visited. 
# * STEP 5 - Repeat the actions until the queue is empty.
# * STEP 6 - Stop.
# ## CASE - 1 
# ### STARTING NODE - S, ENDING NODE - F
# * The traversal starts at node S (level 0) and ends with node F.
# * The first level is searched (i.e.,) S to A, B, C.
# * Then the second level is searched (i.e.,) C to D, H, L.
# * It is followed by the third level (i.e.,) L to F.
# * The goal node is reached, so the search stops.
# * It follows the following route to reach the goal node(F) from the starting node(S):
#                                 S -> A -> B -> C -> D -> H -> L -> F
# ## CASE - 2
# ### STARTING NODE - S, ENDING NODE - E
# * The traversal starts at node S (level 0) and ends with node E.
# * The first level is searched (i.e.,) S to A, B, C.
# * Then the second level is searched (i.e.,) C to D, H, L.
# * It is followed by the third level (i.e.,) L to F, G, I, J.
# * It is followed by the fourth level (i.e.,) J to E and since the goal node is reached, the search stops.
# * It follows the following route to reach the goal node(E) from the starting node(S):
#                                 S -> A -> B -> C -> D -> H -> L -> F -> G -> I -> J -> E
