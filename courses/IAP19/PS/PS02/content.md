# Readings 
[Recitation notes 2](https://learning-modules.mit.edu/service/materials/groups/238004/files/e32bf8b0-6f52-4813-af38-5b1664dda1eb/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), 6.006 Fall 2018 on stellar.

# Recursions and recursion tree


## Recursions

<question multiplechoice>
csq_prompt = "Which of the following recursions are equivalent (i.e. we can always simplify the left to be the right)?"
csq_renderer = "checkbox"
csq_soln = [1,0,0,0]
csq_options =  ['$T({n\over 2}) + T({n\over 2}) + f(n)\ = 2T({n\over 2}) + f(n)$',
'$T({n\over 2}) + T({n\over 2}) + f(n)\ = T({n}) + f(n)$',
'$T({n}) + O(n)\ = T({n}) + n$',
'$T({n}) + O(n)\ = T({n}) + \\theta(n)$']
</question>

<question multiplechoice>
csq_prompt = "If $T(n) = a T(n/b) + O(f(n))$ and $T'(n) = a T'(n/b) + \\theta(f(n))$, which of the following is necessarily true?"
csq_renderer = "checkbox"
csq_soln = [0,0,0,1]
csq_options =  ["$T(n) = T'(n)$",
"$T(n) = \\theta(T'(n))$",
"$T'(n) = O(T(n))$",
"$T(n) = O(T'(n)) $"]
</question>





Bob told me that he invented a sort algorithm that splits an array into 3 equal parts, sorts each one of them, and then merges in $O(n)$ the 3 parts.
What is the recursion for the algorithm?
<question expression>
csq_prompt = "$T(n)=$ "
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["3*T(n/3)+O(n)"]
csq_explanation = "3 parts of 1/3 of the size + the work to join"
csq_nsubmits = None
</question>


Now Bob told me that he invented a sort algorithm that splits an array into 2 parts, the first third of the array and the other 2 thirds of the array. It sorts each one of them, and then merges  in $O(n)$ the 2 parts.
What is the recursion for the algorithm? 
<question expression>
csq_prompt = "$T(n)=$ "
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["T(n/3)+T(2*n/3)+O(n)"]
csq_explanation = "2 parts. One of 1/3, one of 2/3 of the size + the work to join"
csq_nsubmits = None
</question>


## Proving the weak master theorem using recursion trees
Consider the following recursion: 

$$T(n) = aT\left(\frac{n}{b}\right) + n^c$$ 


<checkyourself>
Draw it as a recursion tree.

<showhide>
The root contains one node with n elements. What happens on the following levels?
</showhide>
</checkyourself>

 Answer the following about the tree. Assume that the root is the first level, and the immediate children of the root are on the second level. 

 More specifically: the level of a node is defined as: 1 + the number of edges between the node and the root. [source: wikipedia](https://en.wikipedia.org/wiki/Tree_(data_structure))

### Work per level
<question expression>
csq_prompt = "Number of nodes on the second level: "
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["a"]
csq_explanation = "The number of nodes got larger"
csq_nsubmits = None
</question>

<question expression>
csq_prompt = "Number of elements in the nodes of the second level: "
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["n/b"]
csq_explanation = "The number of elements per node got smaller"
csq_nsubmits = None
</question>

<question expression>
csq_prompt = "Amount of work done in each node in the second level: "
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["(n/b)^c"]
csq_explanation = "The number of elements per node got smaller"
csq_nsubmits = None
</question>

<question expression>
csq_prompt = "Total work done in the second level: "
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["a*(n/b)^c"]
csq_explanation = "The number of elements per node got smaller, but the number of nodes increased."
csq_nsubmits = None
</question>


<question expression>
csq_prompt = """Suppose the amount of work done in the first level is $x$ and the amount of work in the second level is $y$.

What is $\\frac{y}{x}$ In terms of $a, b, c, n$?
"""
csq_error_on_unknown_variable = True #make sure they get rid of n in the answer
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["a/(b^c)"]
csq_nsubmits = None
</question>

<question expression>
csq_prompt = """Suppose the amount of work done in the first level is $x$ and the amount of work in the $i_{th}$ level is $y$.

What is $\\frac{y}{x}$ in terms of $a, b, c, n, i$?
"""
csq_error_on_unknown_variable = True #make sure they get rid of n in the answer
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["(a/(b^c))^i"]
csq_nsubmits = None
</question>


<question expression>
csq_prompt = """Suppose the amount of work per level is constant. 

If  $\\frac{y}{x} =1$,  what is $c$ in terms of $a$ and $b$?  To write $\log_x(y)$, please write $\log(y,x)$
"""
csq_error_on_unknown_variable = True #make sure they get rid of n in the answer
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["log(a,b)", "log(a)/log(b)"]
csq_nsubmits = None
csq_name="vdadsvds"
</question>

### Height and base level
Now, let's talk about the **height** of the tree. *Don't worry about off by one errors*. If the height of the tree is h, both h and $h\pm 1$ will be accepted as correct answers if it results in a simpler formula.

<question expression>
csq_prompt = """Given that the root contains $n$ elements, and the second level nodes contains $n/b$ elements. 

How many elements will the nodes of $i_{th}$ level have?
"""
csq_error_on_unknown_variable = True  #make sure they get rid of a in the answer
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["n/b^i","n/b^(i-1)"]
csq_nsubmits = None
</question> 


<question expression>
csq_prompt = """In what level will the nodes have **exactly** $1$ element. Assume that n is a power of b.


To write $\log_x(y)$, please write $\log(y,x)$
"""
csq_error_on_unknown_variable = True  #make sure they get rid of a in the answer
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["log(n,b)", "log(n)/log(b)", "log(n,b)+1", "log(n)/log(b)+1"]
csq_nsubmits = None
</question> 


<question expression>
csq_prompt = """Given that the root contains 1 node, and the second level contains $a$ nodes. 

How many nodes will the $i_{th}$ level have?
"""
csq_error_on_unknown_variable = True  #make sure they get rid of a in the answer
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["a^i", "a^(i-1)"]
csq_nsubmits = None
</question> 


<question expression>
csq_prompt = """Given that the root contains 1 node, and the second level contains $a$ nodes. 

How many nodes will the last level have?
"""
csq_error_on_unknown_variable = True  #make sure they get rid of a in the answer
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["a^log(n,b)", "n^log(a,b)"]
csq_nsubmits = None
</question> 

Note that 
$$A^{\log_B(C)} = \left(B^{\log_B(A)} \right) ^ {\log_B(C)}$$
$$ = B^{\log_B(A) \log_B(C)} = B^{\log_B(C) \log_B(A) } $$
$$ = C^{\log_B(A)}$$

So rewrite the previous expression in the form $n^{exponent}$

<question expression>
csq_prompt = """Given that the root contains $n$ elements, and the second level contains $a$ nodes. 

How many nodes will the last level have?
"""
csq_error_on_unknown_variable = True  #make sure they get rid of a in the answer
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = "n^log(a,b)"
csq_nsubmits = None
</question> 

### 2nd case of the weak version of the master theorem
Now let's use the above to calculate the amount of work per level.

If $\frac{a}{b^c} = 1$, i.e. $c = \log_b(a)$  What is the total amount of work done on the tree? Is it constant per level? Remember that the total work on the root is $n^c$.

 <question expression>
csq_prompt = """What is the total amount of work done in the tree?
"""
csq_error_on_unknown_variable = True  #make sure they get rid of a in the answer
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = "n^c * log(n,b)"
csq_nsubmits = None
</question> 



### 1st case of the weak version of the master theorem
Now, let's prove the first case, when the recursion tree is root heavy.

<checkyourself>
Write the total amount of work done in the tree as a sum, starting at the root.
<showhide>
$$n^c \sum_{i=0}^{\log_b(n)} \left(\frac{a}{b^c}\right)^i $$
</showhide>
</checkyourself>


<checkyourself>
If $\frac{a}{b^c} < 1$, i.e. $c > \log_b(a)$, does the amount of work increase or decrease per level? 
<showhide>
Decreases by $\frac{a}{b^c}$
</showhide>
</checkyourself>

The amount of work per level decreases geometrically per level. We can find an upper bound for the total work done in the tree by taking the bound of the sum to $\infty$.

<checkyourself>
What is the new sum?
<showhide>
$$n^c \sum_{i=0}^{\infty} \left(\frac{a}{b^c}\right)^i $$
</showhide>
</checkyourself>

What does the sum converges to?

 <question expression>
csq_prompt = """What does the sum that upper bounds the work on the tree converges to?
"""
csq_error_on_unknown_variable = True  #make sure they get rid of a in the answer
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = "n^c*(1/(1-(a/b^c)))"
csq_nsubmits = None
</question> 

You know that the total amount of work done in the tree is lower bounded by the amount of the work done on the root, $n^c$. Since we just showed that it is upper bounded by the value you calculated, you have that the total amount of work done on the tree is $\theta(n^c)$.


<checkyourself>
Suppose we know that it's the 1st case of the weak version of the master theorem, and the recursion was:
$$T(n) = aT\left(\frac{n}{b}\right) + O(n^c)$$
Instead of:
$$T(n) = aT\left(\frac{n}{b}\right) + n^c$$

What would be the total work on the tree?
<showhide>
$$O(n^c)$$
</showhide>
</checkyourself>

### 3rd case of the weak version of the master theorem
Now, let's prove the third case, when the recursion tree is leaf heavy. This is the hardest one to prove.



<checkyourself>
If $\frac{a}{b^c} > 1$, i.e. $c < \log_b(a)$, does the amount of work increase or decrease per level? 
<showhide>
Increases by $\frac{a}{b^c}$
</showhide>
</checkyourself>

Since the amount of work per level increases, we will write the total amount of work done in the tree by writing a sum starting from the leaves.

We previously calculated that the number of leaf nodes is $n^{log_b(a)}$. Since each leaf node has an input size of $\theta(1)$, the amount of work we do for each leaf node is $\theta(1)$. So the total work done on the leaf nodes is $n^{log_b(a)}$. Furthermore, we know that the total amount of work decreases by $\frac{b^c}{a}$ per level when going up the tree.


<checkyourself>
What is the total amount of work done in the tree as a sum, starting at the leaves? The total amount of work on the leaves is $n^{log_b(a)}$.
<showhide>
$$n^{log_b(a)} \sum_{i=0}^{\log_b(n)} \left(\frac{b^c}{a}\right)^i$$
</showhide>
</checkyourself>


Since the amount of work per level decreases geometrically per level, we can find an upper bound to this sum by taking the bound of the sum to $\infty$.

<checkyourself>
What is the new sum?
<showhide>
$$n^{log_b(a)} \sum_{i=0}^{\infty} \left(\frac{b^c}{a}\right)^i$$</showhide>
</checkyourself>



 <question expression>
csq_prompt = """What does this sum (the upper bound on the total amount of work on the tree) converge to?
"""
csq_error_on_unknown_variable = True  #make sure they get rid of a in the answer
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = "n^log(a,b)*(1/(1-(b^c/a)))"
csq_nsubmits = None
</question> 

You know that the total amount of work done in the tree is lower bounded by the amount of the work done on the leaves, $n^{\log_b(a)}$. Furthermore, you just calculated an upper bound for that total amount of work. The two of them together shows that the total amount of work done on the tree is $\\theta(n^{\log_b(a)})$

<checkyourself>
Suppose that we know that it's the third case of the weak version of the master theorem, and the recursion was:
$$T(n) = aT\left(\frac{n}{b}\right) + O(n^c)$$
Instead of:
$$T(n) = aT\left(\frac{n}{b}\right) + n^c$$

What would be the total work on the tree?
<showhide>
$$\theta(n^{\log_b(a)})$$
Notice that since the total amount of work is only dependent on the number of leaves, the amount of work per node getting smaller, does not affect the asymptotic bound on the work. 
</showhide>
</checkyourself>

<question pythoncode>
csq_interface = 'ace'
csq_prompt = "Write a recursive function to implement exponentiation. Given nonnegative integers $a$, $n$, return $a^n$. Do NOT use the operator (a**n), or any for loops. Instead, use $a^n = a * a^{n-1}$"

csq_npoints = 2


## Define solution that will be printed to student.
csq_soln = """
def pow(a, n): 
	if n == 0:
		return 1
	else:
		return a * pow(a, n - 1)
"""

## Code that will be initially on the thingy
csq_initial = """def pow(a, n): 
    return 0
"""
csq_name= "ps2code0"

## Code that will be written before the user code as well as solution
## Particularly useful for defining classes and things that we don't want the user to modify
## For example, define a DFS function.
csq_code_pre = ""


## Code that will be written after the user code as well as solution code
## Seems quite useless to me.
csq_code_post = ""

## Sandbox options to block libraries or decide how long to run thingy
csq_sandbox_options = {
    'BADIMPORT': ['lib601', 'numpy', 'scipy', 'matplotlib'], 
    #'CLOCKTIME': 0.30, 
     'CPUTIME': 0.10, 
    'MEMORY':1e9
}


## Now we define helper functions
tests = [(0,0), (1, 5), (5, 4), (6, 3), (2, 24), (99, 7), (44, 53), (89, 4), (43, 23), (91, 86), (71, 44), (20, 72), (85, 4), (38, 44), (54, 82), (27, 48), (52, 21), (99, 89), (85, 12), (46, 21), (39, 63), (22, 69), (35, 20), (47, 59), (30, 33), (32, 17)]

#def is_correct(a, n, sol):
#    return (a**n == sol) 

## Now we need to write csq_tests, which defines what code to run
## As well as how to test it. 
## Each csq_testsgi is a dictionary of things (code, check, etc)

## We need to define the key code, which returns a string that will be evaluated with both the user code as well as our solution.
## Code should define a string called ans, which is what will be tested.

## We also define the key check_function, which is a function that takes escaped ans (a string, usually you will want to eval it.) from running user code, ans from running the solution, and i(index of the test), and then returns True or False.

csq_tests = []
for i, t in enumerate(tests):

#    def check(ans, soln, i = i):
#        a, n = tests[i]
#        return is_correct(a, n, eval(ans))
        
    csq_tests.append({
        'code': f"""
a, n = {tests[i]}
ans = pow(a, n)
""" ,
        'show_code': i < 5,
        'grade': True,
        #'check_function': check
    })

</question> 

<checkyourself>
Write a recurrence for the runtime of the above code. Use the tree method or the master theorem to solve for the work. What is the total asymptotic runtime?

<showhide>
$$T(n) = T(n-1) + O(1)$$
The tree has height $n$ with $O(1)$ work per node.
The overall runtime is $O(n)$.
</showhide>
</checkyourself>

<question pythoncode>
csq_interface = 'ace'
csq_prompt = "Define the same function, but this time use the following observation. If $n$ is even, then $a^n =  a^{n//2} * a^{n//2}$. If $n$ is odd, then $a^n = a * a^{n//2} * a^{n//2}$. Again DO NOT use the in-built power operator or a for loop."

csq_npoints = 2

## Define solution that will be printed to student.
csq_soln = """
def pow(a, n): 
	if n == 0:
		return 1
	else:
		x = pow(a, n//2)
		if n % 2 == 0:
			return x * x
		else: 
			return a * x * x
"""

## Code that will be initially on the thingy
csq_initial = """def pow(a, n): 
    return 0
"""
csq_name= "ps2code1"

## Code that will be written before the user code as well as solution
## Particularly useful for defining classes and things that we don't want the user to modify
## For example, define a DFS function.
csq_code_pre = ""


## Code that will be written after the user code as well as solution code
## Seems quite useless to me.
csq_code_post = ""

## Sandbox options to block libraries or decide how long to run thingy
csq_sandbox_options = {
    'BADIMPORT': ['lib601', 'numpy', 'scipy', 'matplotlib'], 
    #'CLOCKTIME': 0.30, 
     'CPUTIME': 0.10, 
    'MEMORY':1e9
}


## Now we define helper functions
tests = [(0,0), (1, 5), (5, 4), (6, 3), (2, 24), (99, 7), (44, 53), (89, 4), (43, 23), (91, 86), (71, 44), (20, 72), (85, 4), (38, 44), (54, 82), (27, 48), (52, 21), (99, 89), (85, 12), (46, 21), (39, 63), (22, 69), (35, 20), (47, 59), (30, 33), (32, 17)]

#def is_correct(a, n, sol):
#    return (a**n == sol) 

## Now we need to write csq_tests, which defines what code to run
## As well as how to test it. 
## Each csq_tests is a dictionary of things (code, check, etc)

## We need to define the key code, which returns a string that will be evaluated with both the user code as well as our solution.
## Code should define a string called ans, which is what will be tested.

## We also define the key check_function, which is a function that takes escaped ans (a string, usually you will want to eval it.) from running user code, ans from running the solution, and i(index of the test), and then returns True or False.

csq_tests = []
for i, t in enumerate(tests):

#    def check(ans, soln, i = i):
#        a, n = t
#        return is_correct(a, n, eval(ans))
        
    csq_tests.append({
        'code': f"""
a, n = {tests[i]}
ans = pow(a, n)
""" ,
        'show_code': i < 5,
        'grade': True,
        #'check_function': check
    })

</question> 

<checkyourself>
Write a recurrence for the runtime of the above code. What is the total asymptotic runtime?

<showhide>
$$T(n) = T(n/2) + O(1)$$
The tree has height $\log{n}$ with $O(1)$ work per node.
The overall runtime is $O(\log{n})$.
</showhide>
</checkyourself>

