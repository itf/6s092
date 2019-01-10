# Readings

[Recitation notes 1](https://learning-modules.mit.edu/service/materials/groups/238004/files/586e0399-eb6a-4695-882d-918b42c8aaa5/link?errorRedirect=%2Fmaterials%2Findex.html&download=true), Section on Model of Computation, 6.006 Fall 2018 on stellar.

[Lecture notes 2](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec02.pdf) on OCW

# Model of computation

<question expression>
csq_prompt = """A student is doing additions by hand in base 10. \n
How many operations does it take to sum $n+n$ ? \n
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
csq_prompt = """ Now the student is performing multiplication. How many operations does it take, asymptotically, to calculate $n^2$? Express your answer in the format Theta$(f(n))$.  \n
\n \n
"""
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["Theta(log(n)^2)", "Theta(log(n,10)^2)"]
csq_explanation = "The base of the log doesn't matter"
csq_nsubmits = None
</question>

<checkyourself>
How would the previous answers be different if you were using base 2 instead of base 10?
<showhide>
The base of the log would be 2. The second answer wouldn't change because there would be a constant multiplying the amount of work.
</showhide>
</checkyourself>


## Word Ram

From the notes:

The Model of Computation that we are using (and is commonly used in computers) is called Word-RAM. A quick run-down of some characteristics of this model:

- *Memory*: Bit storage of 0 or 1
- *Word*: chunk of $w$ bits for some fixed $w$ (word size)
- Treats memory as a random access array of words
- Stores data in a sequence of integer-labeled (addressed), equally-sized chunks
- Supports read and write from any address in O(1) time (random access)
- *Data Structure*: Way of storing data supporting a set of operations

For the following questions, suppose every number (including the results of the operations we perform on them) fit in a word in the RAM. There may be multiple answers for each question.

<question multiplechoice>
csq_prompt = "Suppose we have 2 numbers, $x$, $y$. How many operations does it take to sum them?"
csq_renderer = "checkbox"
csq_soln = [1,0,0,0]
csq_options =  ['$O(1)$',
'$\omega(1)$',
'$o(1)$',
'$\\Theta(n)$']
</question>


<question multiplechoice>
csq_prompt = "How many operations does it take to multiply $x$ and $y$?"
csq_renderer = "checkbox"
csq_soln = [1,0,0,0]
csq_options =  ['$O(1)$',
'$\omega(1)$',
'$o(1)$',
'$\\Theta(n)$']
</question>


<question multiplechoice>
csq_prompt = "How long does it take to find the maximum element in a list of $n$ elements, by comparing the elements?"
csq_renderer = "checkbox"
csq_soln = [0,1,0,1]
csq_options =  ['$O(1)$',
'$\omega(1)$',
'$o(1)$',
'$\\Theta(n)$']
</question>


Python is a language that uses the Word-RAM model. Write the asymptotic run time of the following algorithms in terms of the size of the input.

<question expression>
csq_prompt = """
```python
def average(myList):
    n = len(myList)
    return sum(myList)/n
```
"""
csq_error_on_unknown_variable = True
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["O(n)", "Theta(n)"]
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
csq_soln = ["O(n^2)", "Theta(n^2)"]
csq_nsubmits = None
</question>

Suppose that $\log(n)$ is calculated by repeated division, and that it always returns an integer.

 <question expression>
csq_prompt = """
```python
def get_log(n):
    return log(n)
```
"""
csq_error_on_unknown_variable = True  #make sure they get rid of a in the answer
csq_show_check = True
csq_allow_check = True
csq_allow_submit = True
csq_allow_submit_after_answer_viewed = False
csq_soln = ["O(log(n))", "Theta(log(n))"]
csq_nsubmits = None
</question>

# Register Machines

In this section we consider a register machine with registers `x`, `y`, `z`,
`n` and an unbounded array of memory.
The cost of performing operations is as follows:

| Operation     | Syntax                   | Cost   |
| ------------- | ------------------------ | ------ |
| Load          | `x = mem[y]`             | 10     |
| Store         | `mem[x] = y `            | 10     |
| Add, Subtract | `x = y + z`, `w = w - 1` |  1     |
| Multiply      | `x = y * z`              |  3     |
| Divide        | `x = y / z`              |  6     |
| Comparison    | `x <= y`, `y == 3`       |  1     |
| Control-Flow  | `if`, `while`, `return`  |  0     |

Intuitively, "cost" can be thought of as runtime in nanoseconds, for instance.

## Algorithm A

Let Algorithm A be the following:

```
x = 0 + 0
y = 0 + 0
while (y < n) {
  z = mem[y]
  x = x + z
  y = y + 1
}
return x
```

We denote the initial value of register `n` as $n$.

<checkyourself>
What does Algorithm A compute?

<showhide>
The sum of the first $n$ words in memory.
</showhide>
</checkyourself>

<question multiplechoice>
csq_prompt = 'What is the runtime cost of Algorithm A when $n = 4$?'
csq_renderer = 'radio'
csq_soln = '55'
csq_options =  ['45', '50', '55', '60']
csq_explanation = "The initialization has cost 2.  The comparison has cost 1 and is run 5 times.  The loop body has cost 12 and is run 4 times."
csq_nsubmits = None # infinite submissions
csq_name="algorithm_cost_A4"
</question>

<question expression>
csq_prompt = 'What is the runtime cost of Algorithm A in terms of $n$?'
csq_soln = "13*n + 3"
csq_explanation = "The initialization has cost 2.  The comparison has cost 1 and is run $n + 1$ times.  The loop body has cost 12 and is run $n$ times."
csq_nsubmits = None # infinite submissions
csq_name="algorithm_cost_An"
</question>

<question multiplechoice>
csq_prompt = 'What is the asymptotic complexity of Algorithm A in terms of $n$?'
csq_renderer = 'radio'
csq_options = [r'$\Theta(1)$', r'$\Theta(\log n)$', r'$\Theta(n)$', r'$\Theta(n^2)$']
csq_soln = r'$\Theta(n)$'
csq_explanation = "follows from the previous question"
csq_nsubmits = None # infinite submissions
csq_name="algorithm_asymp_A"
</question>

## Algorithms B and C

Let Algorithm B be the following:

```
x = 0 + 0
y = 0 + 0
while (y < n) {
  y = y + 1
  x = x + y
}
return x
```

Let Algorithm C be the following:

```
x = n + 1
y = x * n
z = y / 2
return z
```

As before, we denote the initial value of register `n` as $n$.

<checkyourself>
Algorithms B and C compute the same quantity.  What is it?

<showhide>
The sum of the first $n$ positive integers.
</showhide>
</checkyourself>

<question multiplechoice>
csq_prompt = 'What is the asymptotic complexity of Algorithm B in $n$?'
csq_renderer = 'radio'
csq_options = [r'$\Theta(1)$', r'$\Theta(\log n)$', r'$\Theta(n)$', r'$\Theta(n^2)$']
csq_soln = r'$\Theta(n)$'
csq_explanation = "Similar reasoning to Algorithm A - the body runs $n$ times"
csq_nsubmits = None # infinite submissions
csq_name="algorithm_asymp_B"
</question>

<question multiplechoice>
csq_prompt = 'What is the asymptotic complexity of Algorithm C in $n$?'
csq_renderer = 'radio'
csq_options = [r'$\Theta(1)$', r'$\Theta(\log n)$', r'$\Theta(n)$', r'$\Theta(n^2)$']
csq_soln = r'$\Theta(1)$'
csq_explanation = "Fixed number of steps, each with fixed cost."
csq_nsubmits = None # infinite submissions
csq_name="algorithm_asymp_C"
</question>

<question multiplechoice>
csq_prompt = 'Which of the following descriptions is accurate?'
csq_renderer = 'radio'
csq_options = ['Algorithm B has lower cost than Algorithm C for all $n$',
               'Algorithm C has lower cost than Algorithm B for all $n$',
               'None of the above']
csq_soln = 'None of the above'
csq_explanation = "Consider n = 0 and n = 1000."
csq_nsubmits = None # infinite submissions
csq_name="comparison_B_C"
</question>

# Term reduction

In this section we consider a simple model of computation.
In this model, programs are defined by *terms*, which are defined by the
following possibilities:

| Name | Syntax |
| ---- | ------ |
| Constant | `0`, `1`, `36`, etc |
| Addition | `(A + B)` where `A` and `B` are terms |
| Multiplication | `(A * B)` where `A` and `B` are terms |

In other words, a term is a constant, or
the sum of two terms, or the product of two terms.

An example of a term is `((3 + 5) * (2 * 3))`.

We will define a family of terms $D_n$ recursively.
Define $D_0$ as the term `1`,
and define $D_{n + 1}$ as the term $(D_n + D_n)$.
For instance, $D_2$ is the term `((1 + 1) + (1 + 1))`.

Similarly we will define a family of terms $E_n$ recursively.
Define $E_0$ as the term `1`,
and define $E_{n + 1}$ as the term $(2 * E_n)$.
For instance, $E_2$ is the term `(2 * (2 * 1))`.

<checkyourself>
$D_n$ and $E_n$ represent the same value.  What value is that?

<showhide>
$2^n$
</showhide>
</checkyourself>

## Sequential computation

We first consider a sequential model of computation.
In this model, the "computer" repeatedly performs the following step:

- Find some subterm of the form `(a + b)` or `(a * b)` where `a` and `b` are constants,
  and replace it by the constant `a + b` or `a * b` respectively.

The *sequential cost* of a term is defined to be the number of steps it
takes until no more steps can be taken.
For instance, the term `((3 + 5) * (2 * 3))` has sequential cost 3.

<question expression>
csq_prompt = 'What is the sequential cost of term $D_n$, in terms of $n$?'
csq_soln = '2^n - 1'
csq_error_on_unknown_variable = True
csq_nsubmits = None # infinite submissions
csq_name="sequential_cost_D"
</question>

<question expression>
csq_prompt = 'What is the sequential cost of term $E_n$, in terms of $n$?'
csq_soln = 'n'
csq_error_on_unknown_variable = True
csq_nsubmits = None # infinite submissions
csq_name="sequential_cost_E"
</question>

## Parallel computation

Now we consider a parallel model of computation.
This time, the "computer" repeatedly performs the following step:

- Find *all* subterms of the form `(a + b)` or `(a * b)` where `a` and `b` are constants,
  and *simultaneously* replace each of them by the constant `a + b` or `a * b` respectively.

The *parallel cost* of a term is defined to be the number of these steps it
takes until no more steps can be taken.
For instance, the term `((3 + 5) * (2 * 3))` has parallel cost 2.

<question expression>
csq_prompt = 'What is the parallel cost of term $D_n$, in terms of $n$?'
csq_soln = 'n'
csq_error_on_unknown_variable = True
csq_nsubmits = None # infinite submissions
csq_name="parallel_cost_D"
</question>

<question expression>
csq_prompt = 'What is the parallel cost of term $E_n$, in terms of $n$?'
csq_soln = 'n'
csq_error_on_unknown_variable = True
csq_nsubmits = None # infinite submissions
csq_name="parallel_cost_E"
</question>

<question multiplechoice>
csq_prompt = 'Which of the following descriptions is accurate?'
csq_renderer = 'radio'
csq_soln = 'The parallel cost of any term is no greater than the sequential cost.'
csq_options = ['The sequential cost of any term is no greater than the parallel cost.',
               'The parallel cost of any term is no greater than the sequential cost.',
               'None of the above']
csq_nsubmits = None # infinite submissions
csq_name="comparison_parallel_sequential"
</question>
