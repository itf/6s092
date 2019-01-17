# Readings 
Recitation notes 8, 6.006 Fall 2018 on stellar.


# Radix Sort

## Tuple sort

In tuple sort, we sort from least significant to most significant by using a stable sort.

Suppose we are sorting tuples of the form (A,B,C), e.g. (3,7,2) using tuple sort, where we want them to be fist sorted by A, then by B, then by C. 


<question multiplechoice>
csq_prompt = "If I use tuple sort with a stable sort in what order should I sort the tuples by each of their keys? "
csq_renderer = "checkbox"
csq_soln = [0,1,0,0]
csq_options =  ['First by A, then by B, then by C',
'First by C, then by B, then by A',
'First by A, then by C, then by B',
'First by C, then by A, then by B']
</question>

<question multiplechoice>
csq_prompt = "Suppose our list of tuples is [(0,4,4), (2,2,3), (1,2,4), (0,3,4)] and I sort it based on the first element of the tuple using a stable sort. What is the result?"
csq_renderer = "checkbox"
csq_soln = [0,1,0,0]
csq_options =  ['[(0,4,4), (2,2,3), (1,2,4), (0,3,4)]',
'[(0,4,4),  (0,3,4), (1,2,4),  (2,2,3)]',
'[(2,2,3), (0,4,4), (1,2,4), (0,3,4)]',
'[(0,3,4), (0,4,4), (2,2,3), (1,2,4)]']
</question>


<question multiplechoice>
csq_renderer = "radio"

csq_prompt = """
Eve really dislikes stable sorts and says that: "I don't need to use a stable sort 3 times in order to do tuple sort on my tuple of 3 elements. I could instead sort based on the last element using a not stable sort followed by 2 stable sorts for the first 2 fields."

Is Eve correct? Would the algorithm still work if we used a non-stable sort in the first step?   
"""
csq_soln = "Yes"
csq_options =  ['No',
'Yes']
</question>

## Building on top of counting sort 

Suppose I am sorting $n$ elements keyed by positive integers upperbounded by $n^2$.

<question expression>
csq_prompt = "How long would it take to sort those $n$ elements using counting sort?"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_allow_viewexplanation = True

csq_soln = ["O(n^2)", "theta(n^2)", "O(n^2,w)", "theta(n^2,w)"]
csq_explanation = "We need to allocate a direct access array of lenght $n^2$"
csq_nsubmits = None
</question>

<question multiplechoice>
csq_renderer = "radio"

csq_prompt = """
Wumpus really dislikes stable sorts and says that: "I don't need to use a stable sort 3 times in order to do tuple sort on my tuple of 3 elements. I could instead sort based on the last element using a not stable sort followed by 2 stable sorts for the first 2 fields."

Is Wumpus correct? Would the algorithm still work if we used a non-stable sort in the first step?   
"""
csq_soln = "Yes"
csq_options =  ['No',
'Yes']
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

