# Readings 
[Recitation notes 3](https://learning-modules.mit.edu/service/materials/groups/238004/files/e6fa926e-a2c0-484f-80a0-c005f3b7f932/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), Sorting, 6.006 Fall 2018 on stellar.

<python>
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_nsubmits = None
</python>

# Sorting

## Insertion Sort

<question expression>
csq_prompt = "How many swaps are necessary to turn this array $[1,\ 2,\ 4,\ 3]$ into a sorted array using insertion sort?"
csq_soln = "1"
csq_explanation = "We only need to swap the $3$ and the $4$"
csq_nsubmits = None #infinite submissions.
csq_name="ps7q1"
</question>

<question multiplechoice>
csq_prompt = "What would be a valid swap to make during insertion sort? Refer to the algorithm described in the recitation notes."
csq_renderer = "checkbox"
csq_soln = [0,1,0,1,0,0]
csq_options = ['$[1,\ 4,\ 2,\ 3] \\rightarrow [1,\ 2,\ 3,\ 4]$',
'$[1,\ 4,\ 2,\ 3] \\rightarrow [1,\ 2,\ 4,\ 3]$',
'$[2,\ 1,\ 4,\ 3] \\rightarrow [2,\ 1,\ 3,\ 4]$',
'$[1,\ 3,\ 5,\ 4,\ 2] \\rightarrow [1,\ 3,\ 4,\ 5,\ 2]$',
'$[1,\ 3,\ 5,\ 4,\ 2] \\rightarrow [1,\ 2,\ 3,\ 5,\ 4]$',
'$[1,\ 3,\ 5,\ 4,\ 2] \\rightarrow [1,\ 3,\ 5,\ 2,\ 4]$']
csq_name = 'ps7q2'
</question>

<checkyourself>
Why can't we make the swap $[2,\ 3,\ 1] \rightarrow [1,\ 2,\ 3]$?
<showhide>
While this might be a simple operation to do with physical objects like cards, arrays in the Word RAM model would require us to make two swaps to move both the '$2$' and the '$3$': '$[2,\ 3,\ 1] \rightarrow [2,\ 1,\ 3] \rightarrow [1,\ 2,\ 3]$'. Refer back to PS03 for more information.
</showhide>
</checkyourself>

A swap is when we take two elements in an array and swap their positions. A comparison is when we compare the values of two numbers.

<question multiplechoice>
csq_prompt = "What is the minimum number of comparisons that we would make in insertion sort?"
csq_renderer = "radio"
csq_soln = '$O(n)$'
csq_options = ['$1$', '$\\Theta(n)$', '$\\Theta(n log n)$', '$\\Theta(n^2)$']
csq_name = 'ps7q3'
</question>

## Selection sort

<question multiplechoice>
csq_prompt = "What would be a valid swap to make during selection sort? Refer to the algorithm described in the recitation notes."
csq_renderer = "checkbox"
csq_soln = [1,0]
csq_options = ['$[3,\ 2,\ 1,\ 4,\ 5] \\rightarrow [2,\ 1,\ 3,\ 4,\ 5]$',
'$[3,\ 2,\ 1,\ 4,\ 5] \\rightarrow [3,\ 1,\ 2,\ 4,\ 5]$']
csq_name = 'ps7q4'
</question>

## Merge Sort

<question multiplechoice>
csq_prompt = "Reference the section on merge sort in the recitation notes for this section. When we say that merge sort takes up a linear amount of space, we mean that we set aside a linear amount of space for $temp$ in addition to the space being used to store the input of size $n$. How much space does temp take?"
csq_renderer = "radio"
csq_soln = '$O(n)$'
csq_options = ['$O(1)$', '$O(log n)$', '$O(n)$', '$O(n^c)$ for any positive $c$', '$r-l$']
csq_name = 'ps7q5'
</question>
