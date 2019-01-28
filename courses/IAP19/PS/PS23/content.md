# Readings 
Recitation notes 13, 6.006 Fall 2018 on Stellar.

Lecture notes 13, 6.006 Fall 2018 on Stellar.
# Shortest paths


Bellman-Ford has the largest asymptotic runtime of the single-source shortest path algorithms covered in this course, but it makes few assumptions about the structure of the graph. For comparison, BFS requires unweighted edges, topological sort relaxation only works on acyclic graphs, and Dijkstra's requires nonnegative edge weights. Bellman-Ford only requires the graph to have no negative-weight cycles for reasons we will discuss later.

The algorithm:

1. Initialize the distance of the start vertex to be 0, and that of all other vertices to be $+\infty$.
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
csq_name = "bf_runtime"
</question>

So why is relaxing all edges $V-1$ times necessary and sufficient? Consider the following linear graph for simplicity.

<center>
<img src="/_static/IAP19/bellman-11.png" height="100"  />
</center>

<question expression>
csq_prompt = "We start Bellman-Ford on the above graph with source vertex $A$. After one round of relaxing all edges, what are the maximum (worst-case) possible distance values associated with each vertex? If there is no such maximum for a vertex, use inf. Give your answer in the form $a,b,c,d$.   \n\n"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = "0,2,inf,inf"
csq_explanation = "If edge $AB$ is the last to be relaxed, then vertices $C$ and $D$ will still have distance $\infty$ after the first relaxation. Because $A$ begins with distance $0$, relaxing $AB$ makes $B$'s distance at most $2$."
csq_name = "bf_relax1"
</question>

<question expression>
csq_prompt = "After the second round of edge relaxation, what are the maximum (worst-case) possible distance values associated with each vertex? Give your answer in the same way as above.   \n\n"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = "0,2,-1,inf"
csq_explanation = "Because $B$ has distance at most $2$ after the first round, $C$ has at most distance $-1$ after relaxing $BC$. $D$ can still have distance $\infty$."
csq_name = "bf_relax2"
</question>

<question expression>
csq_prompt = "After the third round of edge relaxation, what are the maximum (worst-case) possible distance values associated with each vertex?   \n\n"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = "0,2,-1,5"
csq_explanation = "Because $C$ has distance at most $-1$ after the second round, $D$ has at most distance $5$ after relaxing $CD$."
csq_name = "bf_relax3"
</question>

Though this example has only 1 path to each vertex, we can derive a general understanding of how Bellman-Ford finds shortest paths. The key invariant is that after $k$ relaxation passes, all shortest paths with at most $k$ edges are found. Before any relaxation, we have trivially found all $0$-edge shortest paths, which is the $0$-length path to the source vertex. After $1$ pass, we have found all $1$-edge shortest paths, which consist of the outgoing edges from the source.

To show that this invariant holds after pass $k$, consider the shortest path from source $s$ to some vertex $v$, which contains $k$ edges. (The squiggle represents a path with an arbitrary number of edges.) We want to show that we find this shortest path by pass $k$. Say that vertex $u$ immediately precedes $v$ in the path, so edge $uv$ is in the path. This means that the shortest path from $s$ to $u$ is the segment of the same path that stops at $u$, which has $k-1$ edges. By pass $k-1$, we must have found this shortest path to $u$, so relaxing $uv$ in pass $k$ will give us the shortest path to $v$.

<center>
<img src="/_static/IAP19/bellman-12.png" height="70"  />
</center>

So relaxing the edges $V-1$ times will guarantee all shortest paths with at most $V-1$ edges. But what if the shortest path to a vertex has more than $V-1$ edges? Such a path would necessarily repeat a vertex, which means that our path contains a cycle. But because our graph can't have negative cycles, the cycle must have nonnegative weight. By cutting out the cycle, we don't increase the total path weight, so our reduced path must be the shortest one.

<center>
<img src="/_static/IAP19/bellman-13.png" height="150"  />
</center>

<question pythoncode>
csq_interface = 'ace'
csq_npoints = 2
csq_prompt = "Eager to advance his plans for galactic domination, Wumpus has cobbled together a starship from spare parts in EC's backyard, blasting off to explore the galaxy. The galaxy, composed of sectors connected by one-way hyperspace lanes, can be modeled as a weighted directed graph on $n$ vertices. Lanes with positive weights consume that much fuel when used, while lanes with negative weights can be harvested to increase Wumpus's fuel supply. Starting the trip with only $f$ units of fuel, Wumpus would like to know which sectors he can reach from Earth, located at sector $0$. Write an algorithm that computes a <i>set</i> of all the sectors Wumpus can reach.<br><br>The graph will be a dictionary of adjacency lists of the form $\{u: [(v_1,w_1),(v_2,w_2),\dots]\}$ where vertex $u$ has outgoing edges to $v_1$ with weight $w_1$, $v_2$ with weight $w_2$, etc. Remember that a path is valid only if Wumpus's fuel supply stays nonnegative throughout. Your algorithm should run in $O(V,E)$ time. Assume no negative cycles.<br>"
csq_name = "bellman_code1"

## Define solution that will be printed to student.
csq_soln = '''def bellman(n, f, graph):
    edges = [(u, v, w) for u in graph for v, w in graph[u]]
    dist = [f + 1 for i in range(n)]
    dist[0] = 0
    for i in range(n - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                # setting parent pointers here will allow for path reconstruction
    return {i for i in range(n) if dist[i] <= f}
'''

## Code that will be initially on the thingy
csq_initial = '''def bellman(n, f, graph):
    edges = [] ### TODO
    dist = [] ### TODO
    for i in range(n - 1):
        ###
        ### TODO
        ###
    return {0}
'''

from math import inf

def bellman_dist(n, graph):
    edges = [(u, v, w) for u in graph for v, w in graph[u]]
    dist = [inf for i in range(n)]
    dist[0] = 0
    for i in range(n):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                if i == n - 1:
                    return None
                dist[v] = dist[u] + w
    return dist

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
        g = {i: [] for i in range(n)}
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if cs_random.random() < p:
                    g[i].append((j, int(cs_random.gauss(mu, sigma))))
        dist = bellman_dist(n, g)
        remake = dist is None
    f = cs_random.choice([x for x in dist if x != inf and x > 0])
    tests.append((n, f, g))


csq_tests = []
for i, t in enumerate(tests):

    def check(ans, soln, i = i):
        return is_correct(tests[i], eval(ans))
        
    csq_tests.append({
        'code': f"""
n, f, graph = {t}
ans = bellman(n, f, graph)""",
        'show_code': i < 3,
        'grade': True
    })
</question>

# Negative-weight cycles

