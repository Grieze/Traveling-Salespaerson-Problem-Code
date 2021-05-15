### Code that contains solution to Traveling Salesman Problem with Backtracking
answer = []

# define function to solve TSP
def tsp(graph, v, curr, n, count, cost):

    # If last node reached and it has a link to source node,
    # keep the min value out of the total cost of traversal and 'ans'
    # Finally go back and check for more possible values
    if (count == n and graph[curr][0]):
        answer.append(cost + graph[curr][0])
        return

    # Backtracking Step
    # Loop to traverse the adjacency list of curr node
    # Each traversal increases count by 1 and cost by
    # graph[curr][i] value since we're including
    # the new possible node values
    for i in range(n):
        if (v[i] == False and graph[curr][i]):
            # Mark node as visited
            v[i] = True
            tsp(graph, v, i, n, count+1, cost + graph[curr][i])

            # Mark ith node as unvisited
            v[i] = False

# Putting it all together

if __name__ == '__main__':
    # n = 8
    from random import *
    import random
    import numpy as np
    import time    
    # set seed to the answer to life, the universe, and everything
    random.seed(42)

    def testTSP(n):
        # create an 8 x 8 sparse matrix to represent an initilaized blank graph
        graph = np.zeros((n,n))
        
        # assign random integers 
        for i in range(n):
            for j in range(n):
                # if i == j that means we're at the same node (i.e. no edge)
                # which should have a distance of 0 with itself
                if i == j:
                    continue
                # assign rand int between 1 and 20 as edge weight
                else:
                    graph[i][j] = randint(1,20)

        # print out our randomly generated graph
        print('Randomly Generated Graph is:')
        for i in range(n):
            print(graph[i])
            
        # boolean array to check if a node has been visited or not
        v = [False for i in range(n)]
        # mark 0th node as visited
        v[0] = True
        
        # time our program
        start_time = time.time()

        # execute our function
        tsp(graph, v, 0, n, 1, 0)

        # ans is the minimum weight Hamoltonian Cycle or the optimal path for the salesman
        print(min(answer))
        print("--- %s seconds ---" % (time.time() - start_time))

    testTSP(8)
    trials = [2, 3, 4, 5, 6, 7]
    for trial in trials:
        testTSP(trial)
