# Readings

[Recitation 10](https://learning-modules.mit.edu/service/materials/groups/238004/files/fb806d51-1a22-4a1c-b388-33211a880b42/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), First part of notes on Graphs and Graph Representations, 6.006 Fall 2018

[Lecture 10](https://learning-modules.mit.edu/service/materials/groups/238004/files/5f6a6fa2-26f7-4791-8e6e-2246ab4a4d83/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), First part before Breadth-First Search, 6.006 Fall 2018

[Recitation 11](https://learning-modules.mit.edu/service/materials/groups/238004/files/b3fc7631-d76e-48c3-85a5-00d10b81e70c/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), Depth-First Search, 6.006 Fall 2018

# Depth-First Search: Theory

In *depth-first search*, we travel through every vertex reachable from some start vertex *s*. We do so by following a single path as deeply as possible before continuing to another path. 

The basic algorithm of the depth-first search is as follows:

1. Keep an array `A` of parents, where the $i$th entry will be the "parent" of a vertex. Initially, the array is full of `None`.

2. Set the parent of the start vertex, `s`, to be itself. Let `s` be our first "working vertex" `v`.

3. For a given "working vertex" `v`, find the first vertex adjacent to it that has not been visited yet (and therefore does not have a parent), `v'`. Set its parent to be the working vertex: `A[v'] = v`. Then, make that new vertex the new working vertex: `v = v'`.

4. If, at any point, the working vertex has no adjacent, parentless vertices, backtrack to `v`'s parent: `v = A[v]` and try again.

Let's try to implement this, using a recursive structure. 
```python
depth_first(Adj, s, parent = None): 	# we start with an adjacency list and start vertex.
	if parent is None:			        # we initialize the parent list
		### PART ONE ###
	for v in Adj[s]:			        # we visit all vertices adjacent to s
		### PART TWO ###
	return parent
```

<question multiplechoice>
csq_prompt = "If the parent list is currently `None`, that means no such list exists. What code should we insert into `PART ONE` to initialize our parent list?"
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
</question>

<question multiplechoice>
csq_prompt = "Now, what do we do with the vertex `s`? We need to visit any neighboring nodes that haven't been visited yet. Choose the section of code that we should be inserting into `PART TWO` to accomplish this. Remember, this will follow a recursive structure: for each new vertex `v` we visit, we should be calling `depth_first` on it."
csq_renderer = "radio"
csq_soln = """```
if parent[v] = None:
	parent[v] = s
	depth_first(Adj, v, parent)
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
	depth_first(Adj, v, parent)
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
</question>

<question multiplechoice>
csq_prompt ="Great! We now have an implemention for depth first search. Depth first search can be useful for many graph exploration algorithms. What does this particular implementation return?"
csq_renderer = "radio"
csq_soln = 'A list of parents of vertices that can be used to construct a tree rooted at `s`'
csq_options =  ['The list of vertices reachable from `s` using only edges from the original graph',
'The number of vertices in the graph',
'The number of vertices reachable from `s`',
'A list of parents of vertices that can be used to construct a tree rooted at `s`',
'A list of vertices, ordered by when the depth-first search first reached it.']
csq_explanation = "The only information that this implementation returns is the list of parents."
</question>

Although as written, depth-first search only returns one of the following, it can easily be made to return any of them. 

Now we turn to the big question: what's the runtime? To compute the runtime, we need to consider two things: how many times the `depth_first()` function is called, and how long it takes to execute one instance of the `depth_first()` function. 

<question expression>
csq_prompt = "Let $E$ denote the number of vertices in a graph, and $V$ denote the number of edges. Using big-O notation, how many times will we have to call on `depth_first()`? Hint: what's the maximum number of times we can call on the function for a given vertex?"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ['O(V)', 'Theta(V)']
csq_explanation = "We can only call `depth_first` once on per vertex: it will only be called if the vertex had no parent to start, and after it is called, it will have a parent. So we call the function at most once per vertex, or $O(V)$ times."
csq_nsubmits = None
</question>

<question expression>
csq_prompt = "Let $E$ denote the number of vertices in a graph, and $V$ denote the number of edges. How long does it take to run a `depth_first(v)` on a vertex `s`, with out-degree $d$?"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ['O(d)', 'Theta(d)']
csq_explanation = "For a given vertex, the for-loop `for v in Adj[s]` will do work for each vertex adjacent to `s`. This will take an amount of work proportional to $d$."
csq_nsubmits = None
</question>

<question expression>
csq_prompt = "Let $E$ denote the number of vertices in a graph, $V$ denote the number of edges. Using big-O notation, what is the overall runtime of the depth-first search algorithm? Two facts will be helpful here: first, that the sum of the out-degrees of all vertices is no more than twice the number of edges, so that $$\sum_{v \in V}deg(v) = O(E),$$ and secondly, that there is an extra required runtime of $V$ to initialize the parent array."
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ['O(V+E)', 'Theta(V+E)']
csq_explanation = "We need to sum the work O(d) over all vertices. By the hint, this means that the total runtime is $O(E)$. However, we need also consider the extra $O(V)$ work necesarry to just initialize the array. This gives us a total runtime of $O(V+E)$."
csq_nsubmits = None
</question>

<checkyourself>
Why is it the case that the sum of all out-degrees is no more than twice the number of vertices?
<showhide>
When we count the out-degrees of all vertices, we are counting the number of edges leaving the vertex. So, when we sum over all vertices, we are summing the number of edges that leave *any* vertex, which is necessarily the number of edges. (The reason we say no more than twice the number of vertices is that, in an undirected graph, every edge will be counted twice, since each edge technically "leaves" both end vertices.)
</showhide>
</checkyourself>

# Depth-First Search: Practice

Now it's time to try depth first search in practice! Consider the following graph. 

<center>
<img src="/_static/IAP19/dfs-1.png" height="250"  />
</center>

<question expression>
csq_prompt = "Assuming we visit vertices with lower values before those with higher values, and that $0$ is our start vertex, in what order will we visit vertices? List vertices in order of when `dfs` on that vertex returns. (i.e. $0$ will appear *last* on your list). You might not use all vertices. Your answer should be a single string, such as $1230$."
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = '75612340'
csq_nsubmits = None
</question>

<center>
<img src="/_static/IAP19/dfs-2.png" height="250"  />
</center>

<question expression>
csq_prompt = "As in the last question, assume we visit vertices with lower values before those with higher values and that $0$ is the start vertex. In what order will we visit vertices for this graph? List vertices in order of when `dfs` on that vertex returns. You might not use all vertices. Your answer should be a single string, such as $1230$."
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = '241560'
csq_nsubmits = None
</question>

For the next two questions, suppose the graph is undirected. We define a *connected component* of an undirected graph to be the set of all vertices in the original graph that are reachable by a path to a single vertex in that graph.

<question expression>
csq_prompt = "If I wish to explore the entirety of a graph $G$ with $n$ connected components, how many times will I have to call on the `depth_first()` function? Give an exact answer, i.e. do not use big-O notation for this question."
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = 'n'
csq_explanation = "Every time we finish exploring a connected component, `depth_first()` will terminate, and we will have to call the function again on a new connected component. This will happen $n$ times."
csq_nsubmits = None
</question>

Because graphs are represented as $G = (V,E)$, we say that the run-time of depth-first search is linear in the size of the graph, in $V$ and $E$. When we don't have any other information about the graph, we need to include both the $V$ and $E$ because they are independent.

<question multiplechoice>
csq_prompt = "What are valid relationships between $V$ and $E$?"
csq_soln = [1,1,1,1,0]
csq_renderer = "checkbox"
csq_options = ["$E = \\Theta(1)$",
               "$E = \\Theta(V)$",
               "$E = \\Theta(V log(v))$",
               "$E = \\Theta(V^2)$",
               "$E = \\Theta(V^3)$"]
csq_nsubmits = 3
</question>

We may be able to simplify the run-time for depth-first search if we know the relationship between $V$ and $E$. For instance, if we know there are less edges than vertices, we would be able to say that $E = O(V)$. We can then simplify the run-time of DFS to simply be $O(V)$. 

<question expression>
csq_prompt = "Suppose that the entire graph is connected, so that we can reach any vertex from `s`, the start of our DFS search. What is the run time of DFS in this case?"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ['O(E)', 'Theta(E)', 'theta(E)']
csq_explanation = "For every vertex in the graph to be connected, we need at least $V-1$ edges: this will create a tree that connects all vertices with the minimum number of edges. Since $E > V - 1$, we have that $V = O(E)$ and so the run time $O(V+E)$ becomes $O(V)$."
csq_nsubmits = None
</question>

<question multiplechoice>
csq_prompt = "DFS can easily be modified to compute shortest paths from the start vertex `s` to other vertices connected to it."
csq_renderer = "radio"
csq_soln = 'False'
csq_options = ['True', 'False']
csq_explanation = "While breadth first search can do this well, depth-first search will not choose edges that minimize distance from `s`. For an example, consider the first depth-first search calculation you made in this section: it returns a tree with the edges $(0,1)$ and $(1,6)$, but it would be more efficient to reach $6$ via the edge $(0,6)$."
csq_nsubmits = 1
</question>

# Topological Sort
Suppose a graph $G = (V, E)$ with $k$ vertices is directed and acyclic. When we say a graph is acyclic, that means there is no way to follow the edges of the graph from a vertex back to itself.

Then we can define a *topological sort* on this graph. A topological sort is an ordering of vertices $(v_1, v_2, ..., v_k)$ in a graph so that for every edge $(v_i, v_j) \in E$, $i < j$ in the topological sort ordering. In other words, if there exists a directed edge from a vertex $v_i$ to another vertex $v_j$, then $v_i$ will go before $v_j$ in the sort.


<center>
<img src="/_static/IAP19/dfs-1.png" height="250"  />
</center>

<question multiplechoice>
csq_prompt = "Let's go back to this graph we saw earlier. What are some valid topological sorts of the vertices in this graph?"
csq_renderer = "checkbox"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = [1,0,1,0]
csq_options = ['04321657', '01234657', '04126573', '01234567']
csq_explanation = "If the edge (u,v) exists, then u must appear before v in the topological sort"
csq_nsubmits = 3
</question>

Topological sort is often associated with DFS because there is an easy way to derive a valid topological sort on a graph: run Full DFS on a graph and order the vertices by when DFS returns on each of them. Then the reverse of the resulting list of vertices is a valid topological sort.

<center>
<img src="/_static/IAP19/dfs-2.png" height="250"  />
</center>

<question multiplechoice>
csq_prompt = "What about this graph?"
csq_renderer = "checkbox"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = [1,0,0,0]
csq_soln = '241560'
csq_options = ['3025614', '065142', '315', '0562143']
csq_nsubmits = 3
csq_explanation = "We include every vertex because we're running a Full DFS."
</question>

<checkyourself>
Why do we require that the graph be acyclic to define a topological sort?
<showhide>
Suppose our graph had a cycle, and denote the vertices in the cycle $v_a, v_b, v_c, ..., v_a$ (since we start and end on the same vertex). Then the condition for topological sort requires that $a < b < c < ... <
a$, but it makes no sense for $a < a$. (Intuitively, a cycle means some vertex $v_a$ needs to come after itself... which is impossible.) The graph must be directed because undirected graphs are necessarily cyclic.
</showhide>
</checkyourself>

<question pythonliteral>
csq_prompt = "You have an undirected graph with three nodes. I tell you that the graph has a cycle. What is the minimum possible number of edges in this graph?"
csq_soln = 1
csq_nsubmits = 3
</question>

Why is a topological sort useful?

Consider the following problem: you are given a list of classes `V = {00, 006, 854, 046, 009}` and a set of prerequisites `E = {(00,006), (00, 009), (006, 046), (046, 854)}`, where each edge `(u,v)` means that `u` is a mandatory prerequisite class for `v`. You're taking things slowly, so you're only taking one class at a time. Describe an algorithm to find the order in which you should take these classes to make sure you take all the prereqs first.

The solution is to use topological sort! Topological sort ensures that if an edge `(u,v)` exists, then `u` will come before `v` in the sort, which is exactly what we need here. Topological sort on this graph will return the list of classes `(00, 006, 009, 046, 854)`, and taking classes in this order will not violate any prerequisites.

<question multiplechoice>
csq_prompt = "Which of the following are true about topological sorts for a directed acyclic graph?"
csq_renderer = "checkbox"
csq_soln = [0,1,0,1,1]
csq_options =  ['There is only one valid topological sort.',
'If edges $(a,b)$ and $(b,c)$ exist, then $a$ must come before $c$ in the topological sort.',
'If edges $(a,b)$, $(c,b)$, and $(c,a)$ exist, there is no topological sort for the graph.',
'A topological sort can be computed in the same time (asymptotically) as depth-first search.',
'If a valid topological sort exists, the graph must be acyclic.']
</question>
