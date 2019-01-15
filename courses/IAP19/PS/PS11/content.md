# Readings 
[Recitation notes 8](https://learning-modules.mit.edu/service/materials/groups/238004/files/553c0282-3624-4bc3-aa99-c585e42d335a/link?errorRedirect=%2Fmaterials%2Findex.html&download=true) -- Linear Sorting, 6.006 Fall 2018 on stellar.

# Counting Sort

<question multiplechoice>
csq_prompt = """We want to perform counting sort on some of the students in 6.s092 in order to sort them by heights in inches. Given what you know about human beings, is a reasonable estimate for $u$?"""
csq_renderer = "radio"
csq_soln = '100'
csq_options = ['5', '50','100', '1000']
</question>

<question multiplechoice>
csq_prompt = """All of the 6.s092 students dropped out, so now we only have the following four students. :( Their information is formatted as `(student_id, name, height_inches)`.

We perform counting sort on them anyway, inserting them into a direct access array $d$ in the order shown below. The direct access array has size $u$ as determined in the previous problem. What is true about $d$, given that the list `[x, y]` represents a queue where `x` was inserted into the queue before `y`?

```
h = (1, Helen, 60)
j = (2, Jakob, 66)
c = (3, Courtney, 68)
g = (4, Ghost, 66)
```
"""
csq_renderer = "checkbox"
csq_soln = [0,1,0,0,1,0]
csq_options = [
"`d[1] = [h]`",
"`d[66] = [j, g]`",
"`d[66] = [g, j]`",
"`d['Ghost'] = [g]`",
"`d[60] = [h]`",
"`d[0] = [h, j, c, g]`"
]
csq_explanation = "If we're sorting by height, then the key would be heights and not IDs or names."
</question>

<question expression>
csq_prompt = """Now we read from $d$ to get the list of students sorted by increasing height. What sequence would we get? Submit your answer as 4 letters, i.e. cghj \n"""
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_nsubmits = None
csq_soln = "hjgc"
csq_explanation = "Jakob was before Ghost in the queue."
</question> 

# Coding Questions: Implementing Counting Sort

<question pythoncode>
csq_interface = 'ace'
csq_prompt = """
Let's implement counting sort! Here we implement counting sort in two parts. The first part will construct a direct access `Array d` by inserting the elements in our array `A` by key. The second part extracts a sorted array from the direct access array by reading through the direct access array. We represent these two components with the following code:
```
def counting_sort(A):
    d = construct_daa(A)
    return extract_from_daa(d)
```
In the above segment of code, `A` is a normal Python list, and `d` is a special `Array` object which is a static direct access array that is specially equipped to handle key collisions. We have the following functions and instance attributes on `Array`:

* `at(i)`: Returns the queue located at index `i`
* `add(i, x)`: Adds an element to the queue located at index `i`
* `u`: The size of the direct access array

The objects in the array are `Person` objects, which have the following instance attributes:

* `id`
* `name`
* `height`

In this problem, we implement `construct_daa(A)`, which takes in a normal Python list, and outputs a custom `Array` object where elements have been inserted into the indexed location indicated by their keys. When constructing `d`, use the universe size `u` that you derived in the first problem of this problem set.
"""

csq_soln = """
def construct_daa(A):
    d = Array(100)
    for person in A:
        d.add(person.height, person)
    return d
"""

csq_initial = """def construct_daa(A):
    u = #TODO
    d = Array(u)
    return None
"""

csq_code_pre = """
class Person:
    def __init__(self, id, name, height):
        self.id = id
        self.name = name
        self.height = height

class Array:
    def __init__(self, length):
        self.length = length
        self._array123 = [ [] for x in range(length)]

        self.num_accesses = 0
        self.num_sets = 0

    def __str__(self):
        return str(sorted(self._array123))

    def at(self, i):
        self.num_accesses += 1
        return self._array123[i]

    def add(self, i, x):
        self.num_sets += 1
        assert isinstance(type(x), Person)
        self._array123[i].append(x)
        return
"""


csq_sandbox_options = {
    'BADIMPORT': ['lib601', 'numpy', 'scipy', 'matplotlib'], 
    'CLOCKTIME': 0.36, 
    # 'CPUTIME': 0.36, 
    'MEMORY':1e9
}

tests = [ (4, [(1, "Helen", 60),
               (2, "Jakob", 66),
               (3, "Courtney", 68),
               (4, "Ghost", 66) ])
]
csq_tests = []
for i, t in enumerate(tests):
    csq_tests.append({ 'code': f"""
A = [Person(*x) for x in t[1]]
d = construct_daa({A})
ans = isinstance(d, Array), str(d)
""",
        'show_code': i<5,
        'grade': True,
    })

</question>


<question pythoncode>
csq_interface = 'ace'
csq_prompt = """Now we are going to implement `extract_from_daa(d)`, which takes in our `Array d` and outputs a normal Python list of size $n$, with our $n$ `Person`s arranged in order of increasing heights."""

csq_soln = """
def extract_from_daa(d):
    ans = []
    for d_index in range(d.length):
        queue = d.at(d_index)
        ans = ans + queue
    return ans
"""

csq_initial = """def extract_from_daa(d):
    return []
"""

csq_code_pre = """
class Person:
    def __init__(self, id, name, height):
        self.id = id
        self.name = name
        self.height = height

class Array:
    def __init__(self, length, people = None):

        if people:
            self.length = len(people)
            self._array123 = [Person(x[0], x[1], x[2]) for x in people]
        else:
            self.length = length
            self._array123 = [ [] for x in range(length)]

        self.num_accesses = 0
        self.num_sets = 0

    def __str__(self):
        return str(sorted(self._array123))

    def at(self, i):
        self.num_accesses += 1
        return self._array123[i]

    def add(self, i, x):
        self.num_sets += 1
        assert isinstance(type(x), Person)
        self._array123[i].append(x)
        return

    def num_ats(self):
        return self.num_accesses

def construct_daa(A):
    d = Array(100)
    for person in A:
        d.add(person.height, person)
    return d
"""


csq_sandbox_options = {
    'BADIMPORT': ['lib601', 'numpy', 'scipy', 'matplotlib'], 
    'CLOCKTIME': 0.36, 
    # 'CPUTIME': 0.36, 
    'MEMORY':1e9
}

tests = [ (4, [(1, "Helen", 60),
               (2, "Jakob", 66),
               (3, "Courtney", 68),
               (4, "Ghost", 66) ])
]
csq_tests = []
for i, t in enumerate(tests):
    u = 100
    csq_tests.append({
        'code': f"""
people = [Person(*x) for x in t]
d = construct_daa({people})
sorted_arr = extract_from_daa(d)
enough_ats = d.num_ats() > {u}
ans = enough_ats, str(sorted_arr)
""",
        'show_code': i<5,
        'grade': True,
    })

</question>
