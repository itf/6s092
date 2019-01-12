# Readings 
Recitation notes 4, 6.006 Fall 2018 on stellar.

Lecture notes 4, 6.006 Fall 2018 on stellar.

# Linked List Operations

Let us represent a linked list as an array of arrays that contains "<-" which represents a left pointer, a number, and a right pointer represented by "->". If there is no left, or right pointer, let the string be replaced by "None". For example, if we were to represent the numbers 1, 2, and 3 in order as a linked list, it would look like this: [["None", 1, "->"], ["<-", 2, "->"], ["<-", 3, "None"]].

<question pythonliteral>
csq_prompt= "Wumpus has a linked list storing the numbers 100, 101, 102, and 103, in order. Wumpus adds 105 to the end. What does the linked list look like now? Give the entire linked list, represented as above. \n \n"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = [["None", 100, "->"], ["<-", 101, "->"], ["<-", 102, "->"], ["<-", 103, "->"], ["<-", 105, "None"]]
csq_nsubmits = None
csq_name="LLOp1"
</question>

<question expression>
csq_prompt= "How long does it take to insert or delete an element at the end of a linked list with $n$ elements? Give the asymptotic runtime: O(something) \n \n"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = "O(1)"
csq_nsubmits = None
csq_name="LLOp2"
</question>


<question pythonliteral>
csq_prompt= "Wumpus now deletes the first element. What does the linked list look like now? Give the entire linked list, represented as above. \n \n"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = [["None", 101, "->"], ["<-", 102, "->"], ["<-", 103, "->"], ["<-", 105, "None"]]
csq_nsubmits = None
csq_name="LLOp3"
</question>


<question expression>
csq_prompt= "How long does it take to insert or delete an element at the end of a linked list with $n$ elements? Give the asymptotic runtime: O(something) \n \n"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = "O(1)"
csq_nsubmits = None
csq_name="LLOp4"
</question>

<question expression>
csq_prompt= "Wumpus now has a linked list of numbers from $0$ to $n$. What is the asymptotic runtime of finding the $j$th elment, where $j$ is a number between $0$ and $n$ How long does it take for Wumpus to find a specific number? Give an asymptotic bound: O(something) \n \n"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = "O(n)"
csq_nsubmits = None
csq_name="LLOp5"
</question>

#Using Linked Lists
<question multiplechoice>
csq_prompt = "In which of these scenarios could you use a linked list?"
csq_renderer = "checkbox"
csq_soln = [1,0,0,0]
csq_options =  ['Storing elements in $O(1)$ time, and accessing the most recently inserted element and the first stored element in $O(1)$ time.',
'Finding the 6th, 10, and $n$th element in $O(1)$ time.',
'Implementing a FIFO (first in, first out) queue, where new elements are inserted at one end, and elements are removed in the order that they are inserted into the queue.',
'Finding the smallest value in $O(1) time.',
'Finding the smallest value of $n$ elements in $O(n) time.']
csq_name="ULLmc1"
</question>


<python>
#tutor.init_random()
</python>

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

