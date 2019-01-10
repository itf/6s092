# Readings 
[Recitation notes 1](https://learning-modules.mit.edu/service/materials/groups/238004/files/586e0399-eb6a-4695-882d-918b42c8aaa5/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), Section on Algorithms, 6.006 Fall 2018 on stellar.

Lecture notes [1](https://learning-modules.mit.edu/service/materials/groups/238004/files/9311a06c-25cc-46af-90de-70b7eff0b18b/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), [2](https://learning-modules.mit.edu/service/materials/groups/238004/files/3af97329-8071-4124-b629-5fe90f1f773b/link?errorRedirect=%2Fmaterials%2Findex.html&download=true),  6.006 Fall 2018 on stellar.

[OCW algorithmic thinking](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec01.pdf)

# Algorithmic thinking


<question multiplechoice>
csq_prompt = "Which of the following are algorithms (under the Word-RAM model of computation)?"
csq_renderer = "checkbox"
csq_soln = [1,0,1,0,1]
csq_options =  ['Always return True',
'What is the shortest path between points A and B?',
'Add the input numbers together and then divide by the number of input numbers',
'A sorted binary tree',
'Generate a random number, 0 or 1, with 50% chance. If you generated 0, return True, if not return False']
csq_name="qexample1"
</question>


<checkyourself>
You should have a clear understanding of what is an algorithm. An algorithm is a series of unambiguous instructions mapping an input to an output.
</checkyourself>


## Understanding a simple algorithm

We have the following problem: given an one-dimensional array, we want to find a peak, i.e. an element that is larger or equal to its neighbors. 

<checkyourself>
Does a peak always exist?

<showhide>
Yes. Because the peak can also be equal to its neighbors, a peak will always exist in a non-empty array.
</showhide>
</checkyourself>

<question multiplechoice>
csq_prompt = """
A brute-force algorithm is a general problem-solving technique which enumerates all possibilities and checks whether they are a solution to the problem. A straightforward, brute-force algorithm for this problem is as follows: \n
\n
Iterate over the array, and check whether each element is a peak by checking it against both of its neighbors. \n
What is the runtime of this algorithm?
"""

csq_renderer = "radio"
csq_soln = 'O(n)'
csq_options =  ['O(n^2)',
'O(n)',
'O(log n)',
'O(1)']
csq_name="peakfinding"
</question>

We can get a faster algorithm using a divide-and-conquer approach as follows:

Check the middle element of the array and compare it to its neighbors. If it is a peak, then we are done. If it is not a peak, than either its left neighbor is greater than it, or its right neighbor is greater than it. If its left neighbor is greater, recurse on the left half of the array. Otherwise, recurse on the right half.

<checkyourself>
Try to explain why this algorithm always works.

<showhide>
We start with an array that has a peak. We want to show that our recursive step always preserves this invariant. If the left neighbor is greater than the middle element, then the global maximum of the left side must be a peak. Thus, the subarray that we are recursing on must have a peak.
</showhide>
</checkyourself>

<question multiplechoice>
csq_prompt = """
What is the runtime of this algorithm?
"""

csq_renderer = "radio"
csq_soln = 'O(log(n)'
csq_options =  ['O(n^2)',
'O(n)',
'O(log n)',
'O(1)']
csq_name="peakfinding"
</question>

