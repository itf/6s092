# Readings 
Recitation notes 1, model of computation section, 6.006 Fall 2018 on stellar.

[Lecture notes 2](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec02.pdf) on OCW

# Model of computation


<question multiplechoice>
csq_prompt = "Question?"
csq_renderer = "checkbox"
csq_soln = [1,0,0,0]
csq_options =  ['option 1',
'option 2',
'option 3',
'option 4']
csq_name="qexample1"
</question>


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

