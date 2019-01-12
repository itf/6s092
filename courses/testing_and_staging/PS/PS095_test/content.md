# Readings 
Recitation notes 11, 6.006 Fall 2018 on stellar.

Lecture notes 11, 6.006 Fall 2018 on stellar.
# Depth-First Search


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
csq_prompt = "Return twice the length of the LinkedList"

## Define solution that will be printed to student.
csq_soln = """
def doublelength(ll): 
    return ll.length() * 2
"""

## Code that will be initially on the thingy
csq_initial = """def doublelength(ll):
    return ll.length()
"""
csq_name= "pcode2"

## Code that will be written before the user code as well as solution
## Particularly useful for defining classes and things that we don't want the user to modify
## For example, define a DFS function.
csq_code_pre = """
class LinkedList:
    def __init__(self, n):
        self.n = n # Length
    def length(self):
        return self.n


"""


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

## Now we need to write csq_tests, which defines what code to run
## As well as how to test it. 
## Each csq_tests is a dictionary of things (code, check, etc)

## We need to define the key code, which returns a string that will be evaluated with both the user code as well as our solution.
## Code should define a string called ans, which is what will be tested.

## We also define the key check_function, which is a function that takes escaped ans (a string, usually you will want to eval it.) from running user code, ans from running the solution, and i(index of the test), and then returns True or False.

tests = [cs_random.randint(1,20) for x in range(10)]
csq_tests = []
for i, t in enumerate(tests):

    csq_tests.append({
        'code': f"""
ll = LinkedList({t}])
ans = doublelength(ll)
""" ,
        'show_code': i < 5,
        'grade': True,
    })

</question> 

