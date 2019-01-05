# Readings 
Recitation notes 1, model of computation section, 6.006 Fall 2018 on stellar.

[Lecture notes 2](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec02.pdf) on OCW

# Model of computation

<question expression>
csq_prompt = """A student is doing additions by hand, using the standard base 10 \n
How many operations does it take to sum 2 numbers $\\approx$ n ?\n
Suppose there are no "carry 1"s and that $\log(a, b) = \\lfloor \log_b(a) \\rfloor$  \n
"""
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["log(n,10)", "log(n,10)+1"]
csq_explanation = ""
csq_nsubmits = None
</question>

<question expression>
csq_prompt = """ Now the student is performing multiplication. How many operations does it take, assymptotically to calculate $n^2$? Write it as $\\theta(f(n))$.  \n  
\n \n
"""
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["theta(log(n)^2)", "theta(log(n,10)^2)"]
csq_explanation = "The base of the log doesn't matter"
csq_nsubmits = None
</question>

<checkyourself>
How would the previous answers change if you were using base 2 instead of base 10?
<showhide>
The base of the log would be 2, i.e. there would be a constant mutlpliying the amount of work.
</showhide>
</checkyourself>


## Word Ram

From the notes:

Model of Computation (Word-RAM)

- Memory: Bit storage of 0 or 1
- Word: chunk of w bits for some fixed w (word size)
- Treat memory as a random access array of words
- Stores data in a sequence of integer-labeled, equally-sized chunks
- Supports read, write from any bucket in O(1) time (random access)
- Data Structure: Way of storing data supporting set of operations

For the following questions, suppose every number and the result of the operations we perfomr on them fit in a word in the ram.


<question multiplechoice>
csq_prompt = "Suppose we have 2 numbers, $x$, $y$. How many operations does it take to sum them?"
csq_renderer = "checkbox"
csq_soln = [1,0,0,0]
csq_options =  ['$O(1)$',
'$\omega(1)$',
'$o(1)$',
'$\\theta(n)$']
</question>


<question multiplechoice>
csq_prompt = "How many operations does it take to multiply $x$ and $y$?"
csq_renderer = "checkbox"
csq_soln = [1,0,0,0]
csq_options =  ['$O(1)$',
'$\omega(1)$',
'$o(1)$',
'$\\theta(n)$']
</question>


<question multiplechoice>
csq_prompt = "How long does it take to find the maximum element in a list of $n$ elements, by comparing the elements?"
csq_renderer = "checkbox"
csq_soln = [0,1,0,1]
csq_options =  ['$O(1)$',
'$\omega(1)$',
'$o(1)$',
'$\\theta(n)$']
</question>


Python is a language that use the word ram model. Write the run time of the following algorithms in terms of the size of the input.


 <question expression>
csq_prompt = """ 
```python
def average(myList):
    n = len(myList)
    return sum(myList)/n
```
"""
csq_error_on_unknown_variable = True  #make sure they get rid of a in the answer
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["O(n)", "\\theta(n)"]
csq_nsubmits = None
</question> 



 <question expression>
csq_prompt = """ 
```python
def multiplication_triangle(n):
    table = []
    for i in range(1,n):
        row = []
        for j in range(1,i+1):
            row.append(i*j)
        table.append(row)
    return table
```
"""
csq_error_on_unknown_variable = True  #make sure they get rid of a in the answer
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["O(n^2)", "\\theta(n^2)"]
csq_nsubmits = None
</question> 

