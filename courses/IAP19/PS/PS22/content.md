# Readings 
Recitation notes 12, 6.006 Fall 2018 on stellar.


<style>

.dark_word {
  -webkit-animation: dark_word 2s steps(10) alternate infinite;
          animation: dark_word 2s steps(10) alternate infinite;
   text-shadow: -1px 0px 0px transparent;
}

@-webkit-keyframes dark_word {
  to {
    text-shadow: 1px 0px 3px black;
  }
}
</style>



# Topological Sort Relaxation


<question multiplechoice>
csq_prompt = """Suppose we have the following graph

```
(A) -> (B)
```
Which of the following is true, when using topological order?
"""
csq_renderer = "checkbox"
csq_soln = [1,0,0,1]
csq_options =  ['$A < B$',
'$B < A$',
'**not** $(A  < B)$',
'**not** $(B  < A)$']
csq_explanation = "By the definition of topological sort"
</question>


<question multiplechoice>
csq_prompt = """Suppose we have the following graph

```
(C) <- (A) -> (B)
```
Which of the following is true, when using topological order?
"""
csq_renderer = "checkbox"
csq_soln = [0,0,1,1]
csq_options =  ['$C < B$',
'$B < C$',
'**not** $(C  < B)$',
'**not** $(B  < C)$']
csq_explanation = "B and C and not comparable"
</question>




<question expression>
csq_prompt = """What is the run-time of topological-sort relaxation in terms of V and E?

 """
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["O(V+E)", "Theta(V+E)", "Theta(V+E,w)", "O(V+E,w)"]
csq_explanation = "Same run-time as dfs"
csq_nsubmits = None
</question>

<checkyourself>
Why does calculating topological sort by reversing the order of the finished nodes in a DFS work?
<showhide>
Because, if we can reach node A from node B, dfs will finish visiting node A before node B. So node B will appear in the reversed list before node A.
</showhide>
</checkyourself>


<checkyourself>
Why does topological sort relaxation works?
<showhide>
Because we are guaranteed to have relaxed all the edges of the shortest path in order
</showhide>
</checkyourself>

## Coding topological sort relaxation

<python>
   # tutor.init_random()
</python>
<question pythoncode>
csq_interface = 'ace'
csq_prompt = """
<span class = "dark_word">Wumpus</span>, tired of living in a cave with 20 rooms, has built an underground lair. A young adventurous humans trying to slay the <span class = "dark_word">evil</span> Wumpus decided to explode his lair! 

Now Wumpus has to escape! Help find the shortest path from where Wumpus is to the surface! Since the lair is crumbling down into a bottomless pit, Wumpus will only go from a cave to another if the depth of the following cave is shallower than that of the previous one.

You are given a list of nodes (indexed from 0 to n-1), and an adjacency list of edges. Since the terrible Wumpus only goes from a room to a higher room, you know that the graph contains no cycles.

You have to write a function, `topo_sort_relaxation(nodes, edges, wumpus, freedom)`, which takes as input the list of nodes, an adjacency list of edges, the location of wumpus, and the location of the freedom, and it returns the shortest distance to freedom, followed by the path to freedom. If there is no path, return (inf, [])
"""

## Define solution that will be printed to student.
csq_soln = """
def topo_sort(nodes, edges):
    visited = set()
    l=[]
    def dfs(node):
        visited.add(node)
        for index, weight in edges[node]:
            if not index in visited:
                dfs(index)
        l.append(node)
        
    for i in nodes:
        if i not in visited:
            dfs(i)
    l.reverse()
    return l

def topo_sort_relaxation(nodes, edges, wumpus, freedom):
    topo_order = topo_sort(nodes, edges)
    distances = [inf for n in range(len(nodes))]
    distances[wumpus] = 0
    parents = [None]*len(nodes)
    parents[wumpus] = wumpus
    def relaxNode(n1):
        for n2, weight in edges[n1]:
            if distances[n1] + weight < distances[n2]:
                distances[n2] = distances[n1] + weight
                parents[n2] = n1
    for i in topo_order:
        relaxNode(i)
    path = []
    if distances[freedom] != inf:
        x = freedom
        while x != wumpus:
            path.append(x)
            x = parents[x]
        path.append(wumpus)
    path.reverse()
    return distances[freedom], path
"""

## Code that will be initially on the thingy
csq_initial = """
#Example initial code. Feel free to rewrite it.

# do topo sort
def topo_sort(nodes, edges):
    visited = set()
    l=[]
    def dfs(node):
        for x in nodes:
            l.append(x)
    l.reverse()
    return l

# do toposort relaxation
def topo_sort_relaxation(nodes, edges, wumpus, freedom):
    topo_order = topo_sort(nodes, edges)
    distances = [inf for n in range(len(nodes))]
    distances[wumpus] = 0
    path = [wumpus, freedom]
    def relaxNode(n1):
        for n2, weight in edges[n1]:
            pass
    for node in topo_order:
        relaxNode(node)
    return distances[freedom], path
"""
csq_name= "wumpustopo"

## Code that will be written before the user code as well as solution
## Particularly useful for defining classes and things that we don't want the user to modify
## For example, define a DFS function.
csq_code_pre = "from math import inf"


## Code that will be written after the user code as well as solution code
## Seems quite useless to me.
csq_code_post = ""



## Sandbox options to block libraries or decide how long to run thingy
csq_sandbox_options = {
    'BADIMPORT': ['lib601', 'numpy', 'scipy', 'matplotlib'], 
    'CLOCKTIME': 0.36, 
    # 'CPUTIME': 0.36, 
    'MEMORY':1e9
}


## Now we define helper functions
csq_npoints = 4
tests = [(4, True), (10, True), (20, True), (30, True), (100, True), (300, True), (50, False), (500, True), (1000, True)]

from math import log
from math import inf
random = cs_random.random

def generate_dag(n, sparse = True):
    if sparse:
        epsilon = log(n)/n * 1.1
        probability = log(n)/n + epsilon
    else:
        probability = 0.6
    nodes = [x for x in range(n)]
    height = [random() for x in range(n)]
    edges = []
    gedges = []

    for x in range(n):
        xedges = []
        for y in range(n):
            if random() <= probability and height[x] < height[y]:
                xedges.append((y,random()*20 + (height[y]-height[x])**3*1000))
        edges.append(xedges)

    wumpus = min(enumerate(height), key = lambda x: x[1])[0]
    freedom = max(enumerate(height), key = lambda x: x[1])[0]
    return (nodes, edges, wumpus, freedom)

full_tests = [generate_dag(*x) for x in tests]

## Now we need to write csq_tests, which defines what code to run
## As well as how to test it. 
## Each csq_tests is a dictionary of things (code, check, etc)

## We need to define the key code, which returns a string that will be evaluated with both the user code as well as our solution.
## Code should define a string called ans, which is what will be tested.

## We also define the key check_function, which is a function that takes escaped ans (a string, usually you will want to eval it.) from running user code, ans from running the solution, and i(index of the test), and then returns True or False.

csq_tests = []
for i, t in enumerate(full_tests):
    csq_tests.append({
        'code': f"""
nodes, edges, wumpus, freedom = {t}
ans = topo_sort_relaxation(nodes, edges, wumpus, freedom)
""" ,
        'show_code': i < 4,
        'grade': True,
    })

</question> 

