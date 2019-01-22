# Readings 
Recitation notes 10, 6.006 Fall 2018 on Stellar.

Lecture notes 10, 6.006 Fall 2018 on Stellar.

# Traversing the graph with BFS

BFS shares many characteristics with DFS, but BFS visits vertices in order of increasing distance. This invariant lends itself well to finding nearby vertices from a starting point, as well as computing distances and shortest paths in unweighted graphs.

<center>
<img src="/_static/IAP19/bfs-11.png" height="200"  />
</center>

<question multiplechoice>
csq_prompt = "Which of the following sequences of vertices could be produced by running a breadth-first search on the graph above starting at $A$?\n\n"
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
csq_prompt = "Which of the following sequences of vertices could be produced by running a breadth-first search on the graph above starting at $A$?\n\n"
csq_renderer = "checkbox"
csq_soln = [1, 0, 1, 0]
csq_options =  ['$[A, B, C, D, E, F, G]$',
 '$[A, D, B, E, C, F, G]$',
 '$[A, C, D, B, F, G, E]$',
 '$[A, B, C, F, G, D, E]$']
csq_explanation = 'The second sequence visits $E$ (distance 2 from $A$) before visiting $C$ (distance 1 from $A$). The fourth sequence visits $F$ and $G$ before visiting $D$.'
</question>

<question multiplechoice>
csq_prompt = "Consider a graph with $V$ vertices in which each vertex has degree at most 10. (Recall that the degree of a vertex $v$ is the number of edges incident to $v$.) What is the time complexity of a breadth-first search on this graph?\n\n"
csq_renderer = "radio"
csq_soln = r'$\Theta(V)$'
csq_options =  [r'$\Theta(V)$',
 r'$\Theta(V\log V)$',
 r'$\Theta(V^2)$',
 r'$\Theta(V^{10})$']
csq_explanation = 'A useful property of undirected graphs is that the sum of its vertex degrees is double the number of edges. (One way to think about this is that each degree counts an edge from one of its two endpoints.) The degree sum is $\le 10V$, so our edge count is $E=O(V)$. BFS runs in $\Theta(V+E)$ time, which simplifies to $\Theta(V)$ after our substitution.'
</question>

<center>
<img src="/_static/IAP19/bfs-13.png" height="200"  />
</center>

<question pythoncode>
csq_interface = 'ace'
csq_npoints = 3
csq_prompt = "Wumpus has infiltrated the sanctuary of his nemesis Kason Ju. This complex can be described as an undirected graph on $n$ vertices numbered from $0$ to $n-1$. Wumpus is located at room $0$ and needs to connect his doomsday device by wire to $k$ different rooms (which can include room $0$).\n\nBecause of the exorbitant cost of wire which he bought from LaVerde's, he would like to use as little as possible. Running a wire between adjacent rooms uses 1 unit, and distinct connections cannot share wires on the same edge. In the above graph, one solution is shown for $k=4$.\n\nWrite an algorithm to find a list of $k$ rooms that satisfies the above condition. (In the same example, either $[0, 1, 2, 3]$ or $[0, 1, 2, 4]$ in any order would be correct.)\n\n"

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
    visited = [False for i in range(n)]
    queue = [0]

    # visiting vertex 0
    v = queue[0]
    visited[v] = True
    for w in graph[v]:
        queue.append(w)

    return None
'''

def bfs_dists(n, k, g):
    visited = [False for i in range(n)]
    parent = [None for i in range(n)]
    queue = [0]
    closest = []
    head = 0  # index of queue head, increments when we pop off the queue
    while head < len(queue):
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

    return (dists, sum(dists[i] for i in closest[:k]))

test_params = [(10, 5, 0.25),
         (50, 30, 0.079),
         (100, 70, 0.047),
         (300, 240, 0.0191)]

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


# Building a BFS tree

A breadth-first search that only queues up vertices to be visited can find nearby vertices but can't easily compute the distances to them or reconstruct the shortest paths used to reach them. To do this, we need to introduce <i>parent pointers</i> to our algorithm.

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

<question multiplechoice>
csq_prompt = "Which statements regarding parent pointers are true?\n\n"
csq_renderer = "checkbox"
csq_soln = [0, 1, 1, 0]
csq_options =  [r'A vertex can have multiple parents.',
 r'A vertex can have no parent.',
 r'A vertex can be a parent to multiple vertices.',
 r'The shortest path from vertex $v$ to the starting vertex must include the parent of $v$.']
csq_explanation = 'A vertex can have at most one parent, but a vertex can be a parent to multiple vertices as seen above. A vertex will have no parent if it is the starting vertex (by definition) or if it is unreachable from the starting vertex. While the parent of a vertex is on a shortest path to that vertex, the path need not be unique, and alternate shortest paths can use different vertices.<br>From an implementation standpoint, this makes parent pointers easy to use, as we can store all of our pointers in an array-like structure, where element $i$ is the parent of vertex $i$.'
</question>

<checkyourself>
Can the parent pointers form a cycle?
<showhide>
No, because following the parent pointers from any vertex will always lead to the starting vertex, where the path stops.
</showhide>
</checkyourself>

<center>
<img src="/_static/IAP19/bfs-24.png" height="200"  />
</center>

<question expression>
csq_prompt = "A BFS is run on the graph above starting from $A$. Which vertices could be the parent of $E$ as a result? List them as a string in alphabetical order.   \n\n"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = "FG"
csq_explanation = "By inspection, we see that $E$ is distance 3 away from $A$. Its parent must be an adjacent vertex distance 2 away from $A$, and any such vertex will work. The vertices which satisfy these conditions are $F$ and $G$."
csq_nsubmits = None
</question>


# Harder shortest path finding

Consider the graph below, in which edges are colored either red or blue. How would we find the shortest path from vertex $A$ to another vertex given that the path <i>must contain a blue edge</i>?

<center>
<img src="/_static/IAP19/bfs-31.png" height="250"  />
</center>

Let's look at our options going from $A$ to $E$. The shortest path without the blue edge restriction is $A\to B\to E$, but this doesn't satisfy our condition. If we were to prioritize blue edges first, we would likely find the path $A\to C\to F\to D\to E$, but we can do better with $A\to B\to D\to E$, the correct answer.

Because it isn't easy to change the algorithm to accommodate this restriction, we can think about changing the graph instead. We'd like to make a new graph with colorless edges based on the original one such that performing a simple BFS on this graph will give us our desired answer. The key idea is that this new graph has to describe where we are and whether or not we've used a blue edge to get there. For a vertex $v$ in the original graph, we can split $v$ into two versions, $v$ and $v'$, so that being on $v$ means that we have not used a blue edge and being on $v'$ means that we have. An example of this split for one vertex is illustrated below.

<center>
<img src="/_static/IAP19/bfs-32.png" height="200"  />
</center>
 
When we apply this idea of vertex duplication to the entire graph, we end up with two copies, the "normal" side $({A, B, C,\dots})$ and the "prime" side $({A', B', C',\dots})$. Moving through this new graph captures both our location in the original graph and whether we have used a blue edge. Edges in this new graph can then describe movement in the original graph as well as changes to this "used-a-blue-edge" state. Now we just need to figure out how to transfer our original edges into this new graph.

<question multiplechoice>
csq_prompt = "If edge $uv$ in the original graph was red, which edges would we need to add to our new graph?\n\n"
csq_renderer = "checkbox"
csq_soln = [1, 0, 0, 1]
csq_options =  ["$uv$",
 "$uv'$",
 "$u'v$",
 "$u'v'$"]
csq_explanation = "Moving along a red edge doesn't change our used-a-blue-edge state. If we were on a normal vertex, we move to another normal vertex. Likewise, if we were on a prime vertex, we move to another prime vertex."
</question>

<question multiplechoice>
csq_prompt = "If edge $uv$ in the original graph was blue, which edges would we need to add to our new graph?\n\n"
csq_renderer = "checkbox"
csq_soln = [0, 1, 1, 1]
csq_options =  ["$uv$",
 "$uv'$",
 "$u'v$",
 "$u'v'$"]
csq_explanation = "Moving along a blue edge means that our used-a-blue-edge state is now true if it wasn't already true. That means that if we were on a normal vertex, we have to move to a prime vertex. Because these edges are undirected (i.e. $vu$ is also an edge), we need both $uv'$ and $vu'$ for symmetry. If we were on a prime vertex, we should be able to go to another prime vertex as using another blue edge doesn't change our state, so we also have $u'v'$.\n\nYou might notice that this setup would allow us to move from a prime vertex back to a normal vertex, which seems odd because we can't lose our used-a-blue-edge state. While this is technically allowed, it doesn't create any paths shorter than possible (in fact, the path probably gets longer this way), so for the purpose of finding the shortest path, it's okay. An alternative would be to make these cross-edges directed."
</question>

Now, a path from $s$ to $t$ containing a blue edge in the original graph is equivalent to a path in the new graph starting at $s$ (when we haven't used a blue edge) to $t'$ (when we have). Because the only way to move between the two halves of the new graph is to take a blue edge in the original graph, our new shortest path must satisfy the condition.

An example of this transformation on a small 3-vertex graph is shown below. The edges of the new graph are colored for clarity, though a BFS on this graph treats them all normally. Notice that the length-1 path from $A$ to $C$ that takes the red edge does not translate to a length-1 path from $A$ to $C'$ in the new graph because its structure enforces the blue-edge requirement.

<center>
<img src="/_static/IAP19/bfs-33.png" height="200"  />
</center>

Now, we can use our normal BFS with parent pointers to find the shortest path between any $s$ and $t'$ we choose. Now we just have to translate this path back into the context of the original graph, but luckily, reversing our transformation is the easier part. All we have to do is treat $A$ and $A'$ as just $A$, $B$ and $B'$ as just $B$, etc. In the 3-vertex example, the path $A\to B\to C'$ corresponds to $A\to B\to C$ in the original graph.

With our new and shiny algorithm fleshed out, we can analyze its runtime.

<question expression>
csq_prompt = "What is the runtime of the algorithm described above on a graph with $V$ vertices and $E$ edges? Remember to consider the cost of creating the new graph as well as the subsequent BFS. Express your answer in Theta notation as a function of $V$ and $E$.   \n\n"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = "Theta(V+E)"
csq_explanation = "We can count the number of vertices and edges in our new graph, which will tell us the time cost of creating the graph and the cost of running BFS on it. We know that for each original vertex, we add 2 vertices to our new graph, and for each original edge, we add 2 or 3 edges to our graph depending on its color. Thus, each vertex contributes $\Theta(1)$ new vertices, and each edge contributes $\Theta(1)$ new edges, so our new graph has $V'=\Theta(V)$ vertices and $E'=\Theta(E)$ edges. The BFS runs in $\Theta(V'+E')=\Theta(V+E)$ time, for a grand total of $\Theta(V+E)$, asymptotically equivalent to a BFS on the original graph."
csq_nsubmits = None
</question>

This example only introduced a binary state, but the idea can just as easily be applied to problems with an arbitrary number of states, provided that the state transitions through the graph are fully described.
