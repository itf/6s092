# Readings 
Recitation notes 11, 6.006 Fall 2018 on stellar.

Lecture notes 11, 6.006 Fall 2018 on stellar.

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
csq_name="p1"
</question>

<question multiplechoice>
csq_prompt = "Now, what do we do with the vertex `s`? We need to visit its neighbors, as long as they don't already have parents. Remember, this will follow a recursive structure: for each new vertex `v` we visit, we should be calling `depth_first` on it."
csq_renderer = "radio"
csq_soln = """```
if parent[v] = None:
	parent[v] = s
	depth_first(Adj, v)
```"""
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
csq_name="p1"
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
csq_name="p2"
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
csq_name="p3"
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
csq_name="p4"
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
csq_name="p5"
</question>

<checkyourself>
Why is it the case that the sum of all out-degrees is no more than twice the number of vertices?
<showhide>
When we count the out-degrees of all vertices, we are counting the number of edges leaving the vertex. So, when we sum over all vertices, we are summing the number of edges that leave *any* vertex, which is necesarilly the number of edges. (The reason we say no more than twice the number of vertices is that, in an undirected graph, every edge will be counted twice, since each edge technically "leaves" both end vertices.)
</showhide>
</checkyourself>

# Depth-First Search: Practice

Now it's time to try depth first search in practice! Consider the following graph. 
