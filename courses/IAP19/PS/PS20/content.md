# Readings 
Recitation notes 10, 6.006 Fall 2018 on stellar.

Lecture notes 10, 6.006 Fall 2018 on stellar.
# Breadth First Search


<question multiplechoice>
csq_prompt = "Which of the following sequences of vertices could be produced by running a breadth-first search on the graph below starting at $A$?\n\n"
csq_renderer = "checkbox"
csq_soln = [0, 1, 0]
csq_options =  ['$[A, B, C, D]$',
 '$[A, D, B, C]$',
 '$[B, A, C, D]$']
csq_explanation = 'Because we begin at $A$, our BFS should visit its neighbors $B$ and $D$ before visiting $C$. Also, a BFS which starts at $A$ should visit $A$ first.'
</question>


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
csq_prompt = "Consider a graph with $V$ vertices in which each vertex has degree at most 10. (Recall that the degree of vertex $v$ is the number of edges incident to $v$.) What is the time complexity of a breadth-first search on this graph?\n\n"
csq_renderer = "radio"
csq_soln = [1, 0, 0]
csq_options =  ['$\Theta(V)$',
 '$\Theta(V\log V)$',
 '$\Theta(V^2)$']
csq_explanation = 'A useful property of graphs is that the sum of its vertex degrees is double the number of edges. (One way to think about this is that each degree counts an edge from one of its two endpoints.) The degree sum is $\le 10V$, so our edge count is $E=O(V)$. BFS runs in $\Theta(V+E)$ time, which simplifies to $\Theta(V)$ after our substitution.'
</question>


<question pythoncode>
csq_interface = 'ace'
csq_prompt = 'Closest k vertices in a graph, will flesh out with riveting story.'

## Define solution that will be printed to student.
csq_soln = '''
def closestK(n, k, graph): 
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
csq_initial = '''
def closestK(n, k, graph):
    closest = [i for i in range(k)]
    return closest
'''

def bfs_dist_sets(n, k, g):
    visited = [False for i in range(n)]
    parent = [None for i in range(n)]
    queue = [0]
    last_v = None
    count = 0
    head = 0  # index of queue head, increments when we pop off the queue
    while count < khead < len(queue):
        v = queue[head]
        head += 1
        if visited[v]:
            continue
        closest.append(v)
        visited[v] = True
        count += 1
        if count == k and last_v is not None:
            last_v = v
        for w in g[v]:
            if not visited[w]:
                queue.append(w)
                if parent[w] is None:
                    parent[w] = v

    dists = [n for i in range(n)]
    dists[0] = 0
    for i in range(n):
        if parent[i] is not None:
            dists[i] = dists[parent[i]] + 1

    max_dist = dists[last_v]
    must_have = {i for i in range(n) if dists[i] < max_dist}
    can_have = {i for i in range(n) if dists[i] <= max_dist}
    return (must_have, can_have)

test_params = [(10, 5, 0.25),
         (50, 30, 0.08),
         (100, 60, 0.06),
         (300, 120, 0.02)]

tests = []

for n, k, p in test_params:
    g = {i: [] for i in range(n)}
    for i in range(n):
        for j in range(i + 1, n):
            if cs_random.random() < p:
                g[i].append(j)
                g[j].append(i)
    tests.append((n, k, g))


def is_correct(test, sol):
    return True
    if not isinstance(sol, list):
        return False
    sol = set(sol)
    n, k, g = test
    if len(sol) != k:
        return False
    must_have, can_have = bfs_dist_sets(n, k, g)
    return must_have < sol and sol < can_have


csq_tests = []
for i, t in enumerate(tests):

    def check(ans, soln, i = i):
        return is_correct(tests[i], eval(ans))
        
    csq_tests.append({
        'code': f"""
n, k, g = {t}
ans = closestK(n, k, g)""",
        'check_function': check
    })

</question> 
