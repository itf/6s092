# Readings
Recitation notes 5b, 6.006 Fall 2018 on stellar.

Lecture notes 6, 6.006 Fall 2018 on stellar.
# Binary Search Trees


<question multiplechoice>
csq_prompt = "Which of the following trees are BSTs? (There may be more than one)."
csq_renderer = "checkbox"
csq_soln = [1,1,1,0]
csq_options =  ['    10    \n 5        15',
'    5    \n 5        15',
'    5    \n 5        5',
'    10 \n 5            \n                  15']
csq_name="qexample1"
csq_explanation = "The first three trees satisfy the BST property. Remember that the BST property states that keys in the left subtree must be <= the key of a node, and keys in the right subtree must be >= the key of a node. The fourth tree does not satisfy the BST property because 15 > 10, but 15 is in the left subtree of the node with key 10."
</question>


<question multiplechoice>
csq_prompt = "We have the following BST: \n \
\n   12   \n\
 7   16   \n\
A B C D\n\
\n We insert a node with key 10 into the BST. Where does it go (to satisfy the BST property)?"
csq_renderer = "checkbox"
csq_soln = [0,1,0,0]
csq_options =  ["A", "B", "C", "D"]
csq_name="qexample1"
csq_explanation = "We compare 10 to 12. 10 < 12, so we go to the left subtree. We compare 10 to 7. 10 > 7, so we put 10 in the right subtree at position B."
</question>


<question multiplechoice>
csq_prompt = """
We have the following BST: \n
         8 \n
     /     \\ \n
    4        14 \n
            /    \\ \n
           10     16 \n
We delete the node with key 14. What does the tree look now? (May be more than one answer).
"""
csq_renderer = "checkbox"
csq_soln = [1,1,0,0]
csq_options =  [
'''
        8 \n
      /   \\ \n
     4      10 \n
             \\ \n
                 16 \n
''',
'''
         8 \n
       /    \\ \n
     4       16 \n
            /     \n
          10     
''',
'''
        8 \n
     /     \n
    4       
''',
'''
        8 \n
      /   \\ \n
     4      10 \n
''',
]
csq_name="qexample1"
csq_explanation = "When we delete the node with key 14, either the node with key 10 or the node with key 16 can take its place."
</question>


<question multiplechoice>
csq_prompt = """
We have the following BST: \n
             8 \n
          /     \\ \n
         4        14 \n
       /   \\     /   \\ \n
      2      5   10     16 \n
We delete the root (node with key 8). What does the tree look now? (Follow the delete function we learned in class).
"""
csq_renderer = "checkbox"
csq_soln = [0,1,0]
csq_options =  [
'''
               14
             /   \\
           10     16
         /
        4
       /  \\
     2     5
''',
'''
          10 \n
        /     \\ \n
      4        14 \n
     /  \\        \\ \n
    2     5         16 \n
''',
'''
               4
              /  \\
            2      5
                     \\
                      14
                    /   \\
                  10      16
'''
]
csq_name="qexample1"
csq_explanation = "We are in the case where the node being deleted has two children. We take the min of the right subtree (or the max of the left subtree), and put move it to the place of the deleted node."
</question>


<question expression>
csq_prompt = "For the BST in the above problem (before deletion), what is the result of an in-order traversal? Enter your answer as a python list where the keys are integers (not strings)"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = [2,4,5,8,10,14,16]
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
