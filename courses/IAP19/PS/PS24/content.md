# Readings 
Recitation notes 14, 6.006 Fall 2018 on Stellar.

Lecture notes 14, 6.006 Fall 2018 on Stellar.


# Understanding the algorithm

As mentioned in [PS23](https://s092.xvm.mit.edu/IAP19/PS/PS23), Dijkstra's offers an improved asymptotic runtime over Bellman-Ford for graphs that have nonnegative edge weights. This property allows the algorithm to efficiently determine an order in which to relax every edge only once to compute shortest paths, even when the graph contains cycles.


INSERT EXPLANATION OF ALGORITHM WITH GRAPH DIAGRAM


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
