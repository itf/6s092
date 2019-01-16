# Readings 
[Recitation notes 5a](https://learning-modules.mit.edu/service/materials/groups/238004/files/fc07d4e4-0f2d-403c-940c-7bb587064109/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), 6.006 Fall 2018 on stellar.

[Lecture notes 5](https://learning-modules.mit.edu/service/materials/groups/238004/files/4b4527ac-ff36-46f2-9079-2cd7dee5bec9/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), 6.006 Fall 2018 on stellar.

# Priority Queues: Conceptual Questions


<question multiplechoice>
csq_prompt = "Which of the following operations do most priority queues execute efficiently?"
csq_renderer = "checkbox"
csq_soln = [1,1,1,0]
csq_options =  ['Return the length of the set',
'Remove the element with the greatest (or least) key',
'Insert an element with some key',
'Remove an element with a particular key']
csq_name="p1"
</question>

<question multiplechoice>
csq_prompt = "Which of the following data structures could support the priority queue interface?"
csq_renderer = "checkbox"
csq_soln = [1,1,1,1]
csq_options =  ['An unsorted dynamic array, where, upon being asked for the max, searches through the entire array and returns the element with maximal key',
'A sorted dynamic array, where each element is inserted into the proper location by key (in descending order), and upon being asked for the max returns the first element',
'A binary search tree, as seen in PS16',
'A binary max heap']
csq_name="p2"
</question>

<question expression>
csq_prompt = "How much time would it take to find the min element of a max heap with $n$ elements?"
csq_soln = ["O(n)", "Theta(n)"]
csq_explanation = "We at least must visit every leaf of the tree, and there are $\\Theta(n)$ leaves."
</question>

<checkyourself>
If a priority queue (with unique keys) is optimized to return and remove the element with the greatest key value in $O(1)$ time, can it return the second greatest key in $O(1)$ time as well? How?
<showhide>
Yes. First, remove the element with the greatest key in $O(1)$ time and store it. Then, remove the next element with greatest key: this was the element with the second greatest key originally.
</showhide>
</checkyourself>


# Binary Heaps: Structure

Recall that binary heaps are *complete binary trees*, meaning that they are binary trees in which every row, except possibly the last, is fully filled. When the last row is not full, the leaves are filled in left to right. 

This means that, given $k$ levels or rows to a binary heap, there are  $n = \sum_{i = 0}^{k-2} 2^i + r = 2^{k-1} + r - 1 \geq 2^{k-1}$ elements in the heap, where $r$ represents the number of elements in the last, possibly incomplete level (so $0 < r \leq 2^{k-1}$). With this result we see that $2^{k-1} \leq n$, so $k-1 \leq \log(n)$ and so $k = \log (n)$. This bound on the height of the tree allows us to argue that the operations we use a heap for really are $O(\log n)$. 

In the following questions we explore the completeness of binary heaps.

<question expression>
csq_prompt = "If a binary tree has $41$ elements, how many rows does it have?"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = '6'
csq_nsubmits = None
csq_name="p3"
</question>

<question multiplechoice>
csq_prompt = "In the previous example, is the last row complete?"
csq_renderer = "radio"
csq_soln = 'No'
csq_options =  ['Yes','No']
csq_name="p4"
</question>

<question expression>
csq_prompt = "Suppose a binary tree has $8$ rows. Let $l$ be the minumum number of elements it could contain, and $m$ be the maximum number of elements it could contain. What is $l+m$? Feel free to express your answer as an expression like `a^b + c`"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = '383'
csq_explanation = "The values are $(l,m) = (128, 255)$."
csq_nsubmits = None
csq_name="p5"
</question>

#Binary Trees: Implementation
Recall that binary trees are often implemented as just (dynamic) arrays, with the elements in the first row listed before the elements in the second, before the elements in the third, and so on. With some simple arithmetic (and zero-indexing!) we gather that the left child of the parent in position $i$ is stored in position $2i+1$, and the right child in position $2i+2$.

<!-- <question pythoncode>
csq_interface = 'ace'
csq_prompt = "THIS QUESTION IS INCOMPLETE. Write a function that takes in an index $i$ and returns the index of its parent. If given the root node, the function should return the root node index (0) again, for reasons we will see later."

## Define solution that will be printed to student.
csq_soln = """
def parent(i): 
    return 0 if i == 0 else (i-1)//2
"""

## Code that will be initially on the thingy
csq_initial = """def parent(i): 
    return 
"""

## Sandbox options to block libraries or decide how long to run thingy
csq_sandbox_options = {
    'BADIMPORT': ['lib601', 'numpy', 'scipy', 'matplotlib'], 
    'CLOCKTIME': 0.36, 
    # 'CPUTIME': 0.36, 
    'MEMORY':1e9
}

csq_test = []
</question> -->

Next, determine whether the following arrays represent min heaps, max heaps, or neither.
<question multiplechoice>
csq_prompt = "$[1,2,3,4,5,6,7,8,9,10]$"
csq_renderer = "radio"
csq_soln = 'Min heap'
csq_options =  ['Min heap',
'Max heap',
'Neither']
csq_name="p6"
</question>

<question multiplechoice>
csq_prompt = "$[1,3,2,8,4,5,7,9,10,6]$"
csq_renderer = "radio"
csq_soln = 'Min heap'
csq_options =  ['Min heap',
'Max heap',
'Neither']
csq_name="p7"
</question>

<question multiplechoice>
csq_prompt = "$[10,8,7,9,3,6,5,4,2,1]$"
csq_renderer = "radio"
csq_soln = 'Neither'
csq_options =  ['Min heap',
'Max heap',
'Neither']
csq_name="p8"
</question>

<question multiplechoice>
csq_prompt = "$[10,6,9,4,5,7,8,3,2,1]$"
csq_renderer = "radio"
csq_soln = 'Max heap'
csq_options =  ['Min heap',
'Max heap',
'Neither']
csq_name="p9"
</question>

<question expression>
csq_prompt = "In the example of a non-heap above, exactly two elements $(a,b)$ could have been swapped, resulting in a valid max heap. What is $a+b$?"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = '17'
csq_explanation = "The values are $(a,b) = (8,9)$."
csq_nsubmits = None
csq_name="p10"
</question>

# Binary Heaps: Maintaining Them
The key to binary heaps is maintaining the max-heap property (or min-heap property, if it's a min-heap), which requires a nodes key value to be greater than the key value of its children. 

<checkyourself>
This property gives our heap the ability to find the element with greatest key very quickly: it's always the root of the tree. Why is that?
<showhide>
Suppose the keys are unique. Then, if the maximum were anywhere but the root, it would have a parent that must have a greater key. But this is impossible because it is the maximum, so it must be at the root.

Alternatively the max-heap property ensures that the ancestors of any node have a key value at least that of the node: proving this by induction is pretty straightforward, or you can convince yourself by looking at the parent of the parent of a node. If $\verb|node.key| \leq \verb|node.parent.key|$, and $\verb|node.parent.key| \leq \verb|node.parent.parent.key|$, then clearly $\verb|node.key| \leq \verb|node.parent.parent.key|$. And so on.

Then the root, which is everyone's ancestor, must have key value that is at least the value of any other node. This makes it the maximum.
</showhide>
</checkyourself>

So if we ensure that our binary heap maintains the max-heap property, this will, in turn, make sure that the binary heap keeps the element with greatest key value at the top: the primary feature of a priority queue!

Then the question becomes: how do we ensure that the binary heap maintains the max-heap property, even when we do operations on it (inserting a new element, removing the maximum element)?

For insertions, the answer is simple. Put it at the end of your binary heap! Then, if the element's key is greater than its parent, switch them. But now, it might be that the parent's key is greater that *its* parents key, so we have to compare those as well. The code for this idea, written recursively, looks like:
```python
def max_heapify_up(A, c):
    p = parent(c)                   # get the parent (defined this function earlier)
    if A[p].key < A[c].key:         # if the child has a greater key
        A[p], A[c] = A[c], A[p]     # switch parent and child
        max_heapify_up(A, p)        # check if the new "parent" now needs to be moved up further
```
And so, to add a new element $k$ to our heap we just do:
```python
A.append(k)                         # insert at the end
max_heapify_up(A, len(A)-1)         # make sure max-heap property is satisfied
```

<checkyourself>
Why is $c$ set to len(A)-1 in the code above?
<showhide>
In the definition of `max_heapify_up`, $c$ is an index in the array. We want to apply max heapify to the element we just inserted, which is in position len(A)-1 with zero indexing.
</showhide>
</checkyourself>

<question multiplechoice>
csq_prompt = "The key observation for the runtime of `max_heapify_up` is that each time we have to recurse, we are recursing on the parent, and therefore getting one level closer to the root. So we can bound the runtime using the number of levels in the tree. With this in mind, what is the runtime of inserting an element with this implementation? Here, $n$ represents the number of elements in the heap."
csq_renderer = "radio"
csq_soln = '$O(\log n)$'
csq_options =  ['$O(1)$',
'$O(\log n)$',
'$O(n)$',
'$O(n \log n)$',
'$O(n^2)']
csq_explanation = 'The number of levels in the tree is $O(\log n)$, as discussed earlier in the problem set.'
csq_name="p11"
</question>

<question expression>
csq_prompt = "Suppose we were to add $8$ to a max-heap that is currently $[10,7,9,4,6,5,7,2,2,1,1]$. How many times would we have to call on `max_heapify_up`? (This includes the final time, where it does not switch any elements.)"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = '2'
csq_nsubmits = None
csq_name="p12"
</question>

<question expression>
csq_prompt = "Suppose we were to add $8$ to a max-heap that is currently $[10,7,9,4,6,5,7,2,2,1]$. How many times would we have to call on `max_heapify_up`? (This includes the final time, where it does not switch any elements.)"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = '3'
csq_nsubmits = None
csq_name="p13"
</question>

<checkyourself>
The second max heap is strictly shorter than the first, but it took longer to insert a new element. Does this contradiction the bound we found that it takes $O(\log n)$ time to insert? Why or why not?
<showhide>
No. The insert operation doesn't necesarilly take longer for a longer input. The runtime we found simply tells us that in the long run, we won't do any worse than some constant factor of $\log n$.<!--  This is the case for many algorithms; it's rare for the runtime to increase strictly monotonically with $n$. -->
</showhide>
</checkyourself>

Along with the insert operation, we need to be able to remove the maximum. This is a bit trickier because removing the root leaves us with... a tree with no root. We can't have that. So again, our solution is perhaps the simplest possible one: take the last element in the heap (which has no children) and put it at the root, replacing the maximum.

The only problem is that, of course, it is very unlikely that this element has the greatest key. Note, however, that this element is the *only* one not obeying the max heap property. So we run `max_heapify_down`, which moves this misplaced element back into its place, without messing with the other elements of the heap. It looks very familiar:

```python
def max_heapify_down(A, p):
    l, r = 2 * c + 1, 2 * i + 2             # get the parent (defined this function earlier)
    c = l if A[l].key > A [r].key else r    # chooses the child with the bigger key
    if A[c].key > A[p].key:                 # if the child is bigger than that of p
        A[p], A[c] = A[c], A[p]             # switch parent and child
        max_heapify_down(A, c)                # check if the new "child" now needs to be moved down further
```

<question multiplechoice>
csq_prompt = "Using this `max_heapify_down` function, how would you implement the `remove_max` functionality of a priority queue?"
csq_renderer = "radio"
csq_soln = """
```
A[0]=A[len(A)-1]
delete A[len(A)-1]
max_heapify_down(A,0)
``` """

csq_options =  ["""
```
A.append(k)
max_heapify_down(A, len(A)-1)
``` """, """
```
A[0]=A[len(A)-1]
delete A[len(A)-1]
max_heapify_down(A,0)
``` """, """
```
A[0]=A[len(A)-1]
delete A[len(A)-1]
max_heapify_down(A,len(A)-1)
``` """, """
max_heapify_down(A,0)
delete A[len(A)-1]
``` """, """
```
max_heapify_down(A,len(A)-1)
delete A[0]
``` """]
csq_explanation = 'The number of levels in the tree is $O(\log n)$, as discussed earlier in the problem set.'
csq_name="p14"
</question>
