# Depth-First Search: Theory
In a *depth-first search*, we travel through every vertex reachable from some start vertex *s*, and it does so by following a single path as deeply as possible before continuing to another path. 

The basic algorithm of the depth-first search is as follows: (1) Keep an array `A` of parents, where the $i$th entry will be the "parent" of a vertex. Initially, the array is full of `None`. (2) Set the parent of the start vertex, `s`, to be itself. Let `s` be our first "working vertex" `v`. (3) For a given "working vertex" `v`, find the first vertex adjacent to it that does not already have a parent, `v'`. Set its parent to be the working vertex: `A[v'] = v`. Then, make that new vertex the new working vertex: `v = v'`. (4) If, at any point, the working vertex has no adjacent, parentless vertices, backtrack to `v`'s parent: `v = A[v]` and try again.

Let's try to implement this, using a recursive structure. 
```python
depth_first(Adj, s, parent = None): 	# we start with an adjacency list and start vertex.
	if parent is None:			# how do we initialize the parent list?
		### CODE ###
	for v in Adj[s]:			# what should we do when we visit a vertex?
		### CODE ###
	return parent
```

<question multiplechoice>
csq_prompt = "If the parent list is currently `None`, that means no such list exists, and we need to initialize one. How should we do this?"
csq_renderer = "radio"
csq_soln = """```
parent = [None]*len(Adj)
parent[s] = s
```"""
csq_options =  ["""```
parent = [None]*len(Adj)
```""",
"""```
parent = [None]*len(Adj)
parent[s] = s
```""",
"""```
parent = [None]
parent[s] = s
```""",
"""```
parent = [None]*len(Adj)
parent[s] = s
for v in Adj[s]:
	parent[v] = s
```"""]
csq_explanation = "We wish to create an array with one parent per vertex, so we give it a length of `len(Adj)`, which has a length equal to the number of vertices. Nothing has a parent yet except `s`, which is its own parent."
csq_name="p1"
</question>

<question multiplechoice>
csq_prompt = "Now, what do we do with the vertex `s`? We need to visit its neighbors, as long as they don't already have parents. Remember, this will follow a recursive structure: for each new vertex `v` we visit, we should be calling `depth_first` on it."
csq_renderer = "radio"
csq_soln = """```
if parent[v] = None:
	parent[v] = s
	depth_first(Adj, v)```"""
csq_options =  ["""```
if parent[v] = None:
	parent[v] = s
```""",
"""```
depth_first(Adj, v, parent)
```""",
"""```
if parent[v] = None:
	parent[v] = s
	depth_first(Adj, v)
```""",
"""```
if parent[v] = None:
	depth_first(Adj, v, parent)
```""",
"""```
if parent[v] = None:
	parent = depth_first(Adj, v)
```"""]
csq_explanation = "First, we use the `if` statement to ensure that the vertex we consider has not already been visited. Assuming it hasn't, we want to give it a parent: our current vertex `s`. Then, we want to run a DFS on `v` to explore its subtree (hence the recursive structure). Convince yourself that this does the same as the intuitive explanation at the beginning of this section."
csq_name="p2"
</question>

<question multiplechoice>
csq_prompt ="Great! We've implemented depth first search. But so what? Depth first search can be used for many graph exploration purposes. What does this particular implementation return?"
csq_renderer = "radio"
csq_soln = 'A list of parents of vertices that can be used to construct a tree rooted at `s`'
csq_options =  ['The list of vertices reachable from `s` using only edges from the original graph',
'The number of vertices in the graph',
'The number of vertices reachable from `s`',
'A list of parents of vertices that can be used to construct a tree rooted at `s`',
'A list of vertices, ordered by when the depth-first search first reached it.']
csq_explanation = "The only information that this implementation returns is the list of parents."
csq_name="p3"
</question>

Although as written, depth-first search only returns one of the following, it can easily be made to return any of them. 

Now we turn to the big question: what's the runtime? To compute the runtime, we need to consider two things: how many times the `depth_first()` function is called, and how long it takes to execute one instance of the `depth_first()` function. 

<question expression>
csq_prompt = "Let $E$ denote the number of vertices in a graph, and $V$ denote the number of edges. Using big-O notation, how many times will we have to call on `depth_first()`? Hint: what's the maximum number of times we can call on the function for a given vertex?"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ['$O(V)$', '$Theta(V)']
csq_explanation = "We can only call `depth_first` once on per vertex: it will only be called if the vertex had no parent to start, and after it is called, it will have a parent. So we call the function at most once per vertex, or $O(V)$ times."
csq_nsubmits = None
csq_name="p4"
</question>

<question expression>
csq_prompt = "Let $E$ denote the number of vertices in a graph, and $V$ denote the number of edges. How long does it take to run a `depth_first(v)` on a vertex `s`, with out-degree $d$?"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ['$O(d)$', '$Theta(d)']
csq_explanation = "For a given vertex, the for-loop `for v in Adj[s]` will do work for each vertex adjacent to `s`. This will take an amount of work proportional to $d$."
csq_nsubmits = None
csq_name="p5"
</question>

<question expression>
csq_prompt = "Let $E$ denote the number of vertices in a graph, $V$ denote the number of edges. Using big-O notation, what is the overall runtime of the depth-first search algorithm? Two facts will be helpfull here: first, that the sum of the out-degrees of all vertices is no more than twice the number of edges, so that $$\sum_{v \in V}deg(v) = O(E),$$ and secondly, that there is an extra required runtime of $V$ to initialize the parent array."
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ['$O(V+E)$', '$Theta(V+E)$']
csq_explanation = "We need to sum the work O(d) over all vertices. By the hint, this means that the total runtime is $O(E)$. However, we need also consider the extra $O(V)$ work necesarry to just initialize the array. This gives us a total runtime of $O(V+E)$."
csq_nsubmits = None
csq_name="p6"
</question>

<checkyourself>
Why is it the case that the sum of all out-degrees is no more than twice the number of vertices?
<showhide>
When we count the out-degrees of all vertices, we are counting the number of edges leaving the vertex. So, when we sum over all vertices, we are summing the number of edges that leave *any* vertex, which is necesarilly the number of edges. (The reason we say no more than twice the number of vertices is that, in an undirected graph, every edge will be counted twice, since each edge technically "leaves" both end vertices.)
</showhide>
</checkyourself>

# Depth-First Search: Practice

Now it's time to try depth first search in practice! Consider the following graph. 

<center>
<img src="/_static/IAP19/image-here" height="200"  />
</center>

<Graph indexType="custom" height="400" width="400" nodes={[{label:0,center:{x:169.4,y:176.4}},{label:1,center:{x:223.1,y:287.2}},{label:2,center:{x:240.2,y:66.2}},{label:3,center:{x:106.7,y:67.8}},{label:4,center:{x:92.2,y:282}},{label:5,center:{x:353.7,y:296.2}},{label:"6",center:{x:302.2,y:180.2}},{label:"7",center:{x:267.8,y:399.4}}]} edges={[{source:0,target:1},{source:0,target:2},{source:0,target:3},{source:1,target:5},{source:5,target:7},{source:1,target:6},{source:2,target:6},{source:0,target:6},{source:4,target:1},{source:0,target:4}]} />

<question expression>
csq_prompt = "Assuming we visit vertices with lower values before those with higher values, and that `s` is our start vertex, in what order will we visit vertices? List vertices in order of the *last* time we visit a vertex. Your answer should be in the form $a, b, c, ...$."
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = 'n'
csq_nsubmits = None
csq_name="p7"
</question>

<center>
<img src="/_static/IAP19/image-here" height="200"  />
</center>

<question expression>
csq_prompt = "As in the last question, assume we visit vertices with lower values before those with higher values and that `s` is the start vertex. In what order will we visit vertices? List vertices in order of the *last* time we visit a vertex. Your answer should be in the form $a, b, c, ...$."
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = 'n'
csq_nsubmits = None
csq_name="p8"
</question>

For the next two questions, suppose the graph is undirected. Similarly, a *connected component* of a graph is a connected subgraph of the original graph, which is not connected to any other vertex (that is, it is the biggest connected piece possible).

<question expression>
csq_prompt = "If I wish to explore the entirety of a graph $G$ with $n$ connected components, how many times will I have to call on the `depth_first()` function? Do not use big-O notation for this question."
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = 'n'
csq_explanation = "Every time we finish exploring a connected component, `depth_first()` will terminate, and we will have to call the function again on a new connected component. This will happen $n$ times."
csq_nsubmits = None
csq_name="p9"
</question>

The linear run time of depth-first search great, but sometimes we want to do even better, given some restrictions on the structure of the graph. For instance, if we know there are only a few edges, we might be able to say that $E = O(V)$, in which case the run time is simply $O(V)$. 

<question expression>
csq_prompt = "Suppose that the entire graph is connected, so that we can reach any vertex from `s`, the start of our DFS search. What is the run time of DFS in this case?"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ['$O(E)$', '$Theta(E)$']
csq_explanation = "For every vertex in the graph to be connected, we need at least $V-1$ edges: this will create a tree that connects all vertices with the minimum number of edges. Since $E > V - 1$, we have that $V = O(E)$ and so the run time $O(V+E)$ becomes $O(V)$."
csq_nsubmits = None
csq_name="p11"
</question>

<question multiplechoice>
csq_prompt = "DFS can easily be modified to compute shortest paths from the start vertex `s` to other vertices connected to it."
csq_renderer = "radio"
csq_soln = 'False'
csq_options = ['True', 'False']
csq_explanation = "While breadth first search can do this well, depth-first search will not choose edges that minimize distance from `s`. For an example, consider the second depth-first search calculation you made in this section."
csq_name="p12"
</question>

# Topological Sort
Suppose a graph is directed and acyclic: its edges are directed and there is no way to follow the edges of the graph from a vertex back to itself.

In this case, we can define a *topological sort* on graph. A topological sort is an ordering of vertices $(v_1, v_2, ..., v_k)$ in a graph so that for every edge $(v_i, v_j)$, we have $i < j$. In other words, a directed edge from a vertex $v_i$ to another vertex $v_j$ requires $v_j$ to go after $v_i$ in the sort.

<checkyourself>
Why do we require that the graph be directed and acyclic to define a topological sort?
<showhide>
Suppose our graph had a cycle, and denote the vertices in the cycle $v_a, v_b, v_c, ..., v_a$ (since we start and end on the same vertex). Then the condition for topological sort requires that $a < b < c < ... <
a$, but it makes no sense for $a < a$. (Intuitively, a cycle means some vertex $v_a$ needs to come after itself... which is impossible.) The graph must be directed because undirected graphs are necesarrily cyclic.
</showhide>
</checkyourself>

Why is a topological sort useful? Consider the following familiar scenario: you are given a list of classes, and prerequisites for classes. For instance your set of classes might be `V = {00, 006, 854, 046, 009}` and a set of prerequisites `E = {(00,006), (00, 009), (006, 046), (046, 854)}`. You wish to determine a valid order in which to take classes. The topological sort will give you something like `(00, 006, 009, 046, 854)`, and taking classes in this order will not violate any prerequisites!

<question multiplechoice>
csq_prompt = "Which of the following are true about topological sorts for a directed acyclic graph?"
csq_renderer = "checkbox"
csq_soln = [0,1,0,1,1]
csq_options =  ['There is only one valid topological sort.',
'If edges $(a,b)$ and $(b,c)$ exist, then $a$ must come before $c$ in the topological sort.',
'If edges $(a,b)$, $(c,b)$, and $(c,a)$ exist, there is no topological sort for the graph.',
'A topological sort can be computed in the same time (asymptotically) as depth-first search.',
'If a valid topological sort exists, the graph must be acyclic.']
csq_name="p10"
</question>
