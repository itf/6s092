# Readings 
[Recitation notes 7](https://learning-modules.mit.edu/service/materials/groups/278835/files/99f4474f-81bf-4faa-a94b-f9a429e162bb/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), Section on Comparison Model, 6.006 Fall 2018 on stellar.

<python>
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_nsubmits = None
</python>

# Decision Trees and Informational Theoretic Lower Bound

A decision tree can be used to show how the input of an algorithm is mapped to the output. We start at the root, and for every "decision" made in the algorithm, we pick a branch to travel down. The algorithm then returns a solution when we reach a leaf. The decision tree displays all of these decisions that we make when running the algorithm on a generic input.

## Example with Sorting
For example, suppose we are sorting an array with 3 elements, $a,b,c$ by doing **pairwise comparisons**

The decision tree could be the following:
```
      True         a  <  b      False
                 /          \    
            b < c             b < c
          /      \           /     \
      [abc]     a < c       a < c   [cba]
               /    \       /    \
           [acb]   [cab]  [bac]  [bca]
```

As you can see, there are $3! = 6$ different leaves on the tree, because there are $3!$ different ways to sort 3 elements.

Depending on the decisions, our algorithm might terminate after 2 comparisons or after 3 comparisons. 

The height of the tree is 3.

Another possible decisions tree could be:

```
      True         a   <   b      False
                 /            \    
            b < c               b   <   c
          /      \             /         \
     a < c        a < c       a < c        a < c 
    / \          /    \       /    \       /    \
[abc]  ERROR  [acb]   [cab] [bac]  [bca] ERROR   [cba]
```

Where the tree contains 8 leaves, but 2 of them are unreachable.

Now, suppose that instead of 3 elements, we are sorting $n$ elements by doing **pairwise comparisons**


<question expression>
csq_prompt = """What is the minimum number of leaves that the decision tree to sort n elements would have?

To write $n!$, write $fact(n)$

"""
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = "fact(n)"
csq_explanation = "the number of different ways you can sort n elements"
csq_nsubmits = None
</question>

<checkyourself>
Why is that the number of leaves?
<showhide>
Every single possible outcome has to be reachable, so we need a leaf for each possible outcome of the algorithm
</showhide>
</checkyourself>

<question expression>
csq_prompt = """What is a lower bound for the height of the tree? 

To write $\\lceil log_2(n) \\rceil$,  write $log(n,2)$, and assume $n$ is a power of 2.
"""
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = "log(fact(n),2)"
csq_explanation = "the number of different ways you can sort n elements"
csq_nsubmits = None
</question>


The height of a decision tree is the minimum number of decisions we have to take before we can be sure that we have reached a leaf node. For our example above, this is the minimum number of comparisons we need to perform to be sure that we have sorted an arbitrary input.


We have $n!$ different possible orderings to an array. Therefore we can calculate the height of the decision tree of sorting the array to be at least $\log(n!)$.

We know that:
$$ \log(n!) = \Theta(n\log(n))$$

<checkyourself>
Can you think of why this is true?
<showhide>
$$\left(\frac{n}{2}\right)^{\frac{n}{2}} \le n!\le \left(n \right)^{n}$$
$$\log \left(\left(\frac{n}{2}\right)^{\frac{n}{2}}\right) \le \log(n!)\le \log  \left(\left(n \right)^{n}\right)$$
$$ \frac{n}{2} \log \left(\frac{n}{2}\right) \le \log(n!)\le n \log\left(n \right)$$
</showhide>
</checkyourself>

So the height of our decision tree (and the lower bound on the number of pairwise comparisons we need to make to sort an array of $n$ elements) is:

$$ \Omega(n \log(n))$$

This is the information theoretic lower bound for comparison sort. It is not possible to write a comparison sort that sorts any input in less than $\Omega(n \log(n))$

#### Extra
Another way of describing this, is to say that every comparisons gives us at most 1 bit of information, and we need at least $\log_2(n!)$ bits on average to identify what is the correct output. 

It is common to get less than 1 bit of information per comparison. That is why some sorting algorithms such as selection sort (see PS07) needs so many comparisons. 


### Binary search
Now lets calculate the information theoretic lower bound for performing binary search.

<question expression>
csq_prompt = """
How many different outputs are there for binary search, assuming that our number is in our array?
"""
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = "n"
csq_explanation = "the number of different indexes"
csq_nsubmits = None
</question>


<question expression>
csq_prompt = """
What is a lower bound on the height of the decision tree? Write it as $\Omega(f(n))$.
"""
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["Omega(log(n))", "Omega(log(n,2))"]
csq_explanation = "the minimum height of the decision tree for binary search"
csq_nsubmits = None
</question>


## Improving find
Since we cannot decrease the number of leaves of our decision tree, in order to make its height smaller  than the lower bound that you just calculated, we need to increase its branching factor.

Suppose you are looking for an element in an array, given their id number. Suppose you can jump to location array[id] in 1 step, there is at most one element of each id, and that if an element has $id = k$, they are at location $k$ in the array.


<question expression>
csq_prompt = """
Supposing our array has length $n$, what is the branching factor of our decision tree, when we look for an element at location array[k]? Give your answer in terms of $n$
"""
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = "n"
csq_explanation = "the number of different indexes"
csq_nsubmits = None
</question>


<question expression>
csq_prompt = """
Given this branching factor, what is the minimum height of the tree?
"""
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["1", "Omega(1)", "Theta(1)"]
csq_explanation = "$log_n(n)$"
csq_nsubmits = None
</question>

As you see, if you know exactly where to look, you can find an element much faster than performing binary search.


## Improving sort
Similarly, since we cannot decrease the number of leaves of our decision tree, in order to make its height smaller than $n \log(n)$, we need to increase its branching factor.

Suppose that when you look at an element in your input array, you know exactly in which location it should go in your output array.

<question expression>
csq_prompt = """
Supposing our array has length $n$, what is the branching factor of our decision tree? Let's say we are sorting elements from an input array and placing them into a sorted output array. What are the possible values when we put an element from the input array into our output array, Give your answer in terms of $n$
"""
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = "n"
csq_explanation = "the number of different locations you can put the element"
csq_nsubmits = None
</question>


<question expression>
csq_prompt = """
Given this branching factor, what is the minimum height of the tree? Give you answer as $\Omega(f(n))$
"""
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["Omega(n)", "Theta(n)"]
csq_explanation = "$n \\log_n(n) = n$"
csq_nsubmits = None
</question>

It is possible to use this idea (with some restrictions on the input) in order to improve the run-time of sort to $\\Theta(n)$. This is called radix sort, and requires the input to be an array of integers with some upper-bound in terms of $n$.
