# Readings 
Recitation notes 5, 6.006 Fall 2018 on stellar.

Lecture notes 5, 6.006 Fall 2018 on stellar.

# Priority Queues: Conceptual Questions


<question multiplechoice>
csq_prompt = "Which of the following operations do most priority queues execute efficiently?"
csq_renderer = "checkbox"
csq_soln = [1,1,0,1,0]
csq_options =  ['Return the length of the set',
'Remove the element with the greatest (or least) key',
'Sort the elements of a set by key',
'Insert an element with some key',
'Remove an element with a particular key']
csq_name="pq1"
</question>

<question multiplechoice>
csq_prompt = "Which of the following would be considered a priority queue?"
csq_renderer = "checkbox"
csq_soln = [1,1,0,1]
csq_options =  ['An unsorted array, where, upon being asked for the max, searches through the entire array and returns the element with maximal key',
'A sorted array, where each element is inserted into the proper location by key (in descending order), and upon being asked for the max returns the first element',
'A binary search tree, as seen in PS16',
'A binary max heap']
csq_name="pq2"
</question>

<checkyourself>
If a priority queue (with unique keys) is optimized to return and remove the element with the greatest key value in $O(\log n)$ time, can it return the second greatest key in $O(\log n)$ time as well? How?
<showhide>
Yes. First, remove the element with the greatest key in $O( \log n)$ time and store it. Then, remove the next element with greatest key: this was the element with the second greatest key originally. Reinsert the first element we had to remove, if necesarry.
</showhide>
</checkyourself>


# Binary Heaps: Structure

Recall that binary heaps are *complete binary trees*, meaning that they are binary trees in which every row, except possibly the last, is fully filled. When the last row is not full, the leafs are filled in left to right. 

This means that, given $k$ levels/ rows to a binary heap, there are  
$n = \sum_{i = 0}^{k-2} 2^i + r = 2^{k-1} + r - 1 \geq 2^{k-1}$
elements in the heap, where $r$ represents the number of elements in the last, possibly incomplete level (so $0 < r \leq 2^{k-1}$). With this result we see that $2^{k-1} \leq n$, so $k-1 \leq \log(n)$ and so $k = \log (n)$. This bound on the height of the tree allows us to argue that the operations we use a heap for really are $O(\log n)$. 

In the following questions we explore the completeness of binary heaps.
<question expression>
csq_prompt = "If a binary tree has $41$ elements, how many rows does it have?"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["6"]
csq_explanation = "explanation"
csq_nsubmits = None
</question>

<question multiplechoice>
csq_prompt = "In the previous example, is the last row complete?"
csq_renderer = "radio"
csq_soln = [0,1]
csq_options =  ['Yes',
'No']
csq_name="pq1"
</question>



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

