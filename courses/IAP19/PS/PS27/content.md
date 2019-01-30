# Readings 

Recitation notes 16,17, 6.006 Fall 2018 on stellar.

Lecture notes 16,17, 6.006 Fall 2018 on stellar.

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



<question expression>
csq_prompt = "Question?"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["T(n)+O(n)", "12"]
csq_explanation = "explanation"
csq_nsubmits = None
</question>

<checkyourself>
Are you understanding?
<showhide>
yeah
</showhide>
</checkyourself>



<question pythoncode>
csq_interface = 'ace'
csq_prompt = "Write your code to return a string with 4 repeated n times"

## Define solution that will be printed to student.
csq_soln = """
def print_4_ntimes(n): 
    return 'Solution will be posted to Stellar'
"""

## Code that will be initially on the thingy
csq_initial = """def print_4_ntimes(n): 
    return '4'
"""
csq_name= "pcode2"

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
    'CLOCKTIME': 0.36, 
    # 'CPUTIME': 0.36, 
    'MEMORY':1e9
}


## Now we define helped functions
tests = [cs_random.randint(1,20) for x in range(10)]

def is_correct(n, sol):
    if not(type(sol) == type('44')):
       return False
    if len(sol)==n:
        for i in range(n):
           if sol[i]!='4':
               return False
        return True
    return False

## Now we need to write csq_tests, which defines what code to run
## As well as how to test it. 
## Each csq_tests is a dictionary of things (code, check, etc)

## We need to define the key code, which returns a string that will be evaluated with both the user code as well as our solution.
## Code should define a string called ans, which is what will be tested.

## We also define the key check_function, which is a function that takes escaped ans (a string, usually you will want to eval it.) from running user code, ans from running the solution, and i(index of the test), and then returns True or False.

csq_tests = []
for i, t in enumerate(tests):

    def check(ans, soln, i = i):
        n = tests[i]
        print(ans)
        return is_correct(n, eval(ans))
        
    csq_tests.append({
        'code': f"""
n = {tests[i]}
ans = print_4_ntimes(n)
""" ,
        'show_code': i < 5,
        'grade': True,
        'check_function': check
    })

</question> 

