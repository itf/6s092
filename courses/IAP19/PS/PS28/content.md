# Readings 

Recitation notes [16](https://learning-modules.mit.edu/service/materials/groups/238004/files/89d92dc0-f491-4c06-8d94-d9ce837431b3/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), [17](https://learning-modules.mit.edu/service/materials/groups/238004/files/9851f216-c22a-44a8-a336-d2decdb4b3df/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), [18](https://learning-modules.mit.edu/service/materials/groups/238004/files/a4bebc42-1f06-49cd-8351-6c4a216efe09/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), [19](https://learning-modules.mit.edu/service/materials/groups/238004/files/cc84430b-0d7e-4900-b5d8-73981ee30474/link?errorRedirect=%2Fmaterials%2Findex.html&download=true) 6.006 Fall 2018 on stellar

Lecture notes [16](https://learning-modules.mit.edu/service/materials/groups/238004/files/45d1ea70-2acd-4358-a45a-97ff5f564480/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), [17](https://learning-modules.mit.edu/service/materials/groups/238004/files/34839d8e-0e02-4c0a-8a66-8f53cf87e7ce/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), [18](https://learning-modules.mit.edu/service/materials/groups/238004/files/61d4493d-aa74-44c3-87b3-829caf86e5de/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), [19](https://learning-modules.mit.edu/service/materials/groups/238004/files/a8bce90e-b0f2-4e21-9ecd-e1dc28bcc05d/link?errorRedirect=%2Fmaterials%2Findex.html&download=true) 6.006 Fall 2018 on stellar

Dynamic Programming is easiest learned by working through many example problems. It's not necessary to look through all of these notes, especially because this class is not targetting the kinds of problem-solving skills that you would work on in 6.006, but it would probably be helpful to look through at least some of the problems to make sure you understand the general approach. In this pset, we will help you walk through an example DP problem that is a well-known example of DP.

# The Egg Drop Problem -- Dynamic Programming

Let’s drop some eggs together and see just how powerful (and bizarre) a technique dynamic programming can be. Suppose you want to drop eggs from an $n$ story building, and you would like to find the highest story $s$ an egg can be dropped without breaking. If you drop the egg from a higher floor $>s$, it will break. If you drop it from a floor $\leq s$, it will not break no matter how many times you drop it. You have a fixed number of eggs that are available to you, that are all identical to each other, and you would like to minimize the number of drops you make.

<question multiplechoice>
csq_prompt = "Let us suppose you only had a single egg. You would then be forced to check every single floor. What would be the (worst-case) number of drops?"
csq_renderer = "radio"
csq_soln = "$n$"
csq_options =  ["$\\infty$", "$n^2$", "$n$", "$\\log n$", "$\\log \\log n$"]
csq_explanation = "We have to check every floor, so in the worst-case if the egg breaks at floor $n-1$, we must drop the egg all $n$ floors."
</question>

<question multiplechoice>
csq_prompt = "What if you had infinite eggs? What would be the number of drops you may have to make to find which floor the egg breaks on? Think carefully about what luxury an infinite number of eggs affords you."
csq_renderer = "radio"
csq_soln = "$\\log n$"
csq_options =  ["$\\infty$", "$n^2$", "$n$", "$\\log n$", "$\\log \\log n$"]
csq_explanation = "We can perform binary search on the building to find the exact floor that the egg breaks at."
</question>

Now, let us work through this for the general case of $k$ eggs. First, let us write down our subproblems. Remember that to define our subproblems, we need to define the inputs (the parameters) and the corresponding desired output. 

<checkyourself>
What should our subproblems look like?
<showhide>
$x(f, e)$: minimum number of drops to check any sequence of $f$ floors using $e$ eggs. In this case, the parameters we care about are the number of floors and the number of eggs and the desired output is the minimum number of drops. 
</showhide>
</checkyourself>

<question multiplechoice>
csq_prompt = "The next step is to relate the subproblems. In this case, you are dropping eggs from floors so it makes sense to think about what all can happen when you drop an egg from a floor.  What are then your cases?"
csq_renderer = "checkbox"
csq_options = ["The egg breaks", "The egg does not break", "The egg both breaks and does not break"]
csq_soln = [1,1,0]
csq_explanation = "When we drop an egg from a specific floor, it was either break or not break when it hits the ground."
</question>

<question multiplechoice>
csq_prompt = "Now, lets convert this notion into a relation between $x(f, e)$ and the corresponding subproblems. In this problem, we care about the worst-case. Which relation correctly equals $x(f, e)$ based on our definitions so far?"
csq_renderer = "radio"
csq_options = ["$1 +\\min \\{ \\max \\{ x(i − 1, e − 1), x(f − i, e)\\} |  1 \\leq i \\leq f \\}$",
"$1 + \\max \\{ \\min \\{x(i − 1, e − 1), x(f − i, e)\\} |  1 ≤ i ≤ f \\}$",
"$1 + \\max \\{x(i − 1, e − 1), x(f − i, e)\\}$",
"$\\min \\{ \\max \\{x(i − 1, e − 1), x(f − i, e)\\} |  1 ≤ i ≤ f \\}$",
"$\\max \\{x(i − 1, e − 1), x(f − i, e)\\}$"]
csq_soln = "$\\min \\{ \\max \\{x(i − 1, e − 1), x(f − i, e)\\} |  1 ≤ i ≤ f \\}$"
csq_explanation = "Blah need to fix"
</question>

<question multiplechoice>
csq_prompt = "Next, remember that you should never ever ever recurse without base cases. Which of the following are correct?"
csq_renderer = "checkbox"
csq_options = ["$x(0, e) = 1$", "$x(0, e) = 0$", "$x(f, 0) = \\infty$", "$x(f, 0) = f$", "$x(f, 0) = 1$"]
csq_soln = [0,1,1,0,0]
csq_explanation = ""
</question>

If all is well and correct, $x(n, k)$ should give us the minimum number of egg drops for $n$ floors and $k$ eggs. 

Finally, let us calculate the runtime. 

<question expression>
csq_prompt = "How many subproblems do you have? Express in Theta notation."
csq_soln = ["Theta(nk)", "Theta(n * k)"]
csq_explanation = ""
</question>

<question expression>
csq_prompt = "What is the work per subproblem? Express in Theta notation."
csq_soln = "Theta(n)"
csq_explanation = ""
</question>

<question expression>
csq_prompt = "What is your final runtime?"
csq_soln = "Theta(n^2 * f)"
csq_explanation = ""
</question>



