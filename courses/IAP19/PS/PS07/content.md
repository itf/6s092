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
csq_solution = [0,1,0,1,0,0]
csq_options = ['$[1,\ 4,\ 2,\ 3] \\rightarrow [1,\ 2,\ 3,\ 4]$',
'$[1,\ 4,\ 2,\ 3] \\rightarrow [1,\ 2,\ 3,\ 4]$',
'$[1,\ 4,\ 2,\ 3] \\rightarrow [1,\ 2,\ 3,\ 4]$',
'$[1,\ 4,\ 2,\ 3] \\rightarrow [1,\ 2,\ 3,\ 4]$',
'$[1,\ 4,\ 2,\ 3] \\rightarrow [1,\ 2,\ 3,\ 4]$',
'$[1,\ 4,\ 2,\ 3] \\rightarrow [1,\ 2,\ 3,\ 4]$']
# 1 4 2 3 -> 1 2 3 4
#
# 1 4 2 3 -> 1 2 4 3
# 
# 2 1 4 3 -> 2 1 3 4
# 
# 1 3 5 4 2 -> 1 3 4 5 2
# 
# 1 3 5 4 2 -> 1 2 3 5 4
# 
# 1 3 5 4 2 -> 1 3 5 2 4
csq_name = 'ps7q2'
</question>

# Why can't we make the swap 2 3 1 -> 1 2 3? Refer back to PS03 (Word RAM) for a refresher on why our model necessitates making two swaps: 2 3 1 -> 2 1 3 -> 1 2 3.
# 
# Selection sort:
# 
# 3 2 1 4 5 -> 2 1 3 4 5
# 
# 3 2 1 4 5 -> 3 1 2 4 5
# 
# What is the minimum number of comparisons are made in selection sort?
# 
# What is the maximum number of comparisons?
# 
# Min and max for insertion sort?
# 
# 
# You should reference the code in merge sort for this
# When we say merge sort takes up linear amount of space, we meant that we have to set aside a linear amount of storage for $temp$. What does that mean? (where $n$ is the size of the array)
# O(1)
# O(log n)
# O(n)
# O(n^c) for any positive c



<question multiplechoice>
csq_renderer = "checkbox"
csq_soln = [1]
csq_options =  ['merge sort']
</question>

<checkyourself>
Are you understanding?
<showhide>
yeah
</showhide>
</checkyourself>

