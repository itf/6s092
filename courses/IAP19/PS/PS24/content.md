# Readings 
Recitation notes 14, 6.006 Fall 2018 on Stellar.

Lecture notes 14, 6.006 Fall 2018 on Stellar.


# Understanding the algorithm

As mentioned in [PS23](https://s092.xvm.mit.edu/IAP19/PS/PS23), Dijkstra's offers an improved asymptotic runtime over Bellman-Ford for graphs that have nonnegative edge weights. This property allows the algorithm to efficiently determine an order in which to relax every edge only once to compute shortest paths, even when the graph contains cycles.

One way to think about Dijkstra's is that each edge in the graph is a pipe, and the source node is the faucet. The amount of time that it takes for water to travel through a pipe is proportional to the length of the pipe (the weight of the edge). We open the faucet, and keep track of when water reaches each of those nodes.

Check out this [visualization](https://codepen.io/ZacharyAbel/pen/xyNoWE) (written up by Zachary Abel) for what Dijkstra's might look like on a graph where the edge weights are the lengths of the edges.

Seems intuitive enough: but how do we actually translate this into code? Though the behind it concept may seem simple, Dijkstra's is a little trickier to implement than the other SSSP algorithms we have seen so far, although like Topological Sort Relaxation and Bellman-Ford, it uses the relaxation framework. Integral to the implementation of Dijkstra's is the concept of a priority queue which supports the following operations:

* `build` (B): Builds a priority queue of the nodes keyed by the estimated distance so far from the source
* `del_min` (M): Removes and returns a node from the priority queue with the smallest key
* `dec_key` (D): Decreases the key value of a node in the priority queue

The key differences between all of the different relaxation algorithms (Topological Sort Relaxation, Bellman-Ford, Dijkstra's) that we have seen so far is that they perform the relaxation in different orders. Topological Sort Relaxation performs the relaxations in the order given to us by the topological sort on the vertices. Bellman-Ford does not enforce any particular order, but *does* require that we relax every edge in the graph once before repeating. Dijkstra's algorithm will relax the edges in the order given by this priority queue.

More specifically, from the 6.006 recitation notes linked above: "Dijkstra’s algorithm repeatedly relax[es] edges from a vertex whose minimum weight path estimate is smallest among vertices whose out-going edges have not yet been relaxed." The key invariant of Dijkstra's is that when we pop a vertex off of the priority queue using `del_min`, the distance estimate for that vertex is the correct shortest distance. So at any given time, the nodes for which we are trying to find the shortest distances for are all contained in the progressively shrinking priority queue.

Let's try to get a better understanding of what that means by running Dijkstra's on the graph below, from source node `s`.

<center>
<img src="/_static/IAP19/dijkstra1.png" height="70"  />
</center>

We initialize distance estimates from `s` to be $\infty$ for `a` and `b`, and $0$ for $s$.

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
What can't we pop off the edge `(3, 'b')`?
<showhide>
Our priority queue interface only supports removing the element with the smallest key, so we would have to remove `(1, 'a')`. More importantly, this would break our invariant that we have the correct distance estimates for any vertices popped off of the Priority Queue. As we can see, the correct shortest distance from `s` to `b` is $2$. The correct move here is to pop off the edge `(1, 'a')`.
</showhide>
</checkyourself>

# Evaluating runtime

The runtime of Dijkstra's largely relies upon the properties of the priority queue used to select the next vertex to visit. We will analyze the runtime of the algorithm when implemented with a min-heap priority queue and with a Fibonacci heap priority queue. As mentioned previously, the priority queue selects vertices using their distances as keys.

We can aggregate the work done over the execution of Dijkstra's as follows:

1. For at most $V$ times, we must select the vertex with minimum distance from our priority queue.
2. For at most $E$ times, we must relax an edge and potentially update a vertex's distance.

<question expression>
csq_prompt = "What is the runtime of Dijkstra's algorithm in big-O notation as a function of $V$ and $E$ when implemented with a min-heap priority queue? Recall that dequeuing from and enqueuing into such a queue can be done in $O(\log n)$ time, where $n$ is the heap size. Also, as a hint, recall that accessing any element in a min-heap other than the minimum is inefficient, so adding redundant elements to the heap is preferable to replacing elements in the heap. Consider this when deciding how to 'update' your vertex distances.   \n\n"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = "O(E*log(V))"
csq_explanation = "Because the min-heap stores each vertex and its distance, we can bound its size at $O(V)$. This is important because this bounds the runtime of its operations at $O(\log V)$. For example, selecting the vertex to visit from our min-heap merely requires popping the minimum off the heap, which can be done in $O(\log V)$ time.<br><br>Relaxing an edge itself is an $O(1)$ operation, but updating the vertex distance requires modifying the min-heap. Because we don't want to perform an $O(V)$ linear-scan operation just to locate and change a single key, we simply place a copy of the vertex with its new key on the heap and leave both versions. This works because of the observation that updating a vertex's distance can only decrease it. Thus, our min-heap will pop off the most recent version of any vertex, leaving the remaining copies of that vertex to be discarded after it has been visited once. While this bloats our min-heap to size $O(E)$, we know that $E=O(V^2)$, so its operations still run in $\log E=O(\log V)$ time.<br><br>Thus, one full edge relaxation runs in $O(\log V)$, while vertex selection also runs in $O(\log V)$ per vertex. After scaling by the number of such operations, we arrive at the runtime of $$E\log V+V\log V=O(E\log V)$$"
csq_name = "dijkstra_runtime1"
</question>

While a nicer complexity than that of Bellman-Ford, the algorithm's complexity could potentially be improved with the introduction of Fibonacci heaps. While their precise mechanisms aren't important to know, the key difference is that a Fibonacci heap can perform a decrease-key operation in amortized $O(1)$ time, rather than $O(\log V)$.

<question expression>
csq_prompt = "What is the runtime of Dijkstra's algorithm in big-O notation as a function of $V$ and $E$ when implemented with a Fibonacci heap priority queue? Recall that dequeuing from and enqueuing into such a queue can be done in $O(\log n)$ time, where $n$ is the heap size, and decreasing the key of an element runs in amortized $O(1)$.   \n\n"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = "O(E+V*log(V))"
csq_explanation = "Like before, the vertices are each picked in $O(\log V)$ time, and each edge relaxation happens in $O(1)$ time. Now, each vertex update also happens in $O(1)$ time, so our cumulative runtime is $$O(E+V\log(V))$$"
csq_name = "dijkstra_runtime2"
</question>
