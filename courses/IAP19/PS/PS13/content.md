# Readings 
[Recitation notes 7](https://learning-modules.mit.edu/service/materials/groups/238004/files/4ced90b7-63e9-453c-9f10-4e8c51a94d67/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), Direct Access & Hashing -- section on Hashing, 6.006 Fall 2018 on stellar.

[Lecture notes 8](https://learning-modules.mit.edu/service/materials/groups/238004/files/a90b0fdd-5d81-4f72-b5f2-3fe8e65a99a0/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), Direct Access & Hashing -- section on  6.006 Fall 2018 on stellar.

# Hashtables and Hashing

For the following questions, write $\Theta(f(n), a, e, w)$ to mean $f(n)$ Amortized, Expected, Worst-case run time. 

For example, $\Theta(n, e, a)$ would mean $\underbrace{\Theta(n)}_\text{expected, amortized}$

Assume that the size of the hashtable is $\Theta(n)$, where $n$ is the number of elements we are inserting on the hashtable.


If something runs in worst-case $f(n)$, only the worst case solution will be accepted, even though worst-case also implies expected and amortized.
<question expression>
csq_prompt = """What is the asymptotic run time to find an element by its key on a hashtable?

\n"""
csq_soln = ["O(1,e)", "Theta(1,e)"]
csq_explanation = "Because the expected number of collisions is $O(1)$"
csq_nsubmits = None
</question>

<question expression>
csq_prompt = """What is the asymptotic run-time to insert an element (key-value pair) into a hashtable?  
"""
csq_soln = ["O(1,e,a)", "Theta(1,e,a)"]
csq_explanation = "Amortized because the hash-table is a dynamic array"
csq_nsubmits = None
</question>


<question expression>
csq_prompt = """What is the asymptotic run-time to find an element by its value on a hashtable?  
"""
csq_soln = ["O(n,w)", "Theta(n,w)"]
csq_explanation = "There is no efficient way "
csq_nsubmits = None
</question>


## 2-Universal hashing
In $2$-universal hashing, we randomly select a function from a family of hash functions that maps elements from $\mathbb{M} \to \{0 \dots n-1\}$ , such that the probability of two elements from $\mathbb{M}$ having the same hash is $\le \frac{1}{n}$.

A hash family with those properties is called a $2$-universal hash family. More generally, if the probability of $k$ elements having the same hash was  $\le \frac{1}{n^{k-1}}$, we would have a $k$-universal hash family.

When someone says universal hashing without specifying $k$, it means $2$-universal hashing.

<question expression>
csq_prompt = """If we use $2$-universal hashing to insert $n$ elements into our hash-table, what is the maximum number of elements that share the same hash in the worst case?

\n"""
csq_soln = ["O(n)", "Theta(n)", "Theta(n, w)", "O(n,w)", "n"]
csq_explanation = "Every element might collide"
csq_nsubmits = None
</question>


Suppose our universe $\mathbb{M} = \{\alpha, \beta, \gamma, \delta\}$ 

<question pythonliteral>
csq_prompt = """
Suppose $\\mathbb{H} = \{f,g,h,l\}$ where
 
$$f(\\alpha) =3,\ f(\\beta) =0,\ f(\\gamma) = 1,\ f(\\delta) = 2$$
 $$g(\\alpha) = 0,\  g(\\beta) = 1,\ g(\\gamma) =2, \ g(\\delta) = 3$$
 $$h(\\alpha) = 1,\  h(\\beta) = 2,\ h(\\gamma) =3, \ h(\\delta) = 0$$
 $$l(\\alpha) = 2,\  l(\\beta) = 3,\ l(\\gamma) =0, \ l(\\delta) = 2$$

In other words, they never collide.

What is the probability that $\\alpha$ and $\\beta$ collide when mapped under the hash family $\\mathbb{H}$?
"""
csq_soln = 0
csq_explanation = "None of $f$, $g$, $h$, or $l$ will cause $\\alpha$ and $\\beta$ to collide."
csq_nsubmits = None
</question>


<question multiplechoice>
csq_prompt = """
Is $\\mathbb{H}$ a 2-universal hash family from $ \\{\\alpha, \\beta, \\gamma, \\delta\\} \\to \\{0,1,2,3\\}$?
"""
csq_renderer = "radio"
csq_soln = "yes"
csq_options =  ['yes', 'no']
csq_explanation = "$0 < 1/n$"
</question>

<question pythonliteral>
csq_prompt = """
Now suppose $\\mathbb{H} = \{f,g,h,l\}$ where
 
$$f(\\alpha) = f(\\beta) = f(\\gamma) = f(\\delta) = 0$$
 $$g(\\alpha) = 0,\  g(\\beta) = 1,\ g(\\gamma) =2, \ g(\\delta) = 3$$
 $$h(\\alpha) = 1,\  h(\\beta) = 2,\ h(\\gamma) =3, \ h(\\delta) = 0$$
 $$l(\\alpha) = 2,\  l(\\beta) = 3,\ l(\\gamma) =0, \ l(\\delta) = 1$$

In other words, either all elements collide or none of them collide.

What is the probability that $\\alpha$ and $\\beta$ collide when mapped under the hash family $\\mathbb{H}$?
"""
csq_soln = 1/4
csq_explanation = "If we randomly pick $f$ as the hashing function, then $\\alpha$ and $\\beta$ will collide. Otherwise they will not collide."
csq_nsubmits = None
</question>

<question multiplechoice>
csq_prompt = """
Is $\\mathbb{H}$ a 2-universal hash family from $ \\{\\alpha, \\beta, \\gamma, \\delta\\} \\to \\{0,1,2,3\\}$?
"""
csq_renderer = "radio"
csq_soln = 'yes'
csq_options =  ['yes', 'no']
csq_explanation = "What is the probability of 2 elements colliding?"
</question>

## Hashtable with collisions solved by chaining

Suppose we now have a hashtable where collisions are resolved by chaining, where we always keep the most recent value.

<question multiplechoice>
csq_prompt = """We run the following code on our hashtable, where `(x:y)` denotes an element with key `x` and value `y`:
```
A = hashtable()
A.insert(a:3)
A.insert(a:2)
```
What will `A.get(a)` return?
"""
csq_renderer = "radio"
csq_soln = '2'
csq_options =  ['3',
'2',
'[3,2]',
'[2,3]']
</question>


<question multiplechoice>
csq_prompt = """Suppose `hash(a) = hash(b)`, i.e. there is a collision on our hashtable for those $2$ keys.
We run the following code on our hashtable:
```
A = hashtable()
A.insert(a:3)
A.insert(b:2)
```
What will `A.get(a)` return?

"""
csq_renderer = "radio"
csq_soln = '3'
csq_options =  ['3',
'2',
'[3,2]',
'[2,3]']
</question>



<question expression>
csq_prompt = """Suppose we insert $n$ elements, all with different keys, in our hashtable $A$.

By bad luck, all $n$ of them collided with the element that had `key = a` 

How many elements will be returned when we run `A.get(a)`?"""
csq_soln = "1"
csq_explanation = "It doesn't matter what is happening how the hashtable is handling collisions. It will only return the element with key=a"
csq_nsubmits = None
</question>

<question expression>
csq_prompt = "Still in the case where all $n$ elements collided, how long will it take to run `A.get(a)`"
csq_soln = ["O(n,w)", "Theta(n,w)", "O(n)", "Theta(n)"]
csq_explanation = "In the worst case we will have to look at all elements in the chain before we find the one with key=$a$"
csq_nsubmits = None
</question>

<question expression>
csq_prompt = "Still in the case where all $n$ elements collided, how long will it take to run `A.insert(a: (new value) )`"
csq_soln = ["O(n,w)", "Theta(n,w)", "O(n)", "Theta(n)"]
csq_explanation = "We first have to find $a$ before updating its value"
csq_nsubmits = None
</question>
