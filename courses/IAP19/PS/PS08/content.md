# Readings 
[Lecture notes 4](https://learning-modules.mit.edu/service/materials/groups/238004/files/aad7a820-c5b5-4eba-aff2-79bbdc1355e4/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), 6.006 Fall 2018 on stellar.

[Recitation notes 4](https://learning-modules.mit.edu/service/materials/groups/229217/files/a78ef148-8b86-4ef1-bcf1-bd99fd961120/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), 6.006 Fall 2018 on stellar.
# Dynamic Arrays

Recall that arrays are blocks of memory allocated by the computer to store elements.


<question expression>
    csq_prompt = "Wumpus has an array that has been allocated enough memory to store $n$ elements. There are currently $n-1$ elements in the array. How long does it take to store the $n$th element? Give an asympotic runtime: $\\theta(something)$. Use $theta$ to denote the theta symbol. \n \n \n"
    csq_show_check = True
    csq_allow_check = True
    csq_allow_submit = True
    csq_allow_submit_after_answer_viewed = False
    csq_soln = "theta(1)"
    csq_nsubmits = None
    csq_name = "exp1"
    csq_funcs = {"T": (lambda c: c**3*0.6006+c**2, lambda  c:  f"T({', '.join(c)})" ),
    "O": (lambda c: c**3*1.6006-c**2, lambda  c:  f"O({', '.join(c)})" ),
    "theta": (lambda c: -c**3*0.06006+c**2*0.2, lambda  c:   f"\\theta({', '.join(c)})")}
    </question>

Assume that when we have a full array of size $n$, and we need to perform a new array allocation, it takes $n$ operations to copy the $n$ values (there are also additional operations like creating a new array, and deleting the old one, but let us consider that to be overhead).

<question expression>
    csq_prompt = "Wumpus now wants to add an $n+1$th element to the array. How long does that take? GGive an asympotic runtime: $\\theta(something)$. Use $theta$ to denote the theta symbol. \n \n \n"
    csq_show_check = True
    csq_allow_check = True
    csq_allow_submit = True
    csq_allow_submit_after_answer_viewed = False
    csq_soln = "theta(n)"
    csq_nsubmits = None
    csq_name = "exp2"
    csq_funcs = {"T": (lambda c: c**3*0.6006+c**2, lambda  c:  f"T({', '.join(c)})" ),
    "O": (lambda c: c**3*1.6006-c**2, lambda  c:  f"O({', '.join(c)})" ),
    "theta": (lambda c: -c**3*0.06006+c**2*0.2, lambda  c:   f"\\theta({', '.join(c)})")}
</question>

Wumpus has implemented a dynamic array that he calls $ALO^{TM}$(allocate-less-often) which allocates $n/4$ additional spaces. We will run an analysis to ensure that his array actually achieves the amortized constant bound for insertions.

<question expression>
    csq_prompt = "Wumpus' array just performed a space allocation. It now has $n/4$ additional spaces, compared to the original $n$ spaces before allocation, (for a total of ${5*n}/4$ total spaces). How many insertions can $ALO$ perform in constant $O(1)$ time for every new allocation of the array? Assume space allocation is a separate operation, and we can place the last element in constant time. Give a specific value, ie $2$, $n/10$, not an asymptotic bound. \n \n \n"
    csq_show_check = True
    csq_allow_check = True
    csq_allow_submit = True
    csq_allow_submit_after_answer_viewed = False
    csq_soln = "n/4"
    csq_nsubmits = None
    csq_name = "exp3"
</question>

<question expression>
    csq_prompt = "Per allocation, how many times does Wumpus' dynamic array perform an $\\theta(n)$ operation? \n \n \n"
    csq_show_check = True
    csq_allow_check = True
    csq_allow_submit = True
    csq_allow_submit_after_answer_viewed = False
    csq_soln = "1"
    csq_nsubmits = None
    csq_name = "exp5"
</question>

<question expression>
    csq_prompt = "How many operations are done per allocation, in terms of insertions and the creation of a larger array? Give a specific value. \n \n \n"
    csq_show_check = True
    csq_allow_check = True
    csq_allow_submit = True
    csq_allow_submit_after_answer_viewed = False
    csq_soln = "n+n/4"
    csq_nsubmits = None
    csq_name = "exp6"
</question>

<question expression>
    csq_prompt = "By dividing the total number of operations done per allocation cycle by the number of of insertions per allocation cycle, we can get the average amount of operations done per insertion. If each operation takes a constant amount of work and the average number of operations done per insertion is constant, then we can prove our constant amortized bound for insertions. Find the average number of operations done per insertion. Give a specific value. \n \n \n"
    csq_show_check = True
    csq_allow_check = True
    csq_allow_submit = True
    csq_allow_submit_after_answer_viewed = False
    csq_soln = "5"
    csq_nsubmits = None
    csq_name = "exp7"
</question>

<question multiplechoice>
    csq_prompt = "Which of these space allocations will allow dynamic arrays to achieve an amortized constant insertion operation?"
    csq_renderer = "checkbox"
    csq_soln = [1,0,1,1,0]
    csq_options =  ['Allocating $2n$ space',
    'Allocating $2$ addtional spaces',
    'Allocating $n/1000$ addional spaces',
    'Allocating $c*n$ additional space, where c is some constant non-zero number',
    'Allocating $2x$, where $x$ is a random number between 1 and 100']
    csq_name="mc1"
</question>

<checkyourself>
    Does a dynamic array, as discussed in lecture, support $\theta(1)$ insertions at the beginning of the array?
    <showhide>
        No, because there is no additional space allocated at the beginning of the array. If we want to insert an element at the beginning, we will have to move all elements right, which takes $O(n)$ time.
    </showhide>
</checkyourself>


<python>
#tutor.init_random()
</python>


<question pythoncode>

csq_npoints = 4;
csq_interface = 'ace'
csq_prompt = """
Python's lists are actually dynamic arrays! Get some coding practice with this problem: write a function to simulate the $uniq$ function in Linux, which takes an array of items, and removes consecutive duplicates. \n

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
assert resource.getrusage(resource.RUSAGE_SELF)[0]<0.5, "you used too much cpu!"
"""


## Sandbox options to block libraries or decide how long to run thingy
csq_sandbox_options = {
    'BADIMPORT': ['lib601', 'numpy', 'scipy', 'matplotlib'], 
     'CLOCKTIME': 1.7,
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
         (50, 10000, 30),]
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

