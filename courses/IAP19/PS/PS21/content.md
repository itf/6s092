# Readings
Recitation notes 12, 6.006 Fall 2018 on stellar.


# Relaxation


<question multiplechoice>
csq_prompt = "For some vertices in the graph, there does not exist a shortest path from the source to those vertices when the graph contains: "
csq_renderer = "checkbox"
csq_soln = [1,0,0]
csq_options =  ['a negative weight cycle',
'a positive weight cycle',
'negative weight edges (no cycle)']
csq_name="qexample1"
csq_explanation = "When there is a negative weight cycle, we can get a shorter path by going around the cycle again, giving a path with weight negative infinity."
</question>

<question multiplechoice>
csq_prompt = "The first step of any relaxation algorithm is: "
csq_renderer = "checkbox"
csq_soln = [1,0,0,0]
csq_options =  ["initialize the weights to positive infinity",
"initialize the weights to negative infinity",
"initialize the weights to one random integer; anything works",
"initialize the weights to zero"]
csq_name="qexample2"
csq_explanation = "The invariant for relaxation is that d[v] >= $\\delta$[v], where d[v] is the current estimate for the weight of the path from s to v and $\\delta$[v] is the actual minimum weight of that path. \n
By initializing to positive infinity, we have that this invariant must be true at the beginning. This is not necessarily true if we initialize to anything else (anything else might be smaller than the actual minimum weight)."
</question>

<center>
<img src="/_static/IAP19/relax1.png" height="200"  />
</center>

<question multiplechoice>
csq_prompt = "In the above graph, can we relax any edges?"
csq_soln = [1,0]
csq_options =  ["True", "False"]
csq_name="qexample3"
csq_explanation = "We have d[u] = 5, d[v] = 20, and w(u,v) = 7=12, so d[v] < d[u] + w(u,v), so yes, we can relax."
</question>

<center>
<img src="/_static/IAP19/relax2.png" height="200"  />
</center>

<question multiplechoice>
csq_prompt = "In the above graph, is there a negative weight cycle? If so, which edges are in it?"
csq_soln = [0,1,0,0]
csq_options =  ["No negative weight cycle",
  "Negative weight cycle; edges (a,b), (b,c), (c,d), (d,a)",
  "Negative weight cycle; edges (b,c), (c,d), (d,a)",
  "Negative weight cycle; edges (s,a), (a,b), (b,c), (c,d), (d,a), (c,v)"]
csq_name="qexample4"
csq_explanation = "The path consisting of edges (a,b), (b,c), (c,d), and (d,a) is a cycle. It has negative weight: +10 - 15 -17 -11 = -33. Edges (s,a) and (c,v) are not part of this cycle (even though s and v are connected to the vertices in the cycle)."
</question>

<center>
<img src="/_static/IAP19/relax2.png" height="200"  />
</center>

<question multiplechoice>
csq_prompt = "In the (same) above graph, what is the weight of the minimum weight path from s to v?"
csq_soln = [0,0,0,1]
csq_options =  ["1", "-17", "4", "negative infinity"]
csq_name="qexample4"
csq_explanation = "There is a negative weight cycle on the path from s to v, so the minimum weight path has negative infinity weight."
</question>

<center>
<img src="/_static/IAP19/relax4.png" height="200"  />
</center>

<question multiplechoice>
csq_prompt = "In the above graph, what is the weight of the minimum weight path from s to v?"
csq_soln = [0,0,0,1]
csq_options =  ["negative infinity", "-5"]
csq_name="qexample5"
csq_explanation = "Negative infinity is less than -5; if there exists a path from s to v having a negative weight cycle, this path will produce the minimum weight."
</question>
