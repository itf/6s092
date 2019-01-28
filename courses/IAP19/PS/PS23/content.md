# Readings 
[Recitation notes 13](https://learning-modules.mit.edu/service/materials/groups/238004/files/439cb7b0-29b2-4afe-bbfa-d29a0910366b/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), 6.006 Fall 2018 on Stellar.

[Lecture notes 13](https://learning-modules.mit.edu/service/materials/groups/238004/files/70dd3c14-862c-4f82-bfc1-ed842259ee5e/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), 6.006 Fall 2018 on Stellar.


# Shortest paths

Bellman-Ford has the largest asymptotic runtime of the single-source shortest path algorithms covered in this course, but it makes few assumptions about the structure of the graph. For comparison, BFS requires unweighted edges, topological sort relaxation only works on acyclic graphs, and Dijkstra's requires nonnegative edge weights. Bellman-Ford only requires the graph to have no negative-weight cycles for reasons we will discuss later.

This graph compares the different SSSP algorithms we have covered and will cover in 6.s092 and 6.006, and you can find a similar graph in the lecture notes.


| SSSP Algorithm             | PSet #   | Setting                           | Runtime          |
| ---------------------------| -------- | --------------------------------- | ---------------- |
| BFS                        | 20       | $w(e) = 1$ for all $e \in E$      | $O(V+E)$         |

| Topo Sort Relaxation       | 22       | acyclic graph                     | $O(V+E)$         |

| Dijkstra                   | 24       | $w(e) > 0$ for all $e \in E$      | $O(V log V + E)$ |

| Bellman-Ford               | 23       | General graph                     | $O(VE)$          |

Let's assume for now that our graph does not contain any negative cycles in it. See [here](https://s092.xvm.mit.edu/_static/IAP19/relax6.png) for an example of a graph with a negative cycle.

The algorithm:

1. Initialize the distance of the start vertex to be $0$, and that of all other vertices to be $+\infty$.
2. Relax all edges in any order.
3. Repeat step 2 $(V-1)$ times in total.

<question expression>
csq_prompt = "What is the runtime of this algorithm in Theta notation as a function of $V$ and $E$? Remember to express in simplest asymptotic form.   \n\n"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["Theta(VE)","Theta(EV)","Theta(V*E)"]
csq_explanation = "A single edge can be relaxed in $\Theta(1)$ time. Relaxing $E$ edges $V-1$ times each is done in $\Theta(VE)$ time."
csq_nsubmits = None
csq_name = "bellman_runtime"
</question>

So why is relaxing all edges $V-1$ times necessary (why can't we relax fewer times, like in Topological Sort Relaxation?) and sufficient (how do we know we are done at the end)? Consider the following linear graph for simplicity.

<center>
<img src="/_static/IAP19/bellman-11.png" height="100"  />
</center>

<question pythonliteral>
csq_prompt = "We start Bellman-Ford on the above graph with source vertex $A$. After one round of relaxing all edges, what are the maximum (worst-case) possible distance values associated with each vertex? If there is no such maximum for a vertex, use 'inf'. Give your answer as a python list in the form $a,b,c,d$.   \n\n"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = [0,2,'inf','inf']
csq_explanation = "If edge $AB$ is the last to be relaxed, then vertices $C$ and $D$ will still have distance $\infty$ after the first relaxation. Because $A$ begins with distance $0$, relaxing $AB$ makes $B$'s distance at most $2$."
csq_name = "bellman_relax1"
</question>

<question pythonliteral>
csq_prompt = "After the second round of edge relaxation, what are the maximum (worst-case) possible distance values associated with each vertex? Give your answer in the same way as above.   \n\n"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = [0,2,-1,'inf']
csq_explanation = "Because $B$ has distance at most $2$ after the first round, $C$ has at most distance $-1$ after relaxing $BC$. $D$ can still have distance $\infty$."
csq_name = "bellman_relax2"
</question>

<question pythonliteral>
csq_prompt = "After the third round of edge relaxation, what are the maximum (worst-case) possible distance values associated with each vertex?   \n\n"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = [0,2,-1,5]
csq_explanation = "Because $C$ has distance at most $-1$ after the second round, $D$ has at most distance $5$ after relaxing $CD$."
csq_name = "bellman_relax3"
</question>

Though this example has only 1 path to each vertex, we can derive a general understanding of how Bellman-Ford finds shortest paths. The key invariant is that after $k$ relaxation passes, all shortest paths from the source node with at most $k$ edges are found. Before any relaxation, we have trivially found all $0$-edge shortest paths, which is the $0$-length path from and to the source vertex. After $1$ pass, we have found all $1$-edge shortest paths, which consist of the outgoing edges from the source.

We can prove this invariant using induction: the base case is that we have found all $0$-edge shortest paths by the $0$-th relaxation.

Now we prove the inductive step: assume that we have found all $k-1$-edge shortest paths by the $k-1$th relaxation pass, and are now on the $k$th relaxation pass. Consider the shortest path from source $s$ to some vertex $v$, which contains $k$ edges. (The squiggle edge in the diagram below represents a path with an arbitrary number of edges.) We want to show that we find this shortest path by pass $k$. Say that vertex $u$ immediately precedes $v$ in the path, so edge $uv$ is in the path. We can show with contradiction (can you think of why this is true?) that the subpath from $s$ to $u$ with $k-1$ edges must also be the shortest path between $s$ and $u$. Because of our inductive step assumption, we know that we have already found this shortest path between $s$ and $u$. Therefore, relaxing $uv$ in pass $k$ will give us the shortest path to $v$.

<center>
<img src="/_static/IAP19/bellman-12.png" height="70"  />
</center>

So relaxing the edges $V-1$ times will guarantee all shortest paths with at most $V-1$ edges. But what if the shortest path to a vertex has more than $V-1$ edges? Such a path would necessarily repeat a vertex, which means that our path contains a cycle. But we have assumed so far that our graph doesn't have negative cycles, the cycle must have nonnegative weight. By cutting out the cycle, we don't increase the total path weight, so our reduced acyclic path must be the shortest one.

<center>
<img src="/_static/IAP19/bellman-13.png" height="150"  />
</center>

Note that a few aspects of the algorithm can be adjusted to suit our needs. If we wanted to find the shortest paths from any of multiple possible source vertices, we could initialize multiple vertex distances to 0 and proceed with Bellman-Ford.

<question pythoncode>
csq_interface = 'ace'
csq_npoints = 2
csq_prompt = "Eager to advance his plans for galactic domination, Wumpus has cobbled together a starship from spare parts in EC's backyard, blasting off to explore the galaxy. The galaxy, composed of sectors connected by one-way hyperspace lanes, can be modeled as a weighted directed graph on $n$ vertices. Lanes with positive weights consume that much fuel when used, while lanes with negative weights can be harvested to increase Wumpus's fuel supply by that much. Wumpus would like to plot a course from Earth, located in sector $0$, to a station in sector $n-1$. Write an algorithm that computes a list of sectors beginning with $0$ and ending with $n-1$ describing a valid path that minimizes Wumpus's net fuel expenditure. If no such path exists, return None.<br><br>The graph will be a dictionary of adjacency lists of the form $\{u: \{v_1: w_1, v_2: w_2,\dots\}\}$ where vertex $u$ has outgoing edges to $v_1$ with weight $w_1$, $v_2$ with weight $w_2$, etc. Your algorithm should run in $O(VE)$ time. Assume no negative cycles."
csq_name = "bellman_code1"

## Define solution that will be printed to student.
csq_soln = '''def bellman(n, graph):
    edges = [(u, v, graph[u][v]) for u in graph for v in graph[u]]
    dist = [inf for i in range(n)]
    dist[0] = 0
    parent = [None for i in range(n)]
    for i in range(n - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:  ## if edge relaxed, update distance and parent
                dist[v] = dist[u] + w
                parent[v] = u
    
    if parent[n - 1] is None:
        return None

    ## reconstruct path from parent pointers
    path = []
    curr = n - 1
    while curr is not None:
        path.append(curr)
        curr = parent[curr]
    path.reverse()
    return path
'''

## Code that will be initially on the thingy
csq_initial = '''def bellman(n, graph):
    edges = [(u, v, graph[u][v]) for u in graph for v in graph[u]]
    dist = [inf for i in range(n)]  ### TODO
    parent = [None for i in range(n)]
    for i in range(n - 1):
        ###
        ### TODO
        ###
    return []
'''

from math import inf

def bellman_dist(n, graph):
    edges = [(u, v, graph[u][v]) for u in graph for v in graph[u]]
    dist = [inf for i in range(n)]
    dist[0] = 0
    for i in range(n):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                if i == n - 1:
                    return None
                dist[v] = dist[u] + w
    return dist[n - 1]

csq_code_pre = "from math import inf"

test_params = [(10, 0.3, 14, 11),
        (10, 0.8, 16, 10),
        (50, 0.1, 22, 12),
        (50, 0.6, 20, 8),
        (100, 0.047, 22, 12),
        (500, 0.0127, 25, 12)]

tests = []

for n, p, mu, sigma in test_params:
    remake = True
    while remake:
        g = {i: {} for i in range(n)}
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if cs_random.random() < p:
                    g[i][j] = int(cs_random.gauss(mu, sigma))
        dist = bellman_dist(n, g)
        remake = dist is None
    tests.append((n, g, dist))


# def is_correct(test, sol):
#     n, g, dist = test
#     if sol is None and dist == inf:
#         return True
#     if not isinstance(sol, list):
#         return False
#     return all(sol[i + 1] in g[sol[i]] for i in range(n - 1)) and sum(g[sol[i]][sol[i + 1]] for i in range(n - 1)) == dist


csq_tests = []
for i, t in enumerate(tests):

#    def check(ans, soln, i = i):
#        return is_correct(tests[i], eval(ans))
#        'check_function': check
        
    csq_tests.append({
        'code': f"""
n, graph, _ = {t}
ans = bellman(n, graph)""",
        'show_code': i < 3,
        'grade': True
    })
</question>

# Negative-weight cycles

What happens when our graph does contain a negative cycle? Consider the following graph, in which we have begun running Bellman-Ford from source vertex $A$. The current distances associated with each vertex are written beside them.

<center>
<img src="/_static/IAP19/bellman-21.png" height="200"  />
</center>

<question multiplechoice>
csq_prompt = "If we relaxed all edges another time, which vertex distances are guaranteed to be updated?\n\n"
csq_renderer = "checkbox"
csq_soln = [1, 0, 0]
csq_options =  ["$A$",
 "$B$",
 "$C$"]
csq_explanation = "We see that relaxing edge $CA$ must update vertex $A$, and no other vertices are guaranteed to update."
csq_name = "bellman_neg1"
</question>

<question multiplechoice>
csq_prompt = "If we relax all edges yet again, which vertex distances are guaranteed to be updated?\n\n"
csq_renderer = "checkbox"
csq_soln = [0, 1, 0]
csq_options =  ["$A$",
 "$B$",
 "$C$"]
csq_explanation = "Now that the distance of $A=-4$, we know that relaxing edge $AB$ must update vertex $B$."
csq_name = "bellman_neg2"
</question>

<question multiplechoice>
csq_prompt = "And if we relax again for the third time?\n\n"
csq_renderer = "checkbox"
csq_soln = [0, 0, 1]
csq_options =  ["$A$",
 "$B$",
 "$C$"]
csq_explanation = "Now that the distance of $B=-7$, we know that relaxing edge $BC$ must update vertex $C$."
csq_name = "bellman_neg3"
</question>

Now that we have effectively gone around the cycle, this brings us back to where we started except with lower vertex distances. Because traversing this negative cycle yields a net decrease in distance and can be done arbitrarily many times, the shortest distance from the source to any of these vertices is unbounded below, which we can refer to as $-\infty$.

If the presence of a negative cycle ruins our Bellman-Ford result, how do we figure out if our graph has a negative cycle?

Let's run a full Bellman-Ford on a graph, meaning that we relax all edges for $V-1$ iterations. If this graph has no negative cycles, then we have already computed the shortest paths to all vertices, so relaxing the edges will not produce any shorter distances. Thus, we can simply attempt to relax every edge one more time and conclude that a negative cycle is present if any updates were made.

<checkyourself>
We run Bellman-Ford on a graph then attempt to relax every edge one more time. If no updates were made, can we conclude that no negative cycles exist in the graph?
<showhide>
Actually, no. We can conclude that there are no negative cycles reachable from our chosen source, but a negative cycle totally isolated from the source would not be found in this way. This is because setting the distance of every unreachable vertex to $\infty$ does not allow their edges to be relaxed. If we purely wanted to detect any negative cycles in the graph, we would need to initialize every vertex distance to any finite value.<br><br>It is worth amending our previous statement here that Bellman-Ford requires a graph without negative cycles. Technically, it works so long as no negative cycles are reachable from the source.
</showhide>
</checkyourself>

Thus, running an extended Bellman-Ford with $V$ iterations on any graph either correctly returns all distances or reveals a negative cycle in the graph.

<question multiplechoice>
csq_prompt = "If a graph has a negative cycle reachable from the source, which statements can potentially describe the discrepancies between the true distances and the distances reported by an execution of Bellman-Ford on this graph?\n\n"
csq_renderer = "checkbox"
csq_soln = [1, 1, 0, 0, 0]
csq_options =  ["All reported distances are overestimates.",
 "Some reported distances are overestimates.",
 "All reported distances are correct.",
 "Some reported distances are underestimates.",
 "All reported distances are underestimates."]
csq_explanation = "Because Bellman-Ford fails to fully explore shortest paths when faced with a negative cycle, the real distances must be smaller than the reported ones. Clearly, all vertices in the negative cycle have incorrect distances, as they should be $-\infty$. Furthermore, every vertex reachable from the negative cycle should also have a distance of $-\infty$. However, not all vertices are necessarily incorrect, as the vertices unreachable from the negative cycle remain unaffected."
csq_name = "bellman_neg4"
</question>
