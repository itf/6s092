# Readings
[Recitation notes 12](https://learning-modules.mit.edu/service/materials/groups/238004/files/31fe711d-927b-4355-b8e0-06615e4d2f8a/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), Weights and Relaxation, 6.006 Fall 2018 on stellar.

# Relaxation

<question multiplechoice>
csq_prompt = "Select valid reasons that may not exist a shortest path between vertices $u$ and $v$:"
csq_renderer = "checkbox"
csq_soln = [1,0,0,1]
csq_options =  ['there is a negative weight cycle on the path from $u$ to $v$',
'negative weight edges on the path from $u$ to $v$',
'$u$ and $v$ are not adjacent to each other',
'$u$ and $v$ are in different connected components in an undirected graph',]
csq_explanation = "When there is a negative weight cycle, we can get a shorter path by going around the cycle again, so any shortest path would have $\\infty$ edges."
csq_nsubmits = 3
</question>

<question multiplechoice>
csq_prompt = "A valid first step of any relaxation algorithm could be to initialize the path estimates for the vertices to be:"
csq_renderer = "checkbox"
csq_soln = [1,0,0,0]
csq_options =  ["$\\infty$",
"$\\infty$",
"The same integer",
"$0$"]
csq_explanation = "The invariant for relaxation is that d[v] >= $\\delta$[v], where d[v] is the current estimate for the weight of the path from s to v and $\\delta$[v] is the actual minimum weight of that path. By initializing to positive infinity, we have that this invariant must be true at the beginning. This is not necessarily true if we initialize to anything else (anything else might be smaller than the actual minimum weight)."
csq_nsubmits = 3
</question>

<center>
<img src="/_static/IAP19/relax4.png" height="200"  />
</center>

<question pythonliteral>
csq_prompt = "We are in the middle of performing relaxation on the above graph, in order to find the shortest paths from $s$ to every other node. Right now, our estimates are: \n\n $\\delta[s] = 0$ \n\n $\\delta[1] = 2$ \n\n $\\delta[2] = 7$ \n\n$\\delta[3]=22$ \n\n (Remember that $\\delta[v]$ is shorthand for our current estimate for the length of the shortest path from $s$ to $v$. We can relax one shortest path estimate from having a weight of $a$ to having a weight of $b$. What is $a + b$?"
csq_soln = 36
csq_explanation = "We have `d[2] = 7`, `d[3] = 22`, and `w(2,3) = 7`, so `d[3] > d[2] + w(2,3)$`. We relax 22 to be 14."
csq_nsubmits = 1
</question>

<center>
<img src="/_static/IAP19/relax6.png" height="200"  />
</center>

<question multiplechoice>
csq_prompt = "In the above graph, is there a negative weight cycle? If so, which edges are in it?"
csq_soln = "No negative weight cycle"
csq_renderer = "radio"
csq_options =  ["No negative weight cycle",
  "Negative weight cycle; edges (a,b), (b,c), (c,d), (d,a)",
  "Negative weight cycle; edges (b,c), (c,d), (d,a)",
  "Negative weight cycle; edges (s,a), (a,b), (b,c), (c,d), (d,a), (c,v)"]
csq_explanation = "There is no negative weight cycle, and in fact there is no cycle at all."
csq_nsubmits = 4
</question>

<center>
<img src="/_static/IAP19/relax6.png" height="200"  />
</center>

<question multiplechoice>
csq_prompt = "In the (same) above graph, what is the weight of the minimum weight path from s to v?"
csq_renderer = "radio"
csq_soln = "1"
csq_options =  ["1", "-3", "-22", "$-\\infty$"]
csq_explanation = "There is no negative weight cycle on the path, so we can find a minimum weight path."
csq_nsubmits = 4
</question>

<center>
<img src="/_static/IAP19/relax7.png" height="200"  />
</center>

<question multiplechoice>
csq_prompt = "In the above graph, is there a negative weight cycle? If so, which edges are in it?"
csq_soln = "Negative weight cycle; edges (a,b), (b,c), (c,d), (d,a)"
csq_renderer = "radio"
csq_options =  ["No negative weight cycle",
  "Negative weight cycle; edges (a,b), (b,c), (c,d), (d,a)",
  "Negative weight cycle; edges (b,c), (c,d), (d,a)",
  "Negative weight cycle; edges (s,a), (a,b), (b,c), (c,d), (d,a), (c,v)"]
csq_explanation = "The path consisting of edges (a,b), (b,c), (c,d), and (d,a) is a cycle. It has negative weight: +10 - 15 -17 -11 = -33. Edges (s,a) and (c,v) are not part of this cycle (even though s and v are connected to the vertices in the cycle)."
csq_nsubmits = 4
</question>


The next two problems will deal with the following graph:

<center>
<img src="/_static/IAP19/relax7.png" height="200"  />
</center>

<question multiplechoice>
csq_prompt = "What is the weight of the minimum weight path from $s$ to $v$?"
csq_renderer = "radio"
csq_soln = "$-\\infty$"
csq_options =  ["-5", "1", "-22", "$-\\infty$"]
csq_explanation = "The shortest path has a negative weight cycle, so the minimum weight path is negative infinity."
</question>

<question pythonliteral>
csq_prompt = "We start performing relaxation on the above graph, in order to find the shortest paths from $s$ to every other node. At the beginning, our shortest path estimates are: \n\n $\\delta[s] = 0$ \n\n $\\delta[a] = \\infty$ \n\n $\\delta[b] = \\infty$ \n\n$\\delta[c]=\\infty$ \n\n$\\delta[d]=\\infty$\n\n$\\delta[v]=\\infty$\n\n After we relax along the edge $(s, a)$, what is our new path estimate for $a$? $\\delta[a] =$"
csq_soln = 2
csq_explanation = "$\\delta[s] = 0$, $w(s, a) = 2$, so $\\delta[a] > \\delta[s] + w(s,a)$. By the triangle inequality, we can set $\\delta[a] = 0 + 2 = 2$"
</question>

<question multiplechoice>
csq_prompt = "We proceed to perform relaxation on the edge $(c,v)$. What do we get for $\\delta[v]$?"
csq_soln = "$\\infty$"
csq_renderer = "radio"
csq_options = ["4", "1", "$\\infty$", "-$\\infty$"]
csq_nsubmits = 4
csq_explanation = "We don't change anything. It's not true that $\\delta[v] > \\delta[c] + w(c,v)$ right now, because $\\delta[c] = \\infty$. Therefore we cannot apply triangle inequality."
</question>

<question pythonliteral>
csq_prompt = "We proceed to perform the following relaxations on the edges `[(a,b), (b,c), (c,d), (d,a) ]`. What are our current estimates for $\\delta[a]$, $\\delta[b]$, $\\delta[c]$, $\\delta[d]$? Express as a Python list of four numbers."
csq_soln = [-31, 12, -3, -20]
csq_explanation = "Walk through the relaxations. Because we visit `a` twice, we relax it twice so it goes from $\\infty \\rightarrow 2 \\rightarrow -31$."
</question>

<question pythonliteral>
csq_prompt = "Everytime we relax the edges `[(a,b), (b,c), (c,d), (d,a) ]` in order, which nodes do we decrease the $\\delta$ for? Express your answer as a list of strings in Python format, i.e. ['a', 'b']."
csq_soln = ['a', 'b', 'c', 'd']
</question>

</question pythonliteral>
csq_prompt = "By how much do we decrease $\delta$?"
csq_soln = 33
</question>
