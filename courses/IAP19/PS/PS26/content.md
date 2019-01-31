# Readings 

Recitation notes [16](https://learning-modules.mit.edu/service/materials/groups/238004/files/89d92dc0-f491-4c06-8d94-d9ce837431b3/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), [17](https://learning-modules.mit.edu/service/materials/groups/238004/files/9851f216-c22a-44a8-a336-d2decdb4b3df/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), [18](https://learning-modules.mit.edu/service/materials/groups/238004/files/a4bebc42-1f06-49cd-8351-6c4a216efe09/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), [19](https://learning-modules.mit.edu/service/materials/groups/238004/files/cc84430b-0d7e-4900-b5d8-73981ee30474/link?errorRedirect=%2Fmaterials%2Findex.html&download=true) 6.006 Fall 2018 on stellar

Lecture notes [16](https://learning-modules.mit.edu/service/materials/groups/238004/files/45d1ea70-2acd-4358-a45a-97ff5f564480/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), [17](https://learning-modules.mit.edu/service/materials/groups/238004/files/34839d8e-0e02-4c0a-8a66-8f53cf87e7ce/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), [18](https://learning-modules.mit.edu/service/materials/groups/238004/files/61d4493d-aa74-44c3-87b3-829caf86e5de/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), [19](https://learning-modules.mit.edu/service/materials/groups/238004/files/a8bce90e-b0f2-4e21-9ecd-e1dc28bcc05d/link?errorRedirect=%2Fmaterials%2Findex.html&download=true) 6.006 Fall 2018 on stellar

Dynamic Programming is easiest learned by working through many example problems. It's not necessary to look through all of these notes, especially because this class is not targetting the kinds of problem-solving skills that you would work on in 6.006, but it would probably be helpful to look through at least some of the problems to make sure you understand the general approach. In this pset, we will walk through an example DP problem that is pretty well-known.

# The Egg Drop Problem

Let’s drop some eggs together and see just how powerful (and bizarre) a technique dynamic programming can be. Suppose you want to drop eggs from an $n$ story building, and you would like to find the **highest story $s$ an egg can be dropped without breaking**. If you drop the egg from a higher floor $>s$, it will break. If you drop it from a floor $\leq s$, it will not break no matter how many times you drop it. You have a fixed number of eggs that are available to you, that are all identical to each other, and you would like to minimize the number of drops you have to make to find $s$.

<question multiplechoice>
csq_prompt = "Let us suppose you only had a single egg. You would then be forced to check every single floor. What would be the (worst-case) number of drops?"
csq_renderer = "radio"
csq_soln = "$n$"
csq_options =  ["$\\infty$", "$n^2$", "$n$", "$\\log n$", "$\\log \\log n$"]
csq_nsubmits = 4
csq_explanation = "We have to check every floor, starting at floor $0$. If $s=0$, then we don't want to break our only egg on the first try by dropping it from floor $1$. In the worst-case if $s=n-1$, we must drop the egg from all $n$ floors, starting at floor $0$ and going up one at a time."
</question>

<question multiplechoice>
csq_prompt = "What if you had an infinite supply of eggs? Can you come up with a strategy that minimizes the worst-case number of drops you may have to make? What would this number be?"
csq_renderer = "radio"
csq_soln = "$\\log n$"
csq_options =  ["$\\infty$", "$n^2$", "$n$", "$\\log n$", "$\\log \\log n$"]
csq_nsubmits = 4
csq_explanation = "We can perform binary search on the building to find the exact floor that the egg breaks at."
</question>

Now, let us work through this for the general case of $k$ eggs. First, let us write down our subproblems. Remember that to define our subproblems, we need to define the inputs (the parameters) and the corresponding desired output. 

<checkyourself>
What should our subproblems look like?
<showhide>
$x(f, e)$: minimum number of drops to check any sequence of $f$ floors using $e$ eggs. In this case, the parameters we care about are the number of floors and the number of eggs and the desired output is the minimum number of drops.<br><br>An important observation that you could make about this subproblem definition is that it does not depend on **how high up** the floors are. It will take the same amount of egg drops to determine $s$ if we are looking at floors $0$ through $9$ as if we are looking at floors $100$ through $109$, or even if we're looking at floors $0, 2, 4, \ldots, 18$. It's worth thinking about why that is true, and maybe walking through a few examples.
</showhide>
</checkyourself>

The next step is to relate the subproblems. We have narrowed down $s$ to $f$ possible values. Let's say that we are dropping our egg from the $i$th floor (where by $i$th floor here we mean that there are $f-i$ floors above us and $i-1$ floors below us in these $f$ possible values for $s$). The egg will either break or not break.

<question expression>
csq_prompt = "How many possible values of $s$ do we have if the egg does not break? Express in terms of $f$, $i$, and/or $e$."
csq_soln = "f-i"
csq_explanation = "If the egg does not break, that means that $s \\geq i$, so there are $f-i$ possible values for $s$."
</question>

<question expression>
csq_prompt = "How many possible values of $s$ do we have if the egg breaks? Express in terms of $f$, $i$, and/or $e$."
csq_soln = "i-1"
csq_explanation = "If the egg breaks, that means the value of $s$ is less than $i$, so there are $i-1$ possible values for $s$."
</question>

<question pythoncode>
csq_interface = "ace"
csq_npoints = 1
csq_prompt = "Define the subproblem that we would need to solve if the egg does not break. Express as a function $X(a, b)$, where $a$ and $b$ can be defined in terms of $f$, $i$ and /or $e$. Ignore special/base cases."
csq_soln = '''def subproblems_if_egg_doesnt_break(f, i, e):
    return X(f-i, e)'''

csq_initial = '''def subproblems_if_egg_doesnt_break(f, i, e):
    return X(None, None) #TODO
'''

csq_code_pre = '''def X(a, b):
    return (a**(2) + b**(3)/6)*(a+22)
'''

tests = [(2, 2),
         (4, 4),
         (10, 5),
         (20, 20),
         (100, 100),
         (1000, 1000)]
        
csq_tests = []
for test_num, t in enumerate(tests):
    f_range, e_range = t
    f = cs_random.randint(1, f_range)
    i = cs_random.randint(1, f)
    e = cs_random.randint(1, e_range)
    csq_tests.append({
        'code': f"""
ans = subproblems_if_egg_doesnt_break({f}, {i}, {e}) """,
        'show_code': False,
        'grade': True
    })
</question>

<question pythoncode>
csq_interface = "ace"
csq_npoints = 1
csq_prompt = "Define the subproblem that we would need to solve if the egg breaks. Express as a function $X(a, b)$, where $a$ and $b$ can be defined in terms of $f$, $i$ and /or $e$. Ignore special/base cases"
csq_soln = '''def subproblems_if_egg_breaks(f, i, e):
    return X(i-1, e-1)'''

csq_initial = '''def subproblems_if_egg_breaks(f, i, e):
    return X(None, None) #TODO
'''

csq_code_pre = '''def X(a, b):
    return (a**(2) + b**(3)/6)*(a+22)
'''

tests = [(2, 2),
         (4, 4),
         (10, 5),
         (20, 20),
         (100, 100),
         (1000, 1000)]
        
csq_tests = []
for test_num, t in enumerate(tests):
    f_range, e_range = t
    f = cs_random.randint(1, f_range)
    i = cs_random.randint(1, f)
    e = cs_random.randint(1, e_range)
    csq_tests.append({
        'code': f"""
ans = subproblems_if_egg_breaks({f}, {i}, {e}) """,
        'show_code': False,
        'grade': True
    })
</question>

<question pythoncode>
csq_interface = "ace"
csq_npoints = 1
csq_prompt = "Let's put these two cases together; in the worst case scenario, what is the number of subproblems we have? Use your answers from the previous two problems. You can also use `subproblems_if_egg_doesnt_break`, `subproblems_if_egg_breaks`, and the functions `min` and `max`."
csq_soln = '''def subproblems_i(f, i, e):
    return max(X(i-1, e-1), X(f-i, e))'''

csq_initial = '''def subproblems_i(f, i, e):
    return X(None, None) #TODO
'''

csq_code_pre = '''def X(a, b):
    return (a**(2) + b**(3)/6)*(a+22)

def subproblems_if_egg_doesnt_break(f, i, e):
    return X(f-i, e)

def subproblems_if_egg_breaks(f, i, e):
    return X(i-1, e-1)
'''

tests = [(2, 2),
         (4, 4),
         (10, 5),
         (20, 20),
         (100, 100),
         (1000, 1000)]
        
csq_tests = []
for test_num, t in enumerate(tests):
    f_range, e_range = t
    f = cs_random.randint(1, f_range)
    i = cs_random.randint(1, f)
    e = cs_random.randint(1, e_range)
    csq_tests.append({
        'code': f"""
ans = subproblems_i({f}, {i}, {e}) """,
        'show_code': False,
        'grade': True
    })
</question>

<question pythoncode>
csq_interface = "ace"
csq_npoints = 1
csq_prompt = """Now we can try to put everything together in order to define our recurrence, $X(f,e)$. We want to define the recurrences in dynamic programming in such a way that dependences will not be cyclic (see previous pset for what that means).

A way that we commonly do this is that we define the recurrences to depend on subproblems with smaller parameters (i.e. smaller values of $f$ and/or $e$). That way there is a clear order for when we should calculate our subproblems.

Try to define $X(f,e)$ in terms of subproblems with smaller values of $f$ and/or $e$. You can use all of the functions we have defined or mentioned so far. Ignore special/base cases for now. Hint: how do we pick which floor $i$ we should drop the egg from first? 

Don't forget to take into account your most recent eggthrow"""

csq_soln = '''def subproblems(f, e):
    if f == 0:
        return 0
    else:
        m = min([subproblems_i(f, i, e) for i in range(f)]) + 1
    return m'''

csq_initial = '''def subproblems(f, e):
    return X(None, None) #TODO
'''

csq_code_pre = '''def X(a, b):
    return (a**(2) + b**(3)/6)*(a+22)

def subproblems_i(f, i, e):
    return max(X(i-1, e-1), X(f-i, e))

def subproblems_if_egg_doesnt_break(f, i, e):
    return X(f-i, e)

def subproblems_if_egg_breaks(f, i, e):
    return X(i-1, e-1)
'''

tests = [(2, 2),
         (4, 4),
         (10, 5),
         (20, 20),
         (100, 100),
         (1000, 1000)]
        
csq_tests = []
for test_num, t in enumerate(tests):
    f_range, e_range = t
    f = cs_random.randint(1, f_range)
    e = cs_random.randint(1, e_range)
    csq_tests.append({
        'code': f"""
ans = subproblems({f}, {e}) """,
        'show_code': False,
        'grade': True
    })
</question>

<question multiplechoice>
csq_prompt = "Next, remember that you should never ever ever recurse without base cases. Which of the following are correct? Hint: if a scenario is impossible, it's common to say that we need $\\infty$ steps to solve the problem."
csq_renderer = "checkbox"
csq_options = ["$x(0, e) = 1$", "$x(0, e) = 0$", "$x(f, 0) = \\infty$", "$x(f, 0) = f$", "$x(f, 0) = 1$"]
csq_soln = [0,1,1,0,0]
csq_explanation = ""
</question>

Now we have a general expression for $X(f, e)$, where we can vary the number of floors $f$ and the number of eggs $e$. We can use this to solve the recurrence for $X(n, k)$ (since our building has $n$ floors and we have $k$ eggs, where $n$ and $k$ are fixed constants).

Let's calculate the run-time required to solve for $X(n, k)$.

<question expression>
csq_prompt = "How many subproblems do you have? (How many different instances of $X(f, e)$ will we run?) Express in Theta notation."
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
csq_soln = "Theta(n^2 * k)"
csq_explanation = ""
</question>
