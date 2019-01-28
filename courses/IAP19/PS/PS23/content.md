# Readings 
Recitation notes 13, 6.006 Fall 2018 on Stellar.

Lecture notes 13, 6.006 Fall 2018 on Stellar.
# Shortest paths


Bellman-Ford has the largest asymptotic runtime of the single-source shortest path algorithms covered in this course, but it makes no assumptions about the structure of the graph. For comparison, BFS requires unweighted edges, topological sort relaxation only works on acyclic graphs, and Dijkstra's requires nonnegative edge weights.

The algorithm:

    1. Initialize the distance of the start vertex to be 0, and that of all other vertices to be $+\infty$.
    2. Relax all edges.
    3. Repeat step 2 $V-1$ times in total.

<question expression>
csq_prompt = "What is the runtime of this algorithm in Theta notation as a function of $V$ and $E$?   \n\n"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = "Theta(VE)"
csq_explanation = "A single edge can be relaxed in $\Theta(1)$ time. Relaxing $E$ edges $V-1$ times each is done in $\Theta(VE)$ time."
csq_nsubmits = None
csq_name = "bf_runtime"
</question>

So why does this work? 

<question multiplechoice>
csq_prompt = "Question?"
csq_renderer = "checkbox"
csq_soln = [1,0,0,0]
csq_options =  ['option 1',
'option 2',
'option 3',
'option 4']
csq_name="qexample1"
</question>


<question expression>
csq_prompt = "Question?"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["T(n)+O(n)", "12"]
csq_explanation = "explanation"
csq_nsubmits = None
</question>

<checkyourself>
Are you understanding?
<showhide>
yeah
</showhide>
</checkyourself>



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

