# Readings 
[Recitation notes 3](https://learning-modules.mit.edu/service/materials/groups/238004/files/e6fa926e-a2c0-484f-80a0-c005f3b7f932/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), Sorting, 6.006 Fall 2018 on stellar.

<python>
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_nsubmits = None
</python>

# Sorting

## Invariants
One of the most important things to remember about each algorithm is what $invariant$ it is trying to maintain. The invariant distinguishes different algorithms, allows you to demonstrates correctness, and is instrumental in how you design code implementing the algorithms. Skim the recitation notes, paying special attention to the invariant described for each algorithm.

1. Insertion Sort
2. Selection Sort
3. Merge Sort

What algorithms are described by the following invariants?

* a. We keep track of contiguous sorted chunks of the array.

* b. At step $i$, we have the largest $i$ elements of the array at the end.

* c. Right before we place the $i$th element, the first $i$ elements of the array are sorted.

<question expression>
csq_prompt= "Write your answer as a string of three letters, i.e. 'abc' means that you think 'a' applies to Insertion sort, 'b' applies to Selection Sort, and 'c' to Merge Sort."
csq_soln = "cba"
csq_explanation = "Reread the recitation notes more closely to understand the invariants!"
csq_name="pset7q10"
</question>

## Insertion Sort

<question expression>
csq_prompt = "How many swaps are necessary to sort this array $[1,\ 2,\ 4,\ 3]$?"
csq_soln = "1"
csq_explanation = "We only need to swap the $3$ and the $4$"
csq_nsubmits = None #infinite submissions.
csq_name="ps7q1"
</question>

<question multiplechoice>
csq_prompt = "Which of these (could be multiple answers) would be a valid swap to make during insertion sort? Refer to the algorithm described in the recitation notes."
csq_renderer = "checkbox"
csq_soln = [0,1,0]
csq_options = ['$[1,\ 4,\ 2,\ 3] \\rightarrow [1,\ 2,\ 3,\ 4]$',
'$[1,\ 4,\ 2,\ 3] \\rightarrow [1,\ 2,\ 4,\ 3]$',
'$[2,\ 1,\ 4,\ 3] \\rightarrow [2,\ 1,\ 3,\ 4]$']
csq_name = 'ps7q2'
csq_explanation = "The invariant must be true at all times -- if we're performing a swap on the $i$th element, it must be true that A[:i] have been sorted already. Furthermore, we will only ever be swapping two adjacent numbers."
</question>

<question multiplechoice>
csq_prompt = "Which of these (could be multiple answers) would be a valid swap to make during insertion sort? Refer to the algorithm described in the recitation notes."
csq_renderer = "checkbox"
csq_soln = [1,0,0]
csq_options = ['$[1,\ 3,\ 5,\ 4,\ 2] \\rightarrow [1,\ 3,\ 4,\ 5,\ 2]$',
'$[1,\ 3,\ 5,\ 4,\ 2] \\rightarrow [1,\ 2,\ 3,\ 5,\ 4]$',
'$[1,\ 3,\ 5,\ 4,\ 2] \\rightarrow [1,\ 3,\ 5,\ 2,\ 4]$']
csq_name = 'ps7q25'
csq_explanation = "The invariant must be true at all times -- if we're performing a swap on the $i$th element, it must be true that A[:i] have been sorted already. Furthermore, we will only ever be swapping two adjacent numbers."
</question>


<checkyourself>
Why can't we make the swap $[2,\ 3,\ 1] \rightarrow [1,\ 2,\ 3]$?
<showhide>
While this might be a simple operation to do with physical objects like cards, arrays in the Word RAM model are more like buckets that we would need to move data in and out of. We would need two swaps to move both the $2$ and the $3$, i.e. $[2,\ 3,\ 1] \rightarrow [2,\ 1,\ 3] \rightarrow [1,\ 2,\ 3]$. Refer to PS03 for more information.
</showhide>
</checkyourself>

A swap is when we take two elements in an array and swap their positions. A comparison is when we compare the values of two numbers.

<question multiplechoice>
csq_prompt = "What is the minimum number of comparisons that we would make in insertion sort?"
csq_renderer = "radio"
csq_soln = '$\\Theta(n)$'
csq_options = ['$\\Theta(1)$', '$\\Theta(n)$', '$\\Theta(n log n)$', '$\\Theta(n^2)$']
csq_name = 'ps7q3'
csq_explanation = "Even if the array starts out being completely sorted, we still would compare every element with its neighbor"
</question>

<question multiplechoice>
csq_prompt = "What is the maximum number of comparisons that we would make in insertion sort?"
csq_renderer = "radio"
csq_soln = '$\\Theta(n^2)$'
csq_options = ['$\\Theta(1)$', '$\\Theta(n)$', '$\\Theta(n log n)$', '$\\Theta(n^2)$']
csq_explanation = "The maximum number of swaps we might have to make is $\\Theta(n^2)$, i.e. when we are sorting $[n,\ n-1,\ ...,\ 2,\ 1]$ into increasing order. Since we make one comparison for each of those swaps, we would make $\\Theta(n^2)$ comparisons."
</question>

## Selection sort

<question multiplechoice>
csq_prompt = "Which of these would be a valid swap to make during selection sort? Refer to the algorithm described in the recitation notes."
csq_renderer = "checkbox"
csq_soln = [1,0, 0]
csq_options = ['$[3,\ 2,\ 1,\ 4,\ 5] \\rightarrow [1,\ 2,\ 3,\ 4,\ 5]$',
'$[3,\ 2,\ 1,\ 4,\ 5] \\rightarrow [3,\ 1,\ 2,\ 4,\ 5]$',
'$[3,\ 2,\ 1,\ 4,\ 5] \\rightarrow [2,\ 3,\ 1,\ 4,\ 5]$'
]
</question>

<question multiplechoice>
csq_prompt = "What is the minimum number of comparisons that we would make in selection sort?"
csq_renderer = "radio"
csq_soln = '$\\Theta(n^2)$'
csq_options = ['$\\Theta(1)$', '$\\Theta(n)$', '$\\Theta(n log n)$', '$\\Theta(n^2)$']
csq_explanation = "Every time we calculate the maximum value of an array of $i$ elements, we must make $i$ comparisons. The number of comparisons in selection sort would therefore be $n + (n-1) + ... + 1 = n(n+1)/2 = \\Theta(n^2)$."
</question>

<question multiplechoice>
csq_prompt = "What is the maximum number of $swaps$ that we would make in selection sort?"
csq_renderer = "radio"
csq_soln = '$\\Theta(n)$'
csq_options = ['$\\Theta(1)$', '$\\Theta(n)$', '$\\Theta(n log n)$', '$\\Theta(n^2)$']
csq_explanation = "At each step in selection sort, we keep track of the $i$ largest elements. Each swap we make increases $i$ by $1$. When $i = n$, we are done -- therefore the maximum number of swaps we ever make in selection sort is $\\Theta(n)$."
</question>


## Merge Sort

Read the section on Merge Sort in the Recitation notes. You don't need to understand the code line by line, but you should be able to have some intuition for how the algorithm works. You should look at the [codepen](https://codepen.io/mit6006/pen/RYJdOG) visualization linked in the notes; it's very helpful.

### Intermediate States
Merge sort begins by breaking the original array into many pieces of size $<2$. Then we "merge" these small chunks into larger chunks. After we merge the smaller chunks of a particular size, we start merging the larger chunks. Each merge step of Merge Sort will merge two arrays of length $n$ to form an array of length $2n$.

For the following two problems, you are given an array that is in the middle of merge sort. We are about to merge a chunk of size $n$, containing the first value in the array ($1$), with an adjacent chunk of size $n$. Which of the following are possible values for $n$?

<question multiplechoice>
csq_prompt = "$[1,\ 5,\ 3,\ 8,\ 2,\ 4,\ 6,\ 7]$"
csq_renderer = "checkbox"
csq_soln = [1,1,0,0]
csq_options = ['$1$', '$2$', '$3$', '$4$']
csq_explanation = "The chunks of size $1$ and $2$ are sorted within themselves, so they are possible candidates for merging. However, the first chunk of size $>2$ (the sequence $[1,\ 5,\ 3]$) is not sorted. We must sort smaller chunks before we can move on to larger chunks."
csq_name='ps7q6'
</question>

<question multiplechoice>
csq_prompt = "$[1,\ 3,\ 5,\ 8,\ 2,\ 4,\ 6,\ 7]$"
csq_renderer = "checkbox"
csq_soln = [1,1,0,1]
csq_options = ['$1$', '$2$', '$3$', '$4$']
csq_explanation = "The chunks of size $1$, $2$, and $4$ are sorted within themselves, so those are all possible candidates for merging. Because we double $n$ every time, $n$ will always be a power of $2$, and we will never merge chunks with $n = 3$."
csq_name='ps7q7'
</question>

### Intuiting the Run-Time

Recall from the reading that the runtime of merge-sort is $\Theta(nlog(n))$. One way to get this run-time is by applying case 2 of (the special polynomial form of) the Master's Theorem to the recurrence equation that we have for the run-time: $T(n) = 2T(n/2) + \Theta(n)$. However, we can derive this run-time in a more intuitive way!

For simplicity's sake, let's say that $n = 2^i$ (so, $n$ is a power of $2$). We break the array into chunks of size $1$. An array of length $1$ is trivially sorted, so it takes $\Theta(1)$ time to sort all the $n$ chunks of size $1$.

<question multiplechoice>
csq_prompt = "We merge $n/2$ pairs of size $1$ chunks into $n/2$ chunks of size $2$. How long (how many operations) does it take to merge two chunks of size $1$?"
csq_renderer = "radio"
csq_soln = '$\\Theta(1)$'
csq_options = ['$\\Theta(1)$', '$\\Theta(log(n))$', '$\\Theta(2n)$']
csq_explanation = "It takes a constant number of operations."
csq_name = "ps7q8"
</question>

<question multiplechoice>
csq_prompt = "How long (how many operations) does it take to merge all the chunks of size $1$?"
csq_renderer = "radio"
csq_soln = '$\\Theta(n)$'
csq_options = ['$\\Theta(1)$', '$\\Theta(log(n))$', '$\\Theta(n)$']
csq_explanation = "We perform $n/2$ merges, and each take $\\Theta(1)$"
csq_name = "ps7q9"
</question>

<question multiplechoice>
csq_prompt = "At every 'step', we will be merging $n/2^i$ pairs of size $2^i$ into $n/2^i$ chunks of size $2^{i+1}$. How long does it take to merge two chunks of size $2^i$?"
csq_renderer = "radio"
csq_soln = '$\\Theta(2^i)$' 
csq_options = ['$\\Theta(1)$', '$\\Theta(i)$', '$\\Theta(n)$', '$\\Theta(2^i)$']
csq_explanation = "Merging two chunks is linear in the sizes of the chunks."
csq_name = "ps7q10"
</question>

<question multiplechoice>
csq_prompt = "How long does it take to complete the step by merging all the chunks of size $2^i$?"
csq_renderer = "radio"
csq_soln = '$\\Theta(n)$' 
csq_options = ['$\\Theta(1)$', '$\\Theta(i)$', '$\\Theta(n)$', '$\\Theta(2^i)$']
csq_explanation = "We perform $n/2^i$ merges, so all the merges together add up to $\\Theta(n)$."
csq_name = "ps7q11"
</question>

<question multiplechoice>
csq_prompt = "How many 'steps' are there in total?"
csq_renderer = "radio"
csq_soln = '$log_2(n)$' 
csq_options = ['$1$', '$i$', '$log_2(n)$', '$n$', '$nlog(n)$']
csq_explanation = "The number of distinct values that $i$ can take range from $0$ (when we have chunks of size $1$) to $log(n)$ when we have a single chunk of size $n$. Because each level takes $\\Theta(n)$ work, and we have $log(n)$ levels, it follows that the entire Merge Sort algorithm will take $\\Theta(n log(n))$ time."
csq_name = "ps7q12"
</question>

### In-Place vs "Out of Place"

<question multiplechoice>
csq_prompt = "When we say that merge sort takes up a linear amount of space, we mean that we set aside a linear amount of space for $temp$ in addition to the space being used to store the input of size $n$. WHat do we know about the size of $temp$, given that it takes up a linear amount of space?"
csq_renderer = "radio"
csq_soln = '$O(n)$'
csq_options = ['$O(1)$', '$O(log n)$', '$O(n)$', '$O(n^c)$ for any positive $c$', '$r-l$']
</question>


## Coding portion!

You need to sort the data on a super secret project. 

Since the project is secret, they can't give you access to the data, they can only give you access to the ids of the data, and access to two functions:

```python
class array:
	def isLarger(self, i,j):
		#Returns True if the data in index[i] is larger than the data at index[j]

	def swap(self, i,j):
		# Swaps the data at index i with the data in index[j]
```

Please notice that isLarger compares data at location i, and at location j, rather than comparing elements of value i and value j.

Using those two functions they ask you to sort the data
### Selection sort
The data is stored in different physical locations, so it is really expesive to move the data from one place to another. They need you to minimize the number of swaps.

It is very cheap to perform comparisons however, so you can compare as many times as you want. 

You have no extra space to store the data, since data storage is very expensive.

Knowing this, they ask you to implement the function selection sort.



<question pythoncode>
csq_interface = 'ace'

csq_soln = '''
def selectionSort(arr):
    n = len(arr)
    for i in range(n-1, -1, -1):
        best = i
        for j in range(i, -1, -1):
            if arr.isLarger(j, best):
                best = j
        arr.swap(best, i)
'''

csq_initial = '''
def selectionSort(arr):
    n = len(arr)
    if arr.isLarger(0, 1):
        arr.swap(0, 1)
'''


def shuffle_all(arr):
    cs_random.shuffle(arr)

tests = [(5, 6, 50),
		 (10, 11, 200),
		 (20, 21, 800),
		 (40, 41, 3200)]

orders = []

for n, _, _ in tests:
     a = [x for x in range(n)]
     shuffle_all(a)
     orders.append(a)

csq_code_pre = f'''

class arrayToSort:
    def __init__(self, n, swap_limit, comparison_limit):
        self._a = [x for x in range(n)]
        self._order = [x for x in range(n)]
        self._swap_limit = swap_limit
        self._swaps = 0
        self._comparison = 0
        self._comparison_limit = comparison_limit        

    def __str__(self):
        return self._a

    def __repr__(self):
        return str(self._a)

    def swap(self, i, j):
        self._a[i], self._a[j] = self._a[j], self._a[i]
        self._swaps += 1
        too_many_swaps = self._swaps > self._swap_limit
        assert not too_many_swaps, "You performed too many swaps"

    def isLarger(self, i, j):
        self._comparison += 1
        a = self._a
        too_many_comps = self._comparison > self._comparison_limit
        assert not too_many_comps, "You performed too many comparisons"
        return self._order[a[i]] > self._order[a[j]]

    def __len__(self):
        return len(self._a)


_arrays_to_sort = []

tests = {tests}

orders = {orders}

for i, (n, swap, compare) in enumerate(tests):
	a = arrayToSort(n, swap, compare)
	a._order = orders[i]
	_arrays_to_sort.append(a)

'''




csq_tests = []

for i in range(len(tests)):
    csq_tests.append({
        'code': f"""
arr = _arrays_to_sort[{i}]
selectionSort(arr)
ans = arr
""" })

csq_npoints = 2
csq_name= "pcode1"
</question> 


### Insertion Sort

Now, they tell you that the data is mostly sorted, i.e. at most 10 swaps between adjacency elements is needed to sort the data.

You have no extra space to store the data, since data storage is very expensive.

 Instead of trying to minimize the number of swaps, they just want you to sort is as fast as possible knowing that the data is mostly sorted.

<question pythoncode>
csq_interface = 'ace'

csq_soln = '''
def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr.isLarger(j-1, j):
                arr.swap(j, j-1)
            else:
                break

'''

csq_initial = '''
def insertionSort(arr):
    n = len(arr)
    if arr.isLarger(0, 1):
        arr.swap(0, 1)
'''

def _swapBy1(arr, nSwaps):
    l = len(arr)
    for i in range(nSwaps):
        el = cs_random.randint(0,l-2)
        arr[el], arr[el+1] = arr[el+1], arr[el]

tests = [(5, 20, 20),
		 (10, 25, 25),
		 (20, 35, 35),
		 (40, 55, 55),
		 (100, 115, 115)]

orders = []

for n, _, _ in tests:
     a = [x for x in range(n)]
     _swapBy1(a, 10)
     orders.append(a)

csq_code_pre = f'''

class arrayToSort:
    def __init__(self, n, swap_limit, comparison_limit):
        self._a = [x for x in range(n)]
        self._order = [x for x in range(n)]
        self._swap_limit = swap_limit
        self._swaps = 0
        self._comparison = 0
        self._comparison_limit = comparison_limit        

    def __str__(self):
        return self._a

    def __repr__(self):
        return str(self._a)

    def swap(self, i, j):
        self._a[i], self._a[j] = self._a[j], self._a[i]
        self._swaps += 1
        too_many_swaps = self._swaps > self._swap_limit
        assert not too_many_swaps, "You performed too many swaps"

    def isLarger(self, i, j):
        self._comparison += 1
        a = self._a
        too_many_comps = self._comparison > self._comparison_limit
        assert not too_many_comps, "You performed too many comparisons"
        return self._order[a[i]] > self._order[a[j]]

    def __len__(self):
        return len(self._a)


_arrays_to_sort = []

tests = {tests}

orders = {orders}

for i, (n, swap, compare) in enumerate(tests):
	a = arrayToSort(n, swap, compare)
	a._order = orders[i]
	_arrays_to_sort.append(a)

'''




csq_tests = []

for i in range(len(tests)):
    csq_tests.append({
        'code': f"""
arr = _arrays_to_sort[{i}]
insertionSort(arr)
ans = arr
""" })

csq_npoints = 2
csq_name= "pcode2"
</question> 


### Merging!
Now they finally got some extra memory, and they are asking you to merge 2 sorted arrays of data into a larger array!

Again, they can't give you the data, so now they provide you another function:


```python

def isLarger(self, i,j):
    #Returns True if the data with id i is larger than the data with id j

```

Notice that this is now a global function, and not associated with the array anymore.

Notice that there might be duplicated data, which should be kept duplicated.

Write a function that merges the 2 arrays into a new array, sorted based on the isLarger(i,j) function.
<question pythoncode>
csq_interface = 'ace'

csq_soln = '''
def merge(arr1, arr2):
    l =  len(arr1) + len(arr2)
    i = 0
    j = 0
    newArray = []
    for k in range(l):
        if (i >= len(arr1)) or (j < len(arr2) and isLarger(arr1[i], arr2[j])):
            newArray.append(arr2[j])
            j += 1
        else:
            newArray.append(arr1[i])
            i += 1
    return newArray

'''

csq_initial = '''
def merge(arr1, arr2):
    newArr = []
    if isLarger(arr1[0], arr2[0]):
        newArr.append(arr2[0])
    else:
    	newArr.append(arr1[0])
    return newArr
'''


def _shuffle_all(arr):
    cs_random.shuffle(arr)

tests = [(3, 3),
	 (6, 6),
	 (3, 4),
	 (4, 1),
	 (100, 115),
	 (115, 100)]

full_tests = []

for n1, n2 in tests:
    order = [x for x in range(n1+n2+2)]
    _shuffle_all(order)

    a1 = [x for x in range(n1)]
    a2 = [x for x in range(n1-2, n1+n2-2)]

    a1.sort(key=lambda x: order[x])
    a2.sort(key=lambda x: order[x])
    
    full_tests.append((a1, a2, order, n1+n2))

csq_code_pre = f'''
isLarger = lambda x,y: x>y 
def _generate_isLarger(limit, order):
    swaps = [0]
    def _isLarger(i, j):
        swaps[0] += 1
        too_many_comps = swaps[0] > limit
        assert not too_many_comps, "You performed too many comparisons"
        return order[i] > order[j]
    global isLarger
    isLarger = _isLarger

tests = {full_tests}


'''




csq_tests = []

for i in range(len(tests)):
    csq_tests.append({
        'code': f"""
arr1 = tests[{i}][0] 
arr2 = tests[{i}][1]
_generate_isLarger(len(arr1) + len(arr2) + 3, tests[{i}][2] )
ans = merge(arr1, arr2)

""" })

csq_npoints = 1
csq_name= "pcode3"
</question> 
