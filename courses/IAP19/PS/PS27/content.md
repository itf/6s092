# Readings 

Recitation notes [16](https://learning-modules.mit.edu/service/materials/groups/238004/files/89d92dc0-f491-4c06-8d94-d9ce837431b3/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), [17](https://learning-modules.mit.edu/service/materials/groups/238004/files/9851f216-c22a-44a8-a336-d2decdb4b3df/link?errorRedirect=%2Fmaterials%2Findex.html&download=true) 6.006 Fall 2018 on stellar

Lecture notes [16](https://learning-modules.mit.edu/service/materials/groups/238004/files/45d1ea70-2acd-4358-a45a-97ff5f564480/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), [17](https://learning-modules.mit.edu/service/materials/groups/238004/files/34839d8e-0e02-4c0a-8a66-8f53cf87e7ce/link?errorRedirect=%2Fmaterials%2Findex.html&download=true) 6.006 Fall 2018 on stellar

# Dynamic programming Concepts

<question multiplechoice>
csq_prompt = "Which of the following are important to solving a DP problem?"
csq_renderer = "checkbox"
csq_soln = [1,1,1,0,1,1]
csq_options = ["Define Subproblems", "Relate Subproblems", "Identify Base Cases", "Kill Wumpus", "Compute Solution", "Analyze Running Time"]
csq_nsubmits = 1
csq_explanation = "Don't kill Wumpus! :("
</question>

<question multiplechoice>
csq_prompt = "Our DP subproblem $x(i)$ depends on subproblems $x(1), x(2), \\ldots , x(i − 1)$. In a top-down implementation, the value $x(i)$ is computed before $x(i − 1)$."
csq_renderer = "radio"
csq_soln = "False"
csq_options = ["True", "False"]
csq_nsubmits = 1
csq_explanation = "If $x(i)$ depends on $x(i-1)$, then by definition we need to compute $x(i-1)$ in order to compute $x(i)$."
</question>

<question multiplechoice>
csq_prompt = "Our DP subproblem $x(i)$ depends on subproblems $x(1), x(2), \\ldots , x(i − 1)$. In a top-down implementation, we start solving $x(i)$ before $x(i − 1)$."
csq_renderer = "radio"
csq_soln = "True"
csq_options = ["True", "False"]
csq_nsubmits = 1
csq_explanation = "In a top-down implementation, we will call $x(i)$ first, which will then recursively call all of the subproblems that it depends on (including $x(i-1)$)."
</question>

<center>
<img src="/_static/IAP19/dp2.png" height="210"  />
</center>

<question multiplechoice>
csq_prompt = "Which subproblem relation could be represented by the above subproblem dependencies graph?"
csq_renderer = "checkbox"
csq_soln = [0,1,0,0]
csq_options = ["$X(i) = X(i-1) + 2 X(i-2)$",
"$X(i) = X(i-1) + 1$",
"$X(i) = X(\\lfloor\\frac{i}{2}\\rfloor)$",
"$X(i) = X(i-1) X(i-2)$"]
csq_explanation = "Only in the second option does $X(i)$ depend solely on $X(i-1)$"
</question>

<center>
<img src="/_static/IAP19/dp1.png" height="210"  />
</center>

<question multiplechoice>
csq_prompt = "Which subproblem relation could be represented by the above subproblem dependencies graph?"
csq_renderer = "checkbox"
csq_soln = [1,0,0,1]
csq_options = ["$X(i) = X(i-1) + 2 X(i-2)$",
"$X(i) = X(i-1) + 1$",
"$X(i) = X(\\lfloor\\frac{i}{2}\\rfloor)$",
"$X(i) = X(i-1) X(i-2)$"]
csq_explanation = "In both the first and last option, $X(i)$ depends on $X(i-1)$ and $X(i-2)$"
</question>

<center>
<img src="/_static/IAP19/dp3.png" height="210"  />
</center>

<question pythonliteral>
csq_prompt = "If I tell you that the subproblem relation for our DP problem, represented by the above subproblem dependencies graph, is \n\n $X(i) = X(\\lfloor\\frac{i}{2}\\rfloor) + X(\\lfloor\\frac{i}{2}\\rfloor -1)$\n\n and that $a = 8$, then what are the values of $[b, c, d, e, f]$? Answer as a Python list of 5 non-negative numbers."
csq_soln = [3, 4, 2, 0, 1]
csq_explanation = "Draw out the graph on your own, and compare with the graph in the above image. The longest chain is c->d->f->e, which means that that must be 4->2->1->0."
</question>

<question multiplechoice>
csq_prompt = "Which of these are valid sets of base cases that we need to show in order to solve for the all of the subproblems in the above dependencies graph?"
csq_renderer = "checkbox"
csq_soln = [1,1,1,0]
csq_options = ["e", "e, f", "e, d, a", "a, b, c, d, f"] 
csq_explanation = "Any set of base case that includes `e` will be sufficient to sole for all of those above DP subproblems. Because there are no other leaf nodes in this graph."
</question>

<question multiplechoice>
csq_prompt = """It's important when defining and relating our subproblems to make sure that our subproblem dependencies are acyclic. In other words, we can only solve our problem if the subproblems dependency graph form a DAG. A trivial example of a cyclic dependency is if we define our subproblems to be $X(3) = X(2) + 1$ and $X(2) = X(3)-1$. It's pretty clear to see that we can't solve for either $X(3)$ or $X(2)$ here. We only have two requirements for applying Dynamic Programming to problems:

1. The dependency graph must be acyclic.

2. The base cases must be comprehensive, so that recursion won't go on forever.

Which of these subproblem relations are acyclic?"""

csq_renderer = "checkbox"
csq_soln = [1, 1, 0, 0, 1]
csq_options = ["$X(i) = X(i-1)$",
"$X(i) = \\sum X(j)$ for all $j < i$",
"$X(i) = \\sum X(j)$ for all $j < i$ and $j > i$",
"$X(i) = \\sum X(j)$ for all integer divisors $j$ of $i$",
"$X(i) = \\sum X(j)$ for all primes $j < i$"]
csq_explanation = "In the third case, we can see that $X(3)$ depends on $X(2)$, and $X(2)$ depends on $X(3)$, which creates a cycle of dependencies. In the fourth case, $i$ is also an integer divisor of itself which makes the dependencies graph cyclic."
</question>

<question multiplechoice>
csq_prompt = """Wumpus is trying to solve the shortest path problem by using dynamic programming.

In Wumpus's first attempt, Wumpus defines the following recursion:

The shortest path to a node $x$, $D(x)$, is the minimum of [the shortest path to node $$y+$$ the edge weight connecting $$$y$ and $$x$$] over all $$y$$ such that $$y$$ has an edge to $$x$$.

$$D(x) = \\min_{\\text{$y$, where $y$ has an edge to $x$}} \\left(D(y) + w(y,x) \\right)$$ 

Why doesn't this work?
"""
csq_renderer = "checkbox"
csq_soln = [0,0,1,0]
csq_options =  ['The shortest path to $x$ does not necessarily includes the shortest path to one of the nodes that has edges to $x$',
'It works, but it would take an exponential amount of time to run this algorithm.',
'If there are cycles in the graph, there will be cyclic dependencies.',
'Because it is not true that $D(x) = \\min_y \\left(D(y) + w(y,x) \\right)$']
csq_explanation = "The shortest path from $s$ to $x$, if it goes through some node $y$, will always include the shortest path from $s$ to $y$. The reason why this algorithm doesn't work is because there may be cyclic dependencies if we define our subproblems this way: if we have the graph $x \\rightarrow y, y \\rightarrow x$, then we need to calculate $D(x)$ to calculate $D(y)$, which we need to calculate $D(x)$, and so on."
</question>

