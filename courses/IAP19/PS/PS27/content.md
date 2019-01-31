# Readings 
LOL good luck. Just search around the world wide pipes.

<python>
csq_npoints = 0
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
csq_prompt = """ What is the run-time of Prim's algorithm if we use a binary heap as our priority queue?
"""
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["O((E+V)*log(v))","theta((E+V)*log(v))", "O((E+V)*log(v),w)","theta((E+V)*log(v),w)"]
csq_explanation = ""
csq_nsubmits = None
</question>

TODO one day prove that it works


Write coding question to generate maze.

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
csq_explanation = "log"
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

We know that $ \ln(n) < \sum_{k=1}^{n} \frac{1}{k}< \ln(n)+1$, by bounding above and below by using $\int_1^n \frac{1}{x}$. We also know that $\frac{1}{x}- \frac{1}{x+1} = \frac{1}{(x)+(x+1)}$, which telescopes. So:

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
csq_prompt = "Implement quick sort using Hoare partition scheme! (In practice any sorting algorithm will pass this test, but implement quick sort!) `quicksort(A) -> sorts A, returns None`"

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

## Not in place quickselect (Bad)
This particular implementation uses, in the worst case, O(n^2) extra space, so it is quite bad. It is better to write an in place implementation, similarly to quicksort.

```python
def quickselect(A,k):
    if len(A) == 1:
        return A[0]
    else:
        pivot =  A[0]
        smaller = [x for x in A[1:] if x <= pivot] 
        larger = [x for x in A[1:] if x > pivot]
        if len(smaller) == k:
            return pivot
        elif len(smaller) > k:
            return quickselect(smaller, k)
        else:
            return quickselect(larger, k-len(smaller)-1)
```

# Run time analysis
Sooon
So the expected run time is $\Theta(n)$

# Flajolet-Martin 
Suppose we choose N random numbers between 0 and 1. What is the expected value of the smallest number?

