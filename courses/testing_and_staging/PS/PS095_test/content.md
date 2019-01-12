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
csq_prompt = "Print out the second person's name in the LinkedList"

## Define solution that will be printed to student.
csq_soln = """
def secondName(ll): 
    return ll.left.getNext().name()
"""

## Code that will be initially on the thingy
csq_initial = """def secondName(ll):
    return ll.left.name()
"""
csq_name= "pcode2"

## Code that will be written before the user code as well as solution
## Particularly useful for defining classes and things that we don't want the user to modify
## For example, define a DFS function.
csq_code_pre = """
class LinkedList:
    def __init__(self, people = None):
        self.n = 0 # Length
        self.left = None
        self.right = None
        if people:
            for (name, height) in people:
                self.addPerson(Person(name, height))

    def length(self):
        return self.n

    def addPerson(self, person):
        if self.right is None:
            self.left = person
            self.right = person
        else:
            self.right.setNext(person)
            person.setPrev(self.right)
            self.right = person

        self.n += 1

class Person:
    def __init__(self, name, height):
        self._name = name
        self._height = height
        self._prev123 = None
        self._next123 = None

    def name(self):
        return self._name

    def height(self):
        return self._height

    def setNext(self, person):
        self._next123 = person
        return

    def setPrev(self, person):
        self._prev123 = person
        return

    def getPrev(self):
        return self._prev123

    def getNext(self):
        return self._next123
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


names = ["James", "Michael", "Robert", "David", "William", "Mary", "John", "Maria", "Charles", "Richard", "Jennifer", "Daniel", "Thomas", "Linda", "Patricia", "Barbara", "Joseph", "Mark", "Elizabeth", "Rose", "Ivan", "Justine", "Preksha", "Stef", "Courtney", "Lily"]
tests = [2, 2, 4, 10]

[("Rose", 59), ("Isaac", 2)] ]

# cs_random.randint(1,20) for x in range(10)]
csq_tests = []
for i, t in enumerate(tests):
    test_case = [(names[cs_random.randint(0, len(names), 1)], cs_random.randint(40, 80, 1), for x in range(t)]
    csq_tests.append({
        'code': f"""
ll = LinkedList({test_case})
ans = secondName(ll)
""" ,
        'show_code': i < 5,
        'grade': True,
    })

</question> 

