# Readings 
Recitation notes 8, 6.006 Fall 2018 on stellar.


# Tuple Sort

In counting sort, we found a fast $O(n+u)$ way to sort $n$ items, with keys from $1$ to $n$: first, create a direct access array of size $u$ in $O(u)$ time, and insert the items in $O(n)$ time, and read through array, spitting out the items in sorted order, in $O(u)$ time. If $u = O(n)$, this means we can sort in $O(n)$ time. Awesome! But we can do better. We can leverage the speed of counting sort to quickly sort *any* list of keys, as long as the keys are bounded by $u=O(n^k)$ for some $k$; i.e. they are polynomially bounded.

The first step is to realize that many sorting algorithms can be used repeatedly to sort items by multiple different criteria. We call this *tuple sort*. Formally, we allow elements to have multiple keys: `x.key_1, x.key_2, ...` and we indicate that `key_1` is more important than `key_2`, which is more important than `key_3`, and so on. An example is useful here: suppose we wish to alphabetize the following beings: `AARDVARK, ARMADILLO, WUMPUS, IBIS, IVAN, ARTIC FOX`. In this case `key_1` would be the first letter of the life form, `key_2` the second, and so on: when we alphabetize, the first letter is most relevant, with ties broken by the second letter, and so on.

How would we sort this? We start by sorting with the *least important key*. Then we sort the second least important, and so on, until finally sorting the most important key. 
<checkyourself>
Why do we start with the least important key?
<showhide>
The first sort we do has the least impact on the final sorting of the items. Conversely, whatever we sort by last will dictate the order.
</showhide>
</checkyourself>

In addition to sorting in this order, we need the sort we need to be *stable*, meaning that items with the same key will be returned in the same order that they were in the input list.

<checkyourself>
Why should the sorting algorithm we use be stable?
<showhide>
So that we don't erase the work we did in previous sorts. We sorted by the last key for a reason: so that, all else being equal, the last key can break ties.
</showhide>
</checkyourself>

In tuple sort, we sort from least significant to most significant by using a stable sort.

Suppose we are sorting tuples of the form (A,B,C), e.g. (3,7,2) using tuple sort, where we want them to be fist sorted by A, then by B, then by C. 


<question multiplechoice>
csq_prompt = "Now, consider the example above. Suppose we only use $4$ keys, the first four letters. After the first round of counting sort for our tuple sort, what will be the order of the words?"
csq_renderer = "radio"
csq_soln = '`ARMADILLO, AARDVARK, ARTIC FOX, IVAN, WUMPUS, IBIS`'
csq_options =  ['`AARDVARK, ARMADILLO, WUMPUS, IBIS, IVAN, ARTIC FOX`', '`ARMADILLO, AARDVARK, ARTIC FOX, IVAN, WUMPUS, IBIS`', '`AARDVARK, ARMADILLO, ARTIC FOX, IBIS, IVAN, WUMPUS`', '`WUMPUS, IVAN, IBIS, ARTIC FOX, ARMADILLO, AARDVARK`']
csq_name="p1"
</question>

<question expression>
csq_prompt = "How many steps of counting sort will we have to do in this example?"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = '4'
csq_nsubmits = None
csq_name="p2"
</question>



<question expression>
csq_prompt = "In general, for $n$ elements, each with $k$ keys, all bounded above by $u$, how long will *each* instance of counting sort take?"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["O(n+u)", "Theta(n+u)"]
csq_nsubmits = None
csq_name="p3"
</question>


<question expression>
csq_prompt = "In general, for $n$ elements, each with $k$ keys, all bounded above by $u$, how many rounds of counting sort will we do?"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["O(k)","Theta(k)"]
csq_nsubmits = None
csq_name="p4"
</question>

<question expression>
csq_prompt = "Overall, for $n$ elements, each with $k$ keys, all bounded above by $u$, what is the runtime of tuple sort?"
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["O(k(n+u))","Theta(k(n+u))"]
csq_nsubmits = None
csq_name="p5"
</question>

So, in the case where we have a fixed number of keys $k$, having to sort by all the tuples is no more work asymptotically than regular, one key sorting. This makes sense: we're just multiplying our work by a constant, which doesn't change asymptotics. This is essential to the next section.

# Radix Sort

With tuple sort at our side, we can come up with a straightforward algorithm to sort numbers bounded by $O(n^c)$. The key idea is that, instead of sorting by keys from $0$ to $n^c$, which would be quite slow, we'll sort by keys from $0$ to $n$ many times. How do we do this, without losing lots of information? We write our keys in base $n$. The keys will be the digits in base $n$, so they are necesarilly bounded above by $n$.

How many keys do we have? Well, if the original keys were bounded by $O(n^c)$, the base $n$ representation of it requires no more than $O(c)$ digits. So now, if $c$ is constant (that is, the keys are $O(n^c)$ for some constant $c$), the final problem set up is like this: We wish to sort $n$ elements, each with $c$ constant keys, all bounded above by $n$. The run time is therefore $O(n)$... linear!

<checkyourself>
Try the following example. Here, we are told that the keys are bounded by $n^4$. Since we are given $5$ numbers, we know the keys are smaller than $5^4$. Represent the number in base $5$, and then use counting sort five times:
$$[100, 63, 624, 26, 255]$$
<showhide>
First, we write the numbers in base $5$: $[400_5, 223_5, 4444_5, 101_5, 2010_5]$. Now we sort, first by the ones digit: $$[400_5, 2010_5, 101_5, 223_5, 4444_5].$$
Now by the second, fives digit: $$[400_5, 101_5, 2010_5, 223_5, 4444_5].$$
Now by the third, 25s digit: $$[2010_5, 101_5, 223_5, 400_5, 4444_5].$$
And lastly, by the fourth, 125s digit: $$[101_5, 223_5, 400_5, 2010_5, 4444_5].$$
When the last digit didn't exist, we interpret it as a $0$. Note that it took us $4$ sorts to do this: a number that would stay constant regardless of the input size. Additionally, both $n$ and $u$ were $O(n)$ (with $n=5$ in this case).
</showhide>
</checkyourself>

<question multiplechoice>
csq_prompt = "Suppose we are told to sort $n$ numbers, each of which is smaller than $n^3$. For radix sort to work, what base should we represent the numbers in?"
csq_renderer = "radio"
csq_soln = '$n$'
csq_options =  ['$3$', '$n$', '$10$', '$n^3$']
csq_name="p6"
</question>

<question multiplechoice>
csq_prompt = "How many digits will this representation have? That is, how many times will we have to do counting sort?"
csq_renderer = "radio"
csq_soln = '$3$'
csq_options =  ['$3$', '$n$', '$10$', '$n^3$']
csq_name="p7"
</question>


<question multiplechoice>
csq_prompt = "For which of the following bounds for $u$ would radix sort work?"
csq_renderer = "checkbox"
csq_soln = [1,1,0,1,0]
csq_options =  ['$O(n)$',
'$O(n^5)$',
'$O(s^2)$, where $s$ is another input to the problem unrelated to $n$',
'$O(n^2 \log n)$',
'$O(2^n)$']
csq_name="p8"
</question>


<question multiplechoice>
csq_prompt = "If I use tuple sort with a stable sort in what order should I sort the tuples by each of their keys? "
csq_renderer = "checkbox"
csq_soln = [0,1,0,0]
csq_options =  ['First by A, then by B, then by C',
'First by C, then by B, then by A',
'First by A, then by C, then by B',
'First by C, then by A, then by B']
</question>

<question multiplechoice>
csq_prompt = "Suppose our list of tuples is [(0,4,4), (2,2,3), (1,2,4), (0,3,4)] and I sort it based on the first element of the tuple using a stable sort. What is the result?"
csq_renderer = "checkbox"
csq_soln = [0,1,0,0]
csq_options =  ['[(0,4,4), (2,2,3), (1,2,4), (0,3,4)]',
'[(0,4,4),  (0,3,4), (1,2,4),  (2,2,3)]',
'[(2,2,3), (0,4,4), (1,2,4), (0,3,4)]',
'[(0,3,4), (0,4,4), (2,2,3), (1,2,4)]']
</question>


<question multiplechoice>
csq_renderer = "radio"

csq_prompt = """
Eve really dislikes stable sorts and says that: "I don't need to use a stable sort 3 times in order to do tuple sort on my tuple of 3 elements. I could instead sort based on the last element using a not stable sort followed by 2 stable sorts for the first 2 fields."

Is Eve correct? Would the algorithm still work if we used a non-stable sort in the first step?   
"""
csq_soln = "Yes"
csq_options =  ['No',
'Yes']
</question>

## Building on top of counting sort 

Suppose I am sorting $n$ elements keyed by positive integers upperbounded by $n^2$.

<question expression>
csq_prompt = "How long would it take to sort those $n$ elements using counting sort?"
csq_allow_viewexplanation = True

csq_soln = ["O(n^2)", "theta(n^2)", "O(n^2,w)", "theta(n^2,w)"]
csq_explanation = "We need to allocate a direct access array of lenght $n^2$"
</question>

<question multiplechoice>
csq_renderer = "radio"

csq_prompt = """
Wumpus really dislikes stable sorts and says that: "I don't need to use a stable sort 3 times in order to do tuple sort on my tuple of 3 elements. I could instead sort based on the last element using a not stable sort followed by 2 stable sorts for the first 2 fields."

Is Wumpus correct? Would the algorithm still work if we used a non-stable sort in the first step?   
"""
csq_soln = "Yes"
csq_options =  ['No',
'Yes']
</question>

