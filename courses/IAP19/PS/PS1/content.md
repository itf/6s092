# Readings 
Asymptotic Notation and Efficiency sections of Recitation notes 1, 6.006 Fall 2018 on stellar.


#Asymptotics

##Big O Notation

We say that $f(n) \in O(g(n)$ if there exists $n_0$ and c such that for all $n>n_0$, $f(n) \le cg(n)$, where c is a positive constant.

It is common to write $f(n) = O(g(n))$ instead of $f(n) \in O(g(n))$. Both mean the same.

Order the following functions such that if f is to the left of g, then $f(n) \in O(g(n))$. If more than one solution exists, mark all of them.

<question multiplechoice>
csq_renderer = "checkbox"
csq_soln = [1,1,1]
csq_options =  ['$(n),\ (n+4),\ (5n)$',
 '$(n+4),\ (5n),\ (n)$',
 '$(5n),\ (n+4),\ (n)$']
</question>

<question multiplechoice>
csq_renderer = "checkbox"
csq_soln = [1,1,0]
csq_options =  ['$(n),\ (n+4),\ (5n),\ (n^2),\ (n^2+n),\ (5n)^2$',
 '$(n+4),\ (5n),\ (n),\ (5n)^2,\ (n^2),\ (n^2+n)$',
 '$(n^2),\ (5n)^2,\ (n^2+n),\ (5n),\ (n),\ (n+4)$']
</question>


<question multiplechoice>
csq_renderer = "checkbox"
csq_soln = [0,1,0]
csq_options =  ['$(n\log(n)),\ (n),\ (n^2)$',
 '$(n),\ (n\log(n)),\ (n^2)$',
 '$(n),\ (n^2),\ n\log(n)$']
</question>

<question multiplechoice>
csq_renderer = "checkbox"
csq_soln = [1,0,0]
csq_options =  ['$(n\log(n)),\ (n^{1.01}),\ (n^2)$',
 '$(n^{1.01}),\ (n\log(n)),\ (n^2)$',
 '$(n^{1.01}),\ (n^2),\ n\log(n)$']
</question>

<checkyourself>
Is ${n \choose 3} \in O(n^3)$? What about  $n^3 \in O({n \choose 3})$

<showhide>
Yes and yes.
</showhide>
</checkyourself>

## Big $\Omega$

We say that $f(n) \in \Omega(g(n)$ if there exists $n_0$ and c such that for all $n>n_0$, $cf(n) \ge g(n)$, where c is a positive constant.

Order the following functions such that if f is to the left of g, then $f(n) \in \Omega(g(n))$. If more than one solution exists, mark all of them.

<question multiplechoice>
csq_renderer = "checkbox"
csq_soln = [1,1,1]
csq_options =  ['$(n),\ (n+4),\ (5n)$',
 '$(n+4),\ (5n),\ (n)$',
 '$(5n),\ (n+4),\ (n)$']
</question>

<question multiplechoice>
csq_renderer = "checkbox"
csq_soln = [0,0,1]
csq_options =  ['$(n),\ (n+4),\ (5n),\ (n^2),\ (n^2+n),\ (5n)^2$',
 '$(n+4),\ (5n),\ (n),\ (5n)^2,\ (n^2),\ (n^2+n)$',
 '$(n^2),\ (5n)^2,\ (n^2+n),\ (5n),\ (n),\ (n+4)$']
</question>


<question multiplechoice>
csq_renderer = "checkbox"
csq_soln = [0,1,0]
csq_options =  ['$(n\log(n)),\ (n),\ (n^2)$',
 '$(n^2),\ (n\log(n)),\ (n)$',
 '$(n),\ (n^2),\ n\log(n)$']
</question>

<question multiplechoice>
csq_renderer = "checkbox"
csq_soln = [0,0,1]
csq_options =  ['$(n\log(n)),\ (n^{1.01}),\ (n^2)$',
 '$(n^{1.01}),\ (n\log(n)),\ (n^2)$',
 '$(n^{2}),\ (n^{1.01}),\ n\log(n)$']
</question>


## $\theta$

We say that $f(n) \in \theta(g(n)$ if $f(n) \in O(g(n)$ and $f(n) \in \Omega(n)$

Choose the groups such that for any 2 functions in the groups, $f(n)$, $g(n)$, we have $f(n) \in \theta(g(n)$

<question multiplechoice>
csq_renderer = "checkbox"
csq_soln = [1,1,0,0,0,1,0]
csq_options =  ['$(n),\ (n+4),\ (5n)$',
 '$(n\log_2(n)),\ (n\log_3(n)),\ (n\log_{10}(n))$',
 '$(n^2),\ (n^3),\ (n^4)$',
'$(n^{2^n}),\ (n^{2^{n+1}}),\ (n^{2^{n+2}})$',
'$(n^{\log_2(5)}),\ (n^{\log_3(5)}),\ (n^{\log_5(5)})$',
'$(2^n),\ (2^{n+1}),\ (2^{n+2})$',
'$(2^{2^n}),\ (2^{2^{n+1}}),\ (2^{2^{n+2}})$']
</question>


## Recursions and recursion tree


Which of the following recursions are equivalent?

<question multiplechoice>
csq_prompt = "$T(n) =$"
csq_renderer = "checkbox"
csq_soln = [1,0,0,0]
csq_options =  ['$T({n\over 2}) + T({n\over 2}) + f(n)\ = 2T({n\over 2}) + f(n)$',
'$T({n\over 2}) + T({n\over 2}) + f(n)\ = T({n}) + f(n)$',
'$T({n}) + O(n)\ = T({n}) + n$',
'$T({n}) + O(n)\ = T({n}) + \\theta(n)$']
</question>






Bob told me that he invented a sort algorithm that splits an array into 3 equal parts, sorts each one of them, and then merges in $O(n)$ the 3 parts.
What is the recursion for the algorithm 
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


Consider the following recursion: 

$$T(n) = aT\left(\frac{n}{b}\right) + n^c$$ 

Draw it as a recursion tree. Answer the following about the tree.

<question expression>
csq_prompt = "Number of nodes on the second level: "
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["a"]
csq_explanation = ""
csq_nsubmits = None
</question>

<question expression>
csq_prompt = "Number of elements in the nodes of the second level: "
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["n/b"]
csq_explanation = ""
csq_nsubmits = None
</question>

<question expression>
csq_prompt = "Amount of work done in each node in the second level: "
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["(n/b)^c"]
csq_explanation = ""
csq_nsubmits = None
</question>

<question expression>
csq_prompt = "Total work done in the second level: "
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["a*(n/b)^c"]
csq_explanation = ""
csq_nsubmits = None
</question>

<question expression>
csq_prompt = """Suppose the amount of work done in the first level is $x$ and the amount of work in the second level is $y$.

What is $\\frac{y}{x}$?
"""
csq_error_on_unknown_variable = True #make sure they get rid of n in the answer
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["a/(b^c)"]
csq_explanation = ""
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
csq_explanation = ""
csq_nsubmits = None
csq_name="question"
</question>



