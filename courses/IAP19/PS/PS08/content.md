# Readings 
Recitation notes 4, 6.006 Fall 2018 on stellar.

Lecture notes 4, 6.006 Fall 2018 on stellar.

# Arrays

<python>
#tutor.init_random()
</python>


<question pythoncode>

csq_npoints = 4;
csq_interface = 'ace'
csq_prompt = """
Write a function to simulate the $uniq$ function in Linux, which takes an array of items, and removes consecutive duplicates. \n

For example, $uniq([1, 1, 4, 2, 5, 1, 1, 1, 5, 5, 5])$ should return $[1, 4, 2, 5, 1, 5]$.

Note that the original order is preserved, and that only the consecutive duplicates are removed.
"""

## Define solution that will be printed to student.
csq_soln = """
def uniq(A): 
    result = [A[0]]              # first element
    for i in range(1, len(A)):
        if A[i] != result[-1]:   # not the same as the last element added
            result.append(A[i])
    return result
"""

## Code that will be initially on the thingy
csq_initial = """def uniq(A): 
    return A
"""
csq_name= "pcode5"

## Code that will be written before the user code as well as solution
## Particularly useful for defining classes and things that we don't want the user to modify
## For example, define a DFS function.
csq_code_pre = ""


## Code that will be written after the user code as well as solution code
## Seems quite useless to me.
csq_code_post = """
import resource
assert resource.getrusage(resource.RUSAGE_SELF)[0]<0.35, "you used too much cpu!"
"""


## Sandbox options to block libraries or decide how long to run thingy
csq_sandbox_options = {
    'BADIMPORT': ['lib601', 'numpy', 'scipy', 'matplotlib'], 
     'CLOCKTIME': 1.0, 
    #'CPUTIME': 0.10, 
    'MEMORY':1e9
}


## Now we define helper functions
def generate_test(k, m, n):
    return [x for y in [[cs_random.randint(-k,k)] * cs_random.randint(1,m) for x in range(n)] for x in y]

tests = [(2, 4, 4),
         (2, 4, 8),
         (10, 10, 20),
         (30, 30, 30),
         (50, 30, 300),
         (50, 1000, 300),
         (50, 10000, 30),
         (50, 10000, 30),
         (50, 20000, 30),]
full_tests = [generate_test(*i) for i in tests]


## Now we need to write csq_tests, which defines what code to run
## As well as how to test it. 
## Each csq_tests is a dictionary of things (code, check, etc)

## We need to define the key code, which returns a string that will be evaluated with both the user code as well as our solution.
## Code should define a string called ans, which is what will be tested.

## We also define the key check_function, which is a function that takes escaped ans (a string, usually you will want to eval it.) from running user code, ans from running the solution, and i(index of the test), and then returns True or False.

csq_tests = []
for i, t in enumerate(tests):

        
    csq_tests.append({
        'code': f"""
A = {full_tests[i]}
ans = uniq(A)
""" ,
        'show_code': i<4,
        'grade': True,
    })

</question> 

