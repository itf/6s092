# Readings 
[Recitation notes 14](https://learning-modules.mit.edu/service/materials/groups/238004/files/b7106e72-c013-47e4-a483-894f060f6743/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), 6.006 Fall 2018 on Stellar.

[Lecture notes 14](https://learning-modules.mit.edu/service/materials/groups/238004/files/3168e756-f6d5-45f8-b139-3c2b30399194/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), 6.006 Fall 2018 on Stellar.


# Understanding the Algorithm

As mentioned in [PS23](https://s092.xvm.mit.edu/IAP19/PS/PS23), Dijkstra's offers an improved asymptotic runtime over Bellman-Ford for graphs that have nonnegative edge weights. This property allows the algorithm to efficiently determine an order in which to relax every edge only once to compute shortest paths, even when the graph contains cycles.

One way to think about Dijkstra's is that each edge in the graph is a pipe, and the source node is the faucet. The amount of time that it takes for water to travel through a pipe is proportional to the length of the pipe (the weight of the edge). We open the faucet, and keep track of when water reaches each of those nodes.

Check out this [visualization](https://codepen.io/ZacharyAbel/pen/xyNoWE) (written up by Zachary Abel) for what Dijkstra's might look like on a graph where the edge weights are the lengths of the edges.

Seems intuitive enough: but how do we actually translate this into code? Though the behind it concept may seem simple, Dijkstra's is a little trickier to implement than the other SSSP algorithms we have seen so far, although like Topological Sort Relaxation and Bellman-Ford, it uses the relaxation framework. Integral to the implementation of Dijkstra's is the concept of a priority queue which supports the following operations:

* `build`: Builds a priority queue of the nodes keyed by the estimated distance so far from the source
* `del_min`: Removes and returns a node from the priority queue with the smallest key
* `dec_key`: Decreases the key value of a node in the priority queue

The key differences between all of the different relaxation algorithms (Topological Sort Relaxation, Bellman-Ford, Dijkstra's) that we have seen so far is that they perform the relaxation in different orders. Topological Sort Relaxation performs the relaxations in the order given to us by the topological sort on the vertices. Bellman-Ford does not enforce any particular order, but *does* require that we relax every edge in the graph once before repeating. Dijkstra's algorithm will relax the edges in the order given by this priority queue.

More specifically, from the 6.006 recitation notes linked above: "Dijkstra’s algorithm repeatedly relax[es] edges from a vertex whose minimum weight path estimate is smallest among vertices whose out-going edges have not yet been relaxed." The key invariant of Dijkstra's is that when we pop a vertex off of the priority queue using `del_min`, the distance estimate for that vertex is the correct shortest distance. So at any given time, the nodes for which we are trying to find the shortest distances for are all contained in the progressively shrinking priority queue.


# A Simple Example of Dijkstra's algorithm

Let's try to get a better understanding of what that means by running Dijkstra's on the graph below, from source node `s`.

<center>
<img src="/_static/IAP19/dijkstra1.png" height="210" />
</center>

We initialize distance estimates:

$\delta[s, s] = 0$

$\delta[s, a] = \infty$

$\delta[s, b] = \infty$

<question multiplechoice>
csq_prompt = "For now, let's represent our priority queue to be a list of all the vertices keyed by estimated distance so far from the source, sorted in increasing distance. For example, a valid priority queue could be `[(10, 'a'), (20, 'b'), (30, 's')]`. What could the priority queue look like right now for the graph above?"
csq_renderer = 'checkbox'
csq_soln = [0,0,1,1,0]
csq_options = ["""`[(0, 's'), (1, 'a'), (2, 'b')]`""",
"""`[(0, 's'), (1, 'a'), (3, 'b')]`""",
"""`[(0, 's'), ('inf', 'a'), ('inf', 'b')]`""",
"""`[(0, 's'), ('inf', 'b'), ('inf', 'a')]`""",
"""`[('inf', 'a'), ('inf', 'b'), ('inf', 's')]`"""]
csq_explanation = "We start out with a distance of $0$ from `s` to itself, and we don't know anything about `a` or `b` so we set them to be $\\infty$."
</question>

Now we perform `del_min` and we pop off the node with the smallest estimated distance from the priority queue. We then relax every outgoing edge from that node, and update the keys in the priority queue accordingly using `dec_key`.

<question multiplechoice>
csq_prompt = "For which of these nodes would we update the keys after one iteration of this?"
csq_renderer = 'checkbox'
csq_soln = [1, 1, 0]
csq_options = ["`a`", "`b`", "`s`"]
csq_explanation = "We pop off `s`, so we relax the edges `(s, a)` and `(s, b)`. Because we successfully reduce the estimated distances for `a` and `b`, we use `dec_key` to decrease their keys in the priority queue."
</question>

<question pythonliteral>
csq_prompt = "Now what does the priority queue look like? Express your answer as a Python list sorted in increasing distance, in the same format that we used above."
csq_soln = [(1, 'a'), (3, 'b')]
csq_explanation = "We have only relaxed edges `(s, a)` and `(s, b)` so far, so our distance estimates for them are based off of those two edges only."
</question>

<checkyourself>
Our next step is to pop off the node `a` from the priority queue and repeat the process. Why can't we pop off `b`?
<showhide>
Our priority queue interface only supports removing the element with the smallest key, so we would have to remove `(1, 'a')`. More importantly, this would break our invariant that we have the correct distance estimates for any vertices popped off of the Priority Queue. As we can see, the correct shortest distance from `s` to `b` is $2$.
</showhide>
</checkyourself>

<question pythonliteral>
csq_prompt = "We pop off `a` and relax all outgoing edges from `a`. Now what would our priority queue look like? Use the same format as above."
csq_soln = [(2, 'b')]
csq_explanation = "We relax the edge `(a, b)`, which leads to a distance estimate of $2$ for `b`."
</question>

Finally we pop off the last element in the priority queue. Confirm for yourself that the distances we found were all indeed the correct shortest distances from `s`.

# A More Complicated Example

Now we will try to run Dijkstra's algorithm starting at source node `s` on this slightly more complicated graph.

<center>
<img src="/_static/IAP19/dijkstra2.png" height="210" />
</center>

<question expression>
csq_prompt = "The order in which nodes get popped off of the priority queue is also in order of increasing shortest distances. Based on that, in what order would nodes get popped off here? Express as a string of letters, like sabcd."
csq_soln = ["sbcda", "sbdca"]
csq_explanation = "Shortest distances of nodes $(s, b, c, d, a)$ are $(0, 1, 3, 3, 100)$."
</question>

<question pythonliteral>
csq_prompt = "We perform an iteration of Dijkstra's (we run `del_min`, relax all of the outgoing edges from that node, and then perform `dec_key` for each of those vertices). What does the priority queue look like now? Express your answer as a Python list, use the format from above. Use 'inf' if the distance estimate is $\\infty$. \n\n"
csq_soln = [(1, 'b'), (4, 'c'), (100, 'a'), ('inf', 'd')]
csq_explanation = "We relax all of the outgoing edges from `s`, which are `(s,a)`, `(s,b)` and `(s,c)`."
</question>

<question pythonliteral>
csq_prompt = "We repeat this step again: what is the priority queue now?"
csq_soln = [(3, 'c'), (100, 'a'), ('inf', 'd')]
csq_explanation = "We relax all of the outgoing edges from `b`, including `(b,a)`. But this doesn't decrease our minimum distance estimate for `a`, so we don't change it."
</question>

<question pythonliteral>
csq_prompt = "We repeat this process for a third time: what is the priority queue now?"
csq_soln = [(3, 'd'), (100, 'a')]
csq_explanation = "We relax `(c, d)`."
</question>

Finally, we only have one node left. By definition, this is the minimum distance in the priority queue, so we pop it off and then we are done. Does this match the answer that you gave for the order that you predicted nodes would be popped off?

# Evaluating runtime

Because Dijkstra's algorithm heavily relies on those three priority queue operations, it makes sense that the runtime of Dijkstra's also largely relies upon the implementation of the priority queue. Let's analyze the runtime of the algorithm when implemented with two different implementations: a min-heap priority queue (kind of like the one covered in PS15) and a Fibonacci heap priority queue (we treat this data structure as a black box in 6.s092 or 6.006, but you can learn more about it [here](https://www.cs.princeton.edu/~wayne/teaching/fibonacci-heap.pdf)).

| Implementation of PQ    | Create with $n$ elements | Delete/return min | Decrease key        |
| ----------------------  | ------------------------ | ----------------- | ------------        |
| Min-heap                | $O(n \log n)$            | $O(\log n)$       | $O(\log n)$         |
| Fibonacci heap          | $O(n)$                   | $O(\log n)$       | $O(1)$ amortized    |

<question expression>
csq_prompt = "Every iteration of Dijkstra will remove the vertex with minimum distance from our priority queue. How many times will we perform the `del_min` operation on a graph with $V$ vertices and $E$ edges? Answer with an exact expression."
csq_soln = ["V", "V-1"]
csq_explanation = "We are done when we pop off all of the vertices from the priority queue, and we never add vertices back onto the queue. Because your implementation can start by not including the start vertex (which trivially has the shortest path from itself) in the priority queue, $V-1$ is also an acceptable answer."
</question>

<question expression>
csq_prompt = "After we remove the vertex with minimum distance, we relax all of the outgoing edges from that vertex and we run `dec_min` on nodes that need to be updated. At most how many times could we run `dec_min` on a directed graph with $V$ vertices and $E$ edges? Answer with an exact expression."
csq_soln = ["E"]
csq_explanation = "We relax at most once on every edge. Every edge originates from one node, and we only ever update a node's distance after relaxing an edge that ends there."
</question>

<question multiplechoice>
csq_prompt = "What is the maximum number of times we could run `dec_min` on an undirected graph with $V$ vertices and $E$ edges?"
csq_renderer = "radio"
csq_soln = "$E$"
csq_options = ["$E$", "$2E$", "$V$", "$V + 2E$", "Undefined because any undirected graph with $>1$ edges will contain a cycle"]
csq_explanation = "Dijkstra can be run with cycles; that's actually a requirement for Topological Sort Relaxation. Even though we have $2E$ edges if we convert this back into a directed graph, we can only perform `dec_min` if the end-node of the edge is still contained in the priority queue. If we pop off `u` using `del_min`, causing us to relax some edge `(u, v)`, then we may call `dec_min(v)`. But we will never call `dec_min(u)` because we have already removed `u` from the priority queue."
</question>

These two components (repeatedly removing the min from the queue, and decreasing the queue values) make up the bulk of the work of Dijkstra's algorithm.

<question expression>
csq_prompt = "Given the runtimes shown in the table above for the min-heap priority queue implementation, how long would it take to run Dijkstra's algorithm? Use big-O notation."
csq_soln = ["O(V*log(V)+ E*log(V))"]
csq_explanation = "Because the min-heap stores each vertex and its distance, we can bound its size at $O(V)$. This is important because this bounds the runtime of its operations at $O(\log V)$. For example, selecting the vertex to visit from our min-heap merely requires popping the minimum off the heap, which can be done in $O(\log V)$ time.<br><br>Relaxing an edge itself is an $O(1)$ operation, but updating the vertex distance requires modifying the min-heap. Because we don't want to perform an $O(V)$ linear-scan operation just to locate and change a single key, we simply place a copy of the vertex with its new key on the heap and leave both versions. This works because of the observation that updating a vertex's distance can only decrease it. Thus, our min-heap will pop off the most recent version of any vertex, leaving the remaining copies of that vertex to be discarded after it has been visited once. While this bloats our min-heap to size $O(E)$, we know that $E=O(V^2)$, so its operations still run in $\log E=O(\log V)$ time.<br><br>Thus, one full edge relaxation runs in $O(\log V)$, while vertex selection also runs in $O(\log V)$ per vertex. After scaling by the number of such operations, we arrive at the runtime of $E\log V+V\log V=O(E\log V)$"
csq_name = "dijkstra_runtime1"
</question>

While a nicer complexity than that of Bellman-Ford, the algorithm's complexity could potentially be improved with the introduction of Fibonacci heaps. While their precise mechanisms aren't important to know, the key difference is that a Fibonacci heap can perform a decrease-key operation in amortized $O(1)$ time, rather than $O(\log V)$.

<question expression>
csq_prompt = "We use Fibonacci Heaps to implement the priority queue instead of min-heap. Reference the table above. How long would it take to run Dijkstra's algorithm now? Use big-O notation."
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["O(E+V*log(V))"]
csq_explanation = "Like before, the vertices are each picked in $O(\log V)$ time, and each edge relaxation happens in $O(1)$ time. Now, each vertex update also happens in $O(1)$ time, so our cumulative runtime is $$O(E+V\log(V))$$"
csq_name = "dijkstra_runtime2"
</question>


# Extensions to Dijkstra's Algorithm

<question multiplechoice>
csq_prompt = "Let's say we wanted to slightly modify and extend Dijkstra's algorithm. Which of these could be done with slight modifications to Dijkstra's?"
csq_renderer = "checkbox"
csq_options = ["Find the longest path to some vertex `v`",
"Find the longest path to all vertices as long as the graph has no cycles",
"Find the longest path to all vertices as long as the edge weights are all non-positive",
"Detect cycles in the graph"]
csq_soln = [0,0,1,0]
csq_explanation = "If we multiply all the edge weights by $-1$, then the third option would be the same as Dijkstra's algorithm. It is not easy to find cycles through Dijkstra: not only would we have to keep track of which vertices have been visited so far, we would also need to keep track of which vertices are reachable from each vertex."
</question>

<checkyourself>
We now know that Dijkstra's algorithm has a $O(V \log V + E)$ run-time, which is much better than Bellman-Ford, which has a $O(VE)$ run-time. We still care about Bellman-Ford because it is applicable to general graphs, whereas Dijkstra's is only applicable to graphs with non-negative weights. If we have a graph with negative weights and cycles, we must use Bellman-Ford. What algorithm can we use if the graph has negative weights and no cycles?
<showhide>
Topological Sort Relaxation.
</showhide>
</checkyourself>

<checkyourself>
We can quickly find the minimum edge weight, $e_{min}$ in $O(E)$ time. We can create a new graph $G^{\prime}$ with non-negative edge weights by adding $-e_{min}$ to every edge in $G$. Now we can run Dijkstra's algorithm on $G^{\prime}$ in $O(V \log V + E)$ time. This is clearly much faster than Bellman-Ford...why would we bother running Bellman Ford for $O(VE)$?
<showhide>
This line of reasoning is incorrect. Even though $G^{\prime}$ will have non-negative edge weights, shortest paths on $G$ are not preserved on $G^{\prime}$. For example, consider this [graph](https://s092.xvm.mit.edu/_static/IAP19/dijkstra3.png). If we add $3$ to all of the edges, then we find that the shortest path in $G^{\prime}$ from $s$ to $b$ is $(s, b)$ with a length of $0$. However, the shortest path in $G$ from $s$ to $b$ is $(s, a), (a, b)$ with a length of $-4$.
</showhide>
</checkyourself>


# Ideas for Problems


Using dijkstra's to find the shortest even paths from s to every other vertex
Graph has nonnegative weights and cycles. Need to do something to prevent Bellman ford -- make sure the order that things are popped off the priority queue is consistent

We modify Dijkstra's to have an even PQ and an odd PQ. Let's say we have this code: even and odd queues. Which node do we do?
PQ must have min and del_min.
min(min_even, min_odd) is odd -> del_min odd

Now we're relaxing some outgoing edge (u,v, w) where w is even. What should we check?
update(d_even) = relax(A, w, d_even, parent, u, v)
update(d_odd)

What if w is odd?
update(d_even) = relax(A, w, d_odd, parent, u, v)

Now put everything together and write the code to return the shortest even paths (maybe, maybe this is too hard)
