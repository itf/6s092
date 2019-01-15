# Readings 
Recitation notes 5, 6.006 Fall 2018 on stellar.

Lecture notes 5, 6.006 Fall 2018 on stellar.

# Priority Queues: Conceptual Questions


<question multiplechoice>
csq_prompt = "Which of the following operations do most priority queues execute efficiently?"
csq_renderer = "checkbox"
csq_soln = [1,1,0,1,0]
csq_options =  ['Return the length of the set',
'Remove the element with the greatest (or least) key',
'Sort the elements of a set by key',
'Insert an element with some key',
'Remove an element with a particular key']
csq_name="p1"
</question>

<question multiplechoice>
csq_prompt = "Which of the following would be considered a priority queue?"
csq_renderer = "checkbox"
csq_soln = [1,1,0,1]
csq_options =  ['An unsorted array, where, upon being asked for the max, searches through the entire array and returns the element with maximal key',
'A sorted array, where each element is inserted into the proper location by key (in descending order), and upon being asked for the max returns the first element',
'A binary search tree, as seen in PS16',
'A binary max heap']
csq_name="p2"
</question>

<checkyourself>
If a priority queue (with unique keys) is optimized to return and remove the element with the greatest key value in O(\log n) time, can it return the second greatest key in $O(\log n)$ time as well? How?
<showhide>
Yes. First, remove the element with the greatest key in $O( \log n)$ time and store it. Then, remove the next element with greatest key: this was the element with the second greatest key originally. Reinsert the first element we had to remove, if necesarry.
</showhide>
</checkyourself>


# Binary Heaps: Structure

Recall that binary heaps are *complete binary trees*, meaning that they are binary trees in which every row, except possibly the last, is fully filled. When the last row is not full, the leafs are filled in left to right. 

This means that, given $k$ levels/ rows to a binary heap, there are  $n = \sum_{i = 0}^{k-2} 2^i + r = 2^{k-1} + r - 1 \geq 2^{k-1}$ elements in the heap, where $r$ represents the number of elements in the last, possibly incomplete level (so $0 < r \leq 2^{k-1}$). With this result we see that $2^{k-1} \leq n$, so $k-1 \leq \log(n)$ and so $k = \log (n)$. This bound on the height of the tree allows us to argue that the operations we use a heap for really are $O(\log n)$. 

In the following questions we explore the completeness of binary heaps.
<question expression>
csq_prompt = "If a binary tree has $41$ elements, how many rows does it have?"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = '6'
csq_explanation = "explanation"
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
csq_prompt = "Suppose a binary tree has $8$ rows. Let $l$ be the minumum number of elements it could contain, and $m$ be the maximum number of elements it could contain. What is $(l,m)$?"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = '(128,255)'
csq_explanation = "explanation"
csq_nsubmits = None
csq_name="p5"
</question>

#Binary Trees: Implementation
Recall that binary trees are often implemented as just (dynamic) arrays, with the elements in the first row listed before the elements in the second, before the elements in the third, and so on. With some simple arithmetic (and zero-indexing!) we gather that the left child of the parent in position $i$ is stored in position $2i+1$, and the right child in position $2i+2$.



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
csq_prompt = "In the example of a non-heap above, exactly two elements $(a,b)$ (with $a < b$) could have been swapped, resulting in a valid max heap. What is $(a,b)$?"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = '(8,9)'
csq_explanation = "explanation"
csq_nsubmits = None
csq_name="p10"
</question>

# Binary Heaps: maintaining them
The key to binary heaps is maintaining the max-heap property (or min-heap property, if it's a min-heap), which requires a nodes key value to be greater than the key value of its children. 

<checkyourself>
This property gives our heap the ability to find the element with greatest key very quickly: it's always the root of the tree. Why is that?
<showhide>
Suppose the keys are unique. Then, if the maximum were anywhere but the root, it would have a parent that must have a greater key. But this is impossible because it is the maximum, so it must be at the root.

Alternatively the max-heap property ensures that the ancestors of any node have a key value at least that of the node: proving this by induction is pretty straightforward, or you can convince yourself by looking at the parent of the parent of a node. If $\verb|node.key| \leq \verb|node.parent.key|$, and $\verb|node.parent.key| \leq \verb|node.parent.parent.key|$, then clearly $\verb|node.key| \leq \verb|node.parent.parent.key|$. And so on.

Then the root, which is everyone's ancestor, must have key value that is at least the value of any other node. This makes it the maximum.
</showhide>
</checkyourself>
