# Readings 
Recitation notes 10, 6.006 Fall 2018 on stellar.

Lecture notes 10, 6.006 Fall 2018 on stellar.
# Breadth First Search


## Traversing the graph with BFS

<center>
<img src="/_static/IAP19/bfs-11.png" height="200"  />
</center>

<question multiplechoice>
csq_prompt = "Which of the following sequences of vertices could be produced by running a breadth-first search on the graph below starting at $A$?\n\n"
csq_renderer = "checkbox"
csq_soln = [0, 1, 0]
csq_options =  ['$[A, B, C, D]$',
 '$[A, D, B, C]$',
 '$[B, A, C, D]$']
csq_explanation = 'Because we begin at $A$, our BFS should visit its neighbors $B$ and $D$ before visiting $C$. Also, a BFS which starts at $A$ should visit $A$ first.'
</question>


<center>
<img src="/_static/IAP19/bfs-12.png" height="300"  />
</center>

<question multiplechoice>
csq_prompt = "Which of the following sequences of vertices could be produced by running a breadth-first search on the graph below starting at $A$?\n\n"
csq_renderer = "checkbox"
csq_soln = [1, 0, 1, 0]
csq_options =  ['$[A, B, C, D, E, F, G]$',
 '$[A, D, B, E, C, F, G]$',
 '$[A, C, D, B, F, G, E]$',
 '$[A, B, C, F, G, D, E]$']
csq_explanation = 'The second sequence visits $E$ (distance 2 from $A$) before visiting $C$ (distance 1 from $A$). The fourth sequence visits $F$ and $G$ before visiting $D$.'
</question>

<checkyourself>
Are you understanding?
<showhide>
yeah
</showhide>
</checkyourself>

<question multiplechoice>
csq_prompt = "Consider a graph with $V$ vertices in which each vertex has degree at most 10. (Recall that the degree of a vertex $v$ is the number of edges incident to $v$.) What is the time complexity of a breadth-first search on this graph?\n\n"
csq_renderer = "radio"
csq_soln = r'$\Theta(V)$'
csq_options =  [r'$\Theta(V)$',
 r'$\Theta(V\log V)$',
 r'$\Theta(V^2)$',
 r'$\Theta(V^{10})$']
csq_explanation = 'A useful property of graphs is that the sum of its vertex degrees is double the number of edges. (One way to think about this is that each degree counts an edge from one of its two endpoints.) The degree sum is $\le 10V$, so our edge count is $E=O(V)$. BFS runs in $\Theta(V+E)$ time, which simplifies to $\Theta(V)$ after our substitution.'
</question>


<center>
<img src="/_static/IAP19/bfs-13.png" height="200"  />
</center>


<question pythoncode>
csq_interface = 'ace'
csq_prompt = "Wumpus has infiltrated the sanctuary of his nemesis Kason Ju. This complex can be described as an undirected graph on $n$ vertices numbered from $0$ to $n-1$. Wumpus is located at room 0 and needs to connect his doomsday device by wire to $k$ different rooms (which can include room 0). Because of the exorbitant cost of wire which he bought from LaVerde's, he would like to use as little as possible. Running a wire between adjacent rooms uses 1 unit, and distinct connections cannot share wires on the same edge. In the above graph, one solution is shown for $k=4$. Write an algorithm to find a list of $k$ rooms that satisfies the condition. (In the same example, either [0, 1, 2, 3] or [0, 1, 2, 4] in any order would be correct.)"

## Define solution that will be printed to student.
csq_soln = '''def closestK(n, k, graph):
    closest = []
    visited = [False for i in range(n)]  # list of n Falses
    queue = [0]
    head = 0  # index of queue head, increments when we pop off the queue
    while len(closest) < k and head < len(queue):
        v = queue[head]
        head += 1
        if visited[v]:
            continue
        closest.append(v)
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:
                queue.append(w)
    return closest
'''

## Code that will be initially on the thingy
csq_initial = '''def closestK(n, k, graph):
    queue = []

    # exploring the neighbors of 0
    v = 0
    for w in graph[v]:
        queue.append(w)
'''


def bfs_dists(n, k, g):
    visited = [False for i in range(n)]
    parent = [None for i in range(n)]
    queue = [0]
    closest = []
    head = 0  # index of queue head, increments when we pop off the queue
    while len(closest) < k and head < len(queue):
        v = queue[head]
        head += 1
        if visited[v]:
            continue
        visited[v] = True
        closest.append(v)
        for w in g[v]:
            if not visited[w]:
                queue.append(w)
                if parent[w] is None:
                    parent[w] = v

    # checks that at least k vertices are reachable
    if len(closest) < k:
        return (None, None)

    dists = [n for i in range(n)]
    dists[0] = 0

    def find_dist(i):
        if parent[i] is not None and dists[i] == n:
            dists[i] = find_dist(parent[i]) + 1
        return dists[i]

    for i in range(n):
        find_dist(i)

    return (dists, sum(dists[i] for i in closest))

test_params = [(10, 5, 0.25),
         (50, 30, 0.08),
         (100, 60, 0.06),
         (300, 120, 0.02)]

tests = []
tests.append((6, 4, {0: [1, 2], 1: [0, 2, 3, 4], 2: [0, 1, 3], 3: [1, 2, 5], 4: [1], 5: [3]}, [0, 1, 1, 2, 2, 3], 4))

for n, k, p in test_params:
    remake = True
    while remake:
        g = {i: [] for i in range(n)}
        for i in range(n):
            for j in range(i + 1, n):
                if cs_random.random() < p:
                    g[i].append(j)
                    g[j].append(i)
        dists, min_dist = bfs_dists(n, k, g)
        remake = dists is None
    tests.append((n, k, g, dists, min_dist))


def is_correct(test, sol):
    if not isinstance(sol, list):
        return False
    n, k, g, dists, min_dist = test
    if len(sol) != k:
        return False
    return all(dists[i] < n for i in sol) and sum(dists[i] for i in sol) == min_dist


csq_tests = []
for i, t in enumerate(tests):

    def check(ans, soln, i = i):
        return is_correct(tests[i], eval(ans))
        
    csq_tests.append({
        'code': f"""
n, k, g, _, _ = {t}
ans = closestK(n, k, g)""",
        'check_function': check
    })

</question>


## Building a BFS tree

A breadth-first search that only queues up vertices to be visited can find nearby vertices easily but can't easily compute the distances to these vertices or reconstruct the shortest paths used to reach them. To do this, we need to introduce <i>parent pointers</i> to our algorithm.

In a breadth-first search (as well as in other graph searches), the parent of a vertex is the vertex which immediately precedes it. An example is shown below in which we have just visited vertex $A$. The red arrow edges indicate that vertices $B$ and $C$ each point to $A$ as their parent.

<center>
<img src="/_static/IAP19/bfs-21.png" height="200"  />
</center>

After visiting vertex $B$, we assign it to be the parent of vertices $D$ and $E$. Note that we don't assign $B$ as the parent of $A$ because $A$ has already been visited, and we don't assign it as the parent of $C$ because $C$ already has a parent.

<center>
<img src="/_static/IAP19/bfs-22.png" height="200"  />
</center>

The graph illustrates the completed parent pointers from this BFS. Note that the edges corresponding to the parent pointers form a tree, in which every vertex has exactly one path (namely, the shortest one) to the starting vertex $A$. A graph can have multiple such trees depending on which vertex the BFS starts at and its visit order. In the above example, we could have assigned $C$ to be the parent of $D$ and found an equally valid tree.

<center>
<img src="/_static/IAP19/bfs-23.png" height="200"  />
</center>


<checkyourself>
Can a vertex have multiple parents? Can a vertex have no parent? Can a vertex be a parent to multiple other vertices?
<showhide>
A vertex can have at most one parent, but a vertex can be a parent to multiple vertices as seen above. A vertex will have no parent if it is the starting vertex (by definition) or if it is unreachable from the starting vertex.<br>From an implementation standpoint, this makes parent pointers easy to use, as we can store all of our pointers in an array-like structure, where element $i$ is the parent of vertex $i$.
</showhide>
</checkyourself>

<checkyourself>
Can the parent pointers form a cycle?
<showhide>
No, because following the parent pointers from any vertex will always lead to the starting vertex, where the path stops.
</showhide>
</checkyourself>

## Shortest path finding with state management

Consider the graph below, in which edges are colored either red or blue. How would we find the shortest path from vertex $A$ to another vertex given that the path <i>must contain a blue edge</i>?

<center>
<img src="/_static/IAP19/bfs-31.png" height="200"  />
</center>

Let's look at our options going from $A$ to $E$. The shortest path without the blue edge restriction is $A\to B\to E$, but this doesn't satisfy our condition. If we were to prioritize blue edges first, we would likely find the path $A\to C\to F\to D\to E$, but we can do better with $A\to B\to D\to E$, the correct answer.

Because it isn't easy to change the algorithm to accommodate this restriction, we can think about changing the graph instead. When we explore the graph with BFS and build up our shortest paths, for each vertex $v$, we'd like to know the shortest path to $v$ that <i>does not</i> use a blue edge, and the shortest path to $v$ that <i>does</i> use a blue edge. Instead of maintaining two different paths to one vertex, we can split $v$ into two versions, $v$ and $v'$. An example of this split for one vertex is illustrated below.

<center>
<img src="/_static/IAP19/bfs-32.png" height="200"  />
</center>
