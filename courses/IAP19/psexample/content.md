You put stuff in preload to be loaded before the pset loads. Useful for CS variables, such as name of the pset or date due.

Here is a python block. You can run arbitrary python inside it as well as print other blocks from inside it. You can set defaults to the questions for example. 

<python>
# Some default for all the questions. Change if you need to change!
csq_allow_viewanswer = True
csq_allow_submit_after_answer_viewed = False
csq_allow_viewexplanation = True
csq_explanation = "default explanation lol"
csq_nsubmits = None #infinitely many! Change to a number to have fewer for your question.
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_show_score = True
csq_npoints = 1 #only one point per question
#csq_check_function #If you want to define how to check. def _cmp(sub, soln): return True or False depending on sum or sol
# Examples in catsoop.check (accessible from this file through csm_check.func())

# csq_name="question"
# You can give name for the questions to see stats about it as well as to allow adding new questions to the middle of the pset without changing students scores. Try to always give a name.

# Default for expressions:
csq_error_on_unknown_variable = False #if the answer is 2: a/a * 2 will be accepted. 
# If it was True, then since a is not in the answer, a/a * 2 would not be allowed.
# Useful for making sure students simplify formulas.


# extra functions, to be able to do some of the problems:
# In order to be able to use a function, you need to define it in the csq_func dict. 
# First you have to define what it evaluates to, and how it is printed. 
# This is an example on how to define T, O and \\theta. 
# This is necessary because catsoop evaluates things numerically. Just choose a func that is unlikely that the student will type by chance and that is not linear nor symmetric nor antysimmetric.
# The functions can take multiple inputs as well.

csq_funcs = {"T": (lambda c: c**3*0.6006+c**2, lambda  c:  f"T({', '.join(c)})" ),
"O": (lambda c: c**3*1.6006-c**2, lambda  c:  f"O({', '.join(c)})" ),
"theta": (lambda c: -c**3*0.06006+c**2*0.2, lambda  c:   f"\\theta({', '.join(c)})")}
</python>

You can have as many python blocks as you want.

In this next block we allow the use of randomness in this pset. This kinda sucks, because now every question will have a new random seed thingy when impersonating the user. I think that for the student they can't change the seed, this is just to fix things up.
<python>
#If you intend to use random functions, you need to call tutor.init_random(), exactly once, before you make use of the randomness. This assure that the randomness is per student per page, rather than per call.
#If you don't call it, you will have the following behavior: x=random. print(x): 2. print(x):7
tutor.init_random()
</python>
# Latex
Escape your \\ when writing latex inside a question, but no on the text. \theta means tab + heta in a question.. \\theta means \\ + theta, which is the intended behavior. Escape it in all strings that will be printed.

$\theta$ 

The reason for this is because questions are evaluated as python, and \t in python is tab. and most \letter in python are special.

# Displaying code
Not inline
```
x = 5
y = 5.0
```
inline `code`

# Reading types of questions from the code:
Search on the catsoop code for $csq$, which means cat-soop answer. Or search inside __QTYPES__ for $csq$ to find the options for that particular type of question.


# Writing questions. 
Write a question tag (open and close it) < questiontype > < / question >. 
Write the csq_ python options inside it.

Usually all csq_ options are optional, but some you are likely to want, such as prompt, and solution.

# Multiple choices
2 types of multiple choices.

<question multiplechoice>
csq_prompt = "Second and third checkboxes are correct\n\n "
csq_renderer = "checkbox"
csq_soln = [0,1,1]
csq_options =  ['$(n),\ (n+4),\ (5n)$',
 '$right$',
 'also $\\theta($right$)$']
csq_npoints = 10 #so many points this one is worth!
csq_name="mc1"
</question>

<question multiplechoice>
csq_prompt = "Second option is correct\n\n "
#default renderer is dropdown. It sucks
csq_soln = '$right$'
csq_options =  ['$(n),\ (n+4),\ (5n)$',
 '$right$',
 'this one is \\theta(wrong)']
csq_name="mc2"
</question>


<question multiplechoice>
csq_prompt = "Second option is correct\n\n "
#radio is much better than dropdown!
csq_renderer = "radio"
csq_soln = '$right$'
csq_options =  ['$(n),\ (n+4),\ (5n)$',
 '$right$',
 'this one is \\theta(wrong)']
csq_name="mc2"
</question>


# Check yourself!

Not much to be said. Just a checkyourself box. It is useful to use with the hide text for spoilers.
<checkyourself>
Is ${n \choose 3} \in O(n^3)$? What about  $n^3 \in O({n \choose 3})$
</checkyourself>

 Now with hidden spoilers
<checkyourself>
Is ${n \choose 3} \in O(n^3)$? What about  $n^3 \in O({n \choose 3})$
<showhide>
Yes and yes.
</showhide>
</checkyourself>


# Expressions
You can have expressions that will be evaluated numerically. You can change the precision if you want, but, whatever, keep it in the default.

The answer is 3*T(n/3)+O(n). 3*T(n/3)+O(n)*a/a would also be right.
<question expression>
csq_prompt = "$T(n)=$ "
csq_soln = "3*T(n/3)+O(n)" # Array for multiple solutions or string for single solution.
csq_explanation = "3 parts of 1/3 of the size + the work to join"
csq_nsubmits = None #infinite submissions.
csq_name="exp1"
</question>

The answer is now log(a,b) or log(a)/log(b)

<question expression>
csq_prompt = """Suppose the amount of work per level is constant. 

If  $\\frac{y}{x} =1$,  what is $c$ in terms of $a$ and $b$?  To write $\log_x(y)$, please write $\log(y,x)$
"""
csq_error_on_unknown_variable = True #make sure they get rid of n in the answer
csq_soln = ["log(a,b)", "log(a)/log(b)"]
csq_explanation = "log is log of the log of the log"
csq_nsubmits = None
csq_name="question"
csq_name="exp2"
</question>

# Python literal
Things like lists [1,2,3] or ints 1, or strings "a" or dicts {"a":2}, or sets {1,2,3} or None, or floats or complex 2+3j. Distinguishes between floats and ints.

<question pythonliteral>
csq_prompt='<tt>round(13.000000)</tt>\n\n'
csq_soln=13
</question>

<question pythonliteral>
csq_prompt='<tt>0 ** 1 + 2</tt>'
csq_soln=2
</question>

<question pythonliteral>
csq_prompt='<tt>2.0 ** 3.0</tt>'
csq_soln=8.0
</question>

# Automatically generating questions
Use cs_print to print the questions from inside a python block

<python>
x = [cs_random.randint(1,6) for i in range(20)]
op = ['+','-','/','*']
for i in range(3):
    questionprompt = f'{x[i]}{op[cs_random.randint(0,3)]}{x[i+1]}'
    cs_print(f"""
<question pythonliteral>
csq_prompt='{questionprompt}<br>'
csq_soln={eval(questionprompt)}
</question>
""")
</python>

# Small box
Small box of text. Check if the same.
<question smallbox>
csq_prompt='write banana'
csq_soln='banana'
</question>

# Number
Basically expression question that doesn't calculate and only input is number.
<question number>
csq_prompt='2+2='
csq_soln=['4','4.0']
</question>

# Multiexpression
This is super useless. The expressions are evaluated independent of each other. It is not possible to have something like: x=2, y = 2x.

Here solutions are x=2 or 3. y = sqrt(2).

<question multiexpression>
csq_expressions = [("$x = ~$", ["2", "3"]), ("$y = ~$", ["sqrt(2)"])]
</question>

# Python code questions
Those can do a lot of stuff. Let's start with basic things:

Here both the student solution and user solution define the same function. The tests are of the form: code: `ans = call function with input`. It will compare that the data returned after running the test with the solution is the same as running with the test.


```
>>> full_name('Richard','Nixon')
    Hello, Richard Nixon! 
```

*Your code should return the message, correct with the proper punctuation and spacing*

 
<question pythoncode>
csq_interface = 'ace'
csq_soln = '''def full_name(first_name, last_name):
    return 'Hello, ' + first_name + ' ' + last_name + '!'
'''
csq_initial = '''def full_name(first_name,last_name):
    pass'''
csq_tests = [{'code':'ans= full_name("Joe","Steinmeyer")'},{'code':'ans= full_name("Blanky","McBlankenstein")'},{'code':'ans= full_name("Reimi","Hicks")'}]      
csq_name= "pcode1"
</question> 


A more advanced way of defining a pythoncode question is by modifying the sandbox parameters and the tests.

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
   # 'CLOCKTIME': 0.36, 
    'CPUTIME': 0.36, 
    'MEMORY':1e9
}


## Now we define helper functions
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




# That is all!

If you need, I can help write custom QTYPES.