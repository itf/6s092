# Readings 

[Lecture Notes 4](https://learning-modules.mit.edu/service/materials/groups/238004/files/aad7a820-c5b5-4eba-aff2-79bbdc1355e4/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), Section on Linked Lists, 6.006 Fall 2018 on stellar.

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
csq_prompt= "Wumpus now has a linked list of numbers from $0$ to $n$. What is the asymptotic runtime of finding the $j$th elment, where $j$ is a number between $0$ and $n$? How long does it take for Wumpus to find a specific number? Give an asymptotic bound: O(something) \n \n"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = "O(n)"
csq_nsubmits = None
csq_name="LLOp5"
</question>

# Using Linked Lists
<question multiplechoice>
csq_prompt = "In which of these scenarios could you use a linked list?"
csq_renderer = "checkbox"
csq_soln = [1,0,1,0,1]
csq_options =  ['Storing elements in $O(1)$ time, and accessing the most recently inserted element and the first stored element in $O(1)$ time.',
'Finding the 6th, 10, and $n$th element in $O(1)$ time.',
'Implementing a FIFO (first in, first out) queue, where new elements are inserted at one end, and elements are removed in the order that they are inserted into the queue.',
'Finding the smallest value in $O(1)$ time.',
'Finding the smallest value of $n$ elements in $O(n)$ time.']
csq_name="ULLmc1"
</question>

# Coding: Implementing A Doubly Linked List

Wumpus has implemented most of a doubly linked list to keep track of a bunch of his friends and their heights! Now he need your help to implement some important functions to complete his code.

Right now we have a class called `LinkedList` with the following functions:

* `addPerson(person):` adds a `Person` object to the LinkedList
* `left:` the leftmost `Person` in the LinkedList, is `None` when there is no one in the list
* `right:` the rightmost `Person` in the LinkedList, is `None` when there is no one in the list

We have defined the `Person` object to have the following functions:

* `name():` returns a string
* `height():` returns an integer
* `setNext(person):` takes in another `Person` object and sets it as our current person's next `Person`
* `setPrev(person):` takes in another `Person` object and sets it as our current perons's previous `Person`
* `getNext():` if we read the LinkedList from left to right, returns the next `Person`
* `getPrev():` if we read the LinkedList from left to right, returns the previous `Person`

<question pythoncode>
csq_interface = 'ace'
csq_prompt = "Write a function called `secondName` that takes an input of a `LinkedList` and returns the second person's name in the (remember we are reading from left to right)."

## Define solution that will be printed to student.
csq_soln = """
def secondName(ll): 
    return ll.left.getNext().name()
"""

## Code that will be initially on the thingy
csq_initial = """def secondName(ll):
    return ll.right.name()
"""
csq_name= "pcode1"

## Code that will be written before the user code as well as solution
## Particularly useful for defining classes and things that we don't want the user to modify
## For example, define a DFS function.
csq_code_pre = """
class LinkedList:
    def __init__(self, people = None):
        self.left = None
        self.right = None
        if people:
            for (name, height) in people:
                self.addPerson(Person(name, height))

    def addPerson(self, person):
        if self.right is None:
            self.left = person
            self.right = person
        else:
            self.right.setNext(person)
            person.setPrev(self.right)
            self.right = person

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

csq_tests = []
for i, t in enumerate(tests):
    test_case = [(names[cs_random.randint(0, len(names)-1)], cs_random.randint(40, 80)) for x in range(t)]
    print(test_case)
    csq_tests.append({
        'code': f"""
ll = LinkedList({test_case})
ans = secondName(ll)
""" ,
        'show_code': i < 5,
        'grade': True,
    })

</question> 

<question pythoncode>
csq_interface = 'ace'
csq_prompt = "Wumpus has a spotty memory, so sometimes he can't recall how many people he's measured so far. Help him out by implementing the function `length(ll)`, which takes a `LinkedList` as input and returns the integer length (the number of `Person`s in the list)!"

## Define solution that will be printed to student.
csq_soln = """
def length(ll): 
    ans = 0
    curr_person = ll.left
    while curr_person:
        ans += 1
        curr_person = curr_person.getNext()
    return ans
"""

## Code that will be initially on the thingy
csq_initial = """def length(ll):
    return 0
"""
csq_name= "pcode2"

## Code that will be written before the user code as well as solution
## Particularly useful for defining classes and things that we don't want the user to modify
## For example, define a DFS function.
csq_code_pre = """
class LinkedList:
    def __init__(self, people = None):
        self.left = None
        self.right = None
        if people:
            for (name, height) in people:
                self.addPerson(Person(name, height))

    def addPerson(self, person):
        if self.right is None:
            self.left = person
            self.right = person
        else:
            self.right.setNext(person)
            person.setPrev(self.right)
            self.right = person

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
tests = [0, 1, cs_random.randint(2,4), cs_random.randint(3,5), cs_random.randint(10,20), cs_random.randint(500,600)]

csq_tests = []
for i, t in enumerate(tests):
    test_case = [(names[cs_random.randint(0, len(names)-1)], cs_random.randint(40, 80)) for x in range(t)]
    print(test_case)
    csq_tests.append({
        'code': f"""
ll = LinkedList({test_case})
ans = length(ll)
""" ,
        'show_code': i < 5,
        'grade': True,
    })

</question> 



<question pythoncode>
csq_interface = 'ace'
csq_prompt = "So Wumpus... what's Ivan's height? Wumpus is sad because he can't immediately answer just by looking at his linked list. Help him out by implementing the function `find(ll, name)`, which takes a `LinkedList` object and a name as input and returns the integer height of the first person in the list with that name. Assume that the linked list will always contain at least one person with that name."

## Define solution that will be printed to student.
csq_soln = """
def find(ll, name):
    curr_person = ll.left
    while curr_person:
        if curr_person.name() == name:
            return curr_person.height()
        curr_person = curr_person.getNext()
    return ans
"""

## Code that will be initially on the thingy
csq_initial = """def find(ll, name):
    return 0
"""
csq_name= "pcode3"

## Code that will be written before the user code as well as solution
## Particularly useful for defining classes and things that we don't want the user to modify
## For example, define a DFS function.
csq_code_pre = """
class LinkedList:
    def __init__(self, people = None):
        self.left = None
        self.right = None
        if people:
            for (name, height) in people:
                self.addPerson(Person(name, height))

    def addPerson(self, person):
        if self.right is None:
            self.left = person
            self.right = person
        else:
            self.right.setNext(person)
            person.setPrev(self.right)
            self.right = person

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
tests = [(2, "Patricia"),
         (2, "Michael"), 
         (4, "Ivan"),
         (10, "Preksha")]

csq_tests = []
for i, t in enumerate(tests):
    test_case = [(names[cs_random.randint(0, len(names)-1)], cs_random.randint(40, 80)) for x in range(t[0])]
    test_case = test_case + [(t[1], cs_random.randint(40,80))] # Make sure `name` is in the test_case
    cs_random.shuffle(test_case)
    csq_tests.append({
        'code': f"""
ll = LinkedList({test_case})
ans = find(ll, {t}[1])
""" ,
        'show_code': i < 5,
        'grade': True,
    })

</question> 



<question pythoncode>
csq_interface = 'ace'
csq_prompt = "Sometimes Wumpus gets into a big argument with a friend because of arguing over the ethics of eating children. Afterwards, Wumpus is unhappy and doesn't really care about that friend's height anymore. Help Wumpus out by implementing the function `removePerson(ll, name)`, which takes a `LinkedList` object and a name as input, and removes the first `Person` seen with that name from the linked list. Remember that we are reading the list from left to right. Assume that the linked list will always contain at least one person with that name."

## Define solution that will be printed to student.
csq_soln = """
def removePerson(ll, name):
    curr_person = ll.left
    while curr_person:
        if curr_person.name() == name:
            prev_person = curr_person.getPrev()
            next_person = curr_person.getNext()
            prev_person.setNext(next_person)
            next_person.setPrev(prev_person)
            return
        curr_person = curr_person.getNext()
    return
"""

## Code that will be initially on the thingy
csq_initial = """def removePerson(ll, name):
    return 0
"""
csq_name= "pcode4"

## Code that will be written before the user code as well as solution
## Particularly useful for defining classes and things that we don't want the user to modify
## For example, define a DFS function.
csq_code_pre = """
class LinkedList:
    def __init__(self, people = None):
        self.left = None
        self.right = None
        if people:
            for (name, height) in people:
                self.addPerson(Person(name, height))

    def __str__(self):
        curr_person = self.left
        string_repr = "["
        while curr_person:
            string_repr = string_repr + "({curr_person.name()}, {str(curr_person.height())}), "
            curr_person = curr_person.getNext()
        return string_repr[:-2] + "]"

    def addPerson(self, person):
        if self.right is None:
            self.left = person
            self.right = person
        else:
            self.right.setNext(person)
            person.setPrev(self.right)
            self.right = person

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
tests = [(2, "Patricia"),
         (2, "Michael"), 
         (4, "Ivan"),
         (10, "Preksha")]

csq_tests = []
for i, t in enumerate(tests):
    test_case = [(names[cs_random.randint(0, len(names)-1)], cs_random.randint(40, 80)) for x in range(t[0])]
    test_case = test_case + [(t[1], cs_random.randint(40,80))] # Make sure `name` is in the test_case
    cs_random.shuffle(test_case)
    csq_tests.append({
        'code': f"""
ll = LinkedList({test_case})
removePerson(ll, {t}[1]) 
ans = str(ll)
""" ,
        'show_code': i < 5,
        'grade': True,
    })

</question> 
