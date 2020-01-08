# Readings 
Good luck! Just search around the world wide pipes.

<python>
csq_npoints = 1/250
csq_nsubmits = None
csq_allow_submit_after_answer_viewed = False

</python>
# Prim's algorithm
Prim's algorithm is a **greedy** algorithm that generates a minimum spanning tree in an undirected graph with positive weights. A minimum spanning tree is a subset of edges of minimum total cost 

It is implemented almost exactly like Dijkstra, but instead of relaxing nodes like:

```python
# Dijkstra relaxation step
# supposing an adjacency list
# distances_pq = distances priority queue
def relaxNode(node, edges, distances_pq):
    d_node = distances_pq[node]
    for neighbor, weight in edges[node]:
        if neighbor in distances_pq:
            d_neighbor = distances_pq[neighbor]
            if d_neighbor > d_node + weight:
                distances_pq[neighbor] = d_node + weight
```

We do the following:

```python
# Prim's relaxation step
# supposing an adjacency list
# cost_of_connection_pq = distances priority queue

def relaxNode(node, edges, cost_of_connection_pq):
    d_node = cost_of_connection_pq[node]
    for neighbor, weight in edges[node]:
        if neighbor in cost_of_connection_pq:
            d_neighbor = cost_of_connection_pq[neighbor]
            if d_neighbor >  weight:
                cost_of_connection_pq[neighbor] = weight
```

And instead of being interested on the distances to each node, we are interested in the sum of the cost of connections, which is the total cost of the tree, as well as the edges.

In other words, the algorithm is:

- Start with a single node
- Grow your tree one edge at a time, by choosing the edge of smallest weight that connects a new node to your tree
- Repeat until all nodes are connected.



<question expression>
csq_prompt = """ What is the run-time of Prim's algorithm if we use a binary heap as our priority queue? In terms of E and V. Write it as O(f(V, E))
"""
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["O((E+V)*log(V))", "O((e+v)*log(v))", "O((E+V)*log(v))","theta((E+V)*log(V))", "O((E+V)*log(V),w)","theta((E+V)*log(V),w)"]
csq_explanation = ""
csq_nsubmits = None
</question>

TODO one day write the proof that it works here. But for now, just check the [wikipedia page](https://en.wikipedia.org/wiki/Prim%27s_algorithm).


TODO One day write coding question to generate maze. For now, just look at the [maze animation on wikipedia](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/MAZE_30x20_Prim.ogv/220px--MAZE_30x20_Prim.ogv.jpg)

# Quick sort
Do you wanna sort things quickly? So let's talk about quick sort.

## Algorithm
- Choose a pivot from the array.
- Put everything that is smaller than the pivot to the left.
- Put everything that is larger than the pivot to the right.
- Put the pivot in the middle.
- Recurse on both sides.

Each step runs in expected $O(n)$, and the expected run time will be $O(n log (n))$
## Not in place implementation (

```python
def quicksort(A):
    if len(A) <= 1:
        return A
    else:
        pivot =  A[0]
        return quicksort([x for x in A[1:] if x <= pivot]) \
             + [pivot] \
             + quicksort([x for x in A[1:] if x > pivot])  
```


<question expression>
csq_prompt = """ Consider the best case scenario, when the pivot we choose is always the median of the array we are sorting.

How much time (in big O notation) will the above code take?

"""
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["O(n*log(n))","theta(n*log(n))", "O(n*log(n),w)","theta(n*log(n),w)"]
csq_explanation = "Same as merge sort!"
csq_nsubmits = None
</question>

<question expression>
csq_prompt = """ Consider the best case scenario, when the pivot we choose is always the median of the array we are sorting.

How much extra space (in big O notation) will the above code take?
<showhide>
Hint: one recursive call has to return before we call the other one
</showhide>
"""
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["O(n)","theta(n)", "O(n,w)","theta(n,w)"]
csq_explanation = ""
csq_nsubmits = None
</question>

## In place implementation (good)!
So now, instead we will implement counting sort using the Hoare partition scheme (see [wikipedia!](https://en.wikipedia.org/wiki/Quicksort))

- Our pivot is the first element of the array (or we swap a random pivot with the first element of the array).
- We keep 2 pointers, 
     - one starting at the second element and moving to the right
     - one starting at the last element and moving to the left
- While the pointers don't cross each other:
     - if the left pointer points to an element smaller than the pivot, move the pointer to the right
     - else if the right pointer points to an element larger than the pivot, move the pointer to the left
     - else we swap both of those elements, and move both pointers
- After the elements have crossed, swap the pivot with the element in the right pointer (that is now to the left)

- And, finally, recurse on both sides.


Since we never allocate a new array, i.e. we only pass references of the array to the recursion steps
<question expression>
csq_prompt = """ *Trick question* 

Consider the best case scenario, when the pivot we choose is always the median of the array we are sorting.

How much extra space (in big O notation) will the in place implementation take?
<showhide>
Hint: how much space gets allocated for a function call? What is the height of the recursion tree?
</showhide>
"""
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["O(log(n))","theta(log(n))", "O(log(n),w)","theta(log(n),w)"]
csq_explanation = "O(1) per recursion, and the depth is log(n)"
csq_nsubmits = None
</question>

## Expected runtime of quick sort.
This section will only make sense if you are familiar with linearity of expectation and it will have some math.

We will partially follow [these lecture notes](https://people.engr.ncsu.edu/mfms/Teaching/CSC505/wrap/Lectures/week05.pdf), and [these notes ](http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/7-Sort/Docs/QuickSortAnal.pdf)

Let $\tilde{T}(n)$ be the expected number of comparisons performed by quick sort. 

Since there is a $\frac{1}{n}$ chance of splitting the array into a subarray of size $k$ and size $n-k$, for any value of $k$ between $0$ and $n-1$. And independent on how it splits, it performs $n-1 comparisons.

So:

$$\tilde{T}(n) = (n-1) + \sum_{k=1}^{n-1} \frac{1}{n}\left(\tilde{T}(k) + \tilde{T}(n-k)  \right) = (n-1)+ \sum_{k=1}^{n-1} \frac{1}{n}2 \tilde{T}(k)  $$

So, to simplify the right hand side in order to cancel terms, we multiply everything by $n$.

$$ n \tilde{T}(n) =  n(n-1)+ \sum_{k=1}^{n-1} 2 \tilde{T}(k)  $$

Writing now $T(n-1)$

$$ (n-1) \tilde{T}(n-1) =  (n-1)(n-2)+ \sum_{k=1}^{n-2} 2 \tilde{T}(k) $$

Subtracting one by the other

$$ n \tilde{T}(n) - (n-1) \tilde{T}(n-1) =  n(n-1)-(n-1)(n-2)+ 2 \tilde{T}(n-1) $$

So:

$$ n \tilde{T}(n)  =  2(n-1)+ (n+1) \tilde{T}(n-1) $$
And at last, dividing everything by $n$ and $n+1$

$$ \frac{\tilde{T}(n)}{n+1}  =  \frac{2(n-1)}{n(n+1)}+ \frac{\tilde{T}(n-1)}{n} $$

We can now simplify the above equation by defining $B(n) = \frac{\tilde{T}(n)}{n+1}$


$$ B(n)  =  \frac{2(n-1)}{n(n+1)}+ B(n-1) $$

Which is trivially solved:

$$ B(n)  =  \sum_{k=1}^{n-1} \frac{2(k-1)}{k(k+1)} =  \sum_{k=1}^{n-1} \left( \frac{2}{k+1} - \frac{1}{k(k+1)}\right)$$

$$ B(n)  = \sum_{k=2}^{n} \frac{2}{k} - \sum_{k=1}^{n-1} \frac{1}{k(k+1)}$$

We know that $ \ln(n) < \sum_{k=1}^{n} \frac{1}{k}< \ln(n)+1$, by bounding above and below by using $\int_1^n \frac{1}{x}$ and $1+ \int_1^n \frac{1}{x}$ (draw the graph). We also know that $\frac{1}{x}- \frac{1}{x+1} = \frac{1}{(x)+(x+1)}$, which telescopes. So:

$$ \sum_{k=1}^{n-1} \frac{1}{k(k+1)} = \frac{1}{1} - \frac{1}{n} $$

So,

$$ 2 \left(\ln(n)-\ln(2)-1\right) - \frac{1}{1} + \frac{1}{n} < B(n)  < 2\left(\ln(n)+1-\ln(2)\right) - \frac{1}{1} + \frac{1}{n}$$

$$ 2\ln(n)- 2\ln(2)- 3 + \frac{1}{n} < B(n)  < \ln(n)-\ln(2) + 1 + \frac{1}{n}$$

Since $ -2\ln(2) + 1 + \frac{1}{n} << \ln(n)$

$$  B(n)  \approx 2\ln(n) \approx 1.39 \log_2(n)$$
And, therefore:

$$  T(n)  \approx 2n\ln(n) \approx 1.39 n\log_2(n)$$

<checkyourself>
Try to understand the derivation above and its consequences.
</checkyourself>

<checkyourself>
How does this compare with an optimal algorithm that performs the minimum number of comparisons possible?
<showhide>
The information theoretica lower bound is $\log_2(n!) \approx n\log_2(n) -n \approx n \log_2(n)$. So we perform approximately 39% more comparisons in expectation in quick sort.
</showhide>
</checkyourself>


<question pythoncode>
csq_interface = 'ace'
csq_prompt = """Implement quick sort using Hoare partition scheme! (In practice any sorting algorithm will pass this test, but implement quick sort!) `quicksort(A) -> sorts A, returns None`

Take a look at the solution after you are finished.
"""

## Define solution that will be printed to student.
csq_soln = """
def quicksort(array, start = None, end = None):
    if start == None and end == None:
        start = 0
        end = len(array)-1
    if start >= end:
        return
    else:

        pivot = array[start]
        left = start+1
        right = end

        while left <= right: #equal forces the cross
            if array[left] <= pivot:
                left += 1
            elif array[right] >= pivot:
                right -= 1
            else:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        array[start], array[right] = array[right], array[start]
        quicksort(array, start, right-1)
        quicksort(array, right+1, end)        

"""

## Code that will be initially on the thingy
csq_initial = """def quicksort(A): 
    return A
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
tests = [1, 5, 6, 10, 20, 100, 200, 501, 1000]

full_tests = [[cs_random.random() for x in range(n)] for n in tests]



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
quicksort(A)
ans = A
""" ,
        'show_code': i < 5,
        'grade': True,
    })

</question> 

# Quick Select!

In quick select we solve the following problem: given an array A, return the $k$th smalllest element. In particular, return the median.

On quick sort, we chose a pivot, partitioned the data, and then recursed on both halves. In quick select we will only recurse in one of the halves.

We will use harmonic sum approximation as well as $\ln(n!) = n\ln(n) + O(n)$ approximation

<checkyourself>
Why is the harmonc sum $\sum_{k=1}^{n} \frac{1}{k}< \ln(n)+1$, and $\sum_{k=1}^{n} \frac{1}{k}> \ln(n)$ ?

Draw a curve whose area under the curve is $\sum_{k=1}^{n} \frac{1}{k}$ and another whose area under the curve is $\int_1^n \frac{1}{x} dx$ and at last one that is $1+ \int_1^n \frac{1}{x} dx$. How do they compare?
<showhide>
The harmonic sum wil be the upper riemman sum of one of the integrals and the lower riemman sum of the other one (with rectangles of base 1) 
</showhide>
</checkyourself>


## Not in place quickselect (Bad)
This particular implementation uses, in the worst case, O(n^2) extra space, so it is quite bad. It is better to write an in place implementation, similarly to quicksort.

```python
from random import randint
def quickselect(A,k):
    if len(A) == 1:
        return A[0]
    else:
        random_index = randint(0,len(A)-1)
        A[0], A[random_index] = A[random_index], A[0]
        pivot = A[0]
        smaller = [x for x in A[1:] if x <= pivot] 
        larger = [x for x in A[1:] if x > pivot]
        if len(smaller) == k:
            return pivot
        elif len(smaller) > k:
            return quickselect(smaller, k)
        else:
            return quickselect(larger, k-len(smaller)-1)
```

## Run time analysis
The runtime analysis of quickselect will be done in a different way than the runtime analysis of quick sort. It will be based [on this page](http://www.cs.cmu.edu/afs/cs/academic/class/15451-s99/www/lectures/lect0121).

First we define $X_{i,j}$ to be an indicator variable, it is 1 if element $i$th smallest element is compared with element $j$th smallest element, or 0 otherwise, defined for $i < j$

The expected number number of comparisons done by quickselect, will be, therefore:

$$ E[\text{Comparisons}] = E\left[\sum_{0 \le i < j < n} X_{i,j}\right] $$ $$= \sum_{0 \le i < j < n} P\left( X_{i,j} = 1 \right) $$

Therefore we just need to find the probability of 2 elements being compared with each other.

### When are 2 elements compared?

2 elements are compared with each other if they are in the same partition, they are in the partition we are recursing on, and we randomly choose one of them to be our pivot.

In other words, 2 elements are compared if we choose one of those 2 elements before choosing one of the elements that would split them into separate partitions or would put them in the partition where we'd ignore them.

This naturally leads to 3 base cases: both $i$ and $j$ are smaller or equal to $k$, both $i$ and $j$ are greater or equal to $k$, or $i$ is smaller than $k$ and $j$ is greater than $k$.

#### Case $i< j \le k$

<question expression>
csq_prompt = """Suppose $i< j \le k$

For many different values of the pivot would it result in $i$ and $j$ either being put in different partitions, or both of them being put in the opposite partition as $k$?

In other words, for how many different values of the pivot would $i$ and $j$ never be compared with one another if those values were chose before $i$ or $j$? 
<showhide>
Hint: That is the same number of pivot values that would cause $i$ to be in a separate partition as $k$, including $k$ or $i$ being chosen; -2 element, since $j$ and $i$ are between $i$ and $k$ inclusive. 
</showhide>
"""
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["k-i-1"]
csq_explanation = "there are k-i+1 elements inclusive between $k$ and $i$, but $i$ and $j$ don't count."
csq_nsubmits = None
</question>


<question expression>
csq_prompt = """
What is the probability of $i$ or $j$ being chosen as a pivot before any of the elements above being chosen to be a pivot? 

In other words, what is the probability of $i$ and $j$ being compared?

Notice that there is symmetry, the probability of choosing any element is the same.
"""
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["2/(k-i+1)"]
csq_explanation = "there are k-i+1 elements inclusive between $k$ and $i$, and we want the probablity of choosing 2 of them."
csq_nsubmits = None
</question>

Therefore we have calculated  $P\left( X_{i,j} = 1 \right)$

<question multiexpression>
csq_prompt = """
Supposing $i < j \le k$, the expected number of collisions for those elements is:

$$\\sum_{0 \\le i < j < n} P\\left( X_{i,j} = 1 \\right) = \\sum_{i=a}^{b} \\sum_{j=c}^{d}  P\\left( X_{i,j} = 1 \\right)$$

What are the summation bounds? I.e. what is a,b,c,d?
"""
csq_expressions = [
("$a = $", "0"),
("$b = $", "k-1"),
("$c = $", "i+1"),
("$d = $", "k")]
csq_explanation = ""
</question>


<question expression>
csq_prompt = """
Supposing you did everything correct so far, the inner sum should be independent from $j$, therefore you can expand the double sum to:

$$\\sum_{0 \\le i < j \le k} P\\left( X_{i,j} = 1 \\right) = \\sum_{i=a}^{b} \\text{ expression }$$

What is the value of expression?
"""
csq_soln = ["2 (k-i-1)/(k-i+1)"]
csq_explanation = ""
</question>

<question expression>
csq_prompt = """
The expression above can be rewritten as

$$2 (1 - \\text{ expression2})$$

What is the value of expression2?
"""
csq_soln = ["2/(k-i+1)"]
csq_explanation = ""
</question>

Therefore the sum will be approximately

$$2k - 4 \ln(k-1) + O(1)$$

We will only consider the higher order terms, so $$\sum_{0 \le i < j \le k} P\left( X_{i,j}\right) \le 2k$$

#### Case $k \le i< j$
This case is exactly analogous to the previous one.
<question expression>
csq_prompt = """Suppose $k \le i< j$

For many different values of the pivot would it result in $i$ and $j$ either being put in different partitions, or both of them being put in the opposite partition as $k$?

In other words, for how many different values of the pivot would $i$ and $j$ never be compared with one another if those values were chose before $i$ or $j$? 
<showhide>
Hint: That is the same number of pivot values that would cause $j$ to be in a separate partition as $k$, including $k$ or $j$ being chosen; -2 element, since $i$ and $j$ are between $k$ and $j$ inclusive. 
</showhide>
"""
csq_soln = "j-k-1"
csq_explanation = "there are j-k+1 elements inclusive between $k$ and $j$, but $i$ and $j$ don't count."
csq_nsubmits = None
</question>


<question expression>
csq_prompt = """
What is the probability of $i$ or $j$ being chosen as a pivot before any of the elements above being chosen to be a pivot? 

In other words, what is the probability of $i$ and $j$ being compared?

Notice that there is symmetry, the probability of choosing any element is the same.
"""
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = "2/(j-k+1)"
csq_explanation = "there are j-k+1 elements inclusive between $k$ and $j$, and we want the probablity of choosing 2 of them."
csq_nsubmits = None
</question>

Therefore we have calculated  $P\left( X_{i,j} = 1 \right)$ for this case

<question multiexpression>
csq_prompt = """
Supposing $i < j \le k$, the expected number of collisions for those elements is:

$$\\sum_{0 \\le i < j < n} P\\left( X_{i,j} = 1 \\right) = \\sum_{j=a}^{b} \\sum_{i=c}^{d}  P\\left( X_{i,j} = 1 \\right)$$

What are the summation bounds? I.e. what is a,b,c,d?
"""
csq_expressions = [
("$a = $", "k+1"),
("$b = $", "n"),
("$c = $", "k"),
("$d = $", "j-1")]
csq_explanation = ""
</question>


<question expression>
csq_prompt = """
Supposing you did everything correct so far, the inner sum should be independent from $i$, therefore you can expand the double sum to:

$$\\sum_{k \\le i < j < n} P\\left( X_{i,j} = 1 \\right) = \\sum_{j=a}^{b} \\text{ expression }$$

What is the value of expression?
"""
csq_soln = ["2 (j-k-1)/(j-k+1)"]
csq_explanation = "just multiply by the number of elements in the sum"
</question>

<question expression>
csq_prompt = """
The expression above can be rewritten as

$$2 (1 - \\text{ expression2})$$

What is the value of expression2?
"""
csq_soln = "2/(j-k+1)"
csq_explanation = ""
</question>

Therefore the sum will be approximately

$$2(n-k) - 4 \ln(n-k) + O(1)$$

We will only consider the higher order terms, so $$\sum_{k \le i < j < n } P\left( X_{i,j}\right) \le 2(n-k)$$

#### Case $ i < k < j$
This is the hardest case

<question expression>
csq_prompt = """Suppose $ i < k < j$

For many different values of the pivot would it result in $i$ and $j$ either being put in different partitions, or both of them being put in the opposite partition as $k$?

In other words, for how many different values of the pivot would $i$ and $j$ never be compared with one another if those values were chosen before $i$ or $j$? 
<showhide>
Hint: That is the same number of pivot values that would cause $j$ to be in a separate partition as $i$, including $i$ or $j$ being chosen; -2 element, since $i$ and $j$ are between $i$ and $j$ inclusive. 
</showhide>
"""
csq_soln = "j-i-1"
csq_explanation = "there are j-i-1 elements inclusive between $i$ and $j$, but $i$ and $j$ don't count."
csq_nsubmits = None
</question>


<question expression>
csq_prompt = """
What is the probability of $i$ or $j$ being chosen as a pivot before any of the elements above being chosen to be a pivot? 

In other words, what is the probability of $i$ and $j$ being compared?

Notice that there is symmetry, the probability of choosing any element is the same.
"""
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = "2/(j-i+1)"
csq_explanation = "there are j-i+1 elements inclusive between $k$ and $j$, and we want the probablity of choosing 2 of them."
csq_nsubmits = None
</question>

Therefore we have calculated  $P\left( X_{i,j} = 1 \right)$ for this case

<question multiexpression>
csq_prompt = """
Supposing $i < j \le k$, the expected number of collisions for those elements is:

$$\\sum_{0 \\le i < k < j < n} P\\left( X_{i,j} = 1 \\right) = \\sum_{i=a}^{b} \\sum_{j=c}^{d}  P\\left( X_{i,j} = 1 \\right)$$

What are the summation bounds? I.e. what is a,b,c,d?
"""
csq_expressions = [
("$a = $", "0"),
("$b = $", "k-1"),
("$c = $", "k+1"),
("$d = $", "n")]
csq_explanation = ""
</question>


<question expression>
csq_prompt = """
Supposing you did everything correct so far, the inner sum should be dependent on both $i$ and $j$ 

Using the approximation the harmonic sum approximation.

$$ \\sum_{k=a}^{b} \\frac{1}{k} \\approx \\ln(a) - \\ln(b) $$

What is the result of expanding the inner sum?

$$\\sum_{i=a}^{b} \\sum_{j=c}^{d}  P\\left( X_{i,j} = 1 \\right) = \\sum_{i=a}^{b} \\text{expression}$$

i.e. what is expression?

use ln(x) for natural log of x
"""
csq_soln = "2*(ln(n-i+1) - ln(k-i+2))"
csq_explanation = "Using the harmonic sum approximation"
</question>

<question expression>
csq_prompt = """
Now, remembering that $$\\ln(a) + \\ln(b) = \\ln(a\\cdot b)$$

We can write:

$$ \\sum_{i=a}^{b} \\ln(i) = \\ln\\left(\\frac{a!}{b!}\\right)$$  

So fully expand the sum above.

To write $a!$ write $fact(a)$

if you dop the expansion correct you should have a $+ \\ln(2!)$$ term.
"""
csq_soln = "2*(ln(fact(n+1)/fact(n-k+2))-ln(fact(k+2)/fact(2)))"
csq_explanation = ""
</question>



<question expression>
csq_prompt = """
Now, let's throw away all the non-multiplicative contants, i.e. $$2x + 1 \\approx 2x$$, since the error as $n \\to \\infty $ is negligible.

What is the result from this simplification on the above result?
"""
csq_soln = "2*(ln(fact(n)/fact(n-k))-ln(fact(k)))"
csq_explanation = ""
</question>

<question expression>
csq_prompt = """
By using Sterling's approximation, $$\\ln(n!) = n\\ln(n) -O(n)$$, and using that $$n\\ln(n) >> O(n) \\text{ as $n\\to \\infty$}$$ 

What is the result of using this simplification in the above formula?

Please write it as $(n-k) \\cdot (\\text{expression} + k \\cdot  (\\text{expression 2})$  You will need to substitute $n = (n-k) + k$. If you can't write it in this form, please click view answer after getting an equivlent result.
"""
csq_soln = "2*((n-k)*ln(n/(n-k)) + (k)*ln(n/(k)))"
csq_explanation = ""
</question>

<question expression>
csq_prompt = """
The previous result has a maximum when $k = n/2$.

What is the maximum of the previous question, in terms of $n$?
"""
csq_soln = "2*n*ln(2)"
csq_explanation = ""
</question>


### Putting it all together. 

<question expression>
csq_prompt = """
What is $$ \\sum_{0 \\le i < j < n} P\\left( X_{i,j} = 1 \\right) $$ ?

Write it in terms of $k$ and $n$. Sum the result from the previous 3 parts.

"""
csq_soln = "2*n + 2*((n-k)*ln(n/(n-k)) + (k)*ln(n/(k)))"
csq_explanation = ""
</question>

<question expression>
csq_prompt = """
What is a tight upperbound on $$ \\sum_{0 \\le i < j < n} P\\left( X_{i,j} = 1 \\right) $$ in terms of $n$?

 Sum the result from the previous 3 parts and assume $k =n/2$, since this value maximizes the previous result.

This will be the upperbound.
"""
csq_soln = "n*(2+2ln(2))"
csq_explanation = ""
</question>

If you did it all right, you should have found approximately 3.4.

<checkyourself>
Try implementing in place quickselect.  
</checkyourself>

# Flajolet-Martin 
Read this algorithm. It is really cool. Here are [Ankur Moitra's 6.854 notes](http://people.csail.mit.edu/moitra/docs/6854lec4.pdf). I didn't have time to write the questions.
