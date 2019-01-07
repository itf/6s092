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
csq_prompt = "How many swaps are necessary to sort this array $[1,\ 2,\ 4,\ 3]$?"
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

Read the section on Merge Sort in the Recitation notes. You don't need to understand the code line by line, but you should be able to have some intuition for how the algorithm works. You should look at the codepen visualization, it's very helpful.

### Intermediate States
Merge sort begins by breaking the original array into many pieces of size '$<2$'. Then we "merge" these small chunks into larger chunks. After we merge the smaller chunks of a particular size, we start merging the larger chunks. Each merge step of Merge Sort will merge two arrays of length '$n$' to form an array of length '$2n$'.

For the following two problems, you are given an array that is in the middle of merge sort. We are about to merge a chunk of size $n$, containing the first value in the array ($1$), with an adjacent chunk of size $n$. What are possible values for $n$?

<question multiplechoice>
csq_prompt = "[1,\ 5,\ 3,\ 8,\ 2,\ 4,\ 6,\ 7]$"
csq_renderer = "checkbox"
csq_soln = [1,1,0,0]
csq_options = ['$1$', '$2$', '$3$', '$4$']
csq_explanation = "The chunks of size $1$ and $2$ are sorted within themselves, so they are possible candidates for merging. However, the first chunk of size $>2$ (the sequence $[1,\ 5,\ 3]$) is not sorted. We must merge chunks of size $2$ before we can move on to larger chunks."
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

Recall from the reading that the runtime of merge-sort is $\theta(nlog(n))$. One way to get this run-time is by applying case 2 of (the special polynomial form of) the Master's Theorem to the recurrence equation that we have for the run-time: $T(n) = 2T(n/2) + \theta(n)$. However, we can derive this run-time in a more intuitive way!

For simplicity's sake, let's say that $n = 2^i$ (so, $n$ is a power of $2$). We break the array into chunks of size $1$. An array of length $1$ is trivially sorted, so it takes $\theta(1)$ time to sort all the $n$ chunks of size $1$.

<question multiplechoice>
csq_prompt = "We merge $n/2$ pairs of size $1$ chunks into $n/2$ chunks of size $2$. How long (how many operations) does it take to merge two chunks of size $1$?"
csq_renderer = "radio"
csq_soln = '$\\theta(1)$'
csq_options = ['$\\theta(1)$', '$\\theta(log(n))$', '$\\theta(2n)$']
csq_explanation = "It takes a constant number of operations."
csq_name = "ps7q8"
</question>

<question multiplechoice>
csq_prompt = "How long (how many operations) does it take to merge all the chunks of size $1$?"
csq_renderer = "radio"
csq_soln = '$\\theta(n)$'
csq_options = ['$\\theta(1)$', '$\\theta(log(n))$', '$\\theta(n)$']
csq_explanation = "We perform $n/2$ merges, and each take $\\theta(1)$"
csq_name = "ps7q9"
</question>

<question multiplechoice>
csq_prompt = "At every 'level', we will be merging $n/2^i$ pairs of size $2^i$ into $n/2^i$ chunks of size $2^{i+1}$. How long does it take to merge two chunks of size $2^i$?"
csq_renderer = "radio"
csq_soln = '$\\theta(2^i)$' 
csq_options = ['$\\theta(1)$', '$\\theta(i)$', $\\theta(n)$, $\\theta(2^i)$]
csq_explanation = "Merging two chunks is linear in the sizes of the chunks."
csq_name = "ps7q10"
</question>

<question multiplechoice>
csq_prompt = "How long does it take to complete the level by merging all the chunks of size $2^i$?"
csq_renderer = "radio"
csq_soln = '$\\theta(n)$' 
csq_options = ['$\\theta(1)$', '$\\theta(i)$', $\\theta(n)$, $\\theta(2^i)$]
csq_explanation = "We perform $n/2^i$ merges, so all the merges together add up to $\\theta(n)$."
csq_name = "ps7q11"
</question>

<question multiplechoice>
csq_prompt = "How many levels are there in total?"
csq_renderer = "radio"
csq_soln = '$log(n)$' 
csq_options = ['$1$', 'i', 'log(n, 2)', 'n', '$nlog(n)$']
csq_explanation = "The number of distinct values that $i$ can take range from $0$ (when we have chunks of size $1$) to $log(n)$ when we have a single chunk of size $n$. Because each level takes $\\theta(n)$ work, and we have $log(n)$ levels, it follows that the entire Merge Sort algorithm will take $\\theta(n log(n))$ time."
csq_name = "ps7q12"
</question>

<question multiplechoice>
csq_prompt = "When we say that merge sort takes up a linear amount of space, we mean that we set aside a linear amount of space for $temp$ in addition to the space being used to store the input of size $n$. WHat do we know about the size of $temp$, given that it takes up a linear amount of space?"
csq_renderer = "radio"
csq_soln = '$O(n)$'
csq_options = ['$O(1)$', '$O(log n)$', '$O(n)$', '$O(n^c)$ for any positive $c$', '$r-l$']
csq_name = 'ps7q5'
</question>

Maybe a question on invariants in these three kinds of sorts
