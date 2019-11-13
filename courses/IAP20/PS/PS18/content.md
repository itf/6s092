# Readings 
[Recitation 10](https://learning-modules.mit.edu/service/materials/groups/238004/files/fb806d51-1a22-4a1c-b388-33211a880b42/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), First part of notes on Graphs and Graph Representations, 6.006 Fall 2018

[Lecture 10](https://learning-modules.mit.edu/service/materials/groups/238004/files/5f6a6fa2-26f7-4791-8e6e-2246ab4a4d83/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), First part before Breadth-First Search, 6.006 Fall 2018

# Graph Representation

<question multiplechoice>
csq_prompt = "Which of these are valid graphs $G = (V,E)$?"
csq_renderer = "checkbox"
csq_soln = [1,0,1]
csq_options =  [
"""```V = [0, 1, 2, 3]
E = [(0,1), (1,2), (0,3)]
```""",
"""```V = [0, 1, 2]
E = [(0,1), (1,2), (0,3)]
```""",
"""```V = [a, b, c]
E = [(a,b), (b,c), (a,c)]
```"""]
csq_explanation = "We can't have edges containing nodes outside of $V$"
</question>

The following questions all deal with this graph:

<center>
<img src="/_static/IAP19/relax7.png" height="200"  />
</center>

<question pythonliteral>
csq_prompt = "What is $V$? Express as a Python set of strings, like {'a', 'b'}."
csq_soln = {'a', 'b', 'c', 'd', 'v', 's'}
csq_explanation = "$V$ is the list of vertices in the graph."
</question>

<question pythonliteral>
csq_prompt = "Let's say we decide to represent $E$ with a dictionary. What is `E['s']`? Express as a Python set of strings, like {'a', 'b'}."
csq_soln = {'a', 'v'}
csq_explanation = "The dictionary value contains the set of all vertices $x$ such that $(s, x)$ is an edge in $G$"
</question>

<question pythonliteral>
csq_prompt = "How many different paths are there from $s$ to $v$ that do not contain a cycle?"
csq_soln = 2
csq_explanation = "We have the path `[s,a,b,c,v]` and `[s,v]`."
</question>

