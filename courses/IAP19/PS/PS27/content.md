# Readings 

Recitation notes [16](https://learning-modules.mit.edu/service/materials/groups/238004/files/89d92dc0-f491-4c06-8d94-d9ce837431b3/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), [17](https://learning-modules.mit.edu/service/materials/groups/238004/files/9851f216-c22a-44a8-a336-d2decdb4b3df/link?errorRedirect=%2Fmaterials%2Findex.html&download=true) 6.006 Fall 2018 on stellar

Lecture notes [16](https://learning-modules.mit.edu/service/materials/groups/238004/files/45d1ea70-2acd-4358-a45a-97ff5f564480/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), [17](https://learning-modules.mit.edu/service/materials/groups/238004/files/34839d8e-0e02-4c0a-8a66-8f53cf87e7ce/link?errorRedirect=%2Fmaterials%2Findex.html&download=true) 6.006 Fall 2018 on stellar

# Dynamic programming Concepts

<question multiplechoice>
csq_prompt = """Wumpus is trying to solve the shortest path problem by using dynamic programming.

In Wumpus first attempt, Wumpus defines the following recursion:

The shortest path to a node $x$, $D(x)$, is the minimum of [the shortest path to the nodes that have edges going to $x$, plus the sum of the edge weight between that node and $x$]. $$D(x) = \\min_{\\text{$y$, where $y$ has an edge to $x$}} \\left(D(y) + w(y,x) \\right)$$ 

Why won't this work?
"""
csq_renderer = "checkbox"
csq_soln = [0,0,1,0]
csq_options =  ['The shortest path to $x$ does not necessarily includes the shortest path to one of the nodes that has edges to $x$',
'It works, but it would take an exponential amount of time to run this algorithm.',
'If there are cycles in the graph, there will be cyclic dependencies. In order to find the shortest path to the node $x$, we have to find the shortest path to the nodes that can reach $x$; however, to find those, we need to find the shortest path to $x$.', 
'Because it is not true that $D(x) = \\min_y \\left(D(y) + w(y,x) \\right)$']
</question>

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
csq_prompt = "Which subproblem relation could be represented by this subproblem dependencies graph?"
csq_renderer = "checkbox"
csq_soln = [0,1,0,0]
csq_options = ["$X(i) = X(i-1) + 2 * X(i-2)$",
"$X(i) = X(i-1) + 1$",
"$X(i) = X(\\lfloor\\frac{i}{2}\\rfloor)$",
"$X(i) = X(i-1) * X(i-2)$"]
csq_explanation = ""
</question>

<center>
<img src="/_static/IAP19/dp2.png" height="210"  />
</center>

<question multiplechoice>
csq_prompt = "Which subproblem relation could be represented by this subproblem dependencies graph?"
csq_renderer = "checkbox"
csq_soln = [1,0,0,1]
csq_options = ["$X(i) = X(i-1) + 2 * X(i-2)$",
"$X(i) = X(i-1) + 1$",
"$X(i) = X(\\lfloor\\frac{i}{2}\\rfloor)$",
"$X(i) = X(i-1) * X(i-2)$"]
csq_explanation = ""
</question>

<center>
<img src="/_static/IAP19/dp3.png" height="210"  />
</center>

<question pythonliteral>
csq_prompt = "If I tell you that the subproblem relation for our DP problem is \n\n$X(i) = X(\\lfloor\\frac{i}{2}\\rfloor) + X(\\lfloor\\frac{i}{2}\\rfloor -1)$\n\n and that $a = 8$, then what are the values of $bcdef$? Answer as a Python list of 5 non-negative numbers."
csq_soln = [3, 4, 2, 0, 1]
csq_explanation = "Draw out the graph on your own, and compare with the graph in the above image."
</question>

<question multiplechoice>
csq_prompt = "It's important to make sure that our subproblems are acyclic. That is because we can only solve our problem if the subproblems dependency graph form a DAG. It's easy to see that if we define our subproblem to be $X(i) = X(i)-1$, then it's pretty clear to see that we cannot solve for $X(i)$. Which of these subproblem relations are acyclic?"
csq_renderer = "checkbox"
csq_soln = [1, 1, 0, 0, 1]
csq_options = ["$X(i) = X(i-1)$",
"$X(i) = \\Sigma X(j)$ for all $j < i$",
"$X(i) = \\Sigma X(j)$ for all $j < i$ and $j > i$",
"$X(i) = \\Sigma X(j)$ for all integer divisors $j$ of $i$",
"$X(i) = \\Sigma X(j)$ for all primes $j < i$"]
csq_explanation = "In the third case, we can see that $X(3)$ depends on $X(2)$, and $X(2)$ depends on $X(3)$, which creates a cycle of dependencies. In the fourth case, $i$ is also an integer divisor of itself which makes the dependencies graph cyclic."
</question>
