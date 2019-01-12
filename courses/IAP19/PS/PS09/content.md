# Readings 
Recitation notes 4, 6.006 Fall 2018 on stellar.

Lecture notes 4, 6.006 Fall 2018 on stellar.
# Dynamic Arrays

Recall that arrays are blocks of memory allocated by the computer to store elements.

<question expression>
    csq_prompt = "Wumpus has an array that has been allocated enough memory to store $n$ elements. There are currently $n-1$ elements in the array. How long does it take to store the $n$th element? Give an asympotic runtime: O(something). \n \n \n"
    csq_show_check = True
    csq_allow_check = True
    csq_allow_submit = True
    csq_allow_submit_after_answer_viewed = False
    csq_soln = ["O(1)"]
    csq_nsubmits = None
    csq_name = "exp1"
</question>

<question expression>
    csq_prompt = "Wumpus now wants to add an $n+1$th element to the array. How long does that take? Give an asympotic runtime: O(something). \n \n \n"
    csq_show_check = True
    csq_allow_check = True
    csq_allow_submit = True
    csq_allow_submit_after_answer_viewed = False
    csq_soln = ["O(n)"]
    csq_nsubmits = None
    csq_name = "exp2"
</question>

<question expression>
    csq_prompt = "Wumpus has implemented a dynamic array that he calls $ALO^{TM}$(allocate-less-often) which allocates $n/4$ additional memory. On average, how many insertions can $ALO$ perform for every new allocation of the array?"
    csq_show_check = True
    csq_allow_check = True
    csq_allow_submit = True
    csq_allow_submit_after_answer_viewed = False
    csq_soln = ["n/4"]
    csq_nsubmits = None
    csq_name = "exp3"
</question>

<question expression>
    csq_prompt = "Wumpus has implemented a dynamic array that he calls $ALO^{TM}$(allocate-less-often) which allocates $n/4$ additional memory. On average, how many insertions can $ALO$ perform for every new allocation of the array?"
    csq_show_check = True
    csq_allow_check = True
    csq_allow_submit = True
    csq_allow_submit_after_answer_viewed = False
    csq_soln = ["n/4"]
    csq_nsubmits = None
    csq_name = "exp4"
</question>

<question multiplechoice>
    csq_prompt = "Which of these space allocations will allow dynamic arrays to achieve an amortized constant insertion operation?"
    csq_renderer = "checkbox"
    csq_soln = [1,0,1,1,0]
    csq_options =  ['Allocating $2n$ space',
    'Allocating 2 addtional spaces',
    'Allocating $n/1000$ addional spaces',
    'Allocating $c*n$ additional space, where $c$ is some constant number',
    'Allocating 2*x, where x is a random number between 1 and 100']
    csq_name="mc1"
</question>

<checkyourself>
    Does a dynamic array, as discussed in lecture, support $O(1)$ insertions at the beginning of the array?
    <showhide>
        No, because there is no additional space allocated at the beginning of the array. If we want to insert an element at the beginning, we will have to move all elements right, which takes $O(n)$ time.
    </showhide>
</checkyourself>

<question multiplechoice>
csq_prompt = "Question?"
csq_renderer = "checkbox"
csq_soln = [1,0,0,0]
csq_options =  ['option 1',
'option 2',
'option 3',
'option 4']
csq_name="qexample1"
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

